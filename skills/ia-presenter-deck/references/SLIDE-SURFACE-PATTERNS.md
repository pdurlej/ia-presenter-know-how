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

Good for:
- a point that should read fast
- a slide that does not need a bullet list
- short rhetorical turns

### 3. Agenda / Sequence

Use:
- TAB-prefixed ordered list

Good for:
- setup
- process
- ladder
- action plan

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

### 7. Image or Background Slide

Use:
- `/assets/...`
- `size: contain` or `background: true`

Good for:
- mood
- scene-setting
- visual contrast between text-heavy moments

Only use when a real image helps the argument.

### 8. One-Line Landing

Use:
- one visible sentence or one heading stack

Good for:
- turns
- closers
- explicit decisions

### 9. Section Reset

Use:
- one strong heading with minimal supporting visible text

Good for:
- changing mode
- moving from problem to solution
- moving from story to ask

## Rhythm Rules

- Do not use the same visible surface for the whole deck.
- Change rhythm every few slides when the narrative changes.
- A strong deck usually mixes at least 3 visible surface types.
- If a slide is invisible except for the title, that invisibility must be intentional.

## Hidden-Deck Smell

The deck is too note-heavy when:
- most slides are only title plus two or three tiny tab lines
- the key argument is invisible unless you read the editor pane
- every slide has the same silhouette in the thumbnail column

Fix by:
- promoting one line into `###` or `####`
- turning a paragraph into a visible quote
- converting a vague list into an ordered sequence
- using a tiny table when exact movement matters
- collapsing two weak slides into one stronger surface
