# Repo Skills

This repository can include canonical skills for Codex or other LLM environments.

## Included

- `ia-presenter-deck/`: repo-first skill for creating and improving `.iapresenter` decks using the corpus, anti-patterns, and Golden Deck candidates in this repository
- `ia-presenter-render/`: export-first render skill that drives the installed macOS app and writes rendered artifacts into the local run workspace
- `ia-presenter-story-qa/`: structured story review for logic, pacing, visible payload, and note abuse
- `ia-presenter-qa/`: rendered visual QA over exported slide images

## Local Presentation System

The repository also contains a local-only run workspace contract:
- `.presentation-system/runs/<deck-slug>/<timestamp>/`

This workspace is gitignored. It stores:
- a working deck copy
- `manifest.json`
- `render.json`
- `story-review.json`
- `visual-review.json`
- `fix-plan.json`

## Installation Note

The repository copy is the source of truth.

If you want to use one of these skills directly in Codex, copy or install it into `~/.codex/skills/`. The installed copy is a deployment location, not the canonical authoring location.
