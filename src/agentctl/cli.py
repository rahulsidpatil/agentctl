"""Safely hand development work between coding agents."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Optional

from . import __version__
from .core import (
    AgentctlError,
    Lease,
    Project,
    config_path,
    git,
    initial_handoff,
    load_json,
    providers,
    refresh_handoff_git,
    repository_root,
    run_provider,
    snapshot,
    state_home,
    stop_active_supervisor,
    workspace_runtime_root,
)


def display_name(provider: str) -> str:
    names = {"codex": "Codex", "claude": "Claude", "antigravity": "Antigravity"}
    return names.get(provider, provider)


def write_repository_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def detect_instructions(root: Path) -> list[str]:
    for candidate in ("AGENTS.md", "CLAUDE.md", ".github/copilot-instructions.md"):
        if (root / candidate).is_file():
            return [candidate]
    return []


def detect_validation(root: Path) -> dict[str, str]:
    if (root / "scripts" / "check.sh").is_file():
        return {"full": "./scripts/check.sh"}
    makefile = root / "Makefile"
    if makefile.is_file():
        text = makefile.read_text(encoding="utf-8", errors="replace")
        if "check:" in text:
            return {"full": "make check"}
        if "test:" in text:
            return {"full": "make test"}
    package = root / "package.json"
    if package.is_file():
        try:
            scripts = json.loads(package.read_text(encoding="utf-8")).get("scripts", {})
            if isinstance(scripts, dict) and "test" in scripts:
                return {"full": "npm test"}
        except (json.JSONDecodeError, AttributeError):
            pass
    if (root / "go.mod").is_file():
        return {"full": "go test ./..."}
    if (root / "Cargo.toml").is_file():
        return {"full": "cargo test"}
    return {}


def migrate_legacy_handoff(project: Project) -> bool:
    legacy_path = project.workspace / ".handoff" / "current.json"
    if project.handoff_path.exists() or not legacy_path.exists():
        return False
    legacy = load_json(legacy_path)
    completed = legacy.get("completed", [])
    summary = (
        "; ".join(str(item) for item in completed) or "Imported from the legacy repository handoff."
    )
    state = {
        "schema_version": 1,
        "work_item": str(legacy.get("work_item", "IMPORTED")),
        "objective": str(legacy.get("objective", "Continue the current repository work")),
        "status": "recovering",
        "branch": str(
            legacy.get("branch") or git(project.workspace, "branch", "--show-current") or "detached"
        ),
        "base_commit": str(
            legacy.get("base_commit") or git(project.workspace, "rev-parse", "HEAD")
        ),
        "checkpoint_commit": str(
            legacy.get("checkpoint_commit") or git(project.workspace, "rev-parse", "HEAD")
        ),
        "current_agent": str(legacy.get("current_agent", project.providers[0])),
        "next_agent": None,
        "summary": summary,
        "remaining": [str(item) for item in legacy.get("remaining", [])],
        "decisions": [str(item) for item in legacy.get("decisions", [])],
        "validation": legacy.get("validation", [])
        if isinstance(legacy.get("validation", []), list)
        else [],
        "updated_at": str(legacy.get("updated_at", "1970-01-01T00:00:00Z")),
    }
    project.save_handoff(state)
    return True


def cmd_init(args: argparse.Namespace) -> int:
    root = repository_root(Path(args.workspace))
    destination = root / ".agentctl" / "config.json"
    legacy_path = root / ".agent-relay" / "project.json"
    if destination.exists() and not args.force:
        project = Project.open(root)
        project.validate()
        migrated = migrate_legacy_handoff(project)
        print(f"agentctl is already initialized for {project.name}")
        if migrated:
            print("Legacy handoff imported in recovery mode")
        print("Start with: agentctl switch codex")
        return 0

    legacy = load_json(legacy_path) if legacy_path.exists() else {}
    instructions = detect_instructions(root)
    legacy_instruction = legacy.get("instructions")
    if (
        not instructions
        and isinstance(legacy_instruction, str)
        and (root / legacy_instruction).is_file()
    ):
        instructions = [legacy_instruction]
    validation = legacy.get("validation")
    if not isinstance(validation, dict):
        validation = detect_validation(root)
    enabled = legacy.get("providers", ["codex", "claude", "antigravity"])
    if not isinstance(enabled, list) or not enabled:
        enabled = ["codex", "claude", "antigravity"]
    config = {
        "schema_version": 1,
        "project": str(legacy.get("project") or root.name),
        "instructions": instructions,
        "validation": validation,
        "providers": enabled,
        "handoff": {"checkpoint_minutes": 30},
    }
    write_repository_json(destination, config)
    project = Project.open(root)
    project.validate()
    migrated = migrate_legacy_handoff(project)
    available = providers()
    readiness = [
        f"{display_name(name)} {'ready' if name in available and available[name].available() else 'unavailable'}"
        for name in project.providers
    ]
    print(f"Initialized agentctl for {project.name}")
    print(f"Configuration: {destination.relative_to(root)}")
    print(f"Instructions: {', '.join(instructions) if instructions else 'none'}")
    print(f"Validation: {', '.join(validation.values()) if validation else 'none'}")
    print(f"Agents: {', '.join(readiness)}")
    if migrated:
        print("Legacy handoff imported in recovery mode")
    print("\nStart with: agentctl switch codex")
    return 0


def open_project(args: argparse.Namespace) -> Project:
    return Project.open(Path(args.workspace))


def cmd_doctor(args: argparse.Namespace) -> int:
    project = open_project(args)
    project.validate()
    configured = providers()
    print(f"workspace: {project.workspace}")
    print(f"state home: {state_home()}")
    print(f"machine config: {config_path()} ({'present' if config_path().exists() else 'absent'})")
    ready = 0
    for name in project.providers:
        provider = configured.get(name)
        if not provider or not provider.available():
            executable = provider.executable if provider else name
            print(f"provider {name}: unavailable ({executable})")
        else:
            print(f"provider {name}: ready ({provider.resolved_executable()})")
            ready += 1
    if not ready:
        print("no configured provider is ready", file=sys.stderr)
        return 1
    return 0


def cmd_status(args: argparse.Namespace) -> int:
    project = open_project(args)
    if not project.handoff_path.exists():
        print(f"{project.name}: no active work")
        return 0
    state = project.handoff()
    lease_path = workspace_runtime_root(project.workspace) / "lease.json"
    lease = load_json(lease_path) if lease_path.exists() else None
    if args.verbose:
        print(json.dumps({"handoff": state, "lease": lease}, indent=2))
        return 0
    running = f" · running as PID {lease.get('supervisor_pid')}" if lease else ""
    print(f"{project.name}: {state['work_item']}")
    print(f"Agent: {display_name(str(state['current_agent']))}{running}")
    print(f"State: {str(state['status']).replace('_', ' ')}")
    return 0


def available_rotation(project: Project) -> list[str]:
    configured = providers()
    return [
        name for name in project.providers if name in configured and configured[name].available()
    ]


def select_switch_target(project: Project, requested: Optional[str], current: Optional[str]) -> str:
    configured = providers()
    if requested:
        if requested not in project.providers:
            raise AgentctlError(f"{display_name(requested)} is not enabled for this project")
        provider = configured.get(requested)
        if not provider or not provider.available():
            executable = provider.executable if provider else requested
            raise AgentctlError(
                f"cannot switch to {display_name(requested)}: {executable} is not installed; "
                "install and sign in, then retry the same command"
            )
        return requested
    rotation = available_rotation(project)
    if not rotation:
        raise AgentctlError("no installed coding agent is available")
    if current not in rotation:
        return rotation[0]
    if len(rotation) == 1:
        return rotation[0]
    return rotation[(rotation.index(current) + 1) % len(rotation)]


def cmd_switch(args: argparse.Namespace) -> int:
    project = open_project(args)
    project.validate()
    existing = project.handoff() if project.handoff_path.exists() else None
    current = str(existing["current_agent"]) if existing else None
    target = select_switch_target(project, args.provider, current)

    lease_path = workspace_runtime_root(project.workspace) / "lease.json"
    live_provider: Optional[str] = None
    if lease_path.exists():
        live_provider = str(load_json(lease_path).get("provider", current or "unknown"))
        if live_provider == target:
            raise AgentctlError(f"{display_name(target)} is already running")
        print(f"Stopping {display_name(live_provider)} safely…")
        stop_active_supervisor(project, args.grace_seconds)

    if existing is None or existing["status"] == "complete":
        project.save_handoff(initial_handoff(project, target))
        recovering = False
    else:
        existing = project.handoff()
        recovering = not (
            existing["status"] == "handoff_ready" and existing.get("next_agent") in {target, "auto"}
        )
    candidates = [name for name in available_rotation(project) if name != target]
    next_provider = candidates[0] if candidates else None
    source = live_provider or current
    if source and source != target:
        print(f"Switching {display_name(source)} → {display_name(target)}…")
    else:
        print(f"Starting {display_name(target)}…")
    result = run_provider(
        project,
        target,
        next_provider=next_provider,
        recovering=recovering,
        max_seconds=args.max_seconds,
        echo_output=args.verbose,
    )
    state = project.handoff()
    if not result.safe_state:
        print(f"{display_name(target)} stopped before creating a safe checkpoint.", file=sys.stderr)
        print("Recovery state was preserved for the next switch.", file=sys.stderr)
        if args.verbose:
            show_result(result)
        return result.exit_code or 3
    verb = "Switched" if source and source != target else "Finished"
    print(f"{verb} {project.name}: {display_name(target)}")
    print(f"Work item: {state['work_item']}")
    print(f"State: {state['status'].replace('_', ' ')}")
    if args.verbose:
        show_result(result)
    return 0


def cmd_checkpoint(args: argparse.Namespace) -> int:
    project = open_project(args)
    if not project.handoff_path.exists():
        raise AgentctlError("no active handoff exists")
    state = refresh_handoff_git(project, project.handoff())
    status = args.status.replace("-", "_")
    state["status"] = status
    state["summary"] = args.summary
    state["remaining"] = args.remaining or ([] if status == "complete" else state["remaining"])
    if status == "complete":
        state["next_agent"] = None
    else:
        if args.next != "auto" and args.next not in project.providers:
            raise AgentctlError(f"{display_name(args.next)} is not enabled for this project")
        state["next_agent"] = args.next
    project.save_handoff(state)
    print(f"checkpoint recorded: {status.replace('_', ' ')}")
    return 0


def cmd_snapshot(args: argparse.Namespace) -> int:
    print(snapshot(open_project(args), args.reason))
    return 0


def cmd_release(args: argparse.Namespace) -> int:
    project = open_project(args)
    Lease(project.workspace, "manual").force_release()
    print("stale lease released")
    return 0


def show_result(result: object) -> None:
    value = result
    print(f"command log: {value.log_path}")
    print(f"handoff state: {value.handoff_status}")
    if value.snapshot_path:
        print(f"recovery snapshot: {value.snapshot_path}")


def cmd_run(args: argparse.Namespace) -> int:
    project = open_project(args)
    if not project.handoff_path.exists():
        project.save_handoff(initial_handoff(project, args.provider))
    result = run_provider(
        project,
        args.provider,
        next_provider=args.next_provider,
        recovering=args.recover,
        max_seconds=args.max_seconds,
    )
    show_result(result)
    return 0 if result.safe_state else result.exit_code or 3


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", action="version", version=__version__)
    subcommands = parser.add_subparsers(dest="command", required=True)

    def workspace(command: argparse.ArgumentParser) -> None:
        command.add_argument("--workspace", default=".")

    init = subcommands.add_parser("init", help="initialize agentctl in this Git repository")
    workspace(init)
    init.add_argument("--force", action="store_true", help="replace existing project configuration")
    init.set_defaults(handler=cmd_init)
    doctor = subcommands.add_parser("doctor", help="validate project and provider readiness")
    workspace(doctor)
    doctor.set_defaults(handler=cmd_doctor)
    status = subcommands.add_parser("status", help="show the current handoff")
    workspace(status)
    status.add_argument("--verbose", action="store_true")
    status.set_defaults(handler=cmd_status)
    switch = subcommands.add_parser("switch", help="start or switch to a coding agent")
    workspace(switch)
    switch.add_argument("provider", nargs="?")
    switch.add_argument("--max-seconds", type=int)
    switch.add_argument("--grace-seconds", type=int, default=20, help=argparse.SUPPRESS)
    switch.add_argument("--verbose", action="store_true")
    switch.set_defaults(handler=cmd_switch)

    advanced = subcommands.add_parser("advanced", help="agent and troubleshooting commands")
    advanced_commands = advanced.add_subparsers(dest="advanced_command", required=True)
    checkpoint = advanced_commands.add_parser("checkpoint", help="record a safe agent checkpoint")
    workspace(checkpoint)
    checkpoint.add_argument("--status", choices=["handoff-ready", "complete"], required=True)
    checkpoint.add_argument("--next", default="auto")
    checkpoint.add_argument("--summary", required=True)
    checkpoint.add_argument("--remaining", action="append", default=[])
    checkpoint.set_defaults(handler=cmd_checkpoint)
    snapshot_command = advanced_commands.add_parser("snapshot", help="capture recovery evidence")
    workspace(snapshot_command)
    snapshot_command.add_argument("--reason", required=True)
    snapshot_command.set_defaults(handler=cmd_snapshot)
    release = advanced_commands.add_parser(
        "release-stale-lease", help="release a dead process lease"
    )
    workspace(release)
    release.set_defaults(handler=cmd_release)
    run = advanced_commands.add_parser("run", help="run one provider under supervision")
    workspace(run)
    run.add_argument("--provider", required=True)
    run.add_argument("--next-provider")
    run.add_argument("--recover", action="store_true")
    run.add_argument("--max-seconds", type=int)
    run.set_defaults(handler=cmd_run)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    try:
        return int(args.handler(args))
    except AgentctlError as exc:
        print(f"agentctl: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
