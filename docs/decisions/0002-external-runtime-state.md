# 0002 — External runtime state

- Status: Accepted
- Date: 2026-09-28

## Context

Handoffs, logs, leases, and snapshots may contain transient or private recovery
evidence and should not pollute or be committed to application repositories.

## Decision

Store runtime state in the operating system's user-state location. Keep only
`.agentctl/config.json` in a target repository.

## Consequences

Repository adoption stays small and private evidence remains local. Multi-machine
handoff requires a future explicit synchronization design.

## Revisit when

A secure, opt-in team or multi-machine synchronization model is designed.
