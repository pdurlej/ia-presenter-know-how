# Repository Maintenance Checklist

> Use this checklist before a release, a README rewrite, or any public announcement about the repository.

---

## Positioning and Naming

- [ ] `README.md` describes the repo as an LLM-first corpus, not as a community project or a fresh RAG starter
- [ ] No references to the previous repository name remain in maintained repo-facing documents
- [ ] No placeholder usernames, contact markers, or dead community-path references remain
- [ ] The active repo name shown in examples and instructions is `ia-presenter-know-how`

---

## Content Accuracy

- [ ] `docs/01-course/` still contains 6 tutorial-style documents
- [ ] `docs/02-tips/` still contains 12 articles
- [ ] `docs/03-videos/` is described accurately as transcripts and notes with mixed completeness
- [ ] `syntax/00-complete-reference.md` matches the current corpus convention of `##` as the default content-slide title
- [ ] `examples/` remain readable and use actual TAB characters where slide-visible content is intended
- [ ] `assets/README.md` clearly states that asset paths are illustrative and that no asset pack is bundled

---

## README Sanity Check

- [ ] All internal file paths referenced in `README.md` exist
- [ ] The repository structure block matches the current tree
- [ ] The prompt template and retrieval recipe match the current corpus conventions
- [ ] The video section does not claim five full transcripts
- [ ] The status section does not imply that community workflow is already active

---

## GitHub Surface

- [ ] Repository description matches the current LLM-first positioning
- [ ] Topics are up to date and do not overstate product scope
- [ ] README renders correctly on GitHub
- [ ] LICENSE is present and linked
- [ ] Any public release notes describe the video and asset limitations honestly

---

## Pre-Push Verification

Run these checks before pushing:

```bash
git status --short --branch
rg -n $'\\t' README.md syntax/00-complete-reference.md examples/*.md
```

Expected outcome:
- the stale-string sweep returns no matches
- the TAB grep still finds slide-content examples
- `git status` only shows intentional edits

---

## Deferred Work

These are explicitly outside the current editorial-cleanup baseline:
- a live community contribution process
- a bundled screenshot or image asset pack
- complete transcripts for every video note
- a separate legal review of derivative-source packaging
