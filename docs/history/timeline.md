# Timeline

## 2026-09-28 — Repository-local relay

- ContentArc needed a safe way to resume work after an agent exhausted its
  context or stopped unexpectedly.
- Structured handoff state, recovery snapshots, and supervised ownership were
  prototyped at repository level.
- Manual validation showed that exposing lifecycle implementation details made
  switching too difficult for everyday users.

## 2026-09-28 — Independent product direction

- The product boundary moved from ContentArc to an independent developer tool.
- The primary interface became `agentctl init` and `agentctl switch`.
- Codex, Claude, and Antigravity were selected as initial providers.
- Runtime state moved outside target repositories.

## 2026-09-28 — Public alpha

- Public repository `rahulsidpatil/agentctl` was created.
- `master` became the default protected branch.
- Initial implementation, schemas, tests, architecture, and safety model were
  committed as `45f15aa`.
- A real Codex smoke handoff produced a durable `handoff_ready` checkpoint.

## 2026-09-28 — AI-native SDLC pilot

- Cross-platform support became an explicit MVP requirement.
- TDD became the project delivery policy.
- The project was selected as the first evidence-generating pilot for a
  reusable GitHub-specific AI-native SDLC framework.
