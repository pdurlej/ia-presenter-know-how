# iA Presenter Know-How — Claude Code Context

This repository is a structured Markdown corpus for generating iA Presenter presentations with LLMs.

## Quick orientation

- `syntax/00-complete-reference.md` — master syntax reference (read first for any generation task)
- `examples/01-basic.md` — minimal correct deck
- `examples/02-complex.md` — full-featured deck showing all major surface patterns
- `examples/03-anti-patterns.md` — common mistakes with corrected versions
- `skills/ia-presenter-deck/SKILL.md` — canonical generation skill (read its `references/` directory for workflow, rubric, templates, layout heuristics, and surface patterns)
- `golden-candidates/` — real `.iapresenter` package directories for iterative review
- `reference-decks/` — stable public reference decks, including future anonymized derivatives of private source material

## Core conventions

1. `#` and `##` create the cover slide. Do not use `#` for mid-deck sections.
2. `---` starts a new slide.
3. `##` is the default content-slide title after `---`.
4. `###` and `####` create heading stacks within slides.
5. TAB-prefixed text (`\t`) is visible to the audience. Flush-left text is speaker notes.
6. The visible slide surface must carry real meaning — do not hide the whole argument in notes.
7. End with a real action, decision, or landing line. Never end on "Thank you" or "Questions?".
8. Vary the visible surface across the deck: heading stacks, contrasts, quotes, tables, sequences, one-line landings.

## .iapresenter package format

A deck is a directory, not a single file:
```
example.iapresenter/
├── info.json
└── text.md
```

## When generating or reviewing decks

1. Load `syntax/00-complete-reference.md` first
2. Load one example from `examples/` for pattern reference
3. Follow the workflow in `skills/ia-presenter-deck/references/WORKFLOW.md`
4. Score the result against `skills/ia-presenter-deck/references/RUBRIC.md`
5. Check against `examples/03-anti-patterns.md` before delivering

## When a user shares a strong private deck

1. Treat the source deck as private by default
2. Do not commit the raw source deck into the public repo
3. Anonymize or rewrite it before publication
4. Publish safe derivatives under `reference-decks/`
5. Use `docs/04-project/05-anonymized-deck-ingestion.md` as the operating checklist

## What not to do

- Do not generate PowerPoint, Marp, or generic slide formats
- Do not create a single file named `.iapresenter` — it must be a package directory
- Do not use spaces instead of TABs for slide content
- Do not produce decks where every slide has the same title-plus-bullets shape
