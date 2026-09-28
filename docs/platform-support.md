# Platform support

## Tier 1 MVP environments

| Environment | Automated evidence | Release evidence |
|---|---|---|
| macOS | GitHub-hosted macOS matrix | Clean install and fake-provider switch |
| Ubuntu Linux | GitHub-hosted Ubuntu matrix | Clean install and fake-provider switch |
| Windows native | GitHub-hosted Windows matrix | Clean install and fake-provider switch |
| Ubuntu on WSL2 | Dedicated runner when available | Repeatable manual test until automated |

Passing on Ubuntu does not establish WSL compatibility. WSL validation must
record Windows and WSL versions, Python installation source, filesystem
location, provider executable location, and whether Windows/WSL interop is used.

## Required scenarios

- Install with `pipx` in a clean environment
- Initialize a Git repository idempotently
- Discover available and unavailable provider executables
- Run `status` and `doctor`
- Switch with a deterministic fake provider
- Recover from a crash and interruption
- Reject a concurrent workspace owner
- Handle repository paths containing spaces and Unicode
- Preserve platform-native line endings and executable semantics

Other Linux distributions, containers, and remote-development environments are
best effort until supported by explicit evidence and a roadmap decision.
