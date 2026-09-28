# 0007 — Tier 1 cross-platform MVP

- Status: Accepted
- Date: 2026-09-28

## Context

An independent developer tool cannot assume the operating system used by the
ContentArc prototype.

## Decision

Tier 1 MVP platforms are macOS, Ubuntu Linux, native Windows, and Ubuntu on
WSL2. Other Linux distributions, containers, and remote environments are best
effort until after MVP.

## Consequences

Paths, process control, locking, executable discovery, terminal behavior, and
atomic replacement need explicit platform boundaries and evidence.

## Revisit when

Usage evidence justifies adding or removing a Tier 1 environment.
