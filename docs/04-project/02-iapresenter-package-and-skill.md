# `.iapresenter` Package And Skill Workflow

> The operational reference for how this repo represents decks and how the canonical skill should produce them.

---

## `.iapresenter` Is A Package

In this repository, a real `.iapresenter` deck is a package directory, not a single text file with a renamed extension.

Minimum structure:

```text
example-deck.iapresenter/
├── info.json
└── text.md
```

### `text.md`

Contains the deck body in iA Presenter Markdown.

This includes:
- cover slide headings
- slide breaks
- speaker notes
- TAB-prefixed visible content
- optional tables, quotes, images, or layout patterns

### `info.json`

Contains the minimal metadata that lets iA Presenter recognize and open the package.

In this repository, the current candidate decks use a small, stable metadata shape:
- `type: net.daringfireball.markdown`
- `creatorIdentifier: net.ia.presenter`
- `version: 2`
- a `net.ia.presenter` block with template and preset

### Optional assets

Some decks may later include local `assets/` inside the package or use external or absolute paths during drafting.

This repository does not currently bundle a real shared asset pack.

---

## Visible Text vs Spoken Text

The project relies on one core iA Presenter distinction:

### Spoken text

Flush-left text is presenter speech.

Use it for:
- transitions
- nuance
- caveats
- interpretation

### Visible text

TAB-prefixed text appears on the slide.

Use it for:
- the thing the audience should actually see
- the shape of the argument
- memorable language
- sequences, quotes, or proof

The skill should not hide the whole deck in spoken text.

---

## Canonical Skill

The repo-first generation workflow lives here:
- `skills/ia-presenter-deck/SKILL.md`

Its job is to:
- create new decks
- improve existing `.iapresenter` packages
- generate candidate directions before drafting one full deck

It should use the corpus in this repository, not behave like a generic PowerPoint generator.

---

## Minimum Generation Workflow

### 1. Frame the task

Capture:
- audience
- objective
- CTA
- duration
- tone
- evidence
- constraints

### 2. Choose mode

Use:
- candidate mode when the narrative is still fuzzy
- single-deck mode when the brief is already clear

### 3. Build the story spine

Define:
- the main takeaway
- the 3-5 moves that earn it
- the final ask or closing line

### 4. Design the visible slide surface

For each slide, choose what the audience should actually see.

Common surface types in this project:
- heading stack
- ordered sequence
- contrast slide
- quote-led slide
- proof table
- section reset
- one-line landing

### 5. Write notes

Notes should:
- sound sayable
- deepen the slide
- connect one slide to the next

They should not carry the entire presentation while the slides remain nearly empty.

### 6. Package the deck

Write:
- `text.md`
- `info.json`

Then open the package in iA Presenter for real review.

---

## Quality Expectations

Before calling a deck strong, check:
- does the visible layer carry real meaning?
- does the deck use more than one slide surface pattern?
- is the close a real decision or landing line?
- does it render like an iA Presenter deck rather than a pasted outline?

Primary review references:
- `skills/ia-presenter-deck/references/RUBRIC.md`
- `skills/ia-presenter-deck/references/SLIDE-SURFACE-PATTERNS.md`
- `examples/03-anti-patterns.md`

---

## Common Failure Modes

### Wrong package format

Bad:
- one plain text file named `something.iapresenter`

Good:
- `something.iapresenter/text.md`
- `something.iapresenter/info.json`

### Hidden deck

Bad:
- almost all meaning is flush-left speaker text
- visible slide content is tiny and repetitive

Good:
- visible slide surface carries the main shape of the argument

### One-pattern deck

Bad:
- every slide looks like title plus three small bullets

Good:
- the deck changes rhythm when the narrative changes

---

## Where To Look Next

- `golden-candidates/README.md`
- `skills/ia-presenter-deck/references/WORKFLOW.md`
- `skills/ia-presenter-deck/references/RUBRIC.md`
- `skills/ia-presenter-deck/references/SLIDE-SURFACE-PATTERNS.md`

