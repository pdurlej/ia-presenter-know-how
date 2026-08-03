# iA Presenter Workflow

## Stage 0: Frame the Task

- capture the user brief in one line
- identify audience, objective, CTA, duration, tone, evidence, and constraints
- note defaults being used

## Stage 1: Choose Mode

- use candidate mode for exploration or when the brief is underdefined
- use single-deck mode when the brief is specific enough to draft directly

## Stage 2: Build the Story Spine

- define one core takeaway for the whole talk
- define 3-5 moves that earn that takeaway
- define the final action or decision before writing slides

Common deck shapes:
- problem → reframing → solution → proof → next step
- current state → what changed → implications → decisions
- lesson → examples → pattern → application
- case study → turning point → result → takeaway

## Stage 3: Draft Slide Titles

- draft titles first
- titles must carry momentum, not only label topics
- use short titles by default
- use full assertion sentences only when precision matters

Bad:
- Background
- Overview
- Key metrics

Better:
- The queue is not the problem
- Smaller quarter, stronger business
- Better interviews start before the question

## Stage 4: Assign Layout Intent and Surface

For each slide, decide whether it should be:
- stacked
- side-by-side
- comparison
- quote-led
- image-led
- table-led
- section-break / reset
- heading-stack
- agenda / sequence
- one-line landing

Do not use side-by-side just because the syntax allows it.
Do not decide only on layout. Decide what the audience should actually see on the slide surface.

## Stage 4b: Art Direction

Decide the look before writing slide text — it is what separates a presentation
from a styled document. See `VISUAL-DESIGN.md`, `THEMES.md`, `LAYOUT-ENGINE.md`.

- pick a theme in `info.json` that fits the room (never the default minimal one)
- plan images: open and close on a full-bleed image, and use one at each turn
- if no photos are available, run
  `python3 tools/genbg.py <deck>.iapresenter/assets --palette <name>`
  so the file lands on disk at `<package>/assets/<name>.png`, then reference it in
  `text.md` as `![Mood](/assets/<name>.png)` — leading slash mandatory
- vary the silhouette: alternate image slides, big-type landings, heading
  stacks, and at most one small table
- remember the ceiling: no shapes, cards, or charts — aim editorial, not
  decorative, and don't try to out-PowerPoint PowerPoint

## Stage 5: Write Notes and Slide Text

- keep audience-visible text purposeful, not minimal by reflex
- choose what must be visible and what should remain spoken
- move nuance, caveats, and transitions into speaker notes
- notes should sound spoken
- every slide should hand off naturally to the next

Bad default:
- title
- 2-3 small tabbed bullets
- all real meaning hidden in notes

Better:
- use headings, subheadings, visible lists, quotes, tables, or image surfaces when they strengthen the slide
- let notes deepen the visible slide instead of replacing it

## Stage 6: Close Properly

The final slide should do one of these:
- ask for a decision
- state the next move
- land the key takeaway in a memorable line

Avoid ending with:
- Thank you
- Questions
- vague recap bullets

If needed, put `Questions` on a follow-up slide after the real landing.

## Stage 7: Self-Review and Refine

- score the deck against `RUBRIC.md`
- identify the weakest 3 slides
- refine weak split layouts, weak endings, memo-like bullet lists, invisible slides, and generic business phrasing

## Final Deliverable

Return:
- the `.iapresenter` package contents, at minimum `text.md` and `info.json`
- a short assumptions summary
- a short self-review summary
