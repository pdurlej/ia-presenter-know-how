# Themes

A custom iA Presenter theme is the highest-ceiling visual lever this corpus has.
The built-in themes are deliberately minimal, which is why a generated deck can be
syntactically perfect and still read like a styled document. A theme controls the
type scale, the colour system, the margins and the accent — everything that decides
whether a deck looks *presented* or *printed*.

## The format (verified, and not what you may expect)

**There is no `.iatheme` archive.** A theme is a plain folder:

```
Broadsheet/
├── template.json     identity, and which CSS file to load
├── presets.json      colours + fonts, one entry per preset
├── broadsheet.css    the whole design
└── template.png      1600x900 thumbnail for the theme picker
```

This was verified byte-level against real published themes (iA's own Copenhagen and
Helvetica, plus third-party themes on GitHub). Two details worth knowing:

- **iA's own JSON files contain trailing commas.** Their parser is lenient. Ours are
  strict-valid anyway — do not rely on the tolerance.
- **Fonts are always bundled locally.** No theme examined uses `@import` or an
  `https://` font URL, and there is no evidence the sandbox permits network fetches
  from theme CSS.

## Installing `Broadsheet`

macOS:

```
~/Library/Containers/net.ia.presenter/Data/Library/Application Support/iA Presenter/Themes/
```

Copy the whole `Broadsheet/` folder there, then **Settings → Themes → Reload**, then
quit and reopen iA Presenter. The first install needs a restart; later CSS edits
hot-reload.

Select it per deck from `info.json`:

```json
{ "net.ia.presenter": { "preset": "Default", "template": "broadsheet" } }
```

`Broadsheet` ships two presets: **Default** (dark) and **Paper** (light).

## What Broadsheet is designed to do

It is optimised for iA Presenter itself, not for any personal brand — it leans hard
on the only levers iA actually gives a theme:

- **A strict 1.5 type scale** derived from the engine's own sizing machinery, with
  the hero heading at ~19% of slide height and body at 5.6% — inside the AVIXA/ANSI
  DISCAS legible band for a room, and ≥3× body so a hero reads as a hero.
- **Contrast measured, not asserted.** Body and title clear AAA twice over; both
  accents clear AA. Neither background is pure black or pure white: `#16161A` avoids
  projector black-crush, `#FAFAF8` avoids halation.
- **One accent, used in exactly five places** (bold, links, the eyebrow, the quote
  rule, list markers). One emphasis per slide or emphasis means nothing.
- **Generous margins** (`--padding-scale-px-size: 18.5`), flush-left, ragged right.
- **No gradients and no decoration** — the words and the images carry it.

It rides the engine's own container-query sizing (`3.7cqw`) rather than inventing a
`vw`/`vh` system, which is why the scale stays correct on a projector, a laptop and
a phone at once. The engine hard-caps `h1` at `2.9em` under 480px, so the aggressive
2.25 scale factor does not explode the phone view.

## Four experiments that settle what is still unverified

These need a machine with iA Presenter — about ten minutes. Record what you find
here and in `skills/ia-presenter-deck/references/THEMES.md`.

**E1 — is `template` the lowercased `Name`, or the folder name?**
Open `probes/probe-a.iapresenter` (ships `"template": "broadsheet"`).
- Renders in Broadsheet → the lowercase rule holds.
- Falls back → try `"Broadsheet"`, then `"broadsheet-theme"`.

Then rename the *folder* to `BroadsheetFolder/`, leaving `"Name": "Broadsheet"`,
reload, reopen the probe. Still Broadsheet → the identifier is **Name**. Falls back
→ it is the **folder name**. This is the one test that published themes can never
answer, because HTML exports always rename the theme directory to `theme/`.

**E2 — which appearance does `DarkAccent1` drive?**
Temporarily set `DarkAccent1: "#00FF00"` and `LightAccent1: "#FF00FF"` in
`presets.json`, then open `probes/probe-b.iapresenter` (dark, one bold word).
- Green bold → `Dark*` means dark **mode**; the shipped CSS is correct.
- Magenta bold → `Dark*` means a dark-**coloured** accent; swap the two
  `--sig-accent` lines in section 11 of `broadsheet.css`.

**E3 — which engine do you have?**
Export any deck to HTML and run `grep -c element-group index.htm`.
- Non-zero → modern engine; the `:root` variable block is live.
- Zero → legacy engine; only the section-14 fallbacks apply.

**E4 — what happens without the theme?**
Uninstall `Broadsheet` and reopen `probe-a`. Note what it falls back to. No primary
source documents this today.

## Swapping in a real font (three edits, nothing else)

1. Drop `Broadsheet-Display.woff2` into `themes/Broadsheet/fonts/`.
2. Prepend to `broadsheet.css`, **before** `:root`:

```css
@font-face {
  font-family: 'Broadsheet Display';
  font-style: normal;
  font-weight: 400 900;
  src: local(''),
       url('fonts/Broadsheet-Display.woff2') format('woff2'),
       url('fonts/Broadsheet-Display.ttf')   format('truetype');
}
```

3. Two places, not one:
   - `template.json` → `"TitleFont": "Broadsheet Display"` (the display name shown
     in the Style Inspector)
   - `presets.json` → `"TitleFont": "Broadsheet Display, ui-serif, Georgia, serif"`
     (the CSS name)

Setting the font directly in CSS instead loses the Style Inspector override.
