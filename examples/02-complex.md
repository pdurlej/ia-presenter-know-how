# Complete iA Presenter Example

> **A comprehensive presentation showcasing all major iA Presenter surface patterns and syntax features.**
>
> **This example demonstrates heading stacks, contrasts, quotes, tables, sequences, one-line landings, and proper speaker notes.**

---

# The Onboarding Tax
## Why new hires stay slow longer than they should

---
## What this deck covers

Set expectations early so the audience knows where the argument is going.

	1. The real cost of slow onboarding
	2. Where the friction actually lives
	3. What one team changed
	4. A pilot you can steal

---
### The number nobody tracks
#### Time to first autonomous decision

Most onboarding metrics measure completion — courses finished, docs read, boxes checked. None of them measure when someone can actually make a call without asking.

---
## Current onboarding
#### VS
## First real contribution

This contrast reframes the problem. The audience should feel the gap between what the company measures and what actually matters.

	Courses completed in week 1

	First confident decision in week 8

---
### Where the friction lives

Do not list everything. Pick the three that hurt the most.

	Context is scattered
	Tribal knowledge is oral
	Feedback loops are slow

---
### What new hires actually say

Let the voice of the user carry the argument here.

	> "I finished all the training, but I still did not know who to ask."
	> — Engineer, month two

---
## What One Team Changed

This section reset signals a shift from problem to solution.

---
### Three moves, not a transformation

Good case studies show restraint.

	1. Wrote down the five most common first-week questions
	2. Paired every new hire with a decision buddy
	3. Replaced the 40-page wiki with a one-page cheat sheet

---
### Before and after

Keep the table small enough to scan in one glance.

	| Signal | Before | After 90 days |
	|---|---|---|
	| Time to first solo PR | 6 weeks | 2 weeks |
	| Questions to manager per day | 8 | 3 |
	| "I feel productive" survey | 34% | 71% |

---
### What surprised them

Every good story needs one human moment.

	> "The cheat sheet mattered less than knowing someone expected me to use it."

---
### The pattern worth copying

This slide converts the story into a portable principle.

	Simple documentation beats comprehensive documentation.
	A named person beats a wiki link.
	Permission to decide beats permission to ask.

---
### What this costs

Address the objection before it forms.

	Two hours to write the cheat sheet
	One buddy assignment per new hire
	One retro at day 30

---
## Images and Code

This section demonstrates additional syntax features for reference.

---
### Image syntax

Images can use Markdown syntax, but Content Blocks Syntax is better when you need image metadata.

/assets/onboarding-flow.jpg
size: contain

In this repository, image paths under `/assets/` are illustrative syntax examples.

---
### Code on slides

Code blocks work inside TAB-prefixed content.

	```python
	def first_week_checklist(hire):
	    return [q for q in COMMON_QUESTIONS if not hire.has_answered(q)]
	```

---
### Side-by-side images

Separate visible content blocks with a blank line (no TAB) to create columns.

/assets/before-wiki.jpg

/assets/after-cheatsheet.jpg

---
## Pick one team.
#### Run the pilot for 30 days. Measure confidence, not completion.

The ask is concrete enough to approve in the room. Do not dilute it with a recap.
