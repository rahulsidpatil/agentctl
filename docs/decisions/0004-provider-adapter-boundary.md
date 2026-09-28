# 0004 — Provider adapter boundary

- Status: Accepted
- Date: 2026-09-28

## Context

Codex, Claude, and Antigravity differ in executable discovery, prompt transport,
output, authentication, and exhaustion behavior.

## Decision

Contain provider differences behind a shared adapter contract covering
availability, launch, context injection, output interpretation, and termination.

## Consequences

Core switching stays provider-neutral. Each adapter must pass the same contract
suite, and provider credentials remain owned by its CLI.

## Revisit when

A provider cannot satisfy the contract without changing core safety semantics.
