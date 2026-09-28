# Project origin

## The problem

`agentctl` began while developing ContentArc with multiple coding agents. Work
could be in progress in Codex when its context or token budget ended, leaving a
developer to reconstruct the objective, decisions, modified files, validation,
and remaining work before Claude or Antigravity could continue.

The first response was repository-local relay machinery in ContentArc. It
proved that structured checkpoints, exclusive ownership, and Git recovery
evidence were useful, but it also exposed a product boundary: agent switching
is a developer-machine capability that should work for any repository.

## Product extraction

The relay was redesigned as the independent `agentctl` command-line product.
The intended journey became:

```text
install agentctl
enter any Git repository
agentctl init
agentctl switch [provider]
```

Repository footprint was reduced to portable project configuration. Runtime
handoffs, leases, logs, and recovery snapshots moved to user-owned machine
state. Provider-specific behavior was placed behind adapters.

## Initial publication

On 2026-09-28, commit `45f15aa` initialized the public
`rahulsidpatil/agentctl` repository at version `0.3.0a2`. The default branch was
set to `master`, CI covered Python 3.9 and 3.12 on Ubuntu, and branch protection
required both checks, an up-to-date pull request, and resolved conversations.
Administrator bypass, force pushes, and deletion were disabled; approval was
not required while the project had one maintainer.

This document records verified project facts rather than raw chat transcripts.
Future corrections should cite commits, issues, pull requests, releases, or
experiment evidence.
