#!/usr/bin/env python3
"""Structured story QA for iA Presenter decks."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DECK_SCRIPTS = SCRIPT_DIR.parents[1] / "ia-presenter-deck" / "scripts"
sys.path.insert(0, str(DECK_SCRIPTS))

from presentation_system import (  # noqa: E402
    GENERIC_TITLES,
    WEAK_CLOSERS,
    build_manifest,
    read_json,
    write_json,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Review iA Presenter story quality")
    parser.add_argument("--deck", required=True, help="Path to .iapresenter package or markdown file")
    parser.add_argument("--manifest", help="Optional manifest.json path")
    parser.add_argument("--output", required=True, help="Output path for story-review.json")
    return parser.parse_args()


def build_findings(manifest: dict) -> tuple[list[dict], dict]:
    findings: list[dict] = []
    slides = manifest["slides"]

    generic_heading_count = 0
    note_abuse_count = 0
    weak_visible_count = 0
    list_heavy_count = 0

    for slide in slides:
        slide_id = slide["slide_id"]
        headings = [h.lower() for h in slide["heading_texts"]]
        if any(h in GENERIC_TITLES for h in headings):
            generic_heading_count += 1
            findings.append(
                finding(
                    slide_id,
                    "medium",
                    "story",
                    "generic_heading",
                    "The slide title is generic rather than meaning-bearing.",
                    "Generic titles flatten the deck and make sections harder to remember.",
                    "Rewrite the title as a governing thought or a sharper live line.",
                    0.84,
                )
            )

        if slide["notes_policy"] == "suspicious" and slide["hidden_line_count"] > 0:
            note_abuse_count += 1
            findings.append(
                finding(
                    slide_id,
                    "high",
                    "visible_payload",
                    "notes_substance",
                    "The slide still carries substance in hidden notes.",
                    "The deck becomes clearer in the editor than in presenter view, which breaks the visible-payload contract.",
                    "Promote the main claim or proof into the visible layer and keep notes only for depth or transitions.",
                    0.95,
                )
            )

        if not slide["visible_payload"] and slide["surface"] not in {"cover", "landing"}:
            weak_visible_count += 1
            findings.append(
                finding(
                    slide_id,
                    "high",
                    "visible_payload",
                    "weak_hidden_slide",
                    "The slide lacks a clear visible payload.",
                    "A slide with no strong visible payload is unlikely to survive rendering review.",
                    "Add one visible claim, sequence, quote, proof object, or stronger heading stack.",
                    0.88,
                )
            )

        if slide["surface"] in {"sequence", "stacked"} and slide["visible_line_count"] >= 5:
            list_heavy_count += 1
            findings.append(
                finding(
                    slide_id,
                    "medium",
                    "pacing",
                    "memo_list",
                    "The slide leans toward a memo-like list rather than a presentation surface.",
                    "Too many same-weight lines slow the room down and make the slide forgettable.",
                    "Compress the list, split the thought, or replace the list with a contrast, quote, or proof move.",
                    0.73,
                )
            )

    dominant_signature, dominant_ratio = dominant_surface(slides)
    if dominant_ratio >= 0.6:
        findings.append(
            finding(
                "deck",
                "medium",
                "rhythm",
                "repetitive_surface",
                "Too many slides share the same visible silhouette.",
                "Even strong content feels synthetic when the deck never changes surface rhythm.",
                "Introduce one stronger reset, one proof move, or one image-led change of pace.",
                0.76,
                meta={"signature": dominant_signature, "ratio": round(dominant_ratio, 3)},
            )
        )

    last = slides[-1]
    last_title = " ".join(last["heading_texts"]).strip().lower()
    if last_title in WEAK_CLOSERS or last["closing_role"] == "weak-close":
        findings.append(
            finding(
                last["slide_id"],
                "high",
                "close",
                "weak_close",
                "The ending is generic and does not land with a real action or decision.",
                "The last slide is the most memorable position in the deck.",
                "Replace the generic close with a concrete landing line, ask, or decision request.",
                0.92,
            )
        )

    scores = {
        "headline_strength": clamp_score(10 - generic_heading_count * 2),
        "visible_payload": clamp_score(10 - note_abuse_count * 2 - weak_visible_count * 3),
        "pacing": clamp_score(10 - list_heavy_count * 1.5 - (2 if dominant_ratio >= 0.6 else 0)),
        "closing_quality": clamp_score(6 if any(f["code"] == "weak_close" for f in findings) else 9),
    }
    scores["overall"] = round(sum(scores.values()) / len(scores), 2)
    summary = {
        "slide_count": len(slides),
        "generic_heading_count": generic_heading_count,
        "note_abuse_count": note_abuse_count,
        "weak_visible_count": weak_visible_count,
        "dominant_signature": dominant_signature,
        "dominant_signature_ratio": round(dominant_ratio, 3),
    }
    return findings, {"scores": scores, "summary": summary}


def dominant_surface(slides: list[dict]) -> tuple[str, float]:
    counts: dict[str, int] = {}
    for slide in slides:
        counts[slide["signature"]] = counts.get(slide["signature"], 0) + 1
    signature, count = max(counts.items(), key=lambda item: item[1])
    return signature, count / max(len(slides), 1)


def finding(
    slide_id: str,
    severity: str,
    axis: str,
    code: str,
    problem: str,
    why: str,
    fix: str,
    confidence: float,
    meta: dict | None = None,
) -> dict:
    payload = {
        "slide_id": slide_id,
        "severity": severity,
        "axis": axis,
        "code": code,
        "problem": problem,
        "why_it_matters": why,
        "recommended_fix": fix,
        "confidence": confidence,
    }
    if meta:
        payload["meta"] = meta
    return payload


def clamp_score(value: float) -> float:
    return round(max(0.0, min(10.0, value)), 2)


def main() -> int:
    args = parse_args()
    deck = Path(args.deck)
    manifest = read_json(Path(args.manifest)) if args.manifest else build_manifest(deck)
    findings, review = build_findings(manifest)
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
