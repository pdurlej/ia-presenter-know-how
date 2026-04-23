---
name: "ia-presenter-render"
description: "Render iA Presenter decks through the installed macOS app, exporting HTML and/or slide images into a local run workspace for review."
---

# iA Presenter Render

Use this skill when:
- a deck needs real render artifacts before review
- Codex should export an `.iapresenter` deck from the installed `iA Presenter` app
- the presentation system needs screenshots or exported HTML for downstream QA

This skill is macOS-local and app-driven. It does not approximate layout from Markdown.

Read first:
- `references/CLI.md`

## What it does

1. Opens the deck in the installed `iA Presenter` app
2. Uses UI automation to export:
   - slide images
   - HTML package
3. Writes stable render artifacts into the run workspace
4. Fails fast when `Accessibility` permission for `osascript` is missing

## Contract

Inputs:
- `.iapresenter` deck path
- run directory
- render mode: `images`, `html`, or `both`

Outputs:
- `render.json`
- `render/export-images/` when images export succeeds
- `render/export-html/` when HTML export succeeds

## Notes

- V1 assumes the app label text is English: `Share Presentation`, `HTML`, `Images`.
- Export-first rendering is the primary path.
- Live preview/window capture is a fallback for later versions, not the mainline path.
