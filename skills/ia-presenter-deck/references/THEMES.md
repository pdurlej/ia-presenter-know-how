# iA Presenter Themes

The theme carries most of a deck's look — typeface, color, dark/light, type
scale. Choosing it is the cheapest big win available to an LLM, because it is
just two fields in `info.json`.

## Setting the theme from the package (verified)

`info.json` selects the theme. Setting it from a bundled `.iapresenter` package
**works** — the deck opens in the chosen theme:

```json
{
  "type": "net.daringfireball.markdown",
  "net.ia.presenter": { "preset": "Default", "template": "basel" },
  "version": 2,
  "transient": false,
  "creatorIdentifier": "net.ia.presenter"
}
```

- `template` — the theme id (lowercase). Verified distinct: `basel` (dark
  background, bold sans) and `garamond` (white background, elegant serif).
- `preset` — a variant within the theme (e.g. `Default`); themes ship light and
  dark presets.

Built-in themes are named after cities and typefaces (Basel, Tokyo, Paris,
Copenhagen, Helvetica, Garamond, …). To get the exact id of a theme, open the
Design tab in iA Presenter and read its name; the `template` value is the
lowercased name.

## Choosing a theme for the room

Match the theme to tone, not habit. Never default to the minimal white theme for
everything — that is the single biggest reason a deck reads like a document.

| Tone / setting | Reach for |
|----------------|-----------|
| bold, high-contrast, on stage | a **dark** theme (e.g. `basel`) |
| literary, calm, editorial | an elegant **serif** theme (e.g. `garamond`) |
| neutral, corporate, legible | a clean **sans** theme |

Pair the theme with full-bleed images (`VISUAL-DESIGN.md`) — theme + image is
what moves a deck from "document" to "presentation."

## Custom themes — the high-ceiling lever

The built-in themes are deliberately minimal, so big-type hero stats and strong
accent color are limited. iA's real visual ceiling lives in **custom themes**,
which are CSS-based and fully controllable:

- a theme is a folder installed in iA Presenter's theme directory (one-time,
  manual install by the user), then selected by name / referenced in `info.json`;
- `presets.json` defines fonts, appearance, and colors — `TitleFont`, `BodyFont`,
  `Appearance`, `Accent1`–`Accent6`, background and text colors, gradients;
- `template.json` defines `Css`, fonts, and a `Layouts` array where each layout
  can carry CSS `Classes` (e.g. the grid `grid-items-2/3/4`).

This is where a **signature "house style"** lives — the thing that makes every
generated deck look like *the user's* deck, presentable without shame.

### The format, verified

Checked byte-level against real published themes (iA's own Copenhagen and
Helvetica, plus third-party themes on GitHub):

- **There is no `.iatheme` archive.** A theme is a plain folder containing
  `template.json`, `presets.json`, one `.css` file, and a `template.png`
  thumbnail. Fonts, when used, are bundled inside the folder.
- **iA's own JSON has trailing commas** — their parser is lenient. Write strict
  JSON anyway.
- **The `Dark*` / `Light*` prefix names the colour, and the appearance it is used
  in matches that colour.** `DarkBodyTextColor` is dark-coloured ink, used in
  *light* mode. `DarkBackgroundColor` is a dark background, used in *dark* mode.
  Swapping the text pair yields invisible text.
- **Do not invent a `vw`/`vh` type system.** The engine already sizes type with
  container queries (`--font-size-scale: 3.7cqw`), clamps it, and hard-caps `h1`
  at `2.9em` below 480px. Drive the scale through `--scale-factor-h1..h6`
  instead; setting `font-size` on `h1..h6` directly does nothing, because the
  engine neutralises bare element selectors.
- Still unverified: whether `info.json`'s `template` resolves a custom theme by
  its lowercased `Name` or by its folder name (make them identical and it does
  not matter), and which appearance `DarkAccent1` drives.

### The repo's theme

`themes/Broadsheet/` is the corpus's signature theme — dark-first, editorial,
hero-scale display type, one accent, measured contrast. `themes/README.md` has
the install steps and four short experiments that settle the open questions
above. Two probe decks ship in `themes/probes/`.
