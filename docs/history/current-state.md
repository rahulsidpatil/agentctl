# Current-state baseline

Baseline date: 2026-09-28

## Product

- Version: `0.3.0a2`
- Repository: `rahulsidpatil/agentctl`
- Default branch: `master`
- Distribution: source installation; PyPI publication is pending
- Commands: `init`, `switch`, `status`, `doctor`, and advanced lifecycle tools
- Built-in providers: Codex, Claude, and Antigravity
- Repository footprint: `.agentctl/config.json`
- Runtime state: external user-state directory

## Verification

- Automated suite: 17 tests in the initial repository
- CI: Ubuntu with Python 3.9 and 3.12
- Package formats: wheel and source distribution
- Real evidence: one supervised Codex smoke handoff

## Known gaps

- No native Windows, macOS, or WSL CI evidence
- Provider adapters have not all been validated with real provider processes
- No automated token-exhaustion acceptance test
- No published PyPI package
- No public product backlog or milestone retrospectives
- No stable aggregate CI check for expanding the platform matrix
- Cross-platform process and locking behavior require explicit abstraction

This baseline is intentionally immutable. Subsequent state belongs in issues,
milestone retrospectives, and release reviews.
