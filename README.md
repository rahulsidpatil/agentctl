# agentctl

`agentctl` safely hands development work between AI coding agents. It is a
provider-neutral CLI: initialize any Git repository once, then switch between
Codex, Claude, Antigravity, or a custom command without manually managing
handoff files, process locks, or crash recovery.

> Alpha software: configuration and handoff formats may change before 1.0.

## Quick start

Python 3.9 or newer is required.

```sh
git clone https://github.com/rahulsidpatil/agentctl.git
pipx install ./agentctl
cd /path/to/a/git/repository
agentctl init
agentctl switch codex
```

After the first package release, installation will be `pipx install agentctl`.

Switch explicitly or select the next installed provider:

```sh
agentctl switch claude
agentctl switch antigravity
agentctl switch
```

Everyday users need only `init`, `switch`, `status`, and `doctor`. Lifecycle
and recovery commands live under `agentctl advanced` for supervised agents and
troubleshooting.

## Repository footprint

`agentctl init` creates one committed project file:

```text
.agentctl/config.json
```

It discovers existing instruction files and common validation commands.
Handoffs, leases, logs, and recovery snapshots stay outside the repository in
`~/.local/state/agentctl`. Provider credentials remain owned by provider CLIs.

Example project configuration:

```json
{
  "schema_version": 1,
  "project": "my-project",
  "instructions": ["AGENTS.md"],
  "validation": {"full": "make test"},
  "providers": ["codex", "claude", "antigravity"],
  "handoff": {"checkpoint_minutes": 30}
}
```

Repositories do not need custom lifecycle scripts, handoff schemas, or
provider-specific instruction adapters.

## Provider commands

The alpha includes these defaults:

- Codex: `codex exec --json -`
- Claude: `claude -p <prompt>`
- Antigravity: `agy -p <prompt>`

Override them in `~/.config/agentctl/config.json`:

```json
{
  "providers": {
    "my-agent": {
      "command": ["my-agent", "--prompt-stdin"],
      "prompt_mode": "stdin"
    }
  }
}
```

Then add `my-agent` to the repository's provider list. Authentication is never
stored by `agentctl`; install and sign in with each provider's normal CLI.

## Safety model

- One supervised writer may own a worktree at a time.
- A target provider is checked before the current provider is stopped.
- Graceful exits require a durable handoff checkpoint.
- Sandboxed agents emit checkpoints through their final output; only the
  supervisor writes private machine state.
- Unsafe exits preserve Git patches, status, safe untracked files, and logs.
- Common credential, key, database, and environment files are excluded.
- `agentctl` never commits, pushes, deploys, or approves agent actions.

No supervisor can recover reasoning that existed only in a terminated model
context. Durable checkpoints and Git evidence minimize that loss. See
[the architecture](docs/architecture.md) and
[handoff protocol](docs/handoff-protocol.md).

## Development

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -e . ruff build
.venv/bin/ruff check src tests
.venv/bin/python -m unittest discover -s tests -v
.venv/bin/python -m build
```

See [CONTRIBUTING.md](CONTRIBUTING.md), [SECURITY.md](SECURITY.md), and the
[provider adapter guide](docs/provider-adapters.md) before contributing.

## License

Apache-2.0.
