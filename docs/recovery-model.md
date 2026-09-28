# Recovery model

For an unsafe provider exit, `agentctl` records:

- Git branch, HEAD, and porcelain status;
- staged and unstaged binary-capable patches;
- the latest normalized handoff;
- the provider command-log path; and
- small safe untracked files.

Environment files, credentials, private keys, databases, runtime directories,
large files, and files matching common secret patterns are not copied. Their
names are recorded as excluded evidence.

Snapshots are evidence, not an automatic rollback mechanism. `agentctl` never
discards the user's working tree or retries external operations automatically.
