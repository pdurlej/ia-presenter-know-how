# AGENTS.md for iA Presenter Presentation System

This repository uses `BMAD > BMADX`.

- BMAD remains the process system and workflow architecture.
- BMADX remains the operational routing layer for Codex.
- If routing is unclear, use `bmad-help` instead of inventing a parallel workflow.

## Routing

- `X1` — One-shot: tiny, local task.
- `X2` — Regular: short plan and standard verify.
- `X3` — Complex (BMAD): enter the real BMAD flow.
- `X4` — Rescue Mode (`X4/FUBAR`, BMAD+): scaffold bundle, rollout, verify matrix.

## Durable context

- Process and artifacts: BMAD.
- Technical memory: `_bmad-output/project-context.md`.
- Session-local notes are not source-of-truth.

## Verify before done

- Do not close work without evidence.
- For non-trivial changes, run review.
- If convenience conflicts with the process artifact, BMAD wins.

## Escalation

- If `X1` is not enough, move to `X2`.
- If the task needs BMAD artifacts, move to `X3`.
- If the repo needs scaffolding, ownership cleanup, or a rollout/verify layer, use `X4`.
- Do not render `X4/FUBAR` when `X2` or a normal `X3` is enough.

Generated: PUBLIC_SAMPLE
Project path: $PROJECT_ROOT
