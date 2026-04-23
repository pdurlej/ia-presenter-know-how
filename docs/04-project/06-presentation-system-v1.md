# Presentation System v1

> The local system that turns deck generation into a repeatable author -> render -> review -> fix loop.

---

## Why This Exists

Good iA Presenter output cannot be judged only from Markdown.

The same `text.md` can:
- render cleanly
- produce accidental splits
- strand a proof table
- leak syntax on the slide
- look human or synthetic depending on the actual exported result

The system therefore treats presentation work as a local pipeline, not a single prompt.

---

## Core Roles

V1 separates five roles:
- author: creates or edits the `.iapresenter` package
- render: exports real artifacts from the installed iA Presenter app
- story QA: reviews logic, pacing, visible payload, and note abuse
- visual QA: reviews rendered slides for composition, readability, and image quality
- fix: applies only slide-local corrections, then reruns

The repository keeps `ia-presenter-deck` as the authoring/orchestration layer.

---

## Local Workspace

Runs are stored under:

```text
.presentation-system/runs/<deck-slug>/<timestamp>/
```

This workspace is gitignored by default.

Typical run contents:

```text
working/<deck>.iapresenter/
iterations/iteration-0/
  manifest.json
  render/render.json
  story-review.json
  visual-review.json
  fix-plan.json
summary.json
```

Raw local artifacts stay here because they may contain:
- private deck copies
- rendered exports
- screenshots
- local review evidence

---

## Render Strategy

V1 is export-first.

Primary path:
1. open the deck in the installed macOS app
2. export slide images and/or HTML
3. review the exported result

Why export-first:
- the app itself decides the final responsive layout
- exported images are cheaper to inspect than live window capture
- HTML export can be inspected or re-rendered later if needed

Live preview capture is a fallback, not the mainline path.

---

## Review Artifacts

### `manifest.json`

Per-slide intent contract:
- `slide_id`
- `job`
- `visible_payload`
- `layout_intent`
- `image_intent`
- `closing_role`
- `notes_policy`

### `story-review.json`

Checks:
- headline strength
- pacing
- note abuse
- weak closes
- repetitive visible silhouettes

### `visual-review.json`

Checks:
- syntax leakage
- dead whitespace
- accidental split imbalance
- stranded proof objects
- weak decorative images

### `fix-plan.json`

Only bounded, slide-local actions are allowed in v1.

Examples:
- promote a hidden claim
- merge cells that created a weak split
- widen a proof stack
- remove a decorative image

---

## Correction Loop

The correction loop is intentionally bounded:
- maximum two iterations per run
- stop if score does not improve
- stop if render fails
- never do a freeform whole-deck rewrite after QA

This keeps the system debuggable. A failing slide should have a named reason and a named fix.

---

## Permission Requirements

The render layer currently depends on macOS UI automation.

Required:
- `Accessibility` permission for `osascript` or the host terminal app

Without that permission:
- render fails fast
- `render.json` records the block and remediation
- the deck is not treated as done

---

## BMAD / BMADX Positioning

This initiative is treated as a system change, not a prompt tweak.

Repository artifacts:
- `_bmad-output/project-context.md`
- `_bmad-output/presentation-system-v1/prd.md`
- `_bmad-output/presentation-system-v1/architecture.md`
- `AGENTS.md`
- `bmadx-*`

Rule:
- BMAD owns product, architecture, and durable project context
- BMADX supplies routing, verification discipline, and rollout scaffolding
