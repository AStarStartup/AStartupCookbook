---
layout: page
title: "Contributing"
---

# [Astartup Cookbook](../)

## [Development](./)

### Contributing

This guide is the DRY reference for how to contribute to any AStartup, AStarship, Kabuki Starship, or third-party organization repository. Read it once. It does not change.

#### Before You Start

1. Read the AGENTS.md file in the repository root. It defines the project scope, the kanban board, the code style, and the coordination rules.
2. Read the MissionTickets.md file in the Development chapter. It defines the ticket format, the sub-commit structure, and the commit message convention.
3. Check the kanban board for open issues. You are only allowed to work on an issue that is on the board and assigned to you or unassigned.

#### The Workflow

1. **Pick an issue.** Find an open issue on the kanban board that you can solve. If no issue fits, create one. The issue must have a Problem section and a Solution section before you start.
2. **Create a branch.** Name it `Issue<N>` where N is the issue number. Never work on the default branch.
3. **Update the ticket.** Fill in the Files Affected section with the files you plan to touch. Add sub-commit sections (A, B, C) if the solution requires multiple commits.
4. **Do the work.** Write the code, edit the files, run the tests. Keep each sub-commit focused: one logical change per commit.
5. **Commit.** Use the format: `<Description> #<N>.<Letter> <Details>`. The description is what changed, the number and letter identify the issue and sub-commit, the details explain why.
6. **Push and open a pull request.** The pull request title matches the issue title. The body links to the issue.
7. **Wait for CI.** The pipeline must be green before the pull request can be merged.
8. **Merge.** The founder or the designated merge gate merges the pull request. You do not merge your own pull request.

#### Commit Message Format

```
<Verb> <Object> #<Issue>.<SubCommit> <One-sentence explanation>

Examples:
Rename IDD to ADD in Development Patterns #26.A Updated the chapter to name Agentic Driven Development.
Add Mission Tickets section #47.B Documented the ticket format and sub-commit structure.
Fix broken license link #101.A The repo URL pointed to the old CookingWithCale org.
```

The verb is the first word. The object is what the verb acts on. The issue number and sub-commit letter are the link back to the ticket. The explanation is one sentence, no more.

#### File Naming

* Content files: `CamelCase.md` (e.g., `MissionTickets.md`, `DevelopmentLogs.md`).
* Configuration files: `lower_snake_case` (e.g., `ci_config.yaml`, `lint_rules.json`).
* Client-facing API files: `CamelCase` (e.g., `OrderService.md`, `PaymentGateway.md`).
* Test files: `test_` prefix, `lower_snake_case` (e.g., `test_order_service.py`).

#### What Not to Do

* Do not work on an issue that is not on the kanban board.
* Do not push to the default branch.
* Do not skip the CI pipeline.
* Do not merge your own pull request.
* Do not add files that are not listed in the Files Affected section.
* Do not rename files without updating every reference to the old name.
* Do not commit secrets, credentials, or API keys.
* Do not commit generated files (build output, minified bundles, lock files) unless the project convention requires it.

#### Agent Contribution Rules

When an AI agent is contributing:

1. The agent reads the AGENTS.md and the MissionTickets.md before starting.
2. The agent works on one issue at a time.
3. The agent updates the ticket as it works: Files Affected, sub-commit sections, session notes.
4. The agent runs the linter and tests locally before pushing.
5. The agent pushes the branch and opens the pull request.
6. The agent does not merge the pull request. The merge gate is a human.
7. The agent writes a summary of what it did to the session ticket when the pull request is merged.

The agent is a contributor, not the merge gate. The human reviews, the human merges, the human is accountable.
