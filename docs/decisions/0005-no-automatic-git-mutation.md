# 0005 — Never mutate Git recovery state automatically

- Status: Accepted
- Date: 2026-09-28

## Context

Automatic commit, stash, reset, or clean operations can change authorship,
remove files, conceal conflicts, or lose work during a failed handoff.

## Decision

`agentctl` may inspect Git and copy safe recovery evidence, but it never commits,
pushes, deploys, stashes, resets, cleans, or discards changes automatically.

## Consequences

Some recovery steps remain manual. Safety and inspectability take precedence
over a superficially cleaner worktree.

## Revisit when

Never for destructive defaults; explicit future commands would require separate
consent, recovery guarantees, and an ADR.
