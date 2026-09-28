# Delivery and learning metrics

Metrics answer product or process questions; they are not contributor targets.

| Metric | Question | Source |
|---|---|---|
| Issue lead time | How long does valuable work wait and take? | GitHub issue dates |
| PR cycle time | How quickly can changes be validated and reviewed? | GitHub PR dates |
| CI pass rate | Is the delivery system reliable? | Actions runs |
| Escaped defects | What reached users without adequate evidence? | Bug issues |
| Handoff success rate | Can another provider continue without restatement? | Experiments |
| Recovery time | How costly is exhaustion or a crash? | Experiments |
| Regression-test rate | Do fixes prevent recurrence? | Bug PR review |
| Platform readiness | Which Tier 1 environments have current evidence? | CI/release review |
| Release frequency | Can validated value reach users predictably? | Releases |

Do not optimize lines of generated code, prompt count, or raw token use unless
a specific experiment demonstrates why that measurement matters.
