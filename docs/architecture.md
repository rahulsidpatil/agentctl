# Architecture

`agentctl` separates repository policy from machine execution.

The repository owns `.agentctl/config.json`, source code, Git history, and any
optional agent instructions. The installed tool owns its handoff state machine,
schemas, provider commands, exclusive lease, session logs, and snapshots.

Runtime data lives under `~/.local/state/agentctl/workspaces/<workspace-id>`.
The workspace identifier combines the repository directory name with a digest
of its canonical path. Files are created with user-only permissions.

## Switching transaction

1. Resolve the Git root and validate project configuration.
2. Verify the requested provider is installed before mutating session state.
3. Stop a live supervised provider with a bounded grace period.
4. Accept a matching safe handoff or enter recovery mode.
5. Acquire an exclusive worktree lease.
6. Atomically assign the normalized handoff to the incoming provider.
7. Launch the provider with repository instructions and embedded recovery context.
8. Consume a structured checkpoint from the provider's final-message channel;
   the supervisor writes private state so sandboxed agents do not need access.
9. Accept `handoff_ready` or `complete` as safe terminal states.
10. On any other exit, capture a snapshot and preserve `recovering` state.

The alpha supervises provider CLI processes. It cannot safely stop an agent
started independently in an IDE or unrelated terminal; it can still reconstruct
work from Git when that process is no longer writing.
