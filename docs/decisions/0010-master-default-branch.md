# 0010 — Master default branch

- Status: Accepted
- Date: 2026-09-28

## Context

The repository owner selected `master` while publishing the initial project.

## Decision

Use `master` as the default protected branch. Development occurs on focused
branches and merges through pull requests.

## Consequences

Documentation, workflows, release automation, and examples target `master`.
Changing it would require link, automation, and protection migration.

## Revisit when

The maintainer explicitly chooses a different naming convention and approves a
complete migration.
