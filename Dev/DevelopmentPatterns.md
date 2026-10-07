---
layout: page
title: "Development Patterns"
status: draft
---

# [Astartup Cookbook](../)

## [Development](./)

### Development Patterns

Development patterns are patterns to follow while developing a product, and are not to be confused with design patterns.

#### Waterfall Development

The Waterfall Development Pattern is where a project progresses sequentially through development stages without working on any prior stages. It can be appropriate when requirements and dependencies are stable, but it is less flexible when new information requires revisiting earlier decisions. It is not universally the fastest route to market. For some projects this may or may not matter or be a good or bad thing, it all depends of if the correct user requirements where collected ahead of time. More about this will be elaborated upon in Chapter 8: Design.

A good example of when a Waterfall Development Pattern may be useful is when you know ahead of time exactly what the customer will buy based on inside market information, and you need to rush to market as fast possible, and you're a team of professionals who have build many similar products. In this situation the Waterfall would be preferred.

A good example of when you should never use a Waterfall Development Pattern is when you're making an app, you've got an idea and you think you'll make millions off of it, you have never interviewed a customer, and you spend years working on it till you get the features what you want done. By the time you get done, you'll find the customer had some valuable insights that made your design not a good solution for most people.

In the second example, years of work could be avoided by just asking your customer up front what features are the solution they are willing to pay for.

#### Iterative Development

This is your standard waterfall talk.

#### Agile Development Method

The agile software development method.

##### Tradeoffs

Agile is awesome if you’re a computer programmer.

### Lean Manufacturing

#### Lean Startup

The Lean Startup Method, invented by Eric Ries, is the new rage in business, from small garage startups, to mammoth corporations. It’s something that all inventors, engineers, and entrepreneurs should know about.

### Test Driven Development

Not to be confused with Design for Test, though they are often used together.

#### Agentic Driven Development

Agentic Driven Development (ADD, formerly Issue Driven Development, IDD, and Mission-Driven Development, MDD) is a method that relies on a Kanban board and issue tracking system (ITS) to keep you on track by only working on a single issue at a time, and no work is allowed to happen without an issue first being inputted into the ITS.

ADD is the agentic-era evolution of the method. The core principle is unchanged: the mission drives the development. What has changed is who executes the mission. In the pre-agentic era, a human read the ticket, wrote the code, ran the tests, and committed. In the agentic era, an AI agent reads the ticket, writes the code, runs the tests, and commits. The human's role shifts from executor to director: the human defines the mission, reviews the agent's work, and merges the pull request.

The agentic workflow:

1. The human creates the issue ticket with a clear Problem and Solution.
2. The human assigns the ticket to an agent on the kanban board.
3. The agent reads the ticket, creates a branch, and executes the sub-commits.
4. The agent pushes the branch and opens a pull request.
5. The CI pipeline runs automatically.
6. The human reviews the pull request and merges it.
7. The agent updates the session ticket.

The human may still code, investigate, sell, and support customers. A precise ticket helps but does not guarantee correct output; evidence, implementation quality, tests, and review also matter. The ticket records an authorized next step, not proof of customer demand.

The process starts anytime you are doing work on code, you first create an Issue in the ITS. This issue gets associated with a Project Kanban board. When work begins you place the issue in the todo . The issue needs to be small enough that one or more issues can be tackled per day. Long missions are not automatically out of control. Split them into reviewable steps with checkpoints when that improves verification and coordination.

When the developer wishes to commit files, the developer then copies and pastes the title of the issue from the ITS along with the issue's unique ID (UID), and submits the commit with the issue a message consisting of the title and the UID. In GitHub, clicking on the UID in the commit log will take you to the issue page, which allows developers to chat about the issue and for teams and solo developers to use a digital development log.

IDD may make use of multiple enumerated seams, borrowed from Agile Development. Seams may be enumerated as Minor Seams, which are a group of one or more files of code that have specific debug information needs associated with them; and Major Seams, which are groups of one or more Minor Seams that have related debug information needs. Major and Minor Seams are useful because they allow you to target Unit Test information. When something breaks, the seam layers may be pealed back and only the debug information the developer needs shows up in the unit test script.

IDD's most useful feature is that any project can start using it right away and it helps projects transition into an Agile state where the product always works and new features and changes can be made without breaking everything. The amount of overhead time managing IDD is far less than the time wasted with IDD, I was even able to write books in the extra saved time!

##### Working on Non-contiguous Seams

Seams must be tested in a specific order, or combination of orders, to ensure they are working, do not require that you only work on that seam. It may be advantageous to work on seams that are one or more major seams away from the code you are working on because it helps to avoid reworking the same files because you didn't look ahead. It works best to create a prototype of the work on the higher seam numbers, then go back to working on the sequential seam. This may also allow you to work on something a little bit more fun for a while to break the monotony. The big thing is that you be prepared for changes on previous seam numbers to potentially propagate through to higher number seams.

##### Tips

* Don't let your issues build up: A project with thousands of back-logged issues is by definition not Agile. Use StarUML to backlog issues and add features in the model first before polluting the ITS.

* Only do work on the files with sections that the issue requires: while you're not an inherently bad person for doing so you do lose some useful information from the revision commit history. Some of the most important work that has occurred is the work that occurred directly before what you're doing, so if you make that information harder for the team to see, it greatly increases the chance they won't see the information and make some choice that slows the team down or at worst causes irreparable damage. This scope discipline also applies to unrelated sections in the same file; sharing a filename does not make a change part of the mission.

* Organize your Major Seams using a UML Package Diagram that visibly separates the packages based on seam: UML Package Diagrams are useful because they are a dependency diagram, which helps put the hoarse in front of the cart and decouple the seam layers as much as possible.

The original Kabuki Toolkit seam diagram is missing from this repository; do not infer its structure from a broken image reference.

* Keep your issue titles as short as possible: if your issue title is so long it doesn't fit in the one line, break it up into smaller issues. You need to be able to click on the issue ticket number to take you to the issue and you can explain the work in more detail on the issue description.

#### Historical AStar naming

The earlier AStar-driven terminology inspired the method's name. It is not a proof that following this workflow produces the shortest or cheapest startup path. A startup has uncertain outcomes and incomplete information; a graph-search analogy does not establish a success probability.

Keep the original seam and logging concepts above as material to review and adapt. For current execution authority and verification, use [Agent Operations](./AgentOperations.md). For choosing an outcome before writing a ticket, use [Problem Solving](../Engineering/ProblemSolving.md).
