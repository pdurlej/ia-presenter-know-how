# iA Presenter LLM Corpus

> Structured Markdown corpus for generating iA Presenter presentations with LLMs and agents.

> Human-readable by design, but optimized first for retrieval, prompt assembly, and evaluation workflows.

---

## About

This repository packages curated iA Presenter material into a small, predictable corpus. It combines repo-authored reference material, worked examples, and source-linked notes derived from official iA Presenter documentation and videos.

Primary use cases:
- build a skill or retrieval corpus for Codex, Claude, GPT, or local models
- assemble prompt context for deck generation
- validate generated Markdown against a compact syntax reference
- study iA Presenter patterns manually without browsing multiple sources

This is not an official iA Presenter repository. iA Presenter is a commercial product by Information Architects Inc.

---

## What Is Included

- `syntax/00-complete-reference.md`: master syntax reference for prompt context and validation
- `examples/01-basic.md`: minimal working deck with correct syntax, varied surfaces, and a strong ending
- `examples/02-complex.md`: full-featured deck demonstrating all major surface patterns
- `examples/03-anti-patterns.md`: common mistakes with corrected versions showing proper fixes
- `skills/ia-presenter-deck/`: canonical repo-first skill for generating and improving `.iapresenter` decks
- `golden-candidates/`: first-pass decks for iterative feedback and future Golden Deck development
- `docs/01-course/`: six tutorial-style documents based on official how-to material
- `docs/02-tips/`: twelve articles on storytelling, delivery, visuals, and Markdown
- `docs/03-videos/`: five video-derived files with mixed completeness
- `docs/04-project/`: repo-specific project documentation, package format notes, and Golden Deck workflow

Video coverage in `docs/03-videos/` is intentionally uneven:
- `01-quick-tour.md`: transcript-based note with key points
- `02-write-your-story.md`: duplicate-transcript note pointing back to the quick tour capture
- `03-format-text.md`: duplicate-transcript note pointing back to the quick tour capture
- `04-design-slides.md`: summary note only, transcript unavailable in this repo snapshot
- `05-practice-and-present.md`: summary note only, transcript unavailable in this repo snapshot

---

## Important Limits

- `assets/` does not include the example image files referenced in the examples. Paths like `/assets/landscape.jpg` are illustrative syntax examples, not a bundled asset pack.
- The video directory contains transcripts where available and notes where a transcript was not captured or appears duplicated.
- This cleanup does not introduce a community contribution workflow. Any future community layer should be added explicitly, not implied by README copy.
- The repository copy of `skills/ia-presenter-deck/` is canonical; a copy under `~/.codex/skills/` is only a deployment location.
- In this repo, a real `.iapresenter` deck is a package directory containing at least `text.md` and `info.json`, not a single plain-text file renamed to `.iapresenter`.

---

## Quick Syntax Rules

Use this repository's current example set as the working convention:

```markdown
# Presentation Title
## Subtitle

---
## Slide Title

Speaker notes stay flush-left.
	Slide text is prefixed with a TAB.
```

Core rules:
- `#` and `##` create the cover slide.
- `---` starts a new slide.
- `##` is the default content-slide title convention in this corpus.
- Text without a TAB is speaker notes.
- Text with a TAB is audience-visible slide content.
- Headings, subheadings, quotes, tables, images, and layout structure also shape what the audience sees.
- Side-by-side layouts depend on cell breaks; see the syntax reference and worked examples for the exact patterns used here.

---

## Recommended LLM Context Assembly

For most generation tasks, load context in this order:
1. `syntax/00-complete-reference.md`
2. one example from `examples/`
3. two or three relevant files from `docs/02-tips/`
4. a matching tutorial from `docs/01-course/` if the task is procedural
5. a project doc from `docs/04-project/` if the task involves repo conventions or package output
6. a video-derived note only when you need source overlap or phrasing clues

Minimal retrieval recipe:

```python
def build_presenter_context(topic, level="default"):
    syntax_rules = read_file("syntax/00-complete-reference.md")

    if level == "simple":
        examples = [read_file("examples/01-basic.md")]
    else:
        examples = [read_file("examples/02-complex.md")]

    supporting_docs = read_files_from_dir("docs/02-tips/", limit=3)

    return f"""
    SYNTAX RULES:
    {syntax_rules}

    EXAMPLES:
    {''.join(examples)}

    SUPPORTING DOCUMENTS:
    {''.join(supporting_docs)}

    USER TOPIC:
    {topic}
    """
```

Prompt starter:

```text
You are generating iA Presenter Markdown.

Rules:
1. Use # and ## for the cover slide only. Do not use # for mid-deck sections.
2. Use --- for slide breaks.
3. Use ## for content slide titles in this corpus.
4. Use TAB characters for audience-visible slide content.
5. Use speaker notes for transitions, nuance, and caveats.
6. Make the visible slide surface carry real meaning instead of hiding the whole argument in notes.
7. End with a real action, decision, or landing line. Do not end on "Thank you" or "Questions?".
8. Vary the visible surface across the deck.

Task:
[USER TOPIC]

Context:
{PRESENTER_CONTEXT}
```

---

## Canonical Skill

The repository now includes a repo-first skill at `skills/ia-presenter-deck/`.

Use it when an LLM should:
- create a new iA Presenter deck
- improve or restructure an existing `.iapresenter`
- generate 3-4 candidate directions before drafting a full deck

Design intent:
- stronger iA Presenter fit than generic PowerPoint or Marp skills
- text-first drafting with visible slide surfaces carrying real meaning and notes deepening the argument
- integrated use of this repo's syntax reference, anti-patterns, and Golden Deck candidate loop

Install note:
- the copy in this repository is the source of truth
- copy or install it into `~/.codex/skills/` only when you want it available as a live Codex skill

Deck packaging note:
- candidate decks in `golden-candidates/` are stored as `.iapresenter` package directories
- the Markdown body lives in `text.md`
- iA Presenter metadata lives in `info.json`

---

## Repository Structure

```text
ia-presenter-know-how/
├── README.md
├── CLAUDE.md
├── LICENSE
├── DEPLOYMENT_CHECKLIST.md
├── GITHUB_SETUP.md
├── assets/
│   ├── .gitkeep
│   └── README.md
├── docs/
│   ├── 01-course/
│   ├── 02-tips/
│   ├── 03-videos/
│   └── 04-project/
│       ├── 01-repository-overview.md
│       ├── 02-iapresenter-package-and-skill.md
│       ├── 03-llm-generation-workflow.md
│       └── 04-golden-deck-program.md
├── examples/
│   ├── 01-basic.md
│   ├── 02-complex.md
│   └── 03-anti-patterns.md
├── golden-candidates/
│   ├── README.md
│   ├── 01-ai-support-copilot-pitch.iapresenter
│   ├── 02-q2-board-update.iapresenter
│   ├── 03-customer-interview-workshop.iapresenter
│   ├── 04-support-team-case-study.iapresenter
│   └── 05-jeden-workflow-pilot-ai.iapresenter
├── skills/
│   ├── README.md
│   └── ia-presenter-deck/
│       ├── SKILL.md
│       ├── agents/openai.yaml
│       └── references/
└── syntax/
    └── 00-complete-reference.md
```

---

## Recommended Reading Paths

For LLM builders:
1. start with `syntax/00-complete-reference.md`
2. add `examples/01-basic.md` or `examples/02-complex.md`
3. pull in the most relevant files from `docs/02-tips/`
4. use `skills/ia-presenter-deck/` when you want a reusable generation workflow
5. use `docs/04-project/` when you need repo or package conventions
6. use `docs/01-course/` when you need workflow or UI explanations

For human readers:
1. start with `examples/01-basic.md`
2. read `syntax/00-complete-reference.md`
3. follow `docs/01-course/` in order
4. use `examples/03-anti-patterns.md` as a final review pass
5. review `golden-candidates/` when iterating toward a Golden Deck pattern
6. use `docs/04-project/` when you need to understand how this repo is meant to be operated

---

## Status

- current positioning: LLM-first corpus, secondarily readable as human documentation
- canonical repo-first skill added under `skills/ia-presenter-deck/`
- syntax convention standardized around `##` as the default content-slide title
- `docs/03-videos/` is documented as transcripts and notes, not five full transcripts
- `assets/` is documented as path convention only, not a bundled media pack
- Golden Deck work now has a dedicated candidate loop in `golden-candidates/`

Possible future work:
- fuller video transcript coverage
- a real asset pack or screenshot bundle
- local installer automation from repo skill to `~/.codex/skills/`
- a separate legal review of source-derivative packaging

---

## Attribution and License

This repository is a derivative packaging of iA Presenter-related material, based primarily on:
- [iA Presenter](https://ia.net/presenter)
- [iA Presenter How-To](https://ia.net/presenter/how-to)
- [iA Presenter Support](https://ia.net/presenter/support)
- [iA Presenter on YouTube](https://www.youtube.com/@iAInc101)

The repository is distributed with [CC0 1.0 Universal](LICENSE). Treat that as applying to the repository packaging, examples, and repo-authored editorial material. Referenced upstream source material remains attributable to Information Architects Inc.; if you plan broad redistribution of source-derived text, review the original source pages as well.

---

## Resources

- [iA Presenter Official Website](https://ia.net/presenter)
- [iA Presenter How-To](https://ia.net/presenter/how-to)
- [iA Presenter Support](https://ia.net/presenter/support)
- [iA Presenter on YouTube](https://www.youtube.com/@iAInc101)

---

Great presentations tell great stories. Use this corpus to keep syntax consistent, make the visible slide surface count, and use speaker notes to deepen rather than hide the argument.
