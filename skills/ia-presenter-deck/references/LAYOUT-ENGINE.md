# iA Presenter Layout Engine

iA Presenter has ~18 responsive layouts and **chooses one automatically** by
analysing the slide's content. You never name a layout — you *feed* the engine.
This is how an LLM "designs" without seeing pixels: by shaping the text.

## Cells are the unit of layout

A slide is divided into **cells**. A cell is a block of slide content separated
from the next by a **blank line**. The engine arranges the cells.

- More cells → richer layout. One cell → a single centered block.
- **Two cells → side-by-side / split** (on wide screens; may stack on a narrow
  phone in portrait).
- **Four or more cells → a grid** (verified: four image cells render as a 2×2
  grid). Mixed text + image cells are allowed.
- Put a blank line between elements you want in *separate* cells — e.g. a heading
  and an image. Without the blank line they share one cell.

```markdown
## Heading in cell 1

![Photo in cell 2](/assets/photo.png)
```

```markdown
## Four cells become a grid

![](/assets/a.png)

![](/assets/b.png)

![](/assets/c.png)

![](/assets/d.png)
```

## What each content shape tends to produce

| You write… | The engine tends to give… |
|------------|---------------------------|
| one short heading, nothing else | a large centered title / section slide |
| heading + image in separate cells | a title-image layout (image dominant) |
| a single image, no heading | a full-bleed / dominant image |
| 4+ cells (text or images) | a grid |
| two tabbed blocks split by a blank line | side-by-side columns |
| a flush-left table | a real table grid |

## Rules that make the engine behave

- **Separate elements with a blank line** so each gets its own cell.
  Heading immediately followed by body with no blank line = one cramped cell.
- **Tables, code, headings, images are flush-left** (auto-visible). Only
  paragraphs, lists, and quotes take a TAB. See `syntax/00-complete-reference.md`.
- **Don't over-stuff a slide.** If you need five cells of text, it's two slides.
- **Images carry layout best.** An image cell gives the engine something
  substantial to compose around — far more than another line of tabbed text.

## Verified vs. likely

- ✅ Verified live: 4 image cells → 2×2 grid; lone image → fills slide;
  flush-left table → grid; heading auto-large (scale is theme-dependent).
- ~ Likely / screen-dependent: two-cell side-by-side reads as columns on wide
  screens, can stack on a phone in portrait. Test the target screen if columns
  are load-bearing for the slide's meaning.
