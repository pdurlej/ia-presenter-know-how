# Basic Presentation Example

> **A minimal, working iA Presenter presentation demonstrating core syntax.**
>
> **This example follows the conventions defined in `syntax/00-complete-reference.md` and matches the quality direction of `golden-candidates/`.**

---

# Why We Ship on Fridays
## A case for calmer releases

---
## The pattern everyone knows

Most teams treat Friday deploys as dangerous. But the real danger is not the day — it is the process around it.

	1. Big batch lands Thursday night
	2. Deploy Friday morning
	3. Nobody watches the dashboard
	4. Monday starts with a fire

---
## Friday is not the problem
#### The batch is.

The risk scales with change size, not with the calendar. A small, well-tested deploy on Friday is safer than a large, rushed one on Tuesday.

---
## What changes when deploys get small

This is the core argument. If the audience believes this, the rest follows.

	Smaller diffs
	Faster reviews
	Shorter blast radius

---
## One week of data

Real proof beats philosophy. Keep the table tiny.

	| Metric | Big batch | Small daily |
	|---|---|---|
	| Rollback rate | 14% | 2% |
	| Time to detect | 3h | 18min |
	| On-call pages | 7 | 1 |

---
## Start with one service.
#### Measure confidence before expanding.

The ask is small enough to say yes to in the room.
