---
layout: page
title: "Development Logs"
status: draft
---

# [Astartup Cookbook](../)

## [Documentation](./)

### Development Logs

Development logs have been a staple of engineering and science projects for centuries. If you study some of the greatest thinkers in history, most have kept logbooks and journals, such as Leonardo da Vinci, Isaac Newton, Thomas Edison, Albert Einstein, Thomas Jefferson, George Lucas, Charles Darwin, Ludwig van Beethoven, Benjamin Franklin, and just about every scientist in the history of science kept log books. Development logs are good for organizing your thoughts. Today, people have begun to shy away from written logs, but there are many reasons why you should keep a written development log.
You have to look at it from the perspective of someone who knows absolutely nothing about the project and your opening up the manual. This person knows absolutely nothing about your project aside from a short verbal description. Most people make the mistake of thinking that just because the person that they are talking to is smart, that they got the intricate details of exactly what you said. It’s pretty common.

The best way to think about what a Development Log is to compare it to taking notes in College where a Technical Reference Document is a writing a paper from information from your notes. A development log is meant to be a chronological log of notes. A Technical Reference Document is not Chronological and is organized into sections based on systems and sub-systems. A development log should be in a bound notebook is such a manner that it be allowed as evidence in a court proceeding. It doesn’t have to look professional. You’re not creating a user’s manual, or even a paper that will be peer reviewed or used as an official company document. What you are creating with a development log is for your own reference, and for any employees that get hired to replace you in the future.

#### Log Types

##### Pen and Paper Logs

Pen and paper logs are the preferred method for most because research shows that writing by hand triggers mussel memory that helps you [Insert proof and methods here].

##### IMUL Logs

Not everyone likes to keep handwritten log books. Keeping a digital logbook in MarkDown Format or Google Drive or OneDrive can also be just as useful because it is quicker to communicate with others when the data is entered directly into a shared documentation tool. I am You Language (IMUL) was developed in order to reduce the amount of writing required to make a development useful. IMUL natively supports Doxygen and Markdown tags.

#### Log Purposes

Just because you said Development Lot on the front of the notebook along with the project name, doesn’t mean that the person who reads it is going to know what it is. Ever good technical document has a brief section in the front for it that describes what the document is. An overview can be as simple as one paragraph.

##### Legal Protection

A well-written development log in a bound notebook can help you out greatly with legal protection. The legal stature for what is allowed as admissible log evidence by a court is similar to the process for patent protection. The logbook needs to be bound such that the pages are not removable

##### Research Purposes

A lot of great inventions happened because of people noticing things when they were working on unrelated projects. By documenting things properly, you can assist in other discoveries along the way.

#### Common Log Sections

#### Overview Section
Every document should start with an overview section.

#### Author & Legal Notices
Some random paragraph about why this is completely obvious.

#### Standard Partitioning

Each profession should have its own set of rules that govern what should and should not be in a log to be up to specification. Some standard partitions used across industries are:
* a
* b
* c
* ...

#### Log Entries

##### Logging Hours

If you are not currently using any time logging software, it is possible to use headings to store this information for quick retrieval later. All you have to is record your start time, stop time and any noteworthy breaks into the heading in your pre/post-session header. You can also just have a blank section under your header for your break time. This will allow you to quickly copy the time records from a word processor to your spreadsheet software.

Pending your employer needs an official record of your time records, it can be quite a convent to use any standard revision control system to make official records. Simply make your pre-session entry, save the word document, and push the changes to the server. Also, do the same for unpaid breaks, and post-session entries.

Don’t think that you have to be on someone else’s clock to justify doing this. Keeping track of your own hours has also been linked to increasing your own productivity [Note: Insert citation here]. It’s all too easy to let weeks go by without getting the work done that you wanted to do. By keeping good track of your hours will help keep you on your toes because you’ll feel bad whenever you see large gaps in your time records. Before I started keeping tracking of my time, I would even start growing grey hairs without getting anything done. After I started, I haven’t gone more than a few days without getting something done because I feel bad if I see the holes. If you’re not paying attention to the holes, they often go unnoticed.

There is no real set defined format for a development log other then it is chronological. It’s supposed to be off the cut and personal, but there are some common traits to formatting. A development log is very similar to writing notes for a college-level class. Anything that you can think of that would be important for analyzing your or your teams work.

###### Time-On Log

Chronological Formatting is where notes are kept in strict order that they were addressed in the development log. Each day that work is done on the project would be created as the project unfolds.

###### Time-Out Log

When you are done with your work session, you should make a final entry for that work session.
It is useful to make a log when you start your work shift, and describe what you want to accomplish during that work session. This allows you to focus your attention on what needs to be done.
Common Sections

##### Log Format

* Author & Legal Notices
* Overview/Introduction
* Description
* Purpose
* Vision Statement
* End-user Use Examples

##### Log Reviews

Every good development log should have a peer review their logs. We're all trying to get better but we can't without constructive criticism.

#### Secondary Log: Prior Session Progress Report

The secondary log is the brief summary at the start of each session that tells you where you left off. Without it, every session starts with the same cold open: "What was I working on? What did I do yesterday? Where am I in the project?" The progress report eliminates the cold open.

The format is one to three sentences:

```markdown
## Prior Session Progress

Yesterday I worked on the AStartup Toolkit MCP server and got the
authentication flow passing all tests. The CI pipeline is green.
Today I am moving to the session ticket template.
```

This is not a restatement of the issue ticket. The issue ticket says what the problem is and what the solution is. The progress report says where you are in the solution: what you did, what is done, what is next. It is the handoff note from yesterday-you to today-you.

The rule: if you did not write a progress report at the end of the session, you write one at the start of the next session before you do anything else. Two sentences. What you did. What is next. Then you get to work.

#### Primary Log: List Your Projects

The primary log starts with a list of the projects you will work on that day and the approximate times. This is not a to-do list; it is a schedule. The difference: a to-do list is "things to do sometime," a schedule is "I will do this thing at this time."

```markdown
## Projects

* 08:00 - 10:00 AStarStartup/AStartupCookbook — Content: Psychology chapters
* 10:00 - 12:00 AStarStartup/AStartupToolkit — Code: MCP server auth
* 14:00 - 15:00 AStarStartup/AStartupWorld_ — Code: Next.js landing page
* 15:00 - 16:00 Admin — Email, kanban review, next session setup
```

The times are approximate, not rigid. If the first project runs long, the second starts late. The point is not to hit the times; the point is to know which projects you are working on and in what order. If you did not get a session for a listed project, the next day's log starts with a plan for why it did not happen and how to make it happen.

The organization-level rule: you push the organization name on the stack, not the individual repo. This is because getting a session number for each repo individually is too much friction. The organization is the unit of logging. The individual repo is noted in the project line.
