# Anti-Patterns: Common Mistakes to Avoid

> **This document demonstrates common mistakes in iA Presenter and their fixes.**
>
> **Each section shows a broken pattern, explains why it fails, and provides the correct version.**

---

## Spaces instead of TABs

### The mistake

Text prefixed with spaces does not appear on the slide. iA Presenter requires actual TAB characters (`\t`).

```markdown
## My Slide

    This uses spaces — invisible to audience
```

### The fix

Use real TAB characters. In the examples below, indented lines use TABs.

```markdown
## My Slide

	This uses a TAB — visible to audience
```

---

## Reading from slides

### The mistake

Putting the entire script on the slide turns the presenter into a reader. The audience reads faster than you speak, then stops listening.

```markdown
## Our Strategy

	We are now going to discuss our comprehensive strategy
	for improving customer satisfaction across all channels.
	This involves several key initiatives that we have been
	developing over the past quarter. Let me walk you through
	each of these initiatives in detail.
```

### The fix

Move the argument to speaker notes. Show only what is worth seeing.

```markdown
## Our Strategy

Our full strategy covers four channels, but the audience only needs to remember the priority order and the timeline.

	1. Fix the support queue first
	2. Rebuild the onboarding flow
	3. Launch the self-serve portal
	4. Revisit pricing communication
```

---

## Walls of text on slides

### The mistake

A paragraph dumped onto a slide cannot be scanned. The audience gives up.

```markdown
## Market Analysis

	Lorem ipsum dolor sit amet, consectetur adipiscing elit.
	Sed do eiusmod tempor incididunt ut labore et dolore magna
	aliqua. Ut enim ad minim veniam, quis nostrud exercitation
	ullamco laboris nisi ut aliquip ex ea commodo consequat.
```

### The fix

Distill to the one thing that matters. Let notes carry the detail.

```markdown
## Market Analysis

The full analysis covers five segments, but three drive 80% of the growth story.

	Enterprise: 42% of new revenue
	Mid-market: accelerating
	SMB: stable but low-margin
```

---

## Too many bullet points

### The mistake

A long bullet list reads like a memo, not a slide.

```markdown
## Key Features

	- Feature 1
	- Feature 2
	- Feature 3
	- Feature 4
	- Feature 5
	- Feature 6
	- Feature 7
	- Feature 8
```

### The fix

Three to five points maximum. Group the rest or move them to notes.

```markdown
## Key Features

Features 4-8 are real but secondary. The audience needs to remember only the top three.

	1. Unified inbox
	2. AI-assisted drafts
	3. Real-time quality scoring
```

---

## Forced side-by-side layout

### The mistake

Using side-by-side when the two halves are unrelated or unbalanced makes the slide feel broken.

```markdown
## Update

	Monday meeting notes go here

	Also the logo changed
```

### The fix

Only use side-by-side when comparison adds meaning. Otherwise stack.

```markdown
## This quarter
#### VS
## Last quarter

	Revenue grew 12%
	Churn dropped to 4%

	Revenue flat
	Churn was 9%
```

---

## Hidden deck — all meaning in notes

### The mistake

Every slide is just a title plus two small bullets. The real argument is invisible unless you read the editor pane.

```markdown
## Our Approach

	- Approach item
	- Another item

We spent six months evaluating three vendors, ran pilots with two teams,
and built a custom scoring model that accounts for integration cost,
adoption speed, and long-term maintenance burden. The winner was clear
by week four, but we continued to validate.
```

### The fix

Promote the key substance to the visible slide. Notes deepen, not replace.

```markdown
### Six months. Three vendors. One clear winner.
#### The scoring model made the call by week four.

We validated for two more months after the signal was clear — not because we doubted the result, but because the stakes justified the extra confidence.

	| Criteria | Vendor A | Vendor B | Vendor C |
	|---|---|---|---|
	| Integration cost | Low | High | Medium |
	| Adoption speed | Fast | Slow | Medium |
	| Maintenance | Low | High | Low |
```

---

## Weak ending — "Thank You / Questions?"

### The mistake

Ending on a generic slide wastes the most memorable position in the deck.

```markdown
# Thank You

## Questions?

Let's continue the discussion!
```

### The fix

End with a real action, decision, or landing line. Put "Questions" on a follow-up slide if needed.

```markdown
## Start with one queue.
#### Measure trust before scale.

If this room agrees, we can have a pilot running by Friday. The first data point lands in two weeks.
```

---

## One-pattern deck — same silhouette everywhere

### The mistake

Every slide follows the identical shape: title, three tiny tab-bullets, notes. The deck feels flat even if the content is good.

### The fix

Vary the visible surface. Mix heading stacks, contrasts, quotes, sequences, tables, and one-line landings. See `syntax/00-complete-reference.md` and `skills/ia-presenter-deck/references/SLIDE-SURFACE-PATTERNS.md` for the full pattern set.

---

## No heading hierarchy

### The mistake

Using `#` for mid-deck section breaks creates multiple cover slides. The deck structure breaks.

```markdown
# First Topic
# Second Topic
# Third Topic
```

### The fix

Use `#` only for the cover. Use `##` for content slide titles. Use `###` and `####` for heading stacks within slides.

```markdown
# Presentation Title
## Subtitle

---
## First Topic

---
### Second Topic Detail
#### With a qualifying subtitle
```

---

## Summary Checklist

Before delivering a generated deck, check for these anti-patterns:

	1. TABs, not spaces, for visible content
	2. Speaker notes carry the argument — slides carry the shape
	3. Three to five visible points maximum per slide
	4. Side-by-side only for real comparisons
	5. Visible surface carries meaning, not just titles
	6. Ending is a decision, action, or landing line
	7. Surface rhythm varies across the deck
	8. `#` is cover only — `##` for content slides

---

**Source:** Compiled from iA Presenter conventions and this repository's skill rubric.
