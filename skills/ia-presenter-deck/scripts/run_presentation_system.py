#!/usr/bin/env python3
"""Run the local presentation system pipeline on an iA Presenter deck."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parents[2]
STORY_QA_SCRIPT = ROOT / "skills" / "ia-presenter-story-qa" / "scripts" / "review_story.py"
RENDER_SCRIPT = ROOT / "skills" / "ia-presenter-render" / "scripts" / "render_deck.py"
VISUAL_QA_SCRIPT = ROOT / "skills" / "ia-presenter-qa" / "scripts" / "review_visual.py"
sys.path.insert(0, str(SCRIPT_DIR))

from presentation_system import (  # noqa: E402
    apply_fix_plan,
    build_fix_plan,
    build_manifest,
    ensure_package_copy,
    now_utc,
    read_json,
    slugify,
    timestamp_slug,
    write_json,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run Presentation System v1")
    parser.add_argument("--deck", required=True, help="Path to .iapresenter package or markdown source")
    parser.add_argument(
        "--run-root",
        default=".presentation-system/runs",
        help="Root directory for local run artifacts",
    )
    parser.add_argument(
        "--render-mode",
        choices=("images", "html", "both"),
        default="both",
        help="Render export mode to request from iA Presenter",
    )
    parser.add_argument(
        "--auto-fix",
        action="store_true",
        help="Apply one bounded slide-local fix pass and rerun if the first pass produces supported fixes",
    )
    parser.add_argument("--max-iterations", type=int, default=2, help="Maximum review iterations")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = Path(args.deck).resolve()
    run_root = Path(args.run_root).resolve()
    deck_slug = slugify(source.stem)
    run_dir = run_root / deck_slug / timestamp_slug()
    working_dir = run_dir / "working"
    iteration_root = run_dir / "iterations"
    working_deck = ensure_package_copy(source, working_dir)

    iterations: list[dict] = []
    previous_score: float | None = None
    best_iteration = 0
    best_score = -1.0

    for iteration_index in range(args.max_iterations):
        iteration_dir = iteration_root / f"iteration-{iteration_index}"
        iteration_dir.mkdir(parents=True, exist_ok=True)

        manifest_path = iteration_dir / "manifest.json"
        story_review_path = iteration_dir / "story-review.json"
        visual_review_path = iteration_dir / "visual-review.json"
        fix_plan_path = iteration_dir / "fix-plan.json"
        summary_path = iteration_dir / "iteration-summary.json"

        manifest = build_manifest(working_deck)
        write_json(manifest_path, manifest)

        run_python(
            STORY_QA_SCRIPT,
            ["--deck", str(working_deck), "--manifest", str(manifest_path), "--output", str(story_review_path)],
        )
        run_python(
            RENDER_SCRIPT,
            ["--deck", str(working_deck), "--run-dir", str(iteration_dir), "--mode", args.render_mode],
            allow_nonzero=True,
        )
        render_path = iteration_dir / "render" / "render.json"
        render = read_json(render_path)

        run_python(
            VISUAL_QA_SCRIPT,
            ["--manifest", str(manifest_path), "--render", str(render_path), "--output", str(visual_review_path)],
        )
        story_review = read_json(story_review_path)
        visual_review = read_json(visual_review_path)

        fix_plan = build_fix_plan(manifest, story_review, visual_review)
        write_json(fix_plan_path, fix_plan)

        combined_score = round((story_review["scores"]["overall"] + visual_review["scores"]["overall"]) / 2.0, 2)
        iteration_summary = {
            "generated_at": now_utc(),
            "iteration": iteration_index,
            "combined_score": combined_score,
            "render_status": render["status"],
            "story_score": story_review["scores"]["overall"],
            "visual_score": visual_review["scores"]["overall"],
            "fix_action_count": len(fix_plan["actions"]),
        }
        write_json(summary_path, iteration_summary)

        iterations.append(
            {
                "iteration": iteration_index,
                "path": str(iteration_dir),
                "combined_score": combined_score,
                "render_status": render["status"],
                "fix_action_count": len(fix_plan["actions"]),
            }
        )

        if combined_score > best_score:
            best_score = combined_score
            best_iteration = iteration_index

        if not args.auto_fix:
            break
        if render["status"] not in {"ok", "partial"}:
            break
        if not fix_plan["actions"]:
            break
        if previous_score is not None and combined_score <= previous_score:
            break

        applied = apply_fix_plan(working_deck, manifest, fix_plan)
        if not applied:
            break
        previous_score = combined_score

    summary = {
        "generated_at": now_utc(),
        "source_deck": str(source),
        "working_deck": str(working_deck),
        "run_dir": str(run_dir),
        "iterations": iterations,
        "best_iteration": best_iteration,
        "best_score": best_score,
    }
    write_json(run_dir / "summary.json", summary)
    print(json.dumps(summary, indent=2))
    return 0


def run_python(script: Path, args: list[str], allow_nonzero: bool = False) -> subprocess.CompletedProcess[str]:
    completed = subprocess.run(
        [sys.executable, str(script), *args],
        capture_output=True,
        text=True,
        cwd=str(ROOT),
    )
    if completed.returncode != 0 and not allow_nonzero:
        raise RuntimeError((completed.stderr or completed.stdout).strip() or f"{script.name} failed")
    return completed


if __name__ == "__main__":
    raise SystemExit(main())
