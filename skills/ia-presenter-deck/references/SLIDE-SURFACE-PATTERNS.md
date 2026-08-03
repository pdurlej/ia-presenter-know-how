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
- a very small table, written flush-left with NO TAB on any row
  (a TAB makes iA render the table as an indented code block, not a grid — linter rule E001)
- at most 3 columns x 4 rows; if it needs more, it is a handout, not a slide

Good for:
- exact deltas
- pilot scorecards
- before / target views

Do not use when:
- the grid is less memorable than one distilled line

### 7. Image or Background Slide

Use:
- `![Alt text](/assets/photo.png)` flush-left, with the file bundled at
  `<package>/assets/photo.png` — the leading `/` is mandatory, and a remote
  `http(s)` URL renders nothing at all
- an image ALONE in its own cell — that is the full-bleed move; it fills the slide

Do NOT write trailing `size:` / `background:` / `opacity:` / `filter:` lines.
Those are in-app content-block settings, not plain Markdown, and may render as
literal text on the slide. A generated deck must never depend on them.

Good for:
- the opener and the closer (use one at each)
- every narrative turn
- mood, scene-setting, and rhythm between text-heavy moments

This is the default surface, not a garnish. If no photo exists, generate one:
`python3 tools/genbg.py <deck>.iapresenter/assets --palette ink`

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
