---
name: "ia-presenter-deck"
description: "Create, improve, or restructure iA Presenter decks as `.iapresenter` files. Use when Codex needs to build presentation-ready iA Presenter content, generate multiple candidate directions before choosing one, or turn a brief into a stronger text-first deck with lean slides, speaker notes, and a clear closing action."
---

# iA Presenter Deck

Use this skill when the task is to create a new iA Presenter deck, improve an existing `.iapresenter`, or generate several candidate directions before selecting one for deeper iteration.

This skill is canonical in the repository. It is designed to work with the corpus in the same checkout, especially:
- `syntax/00-complete-reference.md`
- `examples/03-anti-patterns.md`
- `golden-candidates/README.md`

If you install this skill into `~/.codex/skills/`, still use it from within a checkout of this repository so the corpus files above are available.

Always read these first:
- `references/WORKFLOW.md`
- `references/INTAKE.md`
- `references/RUBRIC.md`

Read as needed:
- `references/TEMPLATES.md`
- `references/LAYOUT-HEURISTICS.md`
- `references/SLIDE-SURFACE-PATTERNS.md`

## Output Contract

Default output:
- one `.iapresenter` package directory with at least `text.md` and `info.json`
- short assumptions summary in the assistant response
- short self-review summary in the assistant response

Optional mode:
- candidate mode produces 3-4 distinct directions first
- then one selected direction gets expanded into a full `.iapresenter` package

Do not promise or default to:
- PPTX
- Marp
- PowerPoint orchestration
- chart export scripts
- `/output/` folder bundles

## Core Rules

1. Default to iA Presenter conventions, not PowerPoint conventions.
2. Keep slides lean, but do not hide the whole deck in speaker notes.
3. Use `##` as the default content-slide title convention after `---`.
4. Use TAB-prefixed text only when it should appear on the slide.
5. Use more than one visible slide surface when the deck needs it: headings, subheadings, body text, lists, quotes, tables, images, and one-line landings.
6. Prefer strong, punchy slide titles over generic topic labels.
7. Use full assertion-style headings only when precision matters more than punch.
8. End with a real action, decision, or landing line. Do not end on generic `Thank you` or `Questions`.

## Candidate Mode

Use candidate mode when:
- the user asks for options
- the brief is still fuzzy
- the team is exploring future Golden Deck patterns

Rules:
- produce 3-4 genuinely different directions
- vary narrative spine, pacing, and slide rhythm
- do not create four cosmetic rewrites of the same deck
- keep candidates concise enough to compare quickly

## Drafting Rules

- One slide, one job.
- The audience-visible layer must carry enough meaning to be worth showing.
- Avoid thin two-column slides unless comparison makes the slide stronger.
- Avoid dense tables unless exact deltas truly matter.
- Avoid bullet stacks that read like a memo.
- Avoid repeating the same visible pattern for the whole deck unless the monotony is deliberate.
- If a slide feels empty after splitting, merge or redesign it.
- Speaker notes should sound sayable and should deepen the visible slide, not replace it.

## Self-Review

Before delivery:
1. score the deck using `references/RUBRIC.md`
2. identify the weakest 3 slides or patterns
3. refine once before presenting the result

If the draft still resembles anti-patterns from `examples/03-anti-patterns.md`, do not present it as final.
