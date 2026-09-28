# 0003 — Supervisor persists checkpoints

- Status: Accepted
- Date: 2026-09-28

## Context

Sandboxed agents may not write machine-private state, while repository output
can spoof checkpoint-looking text.

## Decision

Agents emit a structured checkpoint through a trusted final-message channel.
The supervisor validates and persists it atomically.

## Consequences

Agents need no private-state permission. Provider adapters must identify trusted
final messages and reject command-output lookalikes.

## Revisit when

Providers expose a stronger authenticated checkpoint API.
