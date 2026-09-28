# Delivery lifecycle

```text
Problem
  -> issue with measurable acceptance criteria
  -> decision or experiment when uncertainty exists
  -> failing test
  -> implementation and refactoring
  -> cross-platform and provider validation
  -> pull request with evidence
  -> release
  -> retrospective
  -> reusable learning
```

## Entry

New work enters the GitHub Project as `Inbox`. Triage assigns type, area,
platform, priority, size, target milestone, and dependencies. Only issues that
meet the Definition of Ready move to `Ready`.

## Execution

One focused branch and pull request should close one actionable issue. Unknowns
that could materially change the implementation use an experiment or ADR before
large code changes. Agents record sanitized checkpoints at handoff.

## Verification

Required CI is necessary but not always sufficient. Real provider behavior,
WSL, installation, and release workflows may require controlled acceptance
tests. Evidence is linked from the issue or pull request.

## Learning

Milestones and releases compare intended and actual outcomes. Missed scope is
explained rather than silently rescheduled. Repeatable lessons are promoted to
the playbook; project-specific observations stay with their evidence.
