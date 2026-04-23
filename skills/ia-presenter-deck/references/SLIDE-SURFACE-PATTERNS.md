# iA Presenter Slide Surface Patterns

Syntax correctness is not enough. A good iA deck uses the visible slide surface intentionally, not only speaker notes.

## Principle

Notes carry:
- transitions
- caveats
- temperature
- extra explanation

Slides carry:
- the thing worth seeing
- the shape of the argument
- the rhythm of the deck

If every slide becomes `title + a few tabbed bullets`, the deck is probably valid but weak.
If every spoken line is also fully visible, the deck is probably over-explained.
If the only real point lives in notes, the slide is underdesigned.

## Reusable Visible Surfaces

### 1. Cover

Use:
- `#` for the main title
- `##` or `####` for a sharp subtitle

Good for:
- topic framing
- tone setting
- making the first slide feel intentional

### 2. Heading Stack

Use:
- `###` for the main thought on the slide
- `####` for tension, qualifier, or reframing

Remember:
- headings are visible by default
- they should read like live presentation language, not document labels

Good for:
- a point that should read fast
- a slide that does not need a bullet list
- short rhetorical turns

### 2a. Chapter Card / Reset

Use:
- `#` for the section move
- `####` for the frame, tension, or consequence

Good for:
- changing mode
- moving from problem to proof
- preventing a long deck from feeling flat

### 3. Agenda / Sequence

Use:
- TAB-prefixed ordered list

Good for:
- setup
- process
- ladder
- action plan

Warning:
- if half the deck becomes ordered lists, you are no longer using sequence intentionally

### 4. Contrast

Use:
- strong left/right contrast only when the comparison is crisp
- `##`, `###`, `####`, or short TAB lines

Good for:
- before / after
- ambition / learning
- customer / team
- weak / strong

### 5. Quote-Led Slide

Use:
- TAB-prefixed blockquote

Good for:
- customer voice
- founder voice
- one sentence that deserves the slide

### 6. Proof Table

Use:
- a very small TAB-prefixed table

Good for:
- exact deltas
- pilot scorecards
- before / target views

Do not use when:
- the grid is less memorable than one distilled line

If the proof table should own the slide:
- keep the title stack and the table in one intentional stack
- prefer a full-width proof slide over a stranded title plus tiny table split

### 6a. Full-Width Proof

Use:
- `##`, `###`, or `####` title stack
- a TAB-prefixed table directly below it in the same cell

Good for:
- monthly operating watchlists
- pilot scorecards
- executive proof slides

Warning:
- if the title sits on the left and the table floats on the right, the slide is probably asking for a different layout

### 7. Image or Background Slide

Use:
- `/assets/...`
- `size: contain` or `background: true`

Good for:
- mood
- scene-setting
- visual contrast between text-heavy moments
- giving the deck one memorable, human-feeling reset

Only use when a real image helps the argument.
During drafting, placeholders are fine. Replace them later.
Prefer official provider search and licensing-safe sources such as Unsplash or Pexels when no user asset pack exists.
Avoid generic stock symbolism that weakens precision.

### 7a. Image Panel Split

Use:
- one image content block in its own cell
- one text stack in its own cell
- `size: cover` when the image should behave like a panel rather than a floating object

Good for:
- operational context on one side, argument on the other
- a product or workflow scene next to a short sequence
- giving one slide a stronger visual reset without going full background

Warning:
- if the image becomes a tiny postcard in the middle of the slide, the slide is under-designed
- if the text side has only one short line, the split is probably not earning its width

### 8. One-Line Landing

Use:
- one visible sentence or one heading stack

Good for:
- turns
- closers
- explicit decisions

### 9. Checklist / Action Slide

Use:
- TAB-prefixed short lines
- optionally one `###` or `####` frame above them

Good for:
- workshops
- next-step slides
- operating rules

## Rhythm Rules

- Do not use the same visible surface for the whole deck.
- Change rhythm every few slides when the narrative changes.
- A strong deck usually mixes at least 4 visible surface types.
- If a slide is invisible except for the title, that invisibility must be intentional.
- Use chapter cards and heading stacks more often than filler slides.
- Presenter is responsive, so treat slide composition as adaptive, not pixel-fixed.

## Hidden-Deck Smell

The deck is too note-heavy when:
- most slides are only title plus two or three tiny tab lines
- the key argument is invisible unless you read the editor pane
- every slide has the same silhouette in the thumbnail column
- the deck makes more sense in markdown edit view than in presenter view

The deck is too surface-heavy when:
- the audience can read the whole argument before you say it
- visible paragraphs duplicate the spoken notes
- every slide feels like a handout instead of a presentation
- the slide is acting like a document instead of a support surface

Fix by:
- promoting one line into `###` or `####`
- turning a weak section opener into `#` plus `####`
- turning a paragraph into a visible quote
- converting a vague list into an ordered sequence
- using a tiny table when exact movement matters
- collapsing two weak slides into one stronger surface
