# Presentation System v1 PRD

## Summary

Build a local presentation system around iA Presenter so deck generation becomes inspectable, reviewable, and correctable without requiring the user to provide screenshots for every iteration.

## Users

- maintainer using Codex locally
- future agents operating in this repo
- the maintainer's local workflow for private decks and public derivatives

## Problems To Solve

1. Generated decks are improving, but quality is not repeatable.
2. Rendered output is the real product surface, yet the system cannot review it cheaply.
3. Notes abuse, weak splits, and synthetic rhythm need structured checks.
4. Learning from private decks must stay local and safe.

## Goals

- add a run-based local workspace for deck authoring and review
- emit structured slide metadata that makes QA and fixing debuggable
- add a local render step that uses iA Presenter rather than fake browser output
- separate story review from visual review
- support bounded, slide-local auto-fixes

## Non-Goals

- headless Linux support
- CI rendering
- public publishing automation
- full autonomous visual art direction without review

## Functional Requirements

1. The system accepts an existing `.iapresenter` package or a deck markdown source.
2. The system creates a local run directory under `.presentation-system/runs/...`.
3. The system writes `manifest.json` with one record per slide.
4. The system renders deck output using an iA Presenter export or preview mode.
5. The system writes `render.json` with artifact paths and status.
6. The system writes `story-review.json` with structured findings.
7. The system writes `visual-review.json` with structured findings from rendered artifacts.
8. The system writes `fix-plan.json` mapping findings to bounded local fixes.
9. The system can apply up to two auto-fix iterations to a working copy.

## Quality Requirements

- render failures must be explicit and actionable
- review outputs must be machine-readable JSON
- slide-local fixes must be reproducible and limited in scope
- local-only learning data must never enter tracked files

## Success Criteria

- end-to-end runs work on the three public candidate decks when local permissions allow rendering
- render permission failures explain exactly what is missing
- story QA flags hidden-deck anti-patterns
- visual QA flags common composition failures
- at least one automated public-deck test shows a measurable improvement after auto-fix
