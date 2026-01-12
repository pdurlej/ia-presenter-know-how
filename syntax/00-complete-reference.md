# iA Presenter Complete Syntax Reference

> **This is the master reference for creating presentations in iA Presenter using Markdown.**

---

## Core Syntax Rules

### Slide Structure

Use heading levels to control slide hierarchy:

```markdown
# Title          → Creates cover page (always visible)
## Subtitle      → Subtitle on cover (always visible)
---             → New slide separator
### Heading       → Content slide title (always visible)
```

### Cover Slide

```markdown
# Presentation Title
## Subtitle or date
```

### Multiple Slides

```markdown
# Title
## Subtitle

---
## Slide 1 Title

---
## Slide 2 Title

---
## Slide 3 Title
```

---

## Content Visibility

### Speech vs Text on Slide

The most important concept in iA Presenter:

**Speech (Speaker Notes):**
- Text without TAB prefix
- Only visible to presenter (not audience)
- This is what you actually say during presentation

**Text on Slide:**
- Text with TAB prefix (use actual `\t` character, not spaces)
- Visible to audience
- Keep short and impactful

### Example: Speech vs Slide

```markdown
## Key Points

This is speaker notes. Only I can see this while presenting.
The audience won't see this text at all.

	Point 1 - Visible to audience
	Point 2 - Also visible
	Point 3 - Visible content
```

**Rule:** Use TAB characters (`\t`) for slide content. Do NOT use spaces.

---

## Text Formatting

### Basic Formatting

```markdown
**Bold text**
*Italic text*
[Link text](url)
`Inline code`
```

### Lists

```markdown
## Lists Example

	Bullet point 1
	Bullet point 2
	Bullet point 3
```

### Quotes

```markdown
## Quote Example

	> This is a quote
	> - Author
```

---

## Layout Control

### Stacked Layout (Default)

Content stacks vertically:

```markdown
## Vertical Stack

	Point 1
	Point 2
	Point 3
```

### Side-by-Side Layout

Create side-by-side layout by separating tabbed content with a non-tabbed line:

```markdown
## Comparison

Left panel content visible to audience

Right panel content visible to audience
```

**Critical:** The blank line between the two panels must NOT have a TAB. This creates the side-by-side layout.

### Three-Column Layout

```markdown
## Three Columns

	Column 1

	Column 2

	Column 3
```

---

## Images

### Basic Image Syntax

```markdown
## Image Slide

	![Alt text](/assets/image.jpg)
	size: contain
```

### Image Attributes

```markdown
	![Alt text](/assets/image.jpg)
	size: contain
```

Available image attributes:
- `size: contain` - Fit entire image within slide
- `size: cover` - Cover entire slide
- `opacity: 0.5` - Set transparency (0.1 to 1.0)
- `filter: grayscale` - Apply filter
- `position: center` - Position image

### Multiple Images

```markdown
## Multiple Images

	![Image 1](/assets/image1.jpg)

	![Image 2](/assets/image2.jpg)
```

### YouTube Videos

```markdown
## Video Example

	[https://www.youtube.com/watch?v=VIDEO_ID]
```

---

## Code Blocks

```markdown
## Code Example

	```python
	def hello():
	    print("Hello, world!")
	```
```

---

## Tables

```markdown
## Table Example

	| Name | Age | City |
	|------|-----|------|
	| John | 25  | NYC  |
	| Jane | 30  | LA   |
```

---

## Advanced Features

### Slide Breaks

Create new slides in multiple ways:

**Option 1: Three dashes**
```markdown
---
```

**Option 2: Press Enter twice**

**Option 3: Use Text Inspector "Slide Break" option**

### Footers and Headers

Some themes support footers and headers. Add them in the Inspector panel.

### Theme Selection

iA Presenter comes with built-in themes named after cities:
- San Francisco (colorful and bold)
- Milano (restrained and stylish)
- Tokyo
- New York
- Berlin
- And more...

Change themes in the Theme and Style menu in Inspector.

### Export Formats

iA Presenter supports multiple export formats:
- PDF (with or without notes)
- HTML
- Markdown
- PowerPoint
- Images (various aspect ratios)

---

## Common Patterns

### Standard Presentation Structure

```markdown
# Title
## Subtitle

---
## Agenda

	Introduction
	Main content
	Q&A
	Conclusion

---
## 1. Introduction

Speaker notes about introduction...

	Key point 1
	Key point 2
```

### Comparison Slide

```markdown
## Comparison

Feature A description

Feature B description
```

### Quote Slide

```markdown
## Inspiration

	> "The only way to learn to speak... is to speak."
	> — Practice principle

This quote is about practice and dedication.
```

### Image with Caption

```markdown
## Visual Concept

	![Concept](/assets/concept.jpg)

This image illustrates our core concept.
```

---

## Best Practices

### DO:
- ✅ Use TAB characters for slide content (not spaces)
- ✅ Keep slide text minimal (3-5 points max)
- ✅ Use short, punchy headlines
- ✅ Let speech carry the detailed information
- ✅ Test your presentation in iA Presenter before sharing
- ✅ Use meaningful images that support your story

### DON'T:
- ❌ Use spaces instead of TABS
- ❌ Put walls of text on slides
- ❌ Read from your slides
- ❌ Use generic stock images without purpose
- ❌ Overuse bullet points
- ❌ Mix speech and slide content on same line

---

## Quick Reference

| Element | Syntax | Visibility |
|---------|--------|------------|
| Cover title | `# Title` | Always |
| Subtitle | `## Subtitle` | Always |
| Slide break | `---` | N/A |
| Slide heading | `### Heading` | Always |
| Slide content | `⇥Text` | Audience |
| Speaker notes | `Text` (no tab) | Presenter only |
| Bold | `**text**` | As positioned |
| Italic | `*text*` | As positioned |
| Link | `[text](url)` | As positioned |
| Image | `![alt](path)` | As positioned |

---

## Troubleshooting

### Problem: Text not appearing on slide

**Solution:** Make sure you're using TAB characters (`\t`), not spaces.

### Problem: Content stacking instead of side-by-side

**Solution:** Ensure there's a blank line WITHOUT a TAB between the two content blocks.

### Problem: Headings not visible

**Solution:** Headings with `#`, `##`, or `###` are always visible. You cannot hide them.

### Problem: Speech notes visible to audience

**Solution:** Remove the TAB prefix from text you don't want the audience to see.

---

## Examples in This Repository

- `examples/01-basic.md` - Minimal working example
- `examples/02-complex.md` - Full-featured demo
- `examples/03-anti-patterns.md` - Common mistakes

---

**Source:** Compiled from iA Presenter official documentation
**Tags:** `syntax`, `reference`, `markdown`, `rules`, `comprehensive`
