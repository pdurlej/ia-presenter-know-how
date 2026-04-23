#!/usr/bin/env python3
"""Shared helpers for the local iA Presenter presentation system."""

from __future__ import annotations

import json
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

GENERIC_TITLES = {
    "background",
    "overview",
    "summary",
    "context",
    "key metrics",
    "key priorities",
    "next steps",
    "update",
    "agenda",
}

WEAK_CLOSERS = {
    "thank you",
    "questions",
    "discussion",
    "q&a",
}

IMAGE_EXTENSIONS = (".png", ".jpg", ".jpeg", ".webp", ".gif", ".tiff", ".bmp")
IMAGE_ATTR_KEYS = {
    "background",
    "filter",
    "opacity",
    "size",
    "x",
    "y",
    "title",
    "caption",
}


def now_utc() -> str:
    return datetime.now(timezone.utc).isoformat()


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = re.sub(r"-{2,}", "-", value)
    return value.strip("-") or "deck"


def timestamp_slug() -> str:
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def deck_text_path(deck_path: Path) -> Path:
    if deck_path.is_dir():
        return deck_path / "text.md"
    return deck_path


def read_deck_text(deck_path: Path) -> str:
    text_path = deck_text_path(deck_path)
    return text_path.read_text(encoding="utf-8")


def ensure_package_copy(source: Path, target_root: Path) -> Path:
    """Copy a package or markdown source into a working `.iapresenter` package."""
    target_root.mkdir(parents=True, exist_ok=True)
    if source.is_dir():
        target = target_root / source.name
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(source, target)
        return target

    stem = source.stem
    package = target_root / f"{stem}.iapresenter"
    if package.exists():
        shutil.rmtree(package)
    package.mkdir(parents=True, exist_ok=True)
    (package / "text.md").write_text(source.read_text(encoding="utf-8"), encoding="utf-8")
    info = {
        "name": stem,
        "createdBy": "presentation-system-v1",
    }
    write_json(package / "info.json", info)
    return package


def split_slides(text: str) -> list[list[str]]:
    slides: list[list[str]] = []
    current: list[str] = []
    for line in text.splitlines():
        if line.strip() == "---":
            slides.append(current)
            current = []
        else:
            current.append(line)
    slides.append(current)
    return slides


def split_cells(lines: list[str]) -> list[list[str]]:
    cells: list[list[str]] = []
    current: list[str] = []
    for line in lines:
        if line.strip():
            current.append(line)
        else:
            if current:
                cells.append(current)
                current = []
    if current:
        cells.append(current)
    return cells


def line_type(raw: str) -> str:
    stripped = raw.strip()
    if not stripped:
        return "blank"

    if raw.startswith("\t"):
        visible = stripped
        if visible.startswith("|"):
            return "table"
        if visible.startswith(">"):
            return "quote"
        return "visible"

    if stripped.startswith("#"):
        return "heading"
    if stripped.startswith("|"):
        return "table"
    if is_image_reference(stripped):
        return "image"
    if is_attribute_line(stripped):
        return "attribute"
    return "hidden"


def is_image_reference(text: str) -> bool:
    lower = text.lower()
    if lower.startswith(("http://", "https://", "/")) and lower.endswith(IMAGE_EXTENSIONS):
        return True
    return False


def is_attribute_line(text: str) -> bool:
    if ":" not in text:
        return False
    key = text.split(":", 1)[0].strip().lower()
    return key in IMAGE_ATTR_KEYS


def heading_level(raw: str) -> int:
    stripped = raw.lstrip()
    return len(stripped) - len(stripped.lstrip("#"))


def extract_text(raw: str) -> str:
    stripped = raw.strip()
    if raw.startswith("\t"):
        stripped = raw.lstrip("\t").strip()
    if stripped.startswith("#"):
        stripped = stripped.lstrip("#").strip()
    if stripped.startswith(">"):
        stripped = stripped[1:].strip()
    return stripped


def is_ordered_item(text: str) -> bool:
    return bool(re.match(r"^\d+\.\s", text))


def is_list_like(text: str) -> bool:
    return bool(re.match(r"^(\d+\.\s|[-*]\s)", text))


def infer_surface(slide: dict[str, Any], index: int, total: int) -> str:
    headings = slide["heading_texts"]
    image_count = len(slide["image_urls"])
    has_background = slide["has_background_image"]
    has_table = bool(slide["table_rows"])
    has_quote = bool(slide["quotes"])
    visible = slide["visible_lines"]
    ordered = [v for v in visible if is_ordered_item(v)]
    cells = slide["cell_count"]
    joined_heading = " ".join(headings).lower()

    if index == 1 and slide["heading_levels"] and slide["heading_levels"][0] == 1:
        return "cover"
    if index == total and len(headings) <= 2 and not slide["hidden_lines"]:
        return "landing"
    if has_background:
        return "image-background"
    if image_count and cells >= 2:
        return "image-panel-split"
    if has_table and cells <= 1:
        return "full-width-proof"
    if has_table:
        return "proof-table"
    if has_quote:
        return "quote-led"
    if " vs " in joined_heading or any(h.upper() == "VS" for h in headings):
        return "comparison"
    if ordered:
        return "sequence"
    if slide["heading_levels"] and slide["heading_levels"][0] == 1:
        return "section-reset"
    if headings:
        return "heading-stack"
    return "stacked"


def infer_layout_intent(slide: dict[str, Any], surface: str) -> str:
    if surface in {"cover", "landing", "section-reset"}:
        return surface
    if surface in {"image-background", "image-panel-split", "comparison", "full-width-proof", "proof-table", "quote-led"}:
        return surface
    if surface == "sequence":
        return "agenda-sequence"
    if slide["cell_count"] >= 2:
        return "side-by-side"
    return "stacked"


def infer_visible_payload(slide: dict[str, Any], surface: str) -> str:
    headings = slide["heading_texts"]
    visible = slide["visible_lines"]
    if headings:
        if surface in {"cover", "landing", "section-reset"} and len(headings) >= 2:
            return " / ".join(headings[:2])
        if len(headings) >= 2:
            return " / ".join(headings[:2])
        return headings[0]
    if surface in {"full-width-proof", "proof-table"} and slide["table_rows"]:
        header = extract_table_header(slide["table_rows"])
        return f"Proof table: {header}" if header else "Proof table"
    if visible:
        return visible[0]
    if slide["quotes"]:
        return slide["quotes"][0]
    return ""


def extract_table_header(rows: list[str]) -> str:
    for row in rows:
        cells = [cell.strip() for cell in row.strip("|").split("|")]
        meaningful = [cell for cell in cells if cell and not set(cell) <= {"-"}]
        if meaningful:
            return " | ".join(meaningful[:3])
    return ""


def infer_job(slide: dict[str, Any], surface: str, index: int, total: int) -> str:
    if surface == "cover":
        return "cover"
    if index == total:
        return "close"
    if surface in {"full-width-proof", "proof-table"}:
        return "proof"
    if surface in {"comparison", "section-reset"}:
        return "reframe"
    if surface in {"image-background", "image-panel-split"}:
        return "scene"
    if index == 2:
        return "setup"
    return "body"


def infer_image_intent(slide: dict[str, Any], surface: str) -> str | None:
    if not slide["image_urls"]:
        return None
    if surface == "image-background":
        return "scene-setting"
    if surface == "image-panel-split":
        return "context-panel"
    return "visual-support"


def infer_closing_role(slide: dict[str, Any], index: int, total: int) -> str:
    if index != total:
        return "body"
    payload = " ".join(slide["heading_texts"]).strip().lower()
    if payload in WEAK_CLOSERS:
        return "weak-close"
    if any(word in payload for word in ("start", "ship", "decide", "bring", "stay", "measure", "earn")):
        return "landing"
    return "close"


def build_manifest(deck_path: Path) -> dict[str, Any]:
    text = read_deck_text(deck_path)
    raw_slides = split_slides(text)
    slides: list[dict[str, Any]] = []
    total = len(raw_slides)

    for index, raw_lines in enumerate(raw_slides, start=1):
        heading_lines = [line for line in raw_lines if line_type(line) == "heading"]
        visible_lines = [extract_text(line) for line in raw_lines if line_type(line) == "visible"]
        hidden_lines = [extract_text(line) for line in raw_lines if line_type(line) == "hidden"]
        table_rows = [extract_text(line) for line in raw_lines if line_type(line) == "table"]
        quotes = [extract_text(line) for line in raw_lines if line_type(line) == "quote"]
        image_urls = [line.strip() for line in raw_lines if line_type(line) == "image"]
        attributes = [line.strip() for line in raw_lines if line_type(line) == "attribute"]
        heading_texts = [extract_text(line) for line in heading_lines]
        heading_levels = [heading_level(line) for line in heading_lines]
        cells = split_cells(raw_lines)
        has_background_image = any(attr.lower() == "background: true" for attr in attributes)

        slide: dict[str, Any] = {
            "slide_id": f"slide-{index:03d}",
            "index": index,
            "raw_lines": raw_lines,
            "cell_count": len(cells),
            "cells": cells,
            "heading_texts": heading_texts,
            "heading_levels": heading_levels,
            "visible_lines": visible_lines,
            "hidden_lines": hidden_lines,
            "table_rows": table_rows,
            "quotes": quotes,
            "image_urls": image_urls,
            "attributes": attributes,
            "has_background_image": has_background_image,
        }
        surface = infer_surface(slide, index, total)
        slide["surface"] = surface
        slide["layout_intent"] = infer_layout_intent(slide, surface)
        slide["visible_payload"] = infer_visible_payload(slide, surface)
        slide["job"] = infer_job(slide, surface, index, total)
        slide["image_intent"] = infer_image_intent(slide, surface)
        slide["closing_role"] = infer_closing_role(slide, index, total)
        slide["notes_policy"] = "suspicious" if hidden_lines else "visible-first"
        slide["signature"] = build_signature(slide)
        slides.append(slide)

    return {
        "generated_at": now_utc(),
        "deck_path": str(deck_path.resolve()),
        "slide_count": total,
        "slides": [
            {
                "slide_id": slide["slide_id"],
                "index": slide["index"],
                "job": slide["job"],
                "visible_payload": slide["visible_payload"],
                "layout_intent": slide["layout_intent"],
                "image_intent": slide["image_intent"],
                "closing_role": slide["closing_role"],
                "notes_policy": slide["notes_policy"],
                "surface": slide["surface"],
                "signature": slide["signature"],
                "cell_count": slide["cell_count"],
                "heading_texts": slide["heading_texts"],
                "visible_line_count": len(slide["visible_lines"]),
                "hidden_line_count": len(slide["hidden_lines"]),
                "table_row_count": len(slide["table_rows"]),
                "image_count": len(slide["image_urls"]),
            }
            for slide in slides
        ],
        "debug": {"raw_slides": slides},
    }


def build_signature(slide: dict[str, Any]) -> str:
    parts = [
        slide["surface"],
        f"h{len(slide['heading_texts'])}",
        f"v{len(slide['visible_lines'])}",
        f"t{len(slide['table_rows'])}",
        f"i{len(slide['image_urls'])}",
        f"c{slide['cell_count']}",
    ]
    return "|".join(parts)


def find_slide_debug(manifest: dict[str, Any], slide_id: str) -> dict[str, Any]:
    for slide in manifest["debug"]["raw_slides"]:
        if slide["slide_id"] == slide_id:
            return slide
    raise KeyError(slide_id)


def merge_review_findings(*review_docs: dict[str, Any]) -> list[dict[str, Any]]:
    findings: list[dict[str, Any]] = []
    for review in review_docs:
        findings.extend(review.get("findings", []))
    return findings


def build_fix_plan(
    manifest: dict[str, Any],
    story_review: dict[str, Any],
    visual_review: dict[str, Any],
) -> dict[str, Any]:
    actions: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()

    mapping = {
        "notes_substance": "promote_hidden_claim",
        "weak_hidden_slide": "promote_hidden_claim",
        "stranded_proof_table": "merge_title_table_stack",
        "split_imbalance": "merge_cells_for_stack",
        "dead_whitespace": "merge_cells_for_stack",
        "weak_decorative_image": "remove_decorative_image",
    }

    for finding in merge_review_findings(story_review, visual_review):
        code = finding.get("code")
        slide_id = finding.get("slide_id")
        action = mapping.get(code)
        if not action or not slide_id or slide_id == "deck":
            continue
        key = (slide_id, action)
        if key in seen:
            continue
        seen.add(key)
        actions.append(
            {
                "slide_id": slide_id,
                "action": action,
                "source": finding.get("axis"),
                "reason_code": code,
                "supported": True,
                "problem": finding.get("problem"),
                "recommended_fix": finding.get("recommended_fix"),
                "confidence": finding.get("confidence", 0.5),
            }
        )

    return {
        "generated_at": now_utc(),
        "deck_path": manifest["deck_path"],
        "max_iterations": 2,
        "actions": actions,
    }


def apply_fix_plan(deck_path: Path, manifest: dict[str, Any], fix_plan: dict[str, Any]) -> list[dict[str, Any]]:
    text_path = deck_text_path(deck_path)
    slides = split_slides(text_path.read_text(encoding="utf-8"))
    applied: list[dict[str, Any]] = []

    for action in fix_plan.get("actions", []):
        slide_id = action["slide_id"]
        index = int(slide_id.split("-")[-1]) - 1
        if index < 0 or index >= len(slides):
            continue
        updated = apply_slide_action(slides[index], action["action"])
        if updated != slides[index]:
            slides[index] = updated
            applied.append(action)

    rebuilt = "\n---\n".join("\n".join(slide).rstrip() for slide in slides).rstrip() + "\n"
    text_path.write_text(rebuilt, encoding="utf-8")
    return applied


def apply_slide_action(slide_lines: list[str], action: str) -> list[str]:
    if action == "promote_hidden_claim":
        return promote_hidden_claim(slide_lines)
    if action == "merge_title_table_stack":
        return merge_title_table_stack(slide_lines)
    if action == "merge_cells_for_stack":
        return merge_cells_for_stack(slide_lines)
    if action == "remove_decorative_image":
        return remove_decorative_image(slide_lines)
    return slide_lines


def promote_hidden_claim(slide_lines: list[str]) -> list[str]:
    new_lines: list[str] = []
    promoted = 0
    for raw in slide_lines:
        kind = line_type(raw)
        if kind != "hidden":
            new_lines.append(raw)
            continue
        text = extract_text(raw)
        if promoted == 0 and len(text) <= 96:
            new_lines.append(f"#### {text}")
            promoted += 1
            continue
        if promoted < 3 and len(text) <= 96:
            new_lines.append(f"\t{text}")
            promoted += 1
            continue
        # Drop trailing hidden lines in auto-fix mode. The purpose is to force a stronger visible payload.
    return trim_extra_blank_lines(new_lines)


def merge_title_table_stack(slide_lines: list[str]) -> list[str]:
    new_lines: list[str] = []
    for idx, raw in enumerate(slide_lines):
        if not raw.strip():
            prev = previous_nonblank(slide_lines, idx)
            nxt = next_nonblank(slide_lines, idx)
            if prev and nxt and line_type(prev) == "heading" and line_type(nxt) == "table":
                continue
        new_lines.append(raw)
    return trim_extra_blank_lines(new_lines)


def merge_cells_for_stack(slide_lines: list[str]) -> list[str]:
    new_lines: list[str] = []
    for idx, raw in enumerate(slide_lines):
        if not raw.strip():
            prev = previous_nonblank(slide_lines, idx)
            nxt = next_nonblank(slide_lines, idx)
            if not prev or not nxt:
                continue
            if line_type(prev) in {"image", "attribute"} or line_type(nxt) == "attribute":
                new_lines.append(raw)
                continue
            continue
        new_lines.append(raw)
    return trim_extra_blank_lines(new_lines)


def remove_decorative_image(slide_lines: list[str]) -> list[str]:
    new_lines: list[str] = []
    skipping = False
    removed = False
    for raw in slide_lines:
        kind = line_type(raw)
        if kind == "image" and not removed:
            skipping = True
            removed = True
            continue
        if skipping and kind == "attribute":
            continue
        if skipping and kind == "blank":
            skipping = False
            continue
        skipping = False
        new_lines.append(raw)
    return trim_extra_blank_lines(new_lines)


def previous_nonblank(lines: list[str], index: int) -> str | None:
    for candidate in reversed(lines[:index]):
        if candidate.strip():
            return candidate
    return None


def next_nonblank(lines: list[str], index: int) -> str | None:
    for candidate in lines[index + 1 :]:
        if candidate.strip():
            return candidate
    return None


def trim_extra_blank_lines(lines: list[str]) -> list[str]:
    trimmed: list[str] = []
    previous_blank = False
    for raw in lines:
        is_blank = not raw.strip()
        if is_blank and previous_blank:
            continue
        trimmed.append(raw)
        previous_blank = is_blank
    while trimmed and not trimmed[0].strip():
        trimmed.pop(0)
    while trimmed and not trimmed[-1].strip():
        trimmed.pop()
    return trimmed

