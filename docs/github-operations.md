# GitHub operations runbook

This runbook makes the repository's project-management configuration
reproducible. GitHub remains the live source for issue and Project state.

## Labels

Create these namespaced labels:

```text
type:feature type:bug type:task type:documentation type:security
type:experiment type:process-gap type:spike
area:core area:cli area:provider area:platform area:packaging area:ci
area:documentation
platform:all platform:macos platform:ubuntu platform:windows platform:wsl
provider:codex provider:claude provider:antigravity
priority:P0 priority:P1 priority:P2 priority:P3
blocked needs-design good-first-issue help-wanted
```

Status belongs in the Project field, not labels.

## Milestones

Create `M0 — Governance`, `M1 — Reliable Core`, `M2 — Provider Handoffs`,
`M3 — Cross-Platform`, and `M4 — MVP Release`. Copy the exit criteria from
[ROADMAP.md](../ROADMAP.md) into their descriptions.

## Project

Create the public user Project `agentctl Product Development` with fields:

- Status: Inbox, Backlog, Ready, In Progress, In Review, Blocked, Done
- Priority: P0, P1, P2, P3
- Size: XS, S, M, L, XL
- Target: M1 Core, M2 Providers, M3 Platforms, M4 MVP
- Platform: All, macOS, Ubuntu, Windows, WSL
- Area: Core, Provider, Platform, CLI, Packaging, Security, Documentation
- Start date and Target date

Views: MVP board, Current milestone, Platform readiness, Provider readiness,
Release blockers, Bugs, Roadmap, and Recently completed.

Enable one auto-add workflow for all issues and pull requests in
`rahulsidpatil/agentctl`. Set new items to Inbox, closed issues and merged pull
requests to Done, and archive old Done items.

## Backlog

Create the seven headings in [the MVP backlog](backlog/mvp.md) as parent issues.
Create its bullets as sub-issues, add milestone and priority, and use explicit
dependencies when an interface or decision blocks implementation.

## Branch protection migration

The initial protected checks are `test (3.9)` and `test (3.12)`. Migrate safely:

1. Merge the CI workflow that adds `CI / required` while retaining old checks.
2. Verify `CI / required` succeeds on `master`.
3. Add `CI / required` as a protected check from GitHub Actions.
4. Remove the two old checks.
5. Open a small pull request and verify protection end to end.

Keep pull requests, strict up-to-date checks, and conversation resolution
required. Keep administrator bypass, force pushes, and branch deletion disabled.
Do not require approval while there is only one maintainer.

## Security and releases

Enable private vulnerability reporting, secret scanning, Dependabot, and CodeQL.
Before publishing, create a protected `pypi` environment and configure PyPI
trusted publishing for the exact repository and release workflow. Never place a
long-lived publishing token in a general repository secret.

Record material GitHub configuration changes in the timeline or a decision
record so the process remains auditable.
