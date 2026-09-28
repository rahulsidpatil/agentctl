# Changelog

## 0.3.0a2

- Broker checkpoints through trusted provider output so sandboxed agents never
  need write access to agentctl's private machine state.
- Ignore checkpoint-like text from command execution output.

## 0.3.0a1

- Introduce repository-agnostic `agentctl init`.
- Store handoffs and runtime evidence outside target repositories.
- Remove repository lifecycle-script and provider-file requirements.
- Add legacy `.agent-relay` handoff migration.
- Preserve one-command explicit and automatic provider switching.
