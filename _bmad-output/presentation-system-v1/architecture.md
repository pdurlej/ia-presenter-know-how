# Presentation System v1 Architecture

## Summary

The system is a local orchestration layer built around existing repo skills. It creates a per-run working copy, derives structured slide metadata, renders the deck through iA Presenter, reviews both content and rendered output, then applies bounded local corrections.

## Components

### 1. Orchestrator

Entry point for a local run.

Responsibilities:
- create run directory
- copy or reuse the working deck
- call manifest generation
- call render
- call story review
- call visual review
- build fix plan
- optionally apply bounded fixes and rerun

### 2. Manifest Builder

Input:
- `.iapresenter/text.md`

Output:
- `manifest.json`

Fields per slide:
- `slide_id`
- `job`
- `visible_payload`
- `layout_intent`
- `image_intent`
- `closing_role`
- `notes_policy`

### 3. Render Layer

Primary mode:
- iA Presenter export to `HTML` or `Images`

Fallback mode:
- live preview or presentation-window capture

Responsibilities:
- open the deck in `net.ia.presenter`
- fail fast on missing Accessibility or export prerequisites
- emit exported artifacts into the run directory
- write `render.json`

### 4. Story Review

Input:
- `text.md`
- `manifest.json`

Output:
- `story-review.json`

Focus:
- logic
- readability
- pacing
- tension
- visible payload strength
- notes abuse
- closing quality

### 5. Visual Review

Input:
- render artifacts
- `manifest.json`

Output:
- `visual-review.json`

Focus:
- composition
- dead whitespace
- stranded proof tables
- weak image panels
- crop or density issues
- slideument smell in rendered form

### 6. Fix Planner and Fixer

Input:
- review JSON files
- working deck text

Output:
- `fix-plan.json`
- updated working copy if `--auto-fix` is enabled

Supported v1 fixes:
- promote hidden claims into visible payload
- merge weak split cells
- merge title and table into a full-width proof stack
- remove weak decorative images
- strengthen weak closing slides when a safe landing exists

Unsupported v1 fixes:
- unconstrained whole-deck rewrites
- theme redesign
- freeform image art direction

## Data Layout

```text
.presentation-system/
└── runs/
    └── <deck-slug>/
        └── <timestamp>/
            ├── working/
            │   └── <deck>.iapresenter/
            ├── iteration-0/
            │   ├── manifest.json
            │   ├── render.json
            │   ├── story-review.json
            │   ├── visual-review.json
            │   ├── fix-plan.json
            │   └── renders/
            ├── iteration-1/
            └── summary.json
```

## Failure Modes

- missing Accessibility permission
- missing Screen Recording permission for fallback capture
- iA Presenter export flow changed by UI update
- exported artifacts absent or incomplete
- auto-fix does not improve review scores

## Failure Policy

- never silently continue after render failure
- always write structured status to JSON
- stop after two fix iterations or earlier on score regression
- keep the original tracked deck untouched; mutate only the run-local working copy
