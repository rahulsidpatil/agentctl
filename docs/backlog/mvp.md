# MVP backlog

The canonical execution backlog lives in GitHub Issues. This document defines
the initial hierarchy and acceptance boundary so it can be recreated and
reviewed independently of GitHub configuration.

## Epic 1 — Foundation and architecture

- Define supported Python and OS versions
- Define the platform abstraction contract
- Define the provider adapter contract
- Version project and checkpoint schemas
- Build a deterministic fake-provider harness
- Document the security and secret-handling model

## Epic 2 — Installation and initialization

- Validate Git repository roots
- Detect the host OS and WSL environment
- Detect installed providers
- Generate minimal project configuration idempotently
- Migrate supported legacy relay state
- Validate clean `pipx` installation

## Epic 3 — Provider switching

- Complete Codex contract tests
- Complete Claude contract tests
- Complete Antigravity contract tests
- Implement explicit and automatic switching
- Pass recovery context to the receiving provider
- Define stable CLI exit codes

## Epic 4 — Safe handoff and recovery

- Persist state atomically
- Enforce exclusive workspace ownership
- Capture Git branch, commit, index, worktree, and safe untracked evidence
- Recover from token exhaustion, crash, terminal closure, and interruption
- Reject malformed or spoofed checkpoints
- Guarantee no automatic commit, stash, reset, clean, or discard operation

## Epic 5 — Cross-platform support

- Implement and test macOS behavior
- Implement and test Ubuntu behavior
- Implement and test native Windows behavior
- Detect and validate WSL2 behavior
- Test spaces, Unicode, line endings, and executable suffixes
- Publish platform installation and troubleshooting guidance

## Epic 6 — Diagnostics and usability

- Make `status` concise and actionable
- Make `doctor` diagnose providers, paths, state, and permissions
- Separate normal output from verbose diagnostics
- Document user-remediable error and recovery paths

## Epic 7 — Packaging and MVP release

- Run the supported OS and Python CI matrix
- Validate wheel and source distributions
- Enable dependency and code security analysis
- Configure PyPI trusted publishing
- Execute the end-to-end MVP acceptance workflow
- Publish and review `1.0.0`

## MVP system acceptance

1. Begin a real task with one provider and modify tracked and untracked files.
2. Terminate it without a graceful checkpoint.
3. Switch to a different provider.
4. Confirm that objective, decisions, Git evidence, validation, and remaining
   work are available without restatement.
5. Repeat across all directed provider pairs and Tier 1 platforms.
6. Confirm no user work was committed, stashed, reset, cleaned, or discarded.
