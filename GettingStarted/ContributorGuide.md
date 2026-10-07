---
layout: page
title: "Contributor Guide"
---

# [Astartup Cookbook](../)

## [Getting Started](./)

### Contributor Guide

This is the DRY contributor guide for all AStartup, AStarship, Kabuki Starship, Oregon Cooler, and third-party organization repositories. If you are contributing to any of these repos, this is the only guide you need to read.

#### What You Need

1. A GitHub account.
2. Git installed on your machine.
3. A text editor or IDE that can edit markdown files.
4. Access to the repository: you must be a member of the organization or have write access to the specific repo.

#### The First Time

1. Clone the Workspace repo for the organization. The Workspace repo shares the name of the organization: `AStarStartup/AStarStartup`.
2. Read the AGENTS.md in the Workspace repo. It defines the kanban board, the code style, and the coordination rules.
3. Read the MissionTickets.md in the AStartup Cookbook. It defines the ticket format and the commit convention.
4. Read the Contributing.md in the AStartup Cookbook. It defines the workflow.
5. Find an open issue on the kanban board that you can solve.
6. Create a branch: `Issue<N>`.
7. Start working.

#### Ongoing Contribution

1. Check the kanban board at the start of each session.
2. Pick an issue. Update the ticket. Create the branch.
3. Do the work. Commit with the correct format.
4. Push. Open a pull request. Wait for CI.
5. The merge gate (the founder or a designated reviewer) merges the pull request.
6. Update the session ticket. Move to the next issue.

#### Code Style

The code style is defined in the AGENTS.md of the repository. The general rules:

* **Immutable things** (type names, class names, function names, file names for client contracts) use `CamelCase`.
* **Mutable things** (variables, database columns, configuration keys, file names for host/storage) use `lower_snake_case`.
* **Macros and constants** use `UPPER_SNAKE_CASE`.
* **Markdown content files** use `CamelCase.md`.
* **Configuration files** use `lower_snake_case.yaml` or `lower_snake_case.json`.

When in doubt, look at the neighboring files and match their style. Consistency within a project beats adherence to a global rule.

#### Markdown Conventions

* Every content file starts with Jekyll front matter: `layout` and `title`.
* The H1 is the book title with a link to the root: `# [Astartup Cookbook](../)`.
* The H2 is the chapter with a link to the chapter README: `## [Psychology](./)`.
* The H3 or H4 is the page title.
* Sections use H4 or H5, not bold text.
* Code blocks use fenced markdown with the language tag: ````BASH`, ````Python`, ````YAML`.
* Links use relative paths: `[Mission Tickets](./MissionTickets.md)`.
* Do not use absolute URLs for internal links. Use relative paths so the repo can be moved.

#### What to Do When You Are Stuck

1. Read the AGENTS.md again. The answer is usually in there.
2. Read the issue ticket again. The Problem and Solution sections tell you what the expected outcome is.
3. Search the repo for similar patterns. `grep -r "pattern" --include="*.md"` finds how similar problems were solved.
4. Ask in the Questions ticket (#13). Write the question, the context, and what you have already tried.
5. If you are still stuck after an hour, create a parking ticket and move to the next issue. Do not burn the entire session on one problem.

#### Agent Contribution

When an AI agent is contributing, the rules are the same as for a human contributor, with three additions:

1. The agent reads the AGENTS.md, MissionTickets.md, and Contributing.md before starting any task.
2. The agent does not merge its own pull requests. The merge gate is always a human.
3. The agent writes a summary to the session ticket when the work is done, including what it changed, why, and what it did not change.

The agent is a contributor. It is not the founder, not the merge gate, not the architect. It does the work described in the ticket and reports back.
