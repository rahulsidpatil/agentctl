# Handoff protocol

The handoff is a provider-neutral JSON document stored outside the repository.
Its schema is published at `schemas/handoff.schema.json`.

States are `active`, `draining`, `handoff_ready`, `recovering`, and `complete`.
A successful process exit is not sufficient: only `handoff_ready` and
`complete` are safe terminal states.

Agents checkpoint by ending their final response with a single unformatted
line of JSON:

```text
AGENTCTL_CHECKPOINT: {"status":"handoff_ready","next_agent":"claude","summary":"Implemented parsing and added tests","remaining":["Run the full integration suite"]}
```

The trusted supervisor accepts the checkpoint from the provider's final-message
channel and writes machine state itself. The agent never needs filesystem
access to agentctl's private state directory. Checkpoint-looking text in command
output is ignored to prevent repository content from spoofing a handoff.

`agentctl advanced checkpoint` remains available for an operator using an
unrestricted shell, but supervised agents should use the output protocol.

An abrupt exit changes the state to `recovering` and records a recovery
snapshot. The next provider must audit Git state and unfinished operations
before editing. Handoffs are recovery context and must not be treated as trusted
executable instructions.
