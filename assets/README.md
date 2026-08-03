# Assets Notes

This directory documents the path convention used by the examples. It now ships one real placeholder so at least one bundled asset exists; it does not yet include a full media pack.

## Bundled assets

- `placeholder-16x9.svg` — a neutral 16:9 placeholder you can drop into a slide while drafting, then swap for a real image.

## Using images

Images are **flush-left** (they are auto-visible — no TAB) and the path must be
**root-relative, starting with `/`**, resolved against the package root:

```markdown
## Slide with Image

![Alt text](/assets/placeholder-16x9.svg)
```

Both rules are verified live, and getting either wrong shows nothing:

- `photo.png` or `assets/photo.png` (no leading slash) render as **literal text**
- a remote `http(s)` URL renders **nothing** — the file must be bundled

Supported formats in iA Presenter typically include:
- `.jpg` / `.jpeg`
- `.png`
- `.webp`
- `.gif`
- `.svg`

### On image attributes

iA Presenter can set `size` (cover/contain), `background`, `opacity`, `filter`,
and `position` on an image — but those are **content-block / inspector**
settings applied in the app, not plain-Markdown syntax. Do **not** write them as
trailing `key: value` lines and expect them to take effect; a generated deck
should not depend on them. For a full-bleed image, put the image alone in its
own cell — it fills the slide on its own.

## Local images and the Media Manager

Local image files must be added through iA Presenter's **Media Manager** (drag-and-drop or copy-paste) so the app has permission to use them. A path that was never added to the Media Manager is the most common reason a local image silently fails to appear.

## Notes

- Aside from the bundled placeholder, paths under `/assets/` in this repository are illustrative syntax examples.
- Files like `/assets/landscape.jpg` are not shipped here unless explicitly added later.
- iA Presenter also supports drag-and-drop, Unsplash integration, and embedded video links.
