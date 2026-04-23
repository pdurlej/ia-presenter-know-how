---
name: "ia-presenter-qa"
description: "Review rendered iA Presenter slides or screenshots before publication. Use when Codex needs to inspect slide output for visual defects, rendering mistakes, weak composition, bad rhythm, or aesthetic regressions that are only obvious after rendering."
---

# iA Presenter QA

Use this skill when:
- the user shares screenshots of rendered slides
- a deck needs a pre-publication QA pass
- Codex should decide what looks broken, weak, or aesthetically off after rendering

This skill is for rendered output, not just Markdown correctness.

Read first:
- `references/CHECKLIST.md`

Automation entrypoint:
- `scripts/review_visual.py`

## What to check

1. Rendering defects
2. Broken syntax leaking onto the slide
3. Awkward image/text composition
4. Dead whitespace or accidental columns
5. Weak contrast or unreadable overlays
6. Repeated silhouettes across thumbnails
7. Stock imagery that cheapens the deck

## Output format

When reviewing:
- list the most important visual issues first
- explain the likely cause
- propose the smallest fix that improves the slide

If a slide is technically valid but aesthetically weak, say so directly.
