---
layout: page
title: "Mission Tickets"
---

# [Astartup Cookbook](../../)

## [Development](../../)

### [Agentic Driven Development](./)

#### Mission Tickets

A Mission Ticket is the standard tree markdown template for ADD (Agentic Driven Development, formerly IDD and MDD) that defines the contract between the ticket, the branch, and the commit. It is called a Mission Ticket because the mission drives the development: every mission solves a problem, and not every issue is a mission. A human or an agent must explicitly take an issue on as a mission before any work begins. A Mission Ticket is composed of a one-sentence mission statement title, a Problem section, a Solution section, a Files Affected section, and one H2 heading per sub-commit.

#### One-sentence Mission Statement

Every mission ticket should have for its title a one-sentence mission statement. A mission is easiest to describe in terms of a military combat operation. You don't just want to go out fighting the enemy in the abstract, you need to target specific parts of the enemy and attack the enemy until it is defeated. If possible every issue should only address one discrete mission; this however is not possible without addressing a coupled issue, or sometimes you're just too lazy to make an extra issue ticket, so when there is more than one mission they should be separated by a semicolon. In IMUL every mission starts with a verb, such as Rename, Add, Delete, etc.

***Example***

`Title: Rename IDD to Agentic Driven Development; Add Mission Tickets chapter.`

#### Problem

Every mission ticket must address a problem. Sometimes the problem is the same as the one-sentence mission statement. We only want to go on a mission if there is a problem, and if there isn't a problem then the mission itself is a problem. A problem statement should be as short as possible to express why we're going on the mission. The Problem section may be empty when the issue title fully states the problem.

#### Solution

For every problem, there should be at least one solution. A good solution statement should address why this is the appropriate solution for the problem statement. You should describe what the properties of a solution are that will achieve the effect desired. When you're mapping out and prioritizing issues you might not know which solution you'll use, so you should use one H2 heading for each solution. The Solution section is required; a mission ticket without a Solution is not a mission ticket.

#### Files Affected

The Files Affected section is an enumerated list of the files the mission touches. It is the contract between the ticket and the commit: you stage only what the ticket lists, and nothing else. Wildcards are part of the contract:

* `*.*` (or `*`) means any file, so stage everything with `git add --all`.
* `?` means unknown or to be determined. Resolve it before committing: replace the `?` in the ticket with the actual list of files affected, then stage exactly those files.

If no files are altered, leave the list empty.

#### Sub-commits: A, B, C

Multiple commits on one ticket are allowed. One ordered H2 section per sub-commit, in issue order, states what that sub-commit solves and how. A single-commit ticket has no letter sections.

#### Worked Example

***Example***

Issue #26: `Rename the methodology from Issue-driven Development to Agentic Driven Development.`

1. Branch: `Issue26` (never the default branch).
2. Update the ticket's `## A`, `## B`, `## C` sections as the solution evolves.
3. Commit messages, in order:

```BASH
git commit -m "Rename IDD to ADD in Development Patterns #26.A Updated the chapter to name Agentic Driven Development with a formerly IDD/MDD note."
git commit -m "Rename IDD to ADD in the Development chapter #26.B Updated the chapter heading and links with a formerly IDD/MDD note."
git commit -m "Rename IDD to ADD in the root README #26.C Updated the tagline and content table with a formerly IDD/MDD note."
```

The letter must match the section in the ticket: a commit letter with no section (or a section with no commit) is a broken ticket. If the suffix sequence becomes unwieldy, open a new issue instead of extending the same mission.

#### Commit Discipline

1. Read the mission ticket before committing, including the Problem, Solution, and the matching sub-commit section for the commit you are about to make.
2. Stage only what Files Affected lists. Explicit paths stage those paths; do not stage unrelated changes, generated or build noise, binaries, or secrets.
3. Update the ticket as the solution evolves. Keep Files Affected and the active sub-commit section current before each commit.
4. One coherent solution step per commit, one reason to exist. Don't make one giant mixed commit to reduce count, and don't make meaningless micro-commits to inflate count. Let the mission define the unit.
5. Verify with real checks appropriate to the step. Human verification is the merge gate; a green run is evidence, not permission to integrate.
