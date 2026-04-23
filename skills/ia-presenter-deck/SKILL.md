---
name: "ia-presenter-deck"
description: "Create, improve, or restructure iA Presenter decks as `.iapresenter` files. Use when Codex needs to build presentation-ready iA Presenter content, generate multiple candidate directions before choosing one, or turn a brief into a stronger deck with intentional visible slide surfaces, sayable notes, and a clear closing action."
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
- `references/RHYTHM-MAPS.md`
- `references/PRESENTER-LAYERS.md`
- `references/IMAGE-SOURCING.md`
- `references/LITERATURE.md`
- `references/EXECUTIVE-NARRATIVE.md`

System pairings:
- `../ia-presenter-render/`: export-first render layer for real iA Presenter output
- `../ia-presenter-story-qa/`: logic, pacing, and note-abuse review
- `../ia-presenter-qa/`: rendered visual QA over exported slides

## Output Contract

Default output:
- one `.iapresenter` package directory with at least `text.md` and `info.json`
- one `manifest.json` in the local run workspace when using the presentation system
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
2. Write the script first. Design and visual polish come later.
3. Keep slides lean, but do not hide the deck in speaker notes.
4. Use `##` as the default content-slide title convention after `---`.
5. Use TAB-prefixed text only when it should appear on the slide.
6. Preserve tension between what the audience sees and what the presenter says.
7. Use more than one visible slide surface when the deck needs it: headings, subheadings, body text, lists, quotes, tables, images, and one-line landings.
8. Prefer strong, punchy slide titles over generic topic labels.
9. Use full assertion-style headings only when precision matters more than punch.
10. End with a real action, decision, or landing line. Do not end on generic `Thank you` or `Questions`.
11. Design visible rhythm on purpose: chapter cards, heading stacks, contrasts, sequences, proof, and closers should not all look the same.
12. When visuals exist, use them deliberately; when they do not, create contrast through typography and structure, not empty whitespace.
13. Use placeholder visuals freely while drafting, but do not let image hunting interrupt story work.
14. Assume the layout is responsive. Do not rely on brittle side-by-side compositions that break when stacked.
15. If stock imagery is needed, prefer official provider search on Unsplash or Pexels instead of random web scraping.
16. Think in cells, not only in lines of Markdown. Blank lines create separate cells; elements kept together in one cell tend to stack.
17. iA Presenter has a layout picker with many valid layouts. Do not treat the first auto-layout as final when the slide is clearly asking for a different composition.
18. Treat notes as suspicious by default. If a key point only exists in notes, the slide is probably underdesigned.
19. Slides support the presenter; they are not projected documents.
20. The audience will either read or listen. Do not force them to do both at once.

## Candidate Mode

Use candidate mode when:
- the user asks for options
- the brief is still fuzzy
- the team is exploring future Golden Deck patterns

Rules:
- produce 3-4 genuinely different directions
- vary narrative spine, pacing, and slide rhythm
- vary surface mix, not only wording
- do not create four cosmetic rewrites of the same deck
- keep candidates concise enough to compare quickly

## Drafting Rules

- One slide, one job.
- One slide, one visible payload.
- The audience-visible layer must carry enough meaning to be worth showing.
- Avoid thin two-column slides unless comparison makes the slide stronger.
- Avoid dense tables unless exact deltas truly matter.
- Avoid bullet stacks that read like a memo.
- Avoid treating ordered lists as the default shape of every slide.
- Avoid repeating the same visible pattern for the whole deck unless the monotony is deliberate.
- If a slide feels empty after splitting, merge or redesign it.
- If a slide wants a full-width proof table, keep the title stack and table in one intentional cell instead of stranding the title in a left column.
- If a slide wants an image panel, build an intentional split with one visual cell and one text cell instead of letting the image become a tiny floating object.
- Prefer section resets and heading stacks over weak filler slides.
- Avoid showing everything you intend to say.
- Speaker notes should sound sayable and should deepen the visible slide, not replace it.
- If the slide does not make sense without opening the notes, redesign the slide before adding more notes.

## Self-Review

Before delivery:
1. score the deck using `references/RUBRIC.md`
2. identify the weakest 3 slides or patterns
3. render the deck and review the exported output
4. refine once before presenting the result

Presentation-system rule:
- a deck is not done when the Markdown looks plausible
- a deck is done only after a rendered review exists
- if rendered review is blocked by missing permissions or export failure, report that explicitly

If the draft still resembles anti-patterns from `examples/03-anti-patterns.md`, do not present it as final.
