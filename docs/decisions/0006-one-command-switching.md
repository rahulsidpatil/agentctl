# 0006 — One-command switching

- Status: Accepted
- Date: 2026-09-28

## Context

Manual checkpoint and lifecycle commands made the prototype too complex for
normal use.

## Decision

The primary interface is `agentctl switch [provider]`. The supervisor performs
handoff, recovery, selection, and launch mechanics. Diagnostic lifecycle tools
remain under `agentctl advanced`.

## Consequences

Defaults and messages must be trustworthy and actionable. Internal state must
not leak into the everyday workflow.

## Revisit when

User research shows a simpler interface or a necessary ambiguity that cannot be
resolved safely by defaults.
