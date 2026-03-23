# Repository Overview

> What this repository is, how it is structured, and how to use it as an LLM-first package for iA Presenter.

---

## What This Repository Is

This repository is a compact package for generating better iA Presenter decks with LLMs.

It combines three layers:
- corpus: syntax, examples, tips, and source-derived notes
- skill: a canonical generation workflow under `skills/ia-presenter-deck/`
- iteration loop: candidate decks under `golden-candidates/` that can evolve into reusable Golden Deck patterns

The project is optimized first for:
- prompt assembly
- local skill workflows
- retrieval and evaluation
- iterative deck improvement in real iA Presenter previews

It is still readable by humans, but the repo is not positioned as a normal end-user tutorial site.

---

## Main Repository Areas

### `syntax/`

Contains the working syntax reference used by this corpus.

Start here if you need:
- the heading conventions
- TAB-based visible text rules
- examples of tables, images, or columns

Primary file:
- `syntax/00-complete-reference.md`

### `examples/`

Contains compact examples and anti-patterns.

Use these files to:
- sanity-check generated output
- see how slide-visible text differs from speaker notes
- avoid common mistakes such as weak splits, walls of text, or meaningless visuals

### `docs/01-course/`

Tutorial-style material that explains how to use iA Presenter.

### `docs/02-tips/`

Rhetorical and practical guidance around delivery, visuals, Markdown, and presentation craft.

### `docs/03-videos/`

Notes derived from videos. Coverage is intentionally uneven. Some files are transcript-based notes, while others are summaries or duplicate-transcript notes.

### `skills/`

Contains repo-first skills. Right now the important one is:
- `skills/ia-presenter-deck/`

This is the canonical drafting workflow for creating or improving `.iapresenter` decks using this corpus.

### `golden-candidates/`

Contains working candidate decks.

These are not polished final presentations. They are the place where style, pacing, visible slide surfaces, and reusable narrative moves are tested before promoting anything to Golden Deck status.

---

## Intended Users

### LLM builders

Use the repository as:
- a retrieval corpus
- a local skill dependency
- a benchmark set for generated deck quality

### Human editors

Use the repository as:
- a syntax and style reference
- a set of candidate decks to review visually
- a place to document what actually works in iA Presenter

---

## Project Principles

### 1. Repo-first, not deployment-first

The repository version of the skill is canonical.

If the skill is copied into `~/.codex/skills/`, that copy is only a deployment location.

### 2. iA Presenter first

This project is not trying to be generic presentation tooling.

The guidance is specifically shaped around:
- Markdown-based authoring
- visible vs spoken text
- iA Presenter package structure
- deck review inside real iA Presenter previews

### 3. Visible slides matter

Syntax correctness is not enough.

The visible layer of the slide must carry meaning. Speaker notes should deepen the slide, not replace it.

### 4. Golden Decks are earned through iteration

Candidate decks are expected to be revised after visual review. A deck only becomes a real Golden Deck when it survives repeated feedback in iA Presenter itself.

---

## Current Limits

- no bundled image pack
- uneven video transcript coverage
- no automated visual QA pipeline yet
- no final Golden Deck approved yet
- no community workflow implemented yet

---

## Recommended Reading Order

### If you are building prompts or skills

1. `syntax/00-complete-reference.md`
2. `examples/03-anti-patterns.md`
3. `skills/ia-presenter-deck/SKILL.md`
4. `skills/ia-presenter-deck/references/WORKFLOW.md`
5. `skills/ia-presenter-deck/references/RUBRIC.md`
6. one or two files from `golden-candidates/`

### If you are reviewing decks

1. `golden-candidates/README.md`
2. open the candidate deck in iA Presenter
3. compare the visible slide surface against the notes
4. review rhythm, not only correctness

---

## What Success Looks Like

This repository is working as intended when:
- an LLM can draft a valid `.iapresenter` package
- the resulting deck uses multiple visible surface patterns intentionally
- candidate decks become easier to critique and refine
- one or more candidate decks eventually become stable Golden Deck references

