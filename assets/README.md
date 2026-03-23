# Assets Notes

This directory documents the path convention used by the examples. It does not currently bundle an asset pack.

Use image references like this:

```markdown
## Slide with Image

	![Alt text](/assets/your-image.jpg)
	size: contain
```

Supported formats in iA Presenter typically include:
- `.jpg`
- `.jpeg`
- `.png`
- `.webp`
- `.gif`

Common image attributes:
- `size: contain`
- `size: cover`
- `opacity: 0.5`
- `filter: grayscale`
- `position: center`

Important note:
- paths under `/assets/` in this repository are illustrative syntax examples
- referenced files like `/assets/landscape.jpg` are not shipped here unless explicitly added later
- iA Presenter also supports local drag-and-drop, Unsplash integration, and embedded video links
