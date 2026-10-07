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

#### Adding Mission and Vision to Issue Tickets

Every project has a mission and a vision. The mission is what the project does. The vision is where the project is going. Every issue ticket should trace back to the mission: if the issue does not serve the mission, it is not an issue for this project.

To add mission and vision context to an issue ticket, reference the mission in the Problem section:

```markdown
## Problem

The problem is that the pricing page does not show the free tier, which
contradicts the mission of making startup tooling accessible to solo
founders. [Mission: Make startup tooling free and open for solo founders.]
```

The mission reference in brackets is a link back to the mission statement in the project's AGENTS.md or README. This creates a traceable chain: the issue serves the mission, the mission serves the vision, the vision serves the founder.

If an issue cannot be traced to the mission, it is either a parking ticket (see ParkingTickets.md) or it belongs in a different project.

#### Mission Ticket Template

The standard mission ticket template, in full:

```markdown
# <One-sentence mission statement>

## Problem

<Why this mission exists. What is broken, missing, or suboptimal.>

## Solution

<How the problem will be solved. One paragraph minimum.>

### Files Affected

1. `<path/to/file1>`
2. `<path/to/file2>`

## A

<What sub-commit A does and why.>

### Sessions

* <Org>/<Repo>#<SessionNumber>

## B

<What sub-commit B does and why. If no B, omit this section.>

### Sessions

* <Org>/<Repo>#<SessionNumber>
```

The letter sections (A, B, C) are the sub-commits. Each letter section describes one commit. The Sessions subsection records which session ticket the work happened in.

#### Session Numbering: A through Z

Sessions are numbered with letters, not numbers. The session ticket number is the H1 heading, and each section within the session is referred to by its first word.

* `#82.A` refers to sub-commit A of issue 82.
* `#82.Problem` refers to the Problem section of issue 82.
* `#82.Solution` refers to the Solution section of issue 82.

This replaces the old `#1.2` numbering, which was ambiguous: did `.2` mean the second sub-commit or the second session? The letter system is unambiguous: A is always the first sub-commit, B is always the second.

#### Session.Created

Every session ticket has a `Session.Created` field that records when the session was opened. This is the timestamp for when the issue ticket was created, not when the work was done. The format:

```markdown
#### Created

* <Org>/<Repo>#<IssueNumber>
```

The `Session.Created` field is set once, when the session ticket is created, and is not updated. If the session spans multiple days, the creation date is the first day.

#### Groundhog Day

A groundhog day is a day where you make no progress. The log is empty. Nothing was committed. No issue was closed. The demoralization of a groundhog day is real: it feels like the project is stuck, like you are running in place.

The solution is to start the groundhog day with a small, guaranteed win. The sequence:

1. Open the session ticket and write the time you started.
2. Pick the smallest open issue you can close in under fifteen minutes. A typo fix, a missing link, a broken reference.
3. Close the issue. Commit. The log now has an entry.
4. The momentum from the small win carries you into the larger work.

The groundhog day is not a failure. It is a reset. The small win breaks the paralysis, and the rest of the day follows.

#### Session Ticket Template

The standard session ticket template:

```markdown
# Session <Day> <Date>

## Projects

* <Org>/<Repo1> — <what you will work on>
* <Org>/<Repo2> — <what you will work on>

## Created

* <Org>/<Repo>#<IssueNumber>

## Log

### <Time In>

<What you did. What you learned. What you blocked on.>

### <Time Out>

<Summary of the session. What closed. What opened. What is next.>

## Next Session

* <Three tasks to do before anything else next session.>
```

The Projects section lists the repos you will work on that day and what you plan to do in each. This is the primary dev log instruction: you list your projects first, then you work them. If you did not get a session for a listed repo, you need to create a plan the following day to make sure it happens.

The Next Session section is the Kevin O'Leary rule: you set up three tasks at the end of each session that get done before anything else in the next session. This eliminates the cold start problem. You do not wake up and figure out what to do; you wake up and do the three things you already decided to do. The list is done by the end of the day, passed to the next session (or to a coworker or agent) with enough context that they can pick it up without asking.

#### Milestones

Every project has milestones. The first milestone is always GitHub Workspace: the point where the repository is set up, the templates are filled out, the kanban board is configured, and the first issue is created. This is a small milestone, and that is the point. You get a quick psychological reward for completing it, and it proves that the system works before you invest in the larger milestones.

The milestone sequence for every startup:

1. **GitHub Workspace** — repo created, templates filled, board configured.
2. **Mockup** — a visual or interactive prototype that proves the concept. Not a design; a testable artifact.
3. **Proof of Concept** — the mockup plus failing tests. The tests define what the product should do, and they fail because the product does not exist yet.
4. **Alpha** — the first version that works end-to-end for the primary use case. Not polished, not feature-complete, but functional.
5. **Beta** — the version that is ready for external users. Bug-free for the primary use case, documented, deployable.
6. **Debut** — the public launch. The version that is marketed, sold, and supported.

Between GitHub Workspace and Alpha, add milestones as needed. The milestones are the checkpoints that tell you the project is progressing. If you are between milestones and cannot name the next one, you are lost.

#### Issue Ticket Ordering

The first thirteen issue tickets in every repository have reserved roles. You do not get to choose what they are; the system defines them. This is the memory aid: the first seven are days of the week, the next two are session placeholders, and the last four are project lifecycle markers.

| Issue | Role |
|---|---|
| #1 | Session.Next.Monday |
| #2 | Session.Next.Tuesday |
| #3 | Session.Next.Wednesday |
| #4 | Session.Next.Thursday |
| #5 | Session.Next.Friday |
| #6 | Session.Next.Saturday |
| #7 | Session.Next.Sunday |
| #8 | Session.Next.Weeks |
| #9 | Session.Next |
| #10 | Project.Open |
| #11 | Project.Self |
| #12 | Project.Close |
| #13 | Questions |

Issue #10, Project.Open, is where the project is defined: the mission, the vision, the target customer, the value proposition. Issue #11, Project.Self, is where the project describes itself: the assumptions, the constraints, the success metrics. Issue #12, Project.Close, is where the project is wound down: the lessons learned, the handoff notes, the final state. Issue #13, Questions, is the running list of open questions that do not fit in any other ticket.

After #13, issues are numbered in creation order. The reserved slots are the skeleton; the other issues are the flesh.

#### Questions and Hypotheses

A Question is an open item that needs an answer. A Hypothesis is a proposed answer to a question that needs testing. The relationship: every question has a set of hypotheses, addressed as `QnHm` where n is the question number and m is the hypothesis number.

* `Q1H1` — the first hypothesis for the first question.
* `Q1H2` — the second hypothesis for the first question.
* `Q2H1` — the first hypothesis for the second question.

Once a question and its hypotheses are recorded, they cannot be removed. They can only be answered (the hypothesis is confirmed or refuted) or sluffed off (the question is deprioritized and marked as such). This creates a permanent record of what you asked, what you thought the answer might be, and what you actually found.

The Questions ticket (#13) is the index. Each question gets a line:

```markdown
* Q1: Will solo founders pay for a CI pipeline? (Answered: Yes, see Q1H1)
* Q2: Do agents need a merge gate? (Open, see Q2H1, Q2H2)
```

The Hypothesis is not a separate ticket. It is a section within the Question ticket, or a reference from the Question ticket to the experiment that tests it.

#### Agent Workflow for Mission Tickets

When an AI agent picks up a mission ticket:

1. Read the ticket: Problem, Solution, Files Affected, sub-commit sections.
2. Create the branch: `Issue<N>`.
3. Read the files listed in Files Affected.
4. Execute sub-commit A: make the change, run the linter, run the tests.
5. Commit: `<Description> #<N>.A <Explanation>`.
6. Execute sub-commit B (if any): repeat.
7. Push the branch.
8. Open the pull request.
9. Update the session ticket with what was done.

The agent does not merge the pull request. The agent does not create issues that are not on the kanban board. The agent does not modify files that are not in Files Affected. The agent is a contractor: it does the work described in the ticket, nothing more, nothing less.

#### Session Ticket Hierarchy Format

The Hierarchy section of a session ticket links to the issues that the session worked on. The format is:

```markdown
## Hierarchy

* [<Org>#<IssueNumber>](https://github.com/<org>/<repo>/issues/<number>)
```

The link points to the issue in the Workspace repo, not the product repo. The Workspace repo shares the name of the organization: `AStarStartup/AStarStartup`. Session tickets live in the Workspace repo because they are the organization's development log, not a single product's log.

***Example***

```markdown
## Hierarchy

* [AStarStartup#42](https://github.com/AStarStartup/AStarStartup/issues/42)
* [AStarStartup#47](https://github.com/AStarStartup/AStarStartup/issues/47)
```

The session ticket is the log. The issue tickets are the specs. The Hierarchy section connects the two: this session worked on these issues.

#### Issue Tags

Issue tickets are tagged, not typed. The old system used IssueType (Bug, Feature, Mission), which was a single-value field. The new system uses IssueTags, which is a multi-value field. A ticket can have multiple tags:

* `Bug` — something is broken.
* `Feature` — something new to build.
* `Mission` — a ticket that drives a branch and commit sequence.
* `Session` — a daily log entry.
* `Question` — an open question that needs an answer.
* `Hypothesis` — a proposed answer to a question that needs testing.
* `Newb` — the ticket is written for a new contributor.
* `Confusing` — the ticket is unclear and needs rewording.
* `FAQ` — the ticket answers a frequently asked question.

The tags are applied in the Tags section of the ticket:

```markdown
## Tags

* Mission, Newb
```

A ticket without tags is a ticket without context. Tag every ticket when you create it.
