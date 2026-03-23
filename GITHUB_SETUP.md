# GitHub Repository Operations

> Use this document to maintain the published repository at https://github.com/pdurlej/ia-presenter-know-how.

---

## Canonical Repository

- repository: `pdurlej/ia-presenter-know-how`
- primary remote: `https://github.com/pdurlej/ia-presenter-know-how.git`
- current intent: LLM-first corpus for iA Presenter, still readable as human documentation

Verify the local remote before publishing changes:

```bash
git remote -v
```

Expected origin:

```text
origin  https://github.com/pdurlej/ia-presenter-know-how.git (fetch)
origin  https://github.com/pdurlej/ia-presenter-know-how.git (push)
```

If needed, reset the remote URL:

```bash
git remote set-url origin https://github.com/pdurlej/ia-presenter-know-how.git
```

---

## Recommended GitHub Metadata

Suggested repository description:

```text
LLM-first corpus for generating iA Presenter presentations with Markdown. Includes syntax reference, examples, tutorials, and video-derived notes.
```

Suggested topics:

- `presentation`
- `markdown`
- `llm`
- `ai-assistant`
- `prompt-engineering`
- `retrieval`
- `documentation`
- `ia-presenter`

Suggested homepage:

```text
https://github.com/pdurlej/ia-presenter-know-how#readme
```

---

## Publishing Pass

Before pushing a documentation update:

```bash
git status --short --branch
```

Also run a stale-string sweep for:
- the previous repository name
- removed community-path references
- placeholder usernames or contact markers

Review the README render on GitHub after pushing:
- repo positioning matches the current LLM-first intent
- `docs/03-videos/` is described as transcripts and notes, not five full transcripts
- `assets/` is described as path convention only, not a shipped media pack
- internal file paths mentioned in the README actually exist

Push normally once the branch is clean enough:

```bash
git push origin master
```

---

## Release Notes Template

When cutting a release or posting a public update, use wording that matches the repo's actual state:

```markdown
## Included

- 6 tutorial-style course documents
- 12 presentation and storytelling articles
- 1 syntax reference
- 3 worked examples
- 5 video-derived notes with mixed completeness

## Positioning

This repository is an LLM-first corpus for iA Presenter Markdown generation and validation.

## Caveats

- Example asset paths are illustrative and not bundled as media files.
- Video coverage includes transcripts where available and notes where transcripts are missing or duplicated.
```

---

## Troubleshooting

### Wrong remote URL

```bash
git remote set-url origin https://github.com/pdurlej/ia-presenter-know-how.git
```

### Authentication failed

Use the GitHub CLI instead of embedding credentials in the remote URL:

```bash
gh auth login
git push origin master
```

### README still shows stale wording

Run the stale-string sweep described above before pushing.

---

## Deferred Work

These are not part of the current cleanup baseline:
- a live community contribution workflow
- a bundled asset pack
- fuller transcript coverage for all video notes
- a separate legal review of derivative-source packaging
