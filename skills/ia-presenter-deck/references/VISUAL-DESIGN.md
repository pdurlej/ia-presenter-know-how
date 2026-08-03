# iA Presenter Visual Design

Syntax correctness gets a deck that *works*. This file is about a deck that
doesn't embarrass the presenter — the difference between "a styled document"
and "a presentation." Everything here was confirmed by live testing on iA
Presenter (mobile), not guessed.

## What iA Presenter is — and is not

iA Presenter is a **typesetter**, not a canvas. You write text; the engine
chooses type, layout, and rhythm from the **theme**. You do **not** place boxes,
draw shapes, pick per-element colors, or build cards and charts. That is by
design, and it is exactly why it fits an LLM: the model reasons about *words and
structure* (its strength) and never about *pixels and coordinates* (its
weakness). It also means the model **cannot make it ugly** — the floor is high.

**Do not try to beat PowerPoint/Keynote at visual variety. You will lose, and
that is not the game.** A composed PowerPoint deck will always have more cards,
shapes, charts, and color than iA can express. iA wins a different race:

| Use iA Presenter when… | Use PowerPoint/Keynote when… |
|------------------------|------------------------------|
| a person will **present it live** | it's a **leave-behind** read with no speaker |
| the **words and argument** carry it | the **artifact itself** must dazzle standalone |
| you want it **fast, from a brief or voice note** | you have time to art-direct every slide |
| the speaker wants notes + slides in one file | you need dense infographics, org charts, builds |

The north star: *hand the model a voice note, get back a deck you can present in
ten minutes **without shame**.* "Without shame," not "more dazzling than
PowerPoint." iA's aesthetic is **editorial / magazine** — strong typography,
real images, generous space — not **decorative** (icons, ribbons, gradient
cards). Aim for editorial and it looks intentional; chase decoration and it
looks like a tool fighting itself.

## Where "life" actually comes from in iA

Only three levers move the visual needle. Use all three on purpose.

### 1. Images — the biggest single lever (do this by default)

A text-only iA deck reads like a document. A **full-bleed image** turns a slide
into a stage. Make images the backbone, not a garnish.

- **Bundle the file in the package and reference it root-relative:**
  `![Alt text](/assets/photo.png)` with the file at `<package>/assets/photo.png`.
- **A leading `/` is mandatory.** `photo.png` or `assets/photo.png` (no slash)
  render as **literal text**. Remote `http(s)` URLs **do not render at all**.
- An image alone in its own cell fills the slide. Alt text becomes a caption.
- Interleave image slides with text slides to create rhythm (iA's version of a
  dark/light "sandwich").

LLMs cannot pull photos from the web (no URL support), so there are two paths:

- **Generated backgrounds (LLM-autonomous):** generate abstract gradient/duotone
  PNGs and bundle them. See `tools/genbg.py`. This gives color, texture, and
  full-bleed mood without any external assets — and it works today.
- **Real photos (human-in-the-loop):** the person adds Unsplash images in the
  app (one click), or drops in their own files. Write the deck with the image
  *intent* (alt text, placement) so swapping in a real photo is trivial.

### 2. Theme — the second lever (never leave it default)

The theme carries ~90% of the look: typeface, color, dark/light, type scale.
Setting it from the package **works** (verified). Choose it per deck; do not
ship everything on the minimal default. See `THEMES.md`.

### 3. Rhythm — vary the silhouette

If every slide is "small title + a few tab lines," the thumbnail column is a
gray wall. Change the surface every few slides: a full-bleed image, a one-word
big-type landing, a heading stack, a tight table, a section image. Same lever as
`SLIDE-SURFACE-PATTERNS.md`, judged visually.

## Honest limits (so you don't over-promise)

- **Big type is theme-bound.** `# 70%` is *not* a 150pt hero stat in minimal
  themes — the theme decides the scale. A high-impact custom theme is the way to
  get hero numbers (see `THEMES.md` → custom themes).
- **No shapes, cards, badges, or native charts from text.** Don't design around
  them. Use images, headings, quotes, and small tables instead.
- **Side-by-side may stack on a narrow phone in portrait.** It reads as columns
  on wide screens; don't rely on columns being the *only* thing that carries a
  slide.

## The default recipe for a "no-shame" deck

1. Pick a theme that fits the room (`THEMES.md`).
2. Open and close on a **full-bleed image** slide (generated or real).
3. Put **one or two big-type landing slides** at the turns.
4. Keep text slides lean; let the engine lay them out.
5. Use at most one small flush-left table, only if exact numbers matter.
6. Bundle every image under `/assets/` and run `tools/ialint.py` before
   delivering.
