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
- write the raw script before worrying about layout, theme, or polished visuals

For executive or board decks:
- define the `Situation`, `Complication`, `Question`, and `Answer` before slide drafting
- write the answer early, not at the end
- decide whether the core body is deductive or inductive
- map the question chain the room will naturally ask next

Common deck shapes:
- problem → reframing → solution → proof → next step
- current state → what changed → implications → decisions
- lesson → examples → pattern → application
- case study → turning point → result → takeaway
- `SCQA` → answer → proof → risk → ask

## Stage 2a: Draft the Hidden Script

Before making things visible on slides:
- write or paste the argument in plain text
- treat this as a staging area, not as the final delivery state
- avoid polishing fonts, colors, and image choices too early

Good default:
- think in script paragraphs first
- then decide what deserves slide surface

Bad default:
- designing the thumbnail before the message exists
- searching for perfect images before the sequence is clear

Important:
- do not confuse `hidden script first` with `notes-heavy final deck`
- the script draft is a raw material step; the delivered deck still needs a strong visible payload on every slide

## Stage 3: Draft Slide Titles

- draft titles first
- titles must carry momentum, not only label topics
- use short titles by default
- use full assertion sentences only when precision matters
- plan at least one section-reset or chapter-card moment in a deck longer than 6 slides

For executive decks:
- titles should usually read as governing thoughts
- avoid blank framing labels such as `Key priorities`, `Summary`, or `Context`
- each section title should answer a visible or implied question

Bad:
- Background
- Overview
- Key metrics

Better:
- The queue is not the problem
- Smaller quarter, stronger business
- Better interviews start before the question

## Stage 4: Map the Deck Rhythm

Before drafting slide text, choose the rhythm of the deck.

Decide:
- where the deck opens wide versus compresses
- where the audience gets a section reset
- where proof appears
- where the close starts, not only where it ends

Healthy defaults for an 8-10 slide deck:
- 1 cover
- 1 chapter-card or reset slide
- 1 contrast slide
- 1 sequence or checklist slide
- 1 proof slide
- 1 explicit landing or decision close

If every slide is the same silhouette, stop and redesign before writing notes.

Use `RHYTHM-MAPS.md` when the deck needs a stronger archetype.

## Stage 5: Assign Layout Intent and Surface

For each slide, decide whether it should be:
- stacked
- side-by-side
- image-panel split
- comparison
- quote-led
- image-led
- table-led
- full-width proof
- section-break / reset
- heading-stack
- agenda / sequence
- one-line landing

Do not use side-by-side just because the syntax allows it.
Do not decide only on layout. Decide what the audience should actually see on the slide surface.
Assume layouts may stack or shift responsively across devices.
Think in cells:
- a blank line usually creates a new cell
- elements kept together in one cell tend to stack vertically
- one element per cell is a good default, except when a title stack or proof stack should stay together

Use the layout picker as a review step, not as an afterthought. iA Presenter chooses from many valid layouts, but the first auto-layout is not always the right rhetorical layout.

## Stage 5a: Declare the Visible Payload

Before writing notes, state what the audience must get from the slide without opening the editor pane.

For each slide, decide:
- what is the one thing worth seeing
- which element carries it: heading, subheading, list, quote, image, table, or contrast
- whether the slide is supporting the presenter or trying to replace the presenter

Hard gate:
- if the key point only exists in notes, redesign the visible slide
- if the visible slide already contains the whole spoken paragraph, compress it
- if you cannot name the visible payload in one line, the slide probably has no job yet

## Stage 6: Write Notes and Slide Text

- keep audience-visible text purposeful, not minimal by reflex
- choose what must be visible and what should remain spoken
- move nuance, caveats, and transitions into speaker notes
- notes should sound spoken
- every slide should hand off naturally to the next
- if a slide earns a `#`, `###`, or `####`, let it carry real weight instead of adding filler bullets underneath
- body text only belongs on slide when it has a TAB and deserves to be shown
- headings are visible by default, so they must be short, clear, and interesting
- notes are not a hiding place for the real argument
- if a note contains the only real claim on the slide, promote that claim to the visible layer
- if the audience would need to read the note to understand the slide, the slide failed

Bad default:
- title
- 2-3 small tabbed bullets
- all real meaning hidden in notes

Better:
- use headings, subheadings, visible lists, quotes, tables, or image surfaces when they strengthen the slide
- let notes deepen the visible slide instead of replacing it
- let some slides be almost entirely visible if the line is strong enough
- create tension between what the audience sees and what the presenter says next
- build slides that can survive a quick glance without becoming a handout

## Stage 6a: Use Placeholder Visuals While Drafting

If the deck clearly wants images but assets are not ready:
- use placeholders
- use neutral image slots or notes to mark image intent
- keep moving on the story

Do not let image search interrupt story structure.

## Stage 6b: Design Late

Only after script, structure, and visible/spoken balance are working:
- choose or refine theme direction
- source real images if the deck needs them
- swap placeholders for real visuals
- tune image position, scale, and background behavior

Do not use theme selection as a substitute for narrative decisions.
Use `IMAGE-SOURCING.md` when sourcing images from Unsplash or Pexels.

## Stage 7: Close Properly

The final slide should do one of these:
- ask for a decision
- state the next move
- land the key takeaway in a memorable line

Avoid ending with:
- Thank you
- Questions
- vague recap bullets

If needed, put `Questions` on a follow-up slide after the real landing.

## Stage 8: Self-Review and Refine

- score the deck against `RUBRIC.md`
- identify the weakest 3 slides
- refine repeated silhouettes, weak split layouts, weak endings, memo-like bullet lists, invisible slides, and generic business phrasing
- flag any slide whose main idea lives mostly in notes
- for executive decks, also refine:
  - late answers
  - sections that do not answer a question
  - summary lines that do not actually summarize the support below

## Final Deliverable

Return:
- the `.iapresenter` package contents, at minimum `text.md` and `info.json`
- a `manifest.json` describing per-slide jobs, visible payloads, layout intent, image intent, closing role, and notes policy when using the local presentation system
- a short assumptions summary
- a short self-review summary

## Presentation System Loop

For repeatable local quality, run the deck through the presentation system:

1. author or update the `.iapresenter` package
2. build `manifest.json`
3. export rendered output through `iA Presenter`
4. run story QA
5. run visual QA
6. generate a bounded `fix-plan.json`
7. optionally apply one slide-local fix pass and rerun

Rules:
- keep raw runs under `.presentation-system/`
- cap auto-fix at two iterations
- stop if the score does not improve
- do not do freeform whole-deck rewrites after QA
