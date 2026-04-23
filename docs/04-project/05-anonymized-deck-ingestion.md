# Anonymized Deck Ingestion Workflow

> How private source decks should be turned into safe, reusable public references in this repository.

---

## Purpose

This repository should get better over time by learning from real, strong presentations.

Some of those presentations will originate as private decks shared directly with the maintainer. Before anything derived from them is committed to GitHub, the deck must be anonymized and stripped of sensitive context.

This document defines that workflow.

---

## Expected Input

Typical future input:
- a real `.iapresenter` package
- a deck exported from another tool and adapted into `.iapresenter`
- supporting screenshots, notes, or spoken guidance about why the deck works

The source deck may contain:
- company names
- customer names
- employee names
- internal metrics
- product codenames
- private process details
- identifying images or screenshots

Assume source decks are private unless explicitly stated otherwise.

---

## Target Output

The public repo should receive one of these:

### 1. An anonymized reference deck

Store under:
- `reference-decks/<slug>.iapresenter/`

Use when:
- the deck structure is reusable
- the visible slide surfaces are worth studying
- the content can be safely generalized

### 2. A derived pattern deck

Use when:
- the original deck is too sensitive to publish directly
- the best value is in the narrative pattern or slide rhythm
- content should be rewritten from scratch while preserving the structural lesson

### 3. A documented learning only

Use when:
- the deck cannot be safely published even after anonymization
- the learnings still deserve to update the skill, rubric, or templates

In that case, update:
- `skills/ia-presenter-deck/`
- `docs/04-project/`
- possibly `golden-candidates/`

---

## Required Anonymization Pass

Before publishing, remove or generalize:
- names of companies
- names of customers
- names of employees or stakeholders
- internal project names
- exact private metrics when they could identify a company
- dates, timelines, or deal values that materially de-anonymize the source
- URLs, screenshots, or assets that reveal systems, teams, or clients

Replace with:
- role-based labels
- generalized sectors
- rounded or reframed numbers
- neutral placeholders only where necessary

Bad:
- `Acme Corp churn dropped from 17.3% to 9.8% in Q3 2025`

Better:
- `A mid-market SaaS team cut churn meaningfully within one quarter`

Best, when exact deltas still matter structurally:
- `Churn dropped from high teens to under ten percent in one quarter`

---

## Review Checklist

Before committing a public deck, ask:

1. Can the source company or person still be inferred from the content?
2. Do any screenshots, charts, or examples reveal private systems or naming?
3. Are the metrics more precise than the lesson requires?
4. Does the public version preserve the useful deck pattern after anonymization?
5. Would I be comfortable with the source owner seeing the public version on GitHub?

If any answer is unsafe, do not publish the deck as-is.

---

## Recommended Workflow

### Step 1: Import the private deck locally

Do not commit the raw source deck into this repository.

Work from a local copy outside the tracked public corpus if needed.

### Step 2: Identify what is reusable

Usually the reusable parts are:
- story spine
- slide rhythm
- surface patterns
- type of proof
- structure of the close

### Step 3: Decide publication level

Choose one:
- anonymized reference deck
- derived pattern deck
- internal learning only

### Step 4: Rewrite or sanitize

Prefer rewriting over redaction when:
- the source is sensitive
- the original wording is too identifying
- the structure matters more than the exact content

### Step 5: Repackage as a clean `.iapresenter`

Public decks in this repo should follow the normal package format:

```text
deck-name.iapresenter/
├── info.json
└── text.md
```

### Step 6: Document provenance at a high level

Do not expose the source.

Use a neutral note such as:
- derived from a private internal deck
- anonymized from a real client presentation
- rebuilt from a private workshop deck

### Step 7: Commit only the safe derivative

The raw deck stays private. Only the sanitized derivative belongs on GitHub.

---

## Where Public Decks Should Live

Use:
- `reference-decks/` for stable, anonymized public references
- `golden-candidates/` for actively iterated experimental candidates

This separation matters:
- `golden-candidates/` are for exploration
- `reference-decks/` are for stronger reusable patterns that survived review

---

## Project Rule

When in doubt, prefer:
- less specificity
- more rewriting
- stronger anonymization
- publishing the lesson instead of the deck

The public repo should get smarter without leaking the source material that taught it.

