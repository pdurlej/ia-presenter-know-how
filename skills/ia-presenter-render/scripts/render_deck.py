#!/usr/bin/env python3
"""Export rendered artifacts from the installed iA Presenter app."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
DECK_SCRIPTS = SCRIPT_DIR.parents[1] / "ia-presenter-deck" / "scripts"
sys.path.insert(0, str(DECK_SCRIPTS))

from presentation_system import now_utc, write_json  # noqa: E402

APP_PATH = Path("/Applications/iA Presenter.app")
APP_BUNDLE_ID = "net.ia.presenter"
APP_PROCESS_NAME = "iA Presenter"
EXPORT_SCRIPT = SCRIPT_DIR / "export_with_ui.applescript"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render an iA Presenter deck through the macOS app")
    parser.add_argument("--deck", required=True, help="Path to .iapresenter package")
    parser.add_argument("--run-dir", required=True, help="Run directory where render artifacts will be written")
    parser.add_argument(
        "--mode",
        choices=("images", "html", "both"),
        default="both",
        help="Which app-native export modes to run",
    )
    parser.add_argument("--timeout", type=int, default=90, help="Seconds to wait for each export")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    deck = Path(args.deck).resolve()
    run_dir = Path(args.run_dir).resolve()
    render_dir = run_dir / "render"
    render_dir.mkdir(parents=True, exist_ok=True)

    payload = {
        "generated_at": now_utc(),
        "deck_path": str(deck),
        "app_bundle_id": APP_BUNDLE_ID,
        "mode": args.mode,
        "status": "pending",
        "permissions": {
            "accessibility": False,
            "screen_recording": None,
        },
        "artifacts": {},
        "screenshots": [],
    }

    if not APP_PATH.exists():
        payload["status"] = "blocked"
        payload["error"] = "iA Presenter is not installed at /Applications/iA Presenter.app"
        emit(render_dir / "render.json", payload)
        return 1

    ok, reason = check_accessibility()
    payload["permissions"]["accessibility"] = ok
    if not ok:
        payload["status"] = "blocked"
        payload["error"] = reason
        payload["remediation"] = [
            "Grant Accessibility permission to osascript or the host terminal app in System Settings > Privacy & Security > Accessibility.",
            "Retry the same render command after granting permission.",
        ]
        emit(render_dir / "render.json", payload)
        return 2

    export_modes = ["images", "html"] if args.mode == "both" else [args.mode]
    overall_ok = False
    any_failed = False

    for export_kind in export_modes:
        output_dir = render_dir / f"export-{export_kind}"
        reset_output_dir(output_dir)
        result = run_export(deck, export_kind, output_dir, args.timeout)
        payload["artifacts"][export_kind] = result
        if result["status"] == "ok":
            overall_ok = True
            if export_kind == "images":
                payload["screenshots"] = result["files"]
        else:
            any_failed = True

    if overall_ok and not any_failed:
        payload["status"] = "ok"
    elif overall_ok:
        payload["status"] = "partial"
    else:
        payload["status"] = "error"

    emit(render_dir / "render.json", payload)
    return 0 if overall_ok else 1


def emit(path: Path, payload: dict) -> None:
    write_json(path, payload)
    print(json.dumps(payload, indent=2))


def reset_output_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def check_accessibility() -> tuple[bool, str | None]:
    probe = 'tell application "System Events" to tell process "Finder" to count of windows'
    completed = subprocess.run(
        ["osascript", "-e", probe],
        capture_output=True,
        text=True,
    )
    if completed.returncode == 0:
        return True, None
    stderr = (completed.stderr or "").strip()
    if not stderr:
        stderr = "Accessibility permission for UI scripting is unavailable."
    return False, stderr


def run_export(deck: Path, export_kind: str, output_dir: Path, timeout: int) -> dict:
    started_at = now_utc()
    env = dict(os.environ)
    try:
        completed = subprocess.run(
            ["osascript", str(EXPORT_SCRIPT), str(deck), export_kind, str(output_dir)],
            capture_output=True,
            text=True,
            env=env,
            timeout=timeout + 15,
        )
    except subprocess.TimeoutExpired:
        return {
            "kind": export_kind,
            "status": "error",
            "started_at": started_at,
            "finished_at": now_utc(),
            "error": f"{export_kind} export timed out while driving the app UI.",
            "output_dir": str(output_dir),
            "files": [],
        }
    if completed.returncode != 0:
        return {
            "kind": export_kind,
            "status": "error",
            "started_at": started_at,
            "finished_at": now_utc(),
            "error": (completed.stderr or completed.stdout).strip() or "Export failed.",
            "output_dir": str(output_dir),
            "files": [],
        }

    files = wait_for_export(output_dir, export_kind, timeout)
    if not files:
        return {
            "kind": export_kind,
            "status": "error",
            "started_at": started_at,
            "finished_at": now_utc(),
            "error": f"{export_kind} export finished but no files appeared in {output_dir}",
            "output_dir": str(output_dir),
            "files": [],
        }

    return {
        "kind": export_kind,
        "status": "ok",
        "started_at": started_at,
        "finished_at": now_utc(),
        "output_dir": str(output_dir),
        "file_count": len(files),
        "files": [str(path) for path in files],
    }


def wait_for_export(output_dir: Path, export_kind: str, timeout: int) -> list[Path]:
    deadline = time.time() + timeout
    while time.time() < deadline:
        files = collect_export_files(output_dir, export_kind)
        if files:
            return files
        time.sleep(1)
    return []


def collect_export_files(output_dir: Path, export_kind: str) -> list[Path]:
    if export_kind == "images":
        matches = sorted(
            path for path in output_dir.rglob("*")
            if path.is_file() and path.suffix.lower() in {".png", ".jpg", ".jpeg", ".webp"}
        )
        return matches
    if export_kind == "html":
        matches = sorted(path for path in output_dir.rglob("*.html") if path.is_file())
        return matches
    return []


if __name__ == "__main__":
    raise SystemExit(main())
