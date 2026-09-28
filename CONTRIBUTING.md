# Contributing to agentctl

`agentctl` is developed issue-first and test-first. Contributions are welcome,
including bug reports, platform findings, provider integrations, experiments,
and improvements to the AI-native delivery process.

## Before starting

1. Open or select a GitHub issue.
2. Make sure its outcome and acceptance criteria are testable.
3. Identify the affected providers and platforms.
4. Record unresolved product or architecture questions with `needs-design`.
5. For compatibility-breaking work, create an ADR before implementation.

An issue is **Ready** when its scope, non-goals, acceptance criteria,
dependencies, test scenarios, and documentation impact are clear.

## Development workflow

Create a focused branch named `issue-<number>-<short-description>`. Then follow
red-green-refactor:

1. Add a test that fails for the intended reason.
2. Implement the smallest change that makes the test pass.
3. Refactor while keeping the suite green.
4. Add provider-contract, platform-contract, integration, and regression
   coverage where applicable.
5. Update user and architecture documentation in the same pull request.

Provider tests must use deterministic fake executables. Normal pull-request CI
must not require provider credentials or consume paid API quota.

## Local validation

From a virtual environment:

```sh
python -m pip install -e . ruff build twine
ruff check src tests
ruff format --check src tests
python -W error::ResourceWarning -m unittest discover -s tests -v
python -m build
python -m twine check dist/*
```

Platform-specific behavior must have a platform test. If a supported platform
cannot be exercised automatically, document the exact repeatable manual test
and its latest result.

## Pull requests

Pull requests must:

- link and close an issue;
- be small enough to review as one coherent change;
- include TDD evidence and validation results;
- disclose known limitations and deferred work;
- preserve backward-compatible schemas or document an approved migration;
- avoid exposing credentials, prompts, or sensitive session output; and
- update relevant decisions, experiments, or lessons.

A change is **Done** when its acceptance criteria pass, required CI is green,
documentation matches behavior, security and compatibility have been
considered, and any follow-up work is captured as an issue.

## AI-assisted contributions

AI coding agents are welcome, but the contributor remains responsible for the
change. Use [AGENTS.md](AGENTS.md) as the provider-neutral instruction source.
Do not commit raw prompts, private transcripts, credentials, or unrestricted
agent logs. Preserve evidence that another maintainer can reproduce: tests,
commands, decisions, and sanitized checkpoints.

By contributing, you agree that your contribution is licensed under
Apache-2.0.
