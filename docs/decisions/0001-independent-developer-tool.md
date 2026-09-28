# 0001 — Independent developer tool

- Status: Accepted
- Date: 2026-09-28

## Context

The first relay lived inside ContentArc, but safe agent switching is useful to
any Git repository and should not require product-specific scripts.

## Decision

Build `agentctl` as an independently installed open-source CLI. Target
repositories contain only portable configuration and optional instructions.

## Consequences

The tool owns compatibility, packaging, machine state, and provider adapters.
Product repositories avoid duplicated lifecycle machinery.

## Revisit when

Evidence shows repository-local orchestration is required for a capability that
cannot be expressed through configuration or adapters.
