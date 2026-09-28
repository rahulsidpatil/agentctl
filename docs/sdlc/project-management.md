# GitHub project management

## Workflow

The `agentctl Product Development` Project uses:

```text
Inbox -> Backlog -> Ready -> In Progress -> In Review -> Done
                           \-> Blocked
```

Fields are Status, Priority, Size, Target, Platform, Area, Start date, and
Target date. Views cover the MVP board, current milestone, platform readiness,
provider readiness, release blockers, bugs, roadmap, and recently completed
work.

The personal repository uses namespaced labels for type, area, platform,
provider, and priority. Seven parent issues represent the MVP epics, with
actionable work represented as sub-issues and explicit blocking relationships.

## Cadence

- Triage Inbox continuously.
- Review priorities, blockers, and oversized work weekly.
- Pull new work only from Ready.
- Review milestone acceptance when its last issue closes.
- Publish a short Project status update monthly.
- Run a release review for every published version.

Do not duplicate Project Status as labels. Do not use artificial sprints until
coordination among multiple active contributors makes them useful.
