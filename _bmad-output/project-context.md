# Project Context

## Initiative

Presentation System v1 for `ia-presenter-know-how`

## Process Rule

`BMAD > BMADX`

- BMAD artifacts are the durable source of truth for scope and architecture.
- BMADX adds routing, verification discipline, and the X4 scaffold bundle.

## Problem

The repository can generate stronger `.iapresenter` decks than before, but quality is still unstable because the loop depends on manual screenshots and ad hoc feedback.

Current bottlenecks:
- no cheap local render loop
- no structured split between story QA and visual QA
- no bounded auto-fix loop
- no durable local-only learning lane for private decks

## V1 Goal

Build a local macOS-native presentation system that can:
- author or reuse a deck
- emit slide-level manifest data
- render the deck through iA Presenter export or preview workflows
- run structured story review and visual review
- build a bounded fix plan
- optionally apply one or two local auto-fix passes

## Core Roles

- `author`: expands or refines a deck and emits manifest data
- `render`: uses iA Presenter locally to produce rendered artifacts
- `story QA`: judges logic, readability, pacing, tension, and note abuse
- `visual QA`: judges rendered evidence for composition and aesthetic defects
- `fix`: applies only named, local corrections and reruns review

## Local-Only Data Rule

- `.presentation-system/` is local-only and gitignored
- private deck inputs, renders, and review runs never become tracked files
- only anonymized derivatives, public patterns, and updated rules may enter the repo

## Primary V1 Render Strategy

- primary: app-native `HTML` or `Images` export from iA Presenter
- secondary fallback: live preview or presentation-window capture
- do not rely on browser approximations when app-native render exists

## Acceptance Shape

The system is good enough for v1 when:
- it creates a run directory per deck
- it produces `manifest.json`, `render.json`, `story-review.json`, `visual-review.json`, and `fix-plan.json`
- it supports bounded auto-fix on a working copy
- it can improve at least one public anti-pattern deck in an automated test

## Constraints

- local macOS only
- no CI or remote render requirement in v1
- no second durable plan store outside BMAD artifacts
- no raw private deck publishing
