# Provider adapters

Built-in providers have a command, prompt transport (`stdin` or `argument`),
and executable discovery policy. Machine configuration can override a built-in
provider or define a new one without changing the repository.

Custom providers must accept a non-interactive initial prompt and preserve the
working directory. A provider should emit the documented
`AGENTCTL_CHECKPOINT` line in its final response before it exits normally. The
supervisor, rather than the sandboxed provider, persists the checkpoint.

Provider authentication, model selection, billing, and quota enforcement stay
under the provider CLI's control. Provider-specific quota warnings can improve
graceful draining, but correctness must tolerate an immediate process exit.
