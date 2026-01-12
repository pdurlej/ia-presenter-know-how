# This directory is for placeholder images

# Instructions

When adding images to iA Presenter presentations:

1. Place your images in this `/assets/` directory
2. Reference them using relative paths in your Markdown:

```markdown
![Alt text](/assets/your-image.jpg)
	size: contain
```

3. Supported image formats:
   - .jpg
   - .jpeg
   - .png
   - .webp
   - .gif

4. Recommended attributes:
   - `size: contain` - Fit entire image within slide
   - `size: cover` - Cover entire slide
   - `opacity: 0.5` to 1.0` - Set transparency
   - `filter: grayscale` - Apply filter
   - `position: center` - Position image

# Note

Images are optional for presentations. iA Presenter also supports:
- Unsplash integration (built-in)
- YouTube video embedding
- Local image drag-and-drop

# Example

```markdown
## Slide with Image

	![Beautiful landscape](/assets/landscape.jpg)
		size: contain

This image demonstrates the `size: contain` attribute.
```
