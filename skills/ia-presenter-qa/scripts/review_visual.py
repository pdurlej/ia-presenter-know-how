#!/usr/bin/env python3
"""Visual QA for rendered iA Presenter exports."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DECK_SCRIPTS = SCRIPT_DIR.parents[1] / "ia-presenter-deck" / "scripts"
sys.path.insert(0, str(DECK_SCRIPTS))

from presentation_system import read_json, write_json  # noqa: E402

METRICS_SCRIPT = SCRIPT_DIR / "image_metrics.swift"
LEAK_TOKENS = ("opacity:", "background:", "size:", "x:", "y:", ".png", ".jpg", ".jpeg", ".webp")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Review rendered iA Presenter slides")
    parser.add_argument("--manifest", required=True, help="Path to manifest.json")
    parser.add_argument("--render", required=True, help="Path to render.json")
    parser.add_argument("--output", required=True, help="Output path for visual-review.json")
    return parser.parse_args()


def load_metrics(paths: list[str]) -> dict[str, dict]:
    if not paths:
        return {}
    completed = subprocess.run(
        ["swift", str(METRICS_SCRIPT), *paths],
        capture_output=True,
        text=True,
    )
    if completed.returncode != 0:
        raise RuntimeError((completed.stderr or completed.stdout).strip() or "image metrics extraction failed")
    raw = json.loads(completed.stdout)
    return {item["path"]: item for item in raw}


def build_findings(manifest: dict, render: dict) -> tuple[list[dict], dict]:
    findings: list[dict] = []
    images = render.get("artifacts", {}).get("images", {})
    screenshot_paths = images.get("files", []) or render.get("screenshots", [])

    if render.get("status") not in {"ok", "partial"} or not screenshot_paths:
        findings.append(
            finding(
                "deck",
                "high",
                "render",
                "render_missing",
                "Rendered slide images are not available for visual QA.",
                "Without rendered artifacts the system cannot verify composition or output quality.",
                "Fix the render step first and rerun visual QA.",
                0.99,
            )
        )
        scores = {"render_fidelity": 0.0, "composition": 0.0, "image_use": 0.0, "overall": 0.0}
        summary = {"screenshot_count": 0, "ocr_available": False}
        return findings, {"scores": scores, "summary": summary}

    metrics_by_path = load_metrics(screenshot_paths)
    slides = manifest["slides"]
    ocr_available = any(item["textObservationCount"] > 0 for item in metrics_by_path.values())
    missing_images = 0
    composition_hits = 0
    image_hits = 0
    fidelity_hits = 0

    for slide, screenshot_path in zip(slides, screenshot_paths, strict=False):
        slide_id = slide["slide_id"]
        metrics = metrics_by_path.get(screenshot_path)
        if not metrics:
            missing_images += 1
            findings.append(
                finding(
                    slide_id,
                    "high",
                    "render",
                    "missing_slide_capture",
                    "The exported render is missing this slide image.",
                    "Per-slide QA breaks when the screenshot sequence is incomplete.",
                    "Re-run the images export and verify the slide count.",
                    0.96,
                )
            )
            continue

        recognized = " ".join(metrics["recognizedLines"]).lower()
        if any(token in recognized for token in LEAK_TOKENS):
            fidelity_hits += 1
            findings.append(
                finding(
                    slide_id,
                    "high",
                    "render",
                    "syntax_leakage",
                    "Rendered metadata or syntax appears to be leaking onto the slide.",
                    "This is a visible formatting defect, not a stylistic preference.",
                    "Remove the leaked attribute lines or correct the image/content block syntax.",
                    0.91,
                )
            )

        if slide["surface"] not in {"cover", "landing", "image-background", "section-reset"}:
            if metrics["wordCount"] < 6 and metrics["textBoxAreaRatio"] < 0.03 and slide["table_row_count"] == 0:
                composition_hits += 1
                findings.append(
                    finding(
                        slide_id,
                        "medium",
                        "composition",
                        "dead_whitespace",
                        "The rendered slide carries very little visible information and a lot of empty space.",
                        "A sparse slide can be strong, but here the visible payload looks underpowered rather than intentional.",
                        "Strengthen the visible claim, merge cells, or turn the slide into a more deliberate reset.",
                        0.78,
                    )
                )

        if slide["cell_count"] >= 2 and slide["surface"] not in {"image-panel-split"}:
            left_ratio = metrics["leftTextAreaRatio"]
            right_ratio = metrics["rightTextAreaRatio"]
            smaller = min(left_ratio, right_ratio)
            larger = max(left_ratio, right_ratio)
            if larger > 0.08 and smaller < 0.015:
                composition_hits += 1
                findings.append(
                    finding(
                        slide_id,
                        "medium",
                        "composition",
                        "split_imbalance",
                        "The slide renders as an imbalanced split with one starved side.",
                        "The audience reads it as an accidental layout rather than a controlled contrast or panel.",
                        "Merge the cells, change the layout intent, or rebalance the visible payload.",
                        0.74,
                    )
                )

        if slide["surface"] in {"proof-table", "full-width-proof"} and metrics["textBoxAreaRatio"] < 0.08:
            composition_hits += 1
            findings.append(
                finding(
                    slide_id,
                    "high",
                    "composition",
                    "stranded_proof_table",
                    "The proof object renders too small or too isolated to carry the slide.",
                    "A proof slide has to earn attention immediately; a tiny table behaves like side furniture.",
                    "Promote the proof to a wider layout, merge the title stack, or simplify the table so it can scale up.",
                    0.83,
                )
            )

        if slide["surface"] == "image-panel-split" and metrics["wordCount"] < 10 and metrics["textBoxAreaRatio"] < 0.04:
            image_hits += 1
            findings.append(
                finding(
                    slide_id,
                    "medium",
                    "image_use",
                    "weak_decorative_image",
                    "The image-led slide looks decorative without enough visible argument to justify the space.",
                    "Image moments should reset rhythm or sharpen meaning, not just fill half a slide.",
                    "Either strengthen the text payload or remove the image and switch back to a cleaner text surface.",
                    0.69,
                )
            )

    scores = {
        "render_fidelity": clamp_score(10 - fidelity_hits * 3 - missing_images * 4),
        "composition": clamp_score(10 - composition_hits * 2.2),
        "image_use": clamp_score(10 - image_hits * 2.5),
    }
    scores["overall"] = round(sum(scores.values()) / len(scores), 2)
    summary = {
        "screenshot_count": len(screenshot_paths),
        "ocr_available": ocr_available,
        "missing_images": missing_images,
        "composition_findings": composition_hits,
        "image_findings": image_hits,
        "render_findings": fidelity_hits,
    }
    return findings, {"scores": scores, "summary": summary}


def finding(
    slide_id: str,
    severity: str,
    axis: str,
    code: str,
    problem: str,
    why: str,
    fix: str,
    confidence: float,
) -> dict:
    return {
        "slide_id": slide_id,
        "severity": severity,
        "axis": axis,
        "code": code,
        "problem": problem,
        "why_it_matters": why,
        "recommended_fix": fix,
        "confidence": confidence,
    }


def clamp_score(value: float) -> float:
    return round(max(0.0, min(10.0, value)), 2)


def main() -> int:
    args = parse_args()
    manifest = read_json(Path(args.manifest))
    render = read_json(Path(args.render))
    findings, review = build_findings(manifest, render)
    payload = {
        "generated_at": manifest["generated_at"],
        "deck_path": manifest["deck_path"],
        "scores": review["scores"],
        "summary": review["summary"],
        "findings": findings,
    }
    write_json(Path(args.output), payload)
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
