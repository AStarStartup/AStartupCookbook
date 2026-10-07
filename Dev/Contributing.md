---
layout: page
title: "Contributing"
---

# [Astartup Cookbook](../)

## [Development](./)

### Contributing

This is the cookbook's contribution procedure, not a policy for every third-party repository. Read the target project's instructions each time; they may have changed.

1. Confirm the request, the actual repository, the mission issue, and the explicitly assigned board. In this workspace use `astartup`. If no issue exists, request or create one only within your permissions before committing.
2. Read the full issue and comments. The mission record contains `## Problem`, required `## Solution`, and required `### Files Affected`. Problem may be empty if the title fully states it. Record the intended outcome and verification; do not treat an untested solution as established fact.
3. Inspect `git status`, the current branch, and the intended base. Preserve unrelated work. Use `Issue<N>` for the actual issue number; report a mismatch instead of silently switching or discarding changes.
4. Make a scoped change. Keep the file list and the matching sub-commit section current. Read neighboring conventions and trace references before renaming anything.
5. Run the relevant local checks. For this book use [Documentation Checks](../Doc/DocumentationChecks.md). Evidence includes failures and checks that could not run.
6. Review the diff and stage explicit paths. Exclude credentials, unrelated changes, build output, and binaries. Commit only when requested.
7. An authorized contributor may push the mission branch and prepare a pull request when requested. Specialists do not borrow another agent's credentials. Human review decides integration; passing checks alone do not authorize merge or issue closure.
8. Hand off changes and verification while they are reviewable. Do not wait for a merge to report a blocker.

#### Commit grammar

The current AStartup workspace contract is prefix-first:

```text
#<N> <title>
#<N>.A <sub-commit title>
#<N>.B <next sub-commit title>
```

`N` is the real ticket number. Each letter has a corresponding ordered `## A`, `## B`, etc. section in the issue. Other repositories can define different conventions; check them rather than copying this one blindly. The canonical ticket details are in [Mission Tickets](./IDD/MissionTickets.md).

#### Naming and Markdown

Content filenames use `CamelCase.md`. Host scripts and configuration filenames use `lower_snake_case`. Follow `AGENTS.md` for code identifiers and required framework hooks.

Content pages begin with `layout: page` and a descriptive `title`. Retain the book/chapter breadcrumb headings and use relative, case-correct paths. Root utility files and GitHub issue-template metadata are separate formats. Mark unfinished content `status: draft`; do not fill missing research with plausible text.

Use a language identifier such as `bash`, `python`, or `yaml` on executable code fences. Label placeholders and hypothetical examples. Update internal references with every rename.

#### Safety

Do not force-push, rebase shared history, modify permissions, deploy, or publish merely to finish a contribution. Ask when authority or scope is unclear. Never disable a check or replace a failing assertion just to obtain a green result.
