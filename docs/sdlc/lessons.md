# Validated lessons

This file contains practices supported by project evidence. Each entry links to
the decision, experiment, issue, pull request, or release that supports it.

## Initial observations awaiting broader validation

- Repository-local switching logic creates unnecessary adoption and maintenance
  cost; a machine-installed tool provides a cleaner product boundary.
- A successful provider exit is not proof of a recoverable handoff; a durable,
  validated checkpoint is required.
- Normal switching must be a single command; lifecycle mechanics belong behind
  the CLI or under advanced diagnostics.
- Runtime state outside the target repository reduces product-specific clutter
  and limits accidental commits of private session evidence.

These observations came from the ContentArc prototype and initial `agentctl`
smoke test. They become reusable framework rules only after the MVP experiments
and a second-project pilot confirm them.
