---
layout: page
title: "Mission Tickets"
---

# [Astartup Cookbook](../../)

## [Development](../)

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

* `*.*` (or `*`) indicates broad proposed scope, not permission to stage unrelated changes. Resolve the actual changed paths and stage them explicitly.
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
git commit -m "#26.A Rename IDD to ADD in Development Patterns"
git commit -m "#26.B Update the Development chapter heading and links"
git commit -m "#26.C Update the root README methodology references"
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

The bracketed text above is a placeholder, not a working link. Replace it with the actual mission record in the project's AGENTS.md or README. This creates a traceable chain: the issue serves the mission, the mission serves the vision, the vision serves the founder.

If an issue cannot be traced to the mission, it is either a parking ticket (see ParkingTickets.md) or it belongs in a different project.

#### Mission Ticket Template

The standard mission ticket template, in full:

```markdown
# <One-sentence mission statement>

## Problem

<Why this mission exists. What is broken, missing, or suboptimal.>

## Solution

<Proposed or implemented approach, evidence, alternatives, and acceptance checks.>

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

#### A through Z references

The A–Z notation is a local way to identify issue sections and sub-commits. For example, `#82.A` names sub-commit A, while `#82.Problem` names the Problem section. They are not separate GitHub issue numbers or automatically working deep links. To link a heading, use the actual issue URL and its rendered heading anchor.

Keep issue numbers, session-log identifiers, and commit letters distinct. A session can contain work on several missions; a mission can span several sessions. Do not invent a date or suffix to make them line up.

#### Session.Created

The `Created` list records the issues created during the session:

```markdown
## Created

* <Org>/<Repo>#<IssueNumber>
```

The list is not itself a timestamp. Use the issue's recorded creation time when a timestamp is needed. Session-open time and work times are separate fields. Preserve prior entries; append corrections rather than erasing what happened.

The author's session convention allows a session to span multiple days until it contains at least one meaningful commit. Do not manufacture a commit or hide blocked research to satisfy this rule. Record useful findings and blockers honestly while the session remains open.

#### Groundhog Day

The author's groundhog-day technique is a restart routine after a stalled session. Read the last handoff, pick a small authorized action, do it, and record the verified result. The action can expose a blocker rather than close an issue.

Keep the previous day's evidence and timestamps. Do not rewrite yesterday's work as if it happened today or close an issue before its acceptance check. A restart routine is a suggestion, not a guaranteed psychological effect.

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

The author's starting convention is a GitHub Workspace milestone: repository, templates, coordination, and the first mission are set up and checked. This is an organizational checkpoint, not proof of demand.

Define additional milestones with explicit exit criteria:

1. Mockup: a scenario can be demonstrated or discussed with intended users.
2. Proof of concept: the riskiest feasibility claim has been tested. Failing acceptance tests can document unimplemented behavior, but are not evidence that the product works.
3. Alpha: the agreed primary journey works in a controlled environment.
4. Beta: a bounded external trial has suitable support, safety, documentation, and rollback. Do not promise it is bug-free.
5. Debut: public launch is approved with an operator and measurable acceptance criteria.

Adapt this sequence to the startup. Connect it to [problem–solution analysis](../../Engineering/ProblemSolving.md); do not build each milestone simply because it is in a template.

#### Issue ordering and project records

The historical weekday/session/project numbering schemes evolved in issues #87 and #91 and do not define a reliable universal mapping. GitHub assigns issue numbers in creation order, including pull requests; an agent cannot reserve or renumber existing numbers by writing this chapter.

Use descriptive titles and an index of actual issue links for weekday plans, next/future sessions, Project.Open, Project.Self, Project.Close, and Questions. Discover the configured record instead of assuming Questions is always #13. Preserve the author's naming system without overwriting existing issue identities.

The exact numbered bootstrap scheme and additional records proposed in issue #91 need the Captain's decision before they are treated as current policy. Do not migrate a board or create dozens of placeholder issues during a content task.

#### Questions and Hypotheses

A Question is an open item that needs an answer. A Hypothesis is a proposed answer to a question that needs testing. The relationship: every question has a set of hypotheses, addressed as `QnHm` where n is the question number and m is the hypothesis number.

* `Q1H1` — the first hypothesis for the first question.
* `Q1H2` — the second hypothesis for the first question.
* `Q2H1` — the first hypothesis for the second question.

Once a question and its hypotheses are recorded, they cannot be removed. Record whether evidence supports, contradicts, or leaves a hypothesis inconclusive, or mark the question as sluffed off (deprioritized). This creates a permanent record of what you asked, what you thought the answer might be, and what you actually found.

The configured Questions record is the index. Each question gets a line:

```markdown
* Q1: Will the selected customer segment pay for this workflow? (Open; proposed test Q1H1)
* Q2: Do agents need a merge gate? (Open, see Q2H1, Q2H2)
```

The Hypothesis is not a separate ticket. It is a section within the Question ticket, or a reference from the Question ticket to the experiment that tests it.

#### Agent workflow

Follow [Contributing](../Contributing.md) and [Agent Operations](../AgentOperations.md). Read the full mission and comments, inspect local state, agree on the file list and checks, then implement only the authorized scope. The workspace commit grammar is `#<N> <title>` or `#<N>.A <sub-commit title>` with a matching issue section. Remote writes, merge, deployment, and issue closure require their own authority.

Before choosing a solution, use [Problem Solving](../../Engineering/ProblemSolving.md). Link the decision and evidence from the ticket so an executable mission does not silently become a claim of market validation.

#### Session ticket hierarchy

Session logs belong in the organization's designated coordination repository. Discover that location from its instructions; a same-name organization repository is a convention, not a guarantee.

A session's Hierarchy list links to the actual mission issues worked on, which may live in different product repositories. The display label and URL must identify the same issue:

```markdown
## Hierarchy

* [<Org>/<ProductRepo>#<MissionNumber>](https://github.com/<Org>/<ProductRepo>/issues/<MissionNumber>)
```

Use real links in a filled record. Do not redirect all product missions to a workspace issue with the same number.

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
