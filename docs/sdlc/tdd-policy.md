# TDD policy

Behavior changes follow red-green-refactor:

1. Add a failing test that expresses the user-visible or contract behavior.
2. Confirm it fails for the intended reason.
3. Implement the smallest passing change.
4. Refactor with all relevant tests green.
5. Add regression and failure-path coverage.

## Test layers

- **Unit:** parsing, schemas, selection, paths, and state transitions
- **Contract:** every provider and platform implementation against shared rules
- **Integration:** fake processes for completion, exhaustion, crash, hang,
  interruption, malformed output, and checkpoint spoofing
- **End to end:** controlled real-provider and clean-install smoke tests

Real provider credentials and paid quota are never required for normal pull
request CI. An exception to test-first development must be explained in the PR,
such as documentation-only work or a non-reproducible exploratory spike.
