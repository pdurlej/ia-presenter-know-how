# iA Presenter Complete Syntax Reference

> **This is the master reference for creating presentations in iA Presenter using Markdown.**
>
> **This reference follows the conventions used by the `examples/` directory in this repository.**

---

## Core Syntax Rules

### Slide Structure

Use heading levels to control slide hierarchy:

```markdown
# Title          → Cover title on the first slide (always visible)
## Subtitle      → Cover subtitle on the first slide (always visible)
---             → New slide separator
## Slide Title   → Default content slide title in this corpus
# Big Heading    → Mid-deck: a large section/landing heading (use sparingly)
### / ####       → Sub-headings and heading stacks (always visible)
```

**Headings are always visible.** Every heading level (`#` through `####`) is shown to the audience automatically — it does NOT need a TAB. Only *body* text needs a TAB to appear on the slide. This is why heading stacks like `###` + `####` work as a visible slide surface with no list at all.

A standalone `#` heading is not reserved for the cover. On the first slide it is the cover title; later in the deck it reads as a large, standalone section or landing heading. Use it deliberately for resets, turning points, and closers — not as a routine content-slide title (use `##` for those).

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

### What needs a TAB, and what does not

The TAB rule applies to **body text, lists, and quotes**. Some block constructs are shown on the slide *automatically* and must stay flush-left:

| Construct | On slide via | TAB? |
|-----------|--------------|------|
| Headings (`#`–`####`) | automatic | never |
| Images / content blocks | automatic | never |
| **Tables** | automatic | **never — a TAB makes them render as code** |
| **Fenced code blocks** | automatic | **never — a TAB breaks the fence** |
| Body paragraphs | the TAB | yes |
| Lists | the TAB | yes |
| Quotes | the TAB | yes |

Rule of thumb: if it's a recognized Markdown block (heading, image, table, code fence), let it sit flush-left. Only prose, lists, and quotes need the TAB.

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

### Cells drive layout

A slide is divided into **cells**: blocks of slide content separated by a **blank line**.
You never name a layout — the engine picks one from the cell count and content. Verified live:

- one image alone → fills the slide (full-bleed)
- two cells → side-by-side on wide screens (may stack on a phone in portrait)
- four or more cells → a grid (verified 2×2 with four images)

Keep a blank line between elements you want in separate cells. A heading immediately
followed by an image with no blank line is one cramped cell, not two.

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

Reference an image **flush-left** (images are auto-visible — no TAB) with a
**root-relative path that starts with `/`**, and bundle the file in the package:

```markdown
## Image Slide

![Alt text](/assets/image.jpg)
```

> **Two rules, both verified live — get either wrong and nothing shows:**
> 1. **Leading slash, always.** `/assets/photo.png` renders. `photo.png` or
>    `assets/photo.png` (no slash) render as **literal text**.
> 2. **Bundle the file.** The path is relative to the package root, so
>    `/assets/photo.png` means `<package>/assets/photo.png`. iA Presenter does
>    **not** fetch remote `http(s)` image URLs — a web URL renders nothing.

An image alone in its own cell fills the slide; alt text becomes a caption.

### Image Attributes

Richer attributes — `size: cover|contain`, `background: true`, `opacity`,
`filter: grayscale|lighten|darken|sepia|blur`, `position` — are part of iA
Presenter's **content-block** handling and are set in the app's image inspector.
They are not reliably expressible from plain Markdown text, so do **not** depend
on a trailing `size:` line rendering. For full-bleed mood, put a single image in
its own cell (it fills the slide) and adjust framing in-app if needed.

In this repository, image paths under `/assets/` in the prose examples are
illustrative; bundle real files at those paths before the deck will render them.

### Multiple Images

```markdown
## Multiple Images

![Image 1](/assets/image1.jpg)

![Image 2](/assets/image2.jpg)
```

Each image in its own cell (blank line between). Four or more image cells become
a grid — see `skills/ia-presenter-deck/references/LAYOUT-ENGINE.md`.

### Captions and Content Blocks

iA Presenter also supports content blocks — a path on its own line, optionally followed by a caption in straight quotes:

```markdown
## Visual Concept

/assets/diagram.jpg "How the pieces fit together"
```

Content blocks accept metadata such as `Title`, `Alt`, and `Width`. Reach for this form when you want a caption or finer control than plain `![alt](path)` gives.

### Videos and YouTube

Use an empty-text Markdown link whose destination is the media file or video URL:

```markdown
## Video Example

	[](https://www.youtube.com/watch?v=VIDEO_ID)

	[](/assets/demo.mov)
```

Note the empty `[]` link text — the URL goes in the parentheses, exactly like an image without the leading `!`.

In the app, the most reliable way to add a YouTube video is the **Add YouTube Video** button in the Media Manager. For best results, give a video its own otherwise-empty slide so it plays at full size.

---

## Code Blocks

Use fenced code blocks, flush-left with **no TAB**:

````markdown
## Code Example

```python
def hello():
    print("Hello, world!")
```
````

> Like tables, code blocks must start at the beginning of the line. Indented code blocks are not supported in iA Presenter — a leading TAB breaks the fence. Fenced code is shown on the slide automatically, so it does not need a TAB.

---

## Tables

Write the table flush-left, with **no TAB** in front of any row:

```markdown
## Table Example

| Name | Age | City |
|------|-----|------|
| John | 25  | NYC  |
| Jane | 30  | LA   |
```

> **Critical — do not TAB-indent tables.** A leading TAB turns the table into an *indented code block*, so it renders as raw monospace text (`| Name | Age |`) instead of a grid. Tables appear on the slide automatically, like headings and images — they are not body text. The first row and the `|---|` divider must start at the beginning of the line. (Live-verified on iA Presenter mobile.)

---

## Reference-Style Links

Inline links work anywhere (`[text](url)`). For repeated or long URLs, use reference-style links and define the target once:

```markdown
## Sources

	See the [how-to][howto] and the [support site][support].

[howto]: https://ia.net/presenter/how-to
[support]: https://ia.net/presenter/support
```

Keep the link definitions flush-left; they are not shown on the slide.

---

## Math (KaTeX)

iA Presenter typesets LaTeX math with KaTeX.

```markdown
## The Cost Curve

	Inline math like $E = mc^2$ sits in a line of text.

	$$
	\frac{\partial L}{\partial w} = 0
	$$
```

- Inline: `$ ... $` or `\( ... \)`
- Display block: `$$ ... $$`

Remember the TAB: math you want the audience to see still needs to be on a visible (tabbed) line.

---

## Footnotes and Citations

Footnotes are grouped at the end of a slide and appear only if the layout leaves room for them. A citation key starts with `#`:

```markdown
## The Claim

	The result held across three cohorts [p. 23][#Doe:2006].

[#Doe:2006]: John Doe. *Some Big Fancy Book*. Vanity Press, 2006.
```

Any key works as long as it begins with `#`. Keep the definition flush-left.

---

## Local Images and the Media Manager

When you reference a local image file, iA Presenter needs permission to use it. Add local images through the **Media Manager** (drag-and-drop or copy-paste) so the app can resolve and bundle the file. A path that was never added to the Media Manager is the most common reason a local image silently fails to appear.

Do not reach for a remote `http(s)` URL as a workaround — iA Presenter does not fetch them, and the image renders as nothing. The only reliable form is a bundled file referenced root-relative: `/assets/photo.png` with the file at `<package>/assets/photo.png`. Inside a `.iapresenter` package, **bundling the file is what grants access**; the Media Manager step above applies when you add a local file to a deck from inside the app.

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
| Cover title | `# Title` (first slide) | Always |
| Subtitle | `## Subtitle` (first slide) | Always |
| Slide break | `---` | N/A |
| Content slide title | `## Slide Title` | Always |
| Section / landing heading | `# Big Heading` (mid-deck) | Always |
| Sub-heading / heading stack | `### Text` / `#### Text` | Always |
| Slide content | `⇥Text` | Audience |
| Speaker notes | `Text` (no tab) | Presenter only |
| Bold | `**text**` | As positioned |
| Italic | `*text*` | As positioned |
| Link | `[text](url)` | As positioned |
| Image | `![alt](/assets/file.png)` — leading slash + file bundled | Always (never TAB it) |

---

## Troubleshooting

### Problem: Text not appearing on slide

**Solution:** Make sure you're using TAB characters (`\t`), not spaces.

### Problem: Content stacking instead of side-by-side

**Solution:** Ensure there's a blank line WITHOUT a TAB between the two content blocks.

### Problem: Headings not visible

**Solution:** Headings are always visible and never need a TAB. On the first slide, use `#` and `##` for the cover; for content slides use `##` after `---`; use `#` mid-deck only for large section or landing slides; use `###`/`####` for sub-headings and heading stacks.

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
