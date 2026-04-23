# LLM Generation Workflow

> The recommended operating loop for using this repository with Codex, Claude, GPT, or other local LLM tooling.

---

## Goal

The purpose of this workflow is not only to generate valid iA Presenter syntax.

The goal is to generate decks that:
- open correctly as `.iapresenter` packages
- use visible slide surfaces intentionally
- survive visual review inside iA Presenter
- improve over time through the Golden Deck loop
- run through a local presentation system with render artifacts, structured review, and bounded corrections

---

## Step 1: Capture the brief

At minimum, define:
- audience
- objective
- CTA
- duration
- tone
- required evidence or data
- image availability
- hard constraints

If the brief is incomplete, apply defaults explicitly instead of pretending certainty.

Primary reference:
- `skills/ia-presenter-deck/references/INTAKE.md`

---

## Step 2: Assemble context

For most generation tasks, load context in this order:

1. `syntax/00-complete-reference.md`
2. `examples/03-anti-patterns.md`
3. one worked example from `examples/`
4. relevant files from `docs/02-tips/`
5. the canonical skill and its references
6. one or more candidate decks if matching rhythm already exists

Do not load the whole repo by default. Pull only the files that materially change the deck.

---

## Step 3: Choose drafting mode

### Candidate mode

Use when:
- the brief is still fuzzy
- the team wants options first
- you are exploring future Golden Deck patterns

Expected output:
- 3-4 genuinely different directions

### Single-deck mode

Use when:
- the story is clear enough to draft directly
- the audience and CTA are stable
- the work is refinement rather than exploration

Expected output:
- one `.iapresenter` package

Primary reference:
- `skills/ia-presenter-deck/SKILL.md`
- `docs/04-project/06-presentation-system-v1.md`

---

## Step 4: Build the story spine

Before writing slides, define:
- the one thing the audience should leave with
- the 3-5 moves that earn that conclusion
- the final action, decision, or landing line

If you cannot summarize the deck in one sentence, the spine is still weak.

---

## Step 5: Design the visible slide surface

This repository now treats slide-visible content as a first-class design problem.

Do not default every slide to:
- title
- tiny bullet list
- hidden argument in notes

Instead choose the right visible surface for the job:
- heading stack
- ordered sequence
- contrast
- quote-led slide
- proof table
- section reset
- one-line landing
- image-led slide when a real image helps

Primary references:
- `skills/ia-presenter-deck/references/SLIDE-SURFACE-PATTERNS.md`
- `skills/ia-presenter-deck/references/LAYOUT-HEURISTICS.md`

---

## Step 6: Write notes

Speaker notes should:
- sound sayable
- deepen the slide
- carry caveats, transitions, and temperature

They should not carry the entire deck while the audience sees almost nothing.

---

## Step 7: Package the deck

A real output deck should be a package directory:

```text
deck-name.iapresenter/
├── info.json
└── text.md
```

Do not output a plain text file renamed to `.iapresenter`.

Primary reference:
- `docs/04-project/02-iapresenter-package-and-skill.md`

---

## Step 8: Review in iA Presenter

Markdown review is not enough.

Open the package in iA Presenter and check:
- slide thumbnails
- repetition of silhouette
- density
- whether the visible layer earns the screen space
- whether the close lands

---

## Step 9: Score and refine

Use the rubric before treating the draft as strong.

Primary reference:
- `skills/ia-presenter-deck/references/RUBRIC.md`

Especially downgrade decks that are:
- too note-heavy
- too repetitive in visible form
- ending weakly
- syntactically valid but visually generic

---

## Step 10: Feed lessons back into the repo

If a deck improves because of a repeated insight, that insight should move into:
- the canonical skill
- the rubric
- the slide-surface patterns
- the candidate-deck workflow

This is how the repo becomes a better LLM package, not just a bigger one.
