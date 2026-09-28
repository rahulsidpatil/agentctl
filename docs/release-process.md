# Release process

## Before release

1. Freeze the milestone's P0 scope.
2. Confirm all milestone issues are closed or explicitly deferred with reasons.
3. Run unit, contract, integration, package, and Tier 1 platform checks.
4. Complete real-provider handoff experiments required by the milestone.
5. Validate a clean `pipx` installation from built distributions.
6. Review schema compatibility, security reports, and known limitations.
7. Update the version, changelog, documentation, and release review.

## Publish

1. Merge the release pull request through protected `master`.
2. Create a signed version tag from the verified commit.
3. Build distributions from that tag.
4. Validate package metadata and installation.
5. Publish to PyPI using GitHub trusted publishing.
6. Create the GitHub release with user-facing notes and known limitations.

Publishing remains blocked until the PyPI project, trusted publisher, and
protected `pypi` GitHub environment are configured. Do not store a PyPI API
token in repository secrets as a shortcut.

## After release

- Verify installation from PyPI on Tier 1 environments.
- Monitor and triage release defects.
- Complete `docs/releases/vX.Y.Z-review.md`.
- Convert misses and lessons into linked issues or playbook updates.
