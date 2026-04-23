# iA Presenter Complete Syntax Reference

> **This is the master reference for creating presentations in iA Presenter using Markdown.**
>
> **This reference follows the conventions used by the `examples/` directory in this repository.**

---

## Core Syntax Rules

### Slide Structure

Use heading levels to control slide hierarchy:

```markdown
# Title          → Creates cover page (always visible)
## Subtitle      → Subtitle on cover (always visible)
---             → New slide separator
## Slide Title   → Default content slide title in this corpus
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

Create side-by-side layout by separating audience-visible content blocks with a blank line that has no TAB:

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

	![](image-name.png)
```

### Image Attributes

```markdown
/assets/image.jpg
size: contain
x: right
background: true
```

Image metadata such as `size`, `x`, `y`, `background`, `filter`, and `opacity`
works with Content Blocks Syntax, not Markdown image syntax.

Available image attributes for Content Blocks Syntax:
- `size: contain` - Fit entire image within slide
- `size: cover` - Cover available image container
- `x: left|center|right` - Horizontal alignment
- `y: top|center|bottom` - Vertical alignment
- `background: true` - Render image behind visible text
- `filter: darken|lighten|grayscale|sepia|blur` - Apply filter
- `opacity: 50%` - Set transparency

In this repository, image paths under `/assets/` are illustrative syntax examples. The referenced files are not bundled unless explicitly added later.

### Multiple Images

```markdown
## Multiple Images

/assets/image1.jpg

/assets/image2.jpg
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
## What this deck covers

Context for the audience about what to expect.

	1. The core problem
	2. What changed
	3. What we recommend

---
## The core problem

Speaker notes explain the full context here.

	Key visible point 1
	Key visible point 2
```

**Note:** Use `#` only for the cover slide. Use `##` for content slide titles after `---`. Do not use `#` for mid-deck section breaks.

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
- Use TAB characters for slide content (not spaces)
- Keep slide text to 3-5 points maximum
- Use short, punchy headlines that carry momentum
- Let speech carry transitions, caveats, and detailed reasoning
- Vary the visible slide surface — mix heading stacks, quotes, tables, contrasts, and one-line landings
- End with a real action, decision, or landing line
- Test your presentation in iA Presenter before sharing

### DON'T:
- Use spaces instead of TABs
- Put walls of text on slides
- Read from your slides
- Hide the entire argument in speaker notes while slides show only titles and tiny bullets
- End with "Thank You" or "Questions?" as the final slide
- Use the same slide silhouette for the whole deck
- Use `#` for mid-deck section breaks (reserve `#` for the cover)

---

## Quick Reference

| Element | Syntax | Visibility |
|---------|--------|------------|
| Cover title | `# Title` | Always |
| Cover subtitle | `## Subtitle` | Always |
| Slide break | `---` | N/A |
| Content slide title | `## Slide Title` | Always |
| Heading stack | `### Main` / `#### Qualifier` | Always |
| Slide content | `⇥Text` (TAB prefix) | Audience |
| Speaker notes | `Text` (no TAB) | Presenter only |
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

**Solution:** In this corpus, cover titles use `#` and `##`, and content slide titles use `##` after `---`.

### Problem: Speech notes visible to audience

**Solution:** Remove the TAB prefix from text you don't want the audience to see.

---

## Examples in This Repository

- `examples/01-basic.md` — Minimal working deck with correct syntax and a strong ending
- `examples/02-complex.md` — Full-featured deck demonstrating all major surface patterns
- `examples/03-anti-patterns.md` — Common mistakes with corrected versions

---

**Source:** Compiled from iA Presenter official documentation
**Tags:** `syntax`, `reference`, `markdown`, `rules`, `comprehensive`
