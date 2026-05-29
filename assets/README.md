# Assets Notes

This directory documents the path convention used by the examples. It now ships one real placeholder so at least one bundled asset exists; it does not yet include a full media pack.

## Bundled assets

- `placeholder-16x9.svg` — a neutral 16:9 placeholder you can drop into a slide while drafting, then swap for a real image.

## Using images

```markdown
## Slide with Image

	![Alt text](/assets/placeholder-16x9.svg)
	size: contain
```

Supported formats in iA Presenter typically include:
- `.jpg` / `.jpeg`
- `.png`
- `.webp`
- `.gif`
- `.svg`

Common image attributes (see `syntax/00-complete-reference.md` for the Markdown-vs-content-block detail):
- `size: contain` / `size: cover`
- `background: true`
- `opacity: 0.5`
- `filter: grayscale` (also `lighten`, `darken`, `sepia`, `blur`)
- `position: center`

## Local images and the Media Manager

Local image files must be added through iA Presenter's **Media Manager** (drag-and-drop or copy-paste) so the app has permission to use them. A path that was never added to the Media Manager is the most common reason a local image silently fails to appear.

## Notes

- Aside from the bundled placeholder, paths under `/assets/` in this repository are illustrative syntax examples.
- Files like `/assets/landscape.jpg` are not shipped here unless explicitly added later.
- iA Presenter also supports drag-and-drop, Unsplash integration, and embedded video links.
