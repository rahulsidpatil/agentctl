# Roadmap

The MVP proves that a developer can stop work in one coding agent and safely
continue in another without losing repository work or restating the task.

## M0 — Governance

- GitHub-native backlog, milestones, and Project views
- Issue forms and pull-request template
- TDD policy and definition of done
- Decision, experiment, retrospective, and release-review records
- Initial project history and process baseline

## M1 — Reliable core

- Versioned repository configuration and checkpoint schemas
- Atomic state persistence and exclusive workspace ownership
- Git-state evidence and safe recovery snapshots
- Deterministic fake-provider and failure-mode tests
- Stable CLI error and exit behavior

Exit: crash, interruption, invalid-checkpoint, and concurrent-owner scenarios
are deterministic and preserve user work.

## M2 — Provider handoffs

- Codex, Claude, and Antigravity adapter contracts
- Explicit and automatic provider selection
- All six directed provider-pair handoffs
- Token-exhaustion and abrupt-exit recovery

Exit: every provider pair has repeatable evidence that the receiving agent can
continue without the user restating the objective.

## M3 — Cross-platform

- macOS, Ubuntu, and native Windows CI
- WSL2 detection and repeatable validation
- Portable paths, executable discovery, locking, and process supervision
- Spaces, Unicode, and line-ending coverage

Exit: installation, initialization, status, doctor, and fake-provider switching
pass on every Tier 1 platform.

## M4 — MVP release

- Clean-machine `pipx` installation
- Package metadata and distribution validation
- Security and compatibility review
- End-to-end release acceptance test
- PyPI trusted publishing and GitHub release
- MVP retrospective and reusable-framework review

## Deferred until after MVP

- GUI or web dashboard
- Cloud synchronization and multi-machine handoffs
- Team orchestration and agent performance scoring
- Automatic commits, stashes, pull requests, or deployments
- Broad provider marketplace and IDE extensions

See [the MVP backlog](docs/backlog/mvp.md) for the planned issue hierarchy.
