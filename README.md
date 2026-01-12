# iA Presenter Know-How Repository

> **Complete knowledge base for creating beautiful presentations in iA Presenter**

> **⚠️ This is a community-driven project collecting best practices, tips, and examples for creating effective iA Presenter presentations. All content is based on official iA Presenter documentation and community contributions.**

---

## 📖 About

This repository is a comprehensive knowledge base for iA Presenter, collecting documentation, best practices, tips, and examples from various sources.

Perfect for:
- **Beginners** who need guidance on creating presentations
- **Advanced users** looking for advanced techniques and patterns
- **Developers** integrating iA Presenter with AI/LLM systems
- **Anyone** who wants to create beautiful, effective presentations

### Our Mission

To create the most complete, up-to-date, and practical collection of iA Presenter knowledge - all in one place, freely accessible to everyone.

---

## 💡 Share Your Best Practices

This repository grows through community contributions! We're collecting real-world tips and techniques from iA Presenter users worldwide.

### What We're Looking For

**Your tips could include:**
- ✨ Unique layout patterns you've discovered
- 🎯 Best practices for specific use cases (business, academic, creative)
- 💡 Workflow optimizations that save time
- 📝 Effective presentation structures and templates
- 🎨 Theme customization tips
- ⚡ Keyboard shortcuts and productivity hacks
- 🎭 Delivery techniques that work with iA Presenter

**Got a unique way to use iA Presenter? Share it!**

### How Your Contributions Help

- 📚 **Learners benefit** from your experience
- 🤖 **AI systems** learn from real examples
- 👥 **Community grows** through shared knowledge
- 🔧 **Tool improves** with user feedback
- 🌍 **Knowledge spreads** across languages and cultures

### Quick Examples

"Instead of using bullet points for comparisons, I use side-by-side layouts with minimal text on each side. It creates better engagement!"

"I found that putting images in the `assets/` folder and referencing them locally makes presentations much faster to load."

"For technical presentations, I create a glossary slide at the end - it saves questions during Q&A!"

---

## 🤝 How to Contribute

Sharing your knowledge is easy! Here's how:

### Step 1: Document Your Tip

1. Create a new markdown file in `docs/02-tips/community/` (create directory if needed)
2. Use a clear filename: `your-tip-title.md`
3. Include:
   - A descriptive title
   - Brief description of the use case
   - Example code/presentation snippet
   - Why this approach works

### Step 2: Format Your Contribution

```markdown
# Your Tip Title

> **Use case:** Briefly describe when to use this tip

## What It Solves

Explain what problem or challenge this tip addresses.

## How It Works

Provide step-by-step explanation or example:

\`\`\`markdown
## Example Slide

	This content shows the technique
\`\`\`

## Why This Works

Explain why this approach is effective.

## Tips & Variations

- Variation 1
- Variation 2
- Common pitfalls to avoid
```

### Step 3: Submit Your Contribution

**Option A: GitHub Pull Request (Recommended)**
1. Fork this repository
2. Create a new branch: `git checkout -b add-your-tip-name`
3. Add your file to `docs/02-tips/community/`
4. Commit changes: `git commit -m "Add tip: Your Tip Title"`
5. Push to your fork: `git push origin add-your-tip-name`
6. Open Pull Request on GitHub

**Option B: GitHub Issue**
1. Go to [Issues](https://github.com/pdurlej/ia-presenter-rag/issues)
2. Click "New Issue"
3. Use template: "Share a tip or best practice"
4. Paste your markdown content

**Option C: Email/DM**
- Email: `[Your email]`
- DM on social platforms

### Step 4: What Happens Next

1. ✅ We review your contribution
2. 💬 We may ask for clarification or examples
3. 🎉 Approved contributions are merged
4. 📖 Your tip becomes part of the knowledge base
5. ⭐ Contributors are credited in the repository

### Contribution Guidelines

**DO:**
- ✅ Be clear and concise
- ✅ Provide working examples
- ✅ Explain WHY something works
- ✅ Include use cases for your tip
- ✅ Test your examples in iA Presenter

**DON'T:**
- ❌ Submit content that's already documented
- ❌ Share tips that don't work
- ❌ Post without examples
- ❌ Use copyrighted material without permission

### Recognition

All contributors are credited! We'll add your name/handle to:
- The repository's CONTRIBUTORS file
- Each tip you contribute
- Our periodic "Community Highlights" posts

---

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

## 🚀 Quick Start for Creating Presentations

When creating an iA Presenter presentation:

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

### For AI/LLM Integration
1. Use `examples/` as few-shot examples
2. Reference `syntax/00-complete-reference.md` for validation
3. Apply patterns from all documentation
4. Use community tips from `docs/02-tips/community/` for real-world insights

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

This repository is designed to work with any LLM or AI system:
- ✅ GPT-4 / GPT-4o
- ✅ Claude 3 / Claude 3.5
- ✅ Llama 3 / Llama 3.1
- ✅ Local models (Ollama, LM Studio, GPT4All)
- ✅ Custom fine-tuned models

**No framework required** - use plain text context!

### Building Knowledge Context

For optimal results:
1. Start with `syntax/00-complete-reference.md` for rules
2. Include relevant `examples/` for few-shot learning
3. Reference `docs/02-tips/` for best practices
4. Include community tips from `docs/02-tips/community/` for real-world patterns
5. Use `docs/01-course/` for step-by-step guidance

---

## 📊 Status

- ✅ Official documentation (6 courses + 12 tips)
- ✅ Complete syntax reference
- ✅ Working example presentations (3 examples)
- ✅ Community contributions system ready
- 🚧 Phase 2: Advanced patterns and guides (planned)
- 📊 **Community tips**: Check `docs/02-tips/community/` for user contributions!

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

## 🚀 Usage Example for AI/LLM Integration

### Building Knowledge Context

When using this repository for RAG:

```python
# Example: Building knowledge context for iA Presenter

def build_presenter_knowledge_context(user_topic, complexity="beginner"):
    """
    Constructs optimal context for iA Presenter presentation generation.
    Combines official docs, examples, and community tips.
    """
    # Get syntax rules
    syntax_rules = read_file("syntax/00-complete-reference.md")

    # Get relevant examples
    examples = []
    if complexity == "beginner":
        examples.append(read_file("examples/01-basic.md"))
    else:
        examples.append(read_file("examples/02-complex.md"))

    # Get relevant tips from official docs
    official_tips = read_files_from_dir("docs/02-tips/", limit=3)

    # Get community tips (if any)
    try:
        community_tips = read_files_from_dir("docs/02-tips/community/", limit=2)
    except:
        community_tips = []

    # Combine all knowledge sources
    context = f"""
    iA PRESENTER SYNTAX RULES:
    {syntax_rules}

    OFFICIAL EXAMPLES:
    {''.join(examples)}

    OFFICIAL BEST PRACTICES:
    {''.join(official_tips)}

    COMMUNITY TIPS:
    {''.join(community_tips) if community_tips else "No community tips yet. Be the first to contribute!"}

    USER TOPIC:
    {user_topic}

    Generate a presentation following iA Presenter Markdown syntax.
    Focus on creating a compelling story with minimal slide text.
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

This is a **community-driven know-how repository** - it grows with your contributions!

### Share Your Knowledge

Have you discovered a unique pattern, tip, or technique for iA Presenter? Share it with the community!

**Ways to contribute:**
- 📝 Share a tip or best practice (see "Share Your Best Practices" above)
- 🎨 Add example presentations
- 🌍 Translate documentation to other languages
- 🐛 Fix bugs or improve documentation
- 💡 Suggest new features or patterns

### Areas for Enhancement
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
