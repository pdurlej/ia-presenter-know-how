# Golden Candidate Decks

> First-pass candidate decks for iterative feedback.

These files are meant to be imported into iA Presenter, reviewed in presentation mode, and refined until one structure becomes the first real Golden Deck.

Each candidate is a real `.iapresenter` package directory:
- `text.md` contains the deck Markdown
- `info.json` contains iA Presenter metadata

## Included Candidates

- `01-ai-support-copilot-pitch.iapresenter`: product pitch for a buyer or exec audience
- `02-q2-board-update.iapresenter`: candid board-style business update
- `03-customer-interview-workshop.iapresenter`: workshop/training deck
- `04-support-team-case-study.iapresenter`: story-driven case study / keynote-style deck
- `05-jeden-workflow-pilot-ai.iapresenter`: small Polish smoke-test deck for validating package output
- `06-image-first-reference.iapresenter`: **the reference for visual style** — image-first, with bundled full-bleed backgrounds

## Read this before imitating a candidate

Candidates `01`–`05` are first-pass decks about **narrative**: spine, pacing,
note-to-slide ratio. They contain **zero images**, and that is precisely why they
read like styled documents rather than presentations. Do not copy their visual
style.

`06-image-first-reference.iapresenter` is the one to imitate for **look**. It
shows what the corpus actually asks for:

- full-bleed image slides that carry the turns (opening, mid-turn, before the ask)
- images bundled in the package under `assets/`, referenced root-relative
  (`/assets/cover.png`) — the only form that renders
- backgrounds generated with `tools/genbg.py`, so they are licence-clean and
  reproducible with no external assets
- a heading stack and a big-type landing instead of another bullet list
- exactly one small flush-left table, used where the grid genuinely is the message
- a close that lands on a decision, with the questions slide *after* it

A useful exercise: read `01` and `06` back to back. Same craft in the words;
completely different experience in the room.

## What To Review

Focus feedback on:
- whether the narrative moves cleanly from problem to decision
- whether slide density feels too high or too low
- whether the speaker notes sound natural enough to present from
- which deck feels closest to your preferred voice and pacing
- which specific slides should become reusable patterns

## Suggested Feedback Format

For each deck, answer:
- strongest slide
- weakest slide
- where the flow drags
- where the slide text is too heavy
- where the notes are too thin or too long
- whether the ending creates a clear next step

The goal is not to keep all candidates. The goal is to learn which narrative moves, slide rhythms, and note-to-slide ratios should survive into the Golden Deck.
