# 0008 — Test-driven development

- Status: Accepted
- Date: 2026-09-28

## Context

Multi-agent and cross-platform changes are difficult to review from generated
code alone. Safety behavior must be reproducible.

## Decision

Behavior changes follow red-green-refactor. Provider and platform contracts use
deterministic test doubles; real-provider tests are controlled acceptance tests.

## Consequences

Pull requests include TDD evidence. Documentation-only work and exploratory
spikes explain why a failing test is not applicable.

## Revisit when

Project evidence identifies a more effective practice with equal or stronger
regression protection.
