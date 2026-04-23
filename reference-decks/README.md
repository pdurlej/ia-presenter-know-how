# Reference Decks

> Public, reusable `.iapresenter` decks derived from real work and safe to keep in the repository.

This directory is reserved for stronger deck references than `golden-candidates/`.

Use it for decks that are:
- stable enough to study as patterns
- visually and structurally stronger than first-pass candidates
- safe to publish after anonymization

## What Belongs Here

- anonymized decks derived from private source presentations
- rewritten pattern decks based on real presentations
- public reference decks worth reusing in future prompts and reviews

## What Does Not Belong Here

- raw private client or company decks
- experimental drafts still being iterated
- decks that still expose names, systems, metrics, or identifying screenshots

## Package Rule

Each deck should be a real `.iapresenter` package directory:

```text
example-reference.iapresenter/
├── info.json
└── text.md
```

## Suggested Naming

Use neutral, reusable names such as:
- `saas-board-reframe.iapresenter`
- `consulting-proposal-arc.iapresenter`
- `product-vision-reset.iapresenter`

Avoid names that encode the original source company, project, or person.

## Provenance Note

If helpful, add a short line inside the deck or a local note saying the deck was:
- anonymized from a private source
- rewritten from a real presentation pattern
- generalized from internal material

Do not identify the source directly.

