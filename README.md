# iA Presenter RAG Repository

> **Retrieval-Augmented Generation knowledge base for creating beautiful presentations in iA Presenter**

> **⚠️ This is a non-commercial project created to help LLMs generate valid iA Presenter presentations. All content is based on official iA Presenter documentation and is provided for free.**

---

## 📖 About

This repository contains a comprehensive knowledge base designed to help any Large Language Model (LLM) generate valid, beautiful presentations in iA Presenter's Markdown format.

The RAG system is optimized for:
- **Beginner users** who need guidance on creating presentations
- **LLMs** that need clear, actionable documentation
- **Quick reference** for iA Presenter syntax and features

---

## 🎯 What You'll Find

### 📚 Documentation
- **6 Course Tutorials** - Step-by-step guides from official docs
- **12 Presentation Tips** - Best practices for storytelling and delivery
- **5 Video Transcripts** - Full content from YouTube tutorials

### 🎨 Syntax Reference
- Complete iA Presenter Markdown syntax
- Speech vs Text-on-Slide rules
- Layout control (stacked vs side-by-side)
- Image and media handling

### 📝 Example Presentations
- **Basic Example** - Minimal working presentation
- **Complex Example** - Full-featured demo with all syntax
- **Anti-Patterns** - Common mistakes to avoid

---

## 🚀 Quick Start for LLMs

When generating an iA Presenter presentation:

### 1. Start with the structure:

```markdown
# Presentation Title
## Subtitle

---
## Slide 1

---
## Slide 2
```

### 2. Use TABS for slide content:

```markdown
## Slide Title
This text is speaker notes (invisible to audience)
	This text appears on the slide
```

**Critical:** Use actual TAB characters (`\t`), not spaces!

### 3. Create slides with `---`:

```markdown
# Title
## Subtitle

---
## Slide 1

---
## Slide 2
```

### 4. For side-by-side layouts:

```markdown
## Comparison

	Left panel content visible to audience

	Right panel content visible to audience
```

**Critical:** The blank line between panels must NOT have a TAB.

### 5. Add images:

```markdown
## Visual Slide

	![Image](/assets/image.jpg)
	size: contain
```

---

## 📂 Repository Structure

```
ia-presenter-rag/
├── README.md                          # This file
├── LICENSE                            # CC0 Public Domain
├── docs/
│   ├── 01-course/                     # 6 official tutorials
│   │   ├── 01-quick-tour.md
│   │   ├── 02-write-your-story.md
│   │   ├── 03-format-text.md
│   │   ├── 04-design-your-slides.md
│   │   ├── 05-practice-and-present.md
│   │   └── 06-share-and-export.md
│   ├── 02-tips/                       # 12 presentation tips
│   │   ├── 01-markdown-and-formatting.md
│   │   ├── 02-share-presentation.md
│   │   ├── 03-five-canons-rhetoric.md
│   │   ├── 04-speaking-voice.md
│   │   ├── 05-finding-confidence.md
│   │   ├── 06-behind-gesture.md
│   │   ├── 07-good-image-tells-good-story.md
│   │   ├── 08-successful-methods.md
│   │   ├── 09-picture-worth-1000-words.md
│   │   ├── 10-presentation-tips.md
│   │   ├── 11-introducing-ia-presenter.md
│   │   └── 12-how-can-we-make-presentations-better.md
│   └── 03-videos/                     # 5 YouTube transcripts
│       ├── 01-quick-tour.md
│       ├── 02-write-your-story.md
│       ├── 03-format-text.md
│       ├── 04-design-slides.md
│       └── 05-practice-present.md
├── syntax/                            # Complete syntax reference
│   └── 00-complete-reference.md
├── examples/                           # Working examples
│   ├── 01-basic.md
│   ├── 02-complex.md
│   └── 03-anti-patterns.md
├── patterns/                           # Common templates (Phase 2)
├── guides/                             # Best practices (Phase 2)
│   └── troubleshooting/
└── assets/                            # Image placeholders
```

---

## 🔑 Core Concepts

### Speech vs Text-on-Slide

**Speaker Notes (invisible to audience):**
- Text without TAB prefix
- Use for detailed explanations
- Keep slides clean and minimal

**Slide Text (visible to audience):**
- Text with TAB prefix (use actual `\t` character, not spaces)
- Keep short and impactful
- Use bullet points and keywords

### Hierarchy

```markdown
# Title           → Creates cover page (always visible)
## Subtitle        → Subtitle on cover (always visible)
---               → New slide separator
### Heading        → Content slide title (always visible)
```

### Layout Control

**Stacked (default):**
```markdown
## Slide Title
	Point 1
	Point 2
	Point 3
```

**Side-by-side:**
```markdown
## Comparison

	Left content

	Right content
```

---

## 📚 Key Documentation Files

### For Beginners
1. **Quick Start Guide** → `examples/01-basic.md`
2. **Syntax Reference** → `syntax/00-complete-reference.md`
3. **Course Tutorial 1** → `docs/01-course/01-quick-tour.md`

### For Understanding Fundamentals
1. **Presentation Tips** → `docs/02-tips/10-presentation-tips.md`
2. **Five Canons of Rhetoric** → `docs/02-tips/03-five-canons-rhetoric.md`
3. **Finding Confidence** → `docs/02-tips/05-finding-confidence.md`

### For Advanced Users
1. **Complex Example** → `examples/02-complex.md`
2. **Anti-Patterns Reference** → `examples/03-anti-patterns.md`
3. **All Course Tutorials** → `docs/01-course/` directory

---

## 🎓 Learning Path

### For Beginners
1. Start with `examples/01-basic.md`
2. Read `syntax/00-complete-reference.md`
3. Follow `docs/01-course/` tutorials in order

### For Advanced Users
1. Review `examples/02-complex.md`
2. Explore `docs/02-tips/` directory
3. Study `examples/03-anti-patterns.md`

### For LLM Developers
1. Use `examples/` as few-shot examples
2. Reference `syntax/00-complete-reference.md` for validation
3. Apply patterns from all documentation

---

## 🎨 Best Practices

### DO:
- ✅ Use TAB characters for slide content (not spaces)
- ✅ Keep slide text minimal (3-5 points max)
- ✅ Use short, punchy headlines
- ✅ Let speech carry detailed information
- ✅ Use meaningful images that support your story
- ✅ Test your presentation in iA Presenter before sharing

### DON'T:
- ❌ Use spaces instead of TABs
- ❌ Put walls of text on slides
- ❌ Read from your slides
- ❌ Use generic stock images without purpose
- ❌ Overuse bullet points
- ❌ Mix speech and slide content on same line

---

## 🔧 For AI and LLM Integration

This repository is designed to work with any LLM:
- ✅ GPT-4 / GPT-4o
- ✅ Claude 3 / Claude 3.5
- ✅ Llama 3 / Llama 3.1
- ✅ Local models (Ollama, LM Studio)

**No framework required** - use plain text context!

### Retrieval Strategy

For optimal RAG performance:
1. Start with `syntax/00-complete-reference.md` for rules
2. Include relevant `examples/` for few-shot learning
3. Reference `docs/02-tips/` for best practices
4. Use `docs/01-course/` for step-by-step guidance

---

## 📊 Status

- ✅ Content acquisition (23 sources complete)
- ✅ Syntax documentation complete
- ✅ Example presentations (3 created)
- ✅ RAG structure optimized
- 🚧 Phase 2: Patterns and advanced guides (planned)

---

## 📝 Attribution

This repository is a derivative work based on official iA Presenter documentation by Information Architects Inc.

**Original sources:**
- [iA Presenter](https://ia.net/presenter)
- [iA Presenter How-To](https://ia.net/presenter/how-to)
- [iA Presenter Markdown Guide](https://ia.net/presenter/support/basics/markdown)
- [iA Presenter YouTube Channel](https://www.youtube.com/@iAInc101)
- Community examples and best practices

**License:** This RAG repository is provided under CC0 (Public Domain). You are free to use, modify, and distribute it for any purpose.

**Note:** iA Presenter is a commercial application. This repository only documents its Markdown format and usage patterns.

---

## 🚀 Usage Example for LLMs

### Context Construction

When using this repository for RAG:

```python
# Example: How to construct context for iA Presenter generation

def get_ia_presenter_context(query):
    """
    Constructs optimized context for iA Presenter presentation generation.
    """
    # Get syntax rules
    syntax_rules = read_file("syntax/00-complete-reference.md")

    # Get relevant examples
    examples = []
    if "beginner" in query:
        examples.append(read_file("examples/01-basic.md"))
    else:
        examples.append(read_file("examples/02-complex.md"))

    # Get relevant tips
    tips = read_files_from_dir("docs/02-tips/", limit=3)

    # Combine with query-specific content
    context = f"""
    iA PRESENTER SYNTAX RULES:
    {syntax_rules}

    EXAMPLES:
    {''.join(examples)}

    BEST PRACTICES:
    {''.join(tips)}

    USER QUERY:
    {query}
    """

    return context
```

### Prompt Template

```
You are an expert at creating presentations in iA Presenter using Markdown.

Follow these rules:
1. Use # Title and ## Subtitle for the cover slide
2. Use --- to create new slides
3. Use ### for slide titles
4. Use TAB characters (not spaces) for slide content visible to audience
5. Keep text minimal - focus on speaker notes without TABS

Create a presentation about: [USER TOPIC]

CONTEXT:
{RAG_CONTEXT}

Generate valid iA Presenter Markdown that can be imported directly.
```

---

## 🤝 Contributing

Contributions are welcome! Areas for enhancement:
- Additional example presentations
- More use case patterns
- Troubleshooting guides
- Translation to other languages

---

## 📧 Resources

- [iA Presenter Official Website](https://ia.net/presenter)
- [iA Presenter How-To](https://ia.net/presenter/how-to)
- [iA Presenter Support](https://ia.net/presenter/support)
- [iA Presenter on YouTube](https://www.youtube.com/@iAInc101)
- [iA Newsletter](https://ia.net/newsletter)

---

## 📜 License

[CC0 1.0 Universal](LICENSE)

This repository is in the public domain. No rights reserved.

---

**Last Updated:** 2026-01-12

---

**The most important rule: Great presentations tell great stories. Focus on your narrative, use iA Presenter to visualize it, and let your slides support your speech—not replace it.**
