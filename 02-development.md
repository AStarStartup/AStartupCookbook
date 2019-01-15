# 2 Development

This chapter outlines the most important industry standard development processes every beginning tech entrepreneur and inventor needs to know about.

Development Processes are the engineering processes used to design, develop and manage the life cycles of products. Development processes are used to minimize cost and maximize reward. Development processes often times borrow concepts from each other, and are commonly refereed to as the two traditionally distance classes of Development processes, Waterfall-like vs Agile-like Processes.

The best way to think about development processes is that they are project competition rate maximization and completion time minimization optimization techniques; which are two if the most key metrics with startup companies hence why they are at the beginning of the book. Slacking off proper development processes can and almost invariantly will cause a lot of headaches. First that it will greatly increase time and costs to a point that jeopardizes the project, and second that professionals expect you to use the industry standard processes and when you don't use them it makes it hard for the professionals to work.

There are so many different Fill In the Blank Driven Development Processes that it can become somewhat of a shallow buzz word; this is complacency. One of the most important and heavily used development processes reiterated throughout this book is Issue Driven Development (IDD). Studies have proven time after time that people are not good at multitasking, even if they think they are, so the primary principle of this book is to do one thing better, cheaper, and faster than everyone. Throughout your development process, try to put on blinders and choose the correct development pattern that will help you complete your goals in a timely manner with an acceptable product. As you will learn from the lessons in this book that an acceptable product is better than no product.

## 2.1 Case Study:

## 2.2 Revision Control Systems

The goal of this case study is to highlight an entrepreneur who does not program computers who has failed without using revision control, and who now could not live without it. The study should highlight how you should only do work in digestible chunks where you have a clear planned goal, and then synchronize their settings to

This chapter talks about revision control systems and how they are used on projects. The aim of this chapter is to get people who do not use revision control systems on their projects.

### 2.2.a Git

Git is a RCS programmed in C that is the gold standard for RCS. Git is very easy to use when working by yourself. You can get away with only knowing a handful of commands. Reverting changes does take a little bit of a learning curve but if you use a web-based Git tool like GitHub you may use the website to look at past changes and copy and paste or download the original raw data. Git is the primary revision control system that shall be used throughout this book.

```
git init
git add --all
git commit -m "First commit."
git push
```

This works great when you're working by yourself as long as you keep your code working and documented, but it will not fly when working with others. When working with others you will need to use an Issue Tracking System and make a Pull Request for an Issue which you then merge back into the Master branch; we'll cover this more below.

### 2.2.b Mercurial

Mercurial is programmed in Python and is similar to Git in functionality but provides a higher level command line interface. Mercurial distinguishes itself from git in how it manages revision history. Mercurial only allows users to roll back changes and not to modify the history. This may be more useful for more useful for documentation purposes.

## 2.3 Issue Tracking System



## 2.4 Primary Development Patterns

Development patterns are patterns to follow while developing a product, and are not to be confused with design patterns.

### 2.4.a Waterfall Development

The Waterfall Development Pattern is where a project progresses sequentially through development stages without working on any prior stages. This is the fastest possible time-to-market development pattern, but is not flexible to incorporate knowledge learned during the development process. For some projects this may or may not matter or be a good or bad thing, it all depends of if the correct user requirements where collected ahead of time. More about this will be elaborated upon in Chapter 8: Design.

A good example of when a Waterfall Development Pattern may be useful is when you know ahead of time exactly what the customer will buy based on inside market information, and you need to rush to market as fast possible, and you're a team of professionals who have build many similar products. In this situation the Waterfall would be preferred.

A good example of when you should never use a Waterfall Development Pattern is when you're making an app, you've got an idea and you think you'll make millions off of it, you have never interviewed a customer, and you spend years working on it till you get the features what you want done. By the time you get done, you'll find the customer had some valuable insights that made your design not a good solution for most people.

In the second example, years of work could be avoided by just asking your customer up front what features are the solution they are willing to pay for.

### 2.4.b Iterative Development

This is your standard waterfall talk.

### 2.4.c Agile Development Method

The agile software development method.

#### Tradeoffs

Agile is awesome if you’re a computer programmer.

## 2.4.d Lean Manufacturing

### 2.4.e Lean Startup

The Lean Startup Method, invented by Eric Ries, is the new rage in business, from small garage startups, to mammoth corporations. It’s something that all inventors, engineers, and entrepreneurs should know about.

## 2.4.f Test Driven Development

Not to be confused with Design for Test, though they are often used together.

### 2.4.g Issue Driven Development

Issue Driven Development (IDD) is a method that relies on a Kanban board and issue tracking system (ITS) to keep you on track by you only working on a single issue at a time, and no work is allowed to happen without an issue first being inputted into the ITS.

The process starts anytime you are doing work on code, you first create an Issue in the ITS. This issue gets associated with a Project Kanban board. When work begins you place the issue in the todo . The issue needs to be small enough that one or more issues can be tackled per day. If an issue is so big that it takes more than one day to complete then that issue is said to be an *Out of Control Issue*.

When the developer wishes to commit files, the developer then copies and pastes the title of the issue from the ITS along with the issue's unique ID (UID), and submits the commit with the issue a message consisting of the title and the UID. In GitHub, clicking on the UID in the commit log will take you to the issue page, which allows developers to chat about the issue and for teams and solo developers to use a digital development log.

IDD may make use of multiple enumerated seams, borrowed from Agile Development. Seams may be enumerated as Minor Seams, which are a group of one or more files of code that have specific debug information needs associated with them; and Major Seams, which are groups of one or more Minor Seams that have related debug information needs. Major and Minor Seams are useful because they allow you to target Unit Test information. When something breaks, the seam layers may be pealed back and only the debug information the developer needs shows up in the unit test script.

IDD's most useful feature is that any project can start using it right away and it helps projects transition into an Agile state where the product always works and new features and changes can be made without breaking everything. The amount of overhead time managing IDD is far less than the time wasted with IDD, I was even able to write books in the extra saved time!

#### Working on Non-contiguous Seams

Seams must be tested in a specific order, or combination of orders, to ensure they are working, do not require that you only work on that seam. It may be advantageous to work on seams that are one or more major seams away from the code you are working on because it helps to avoid reworking the same files because you didn't look ahead. It works best to create a prototype of the work on the higher seam numbers, then go back to working on the sequential seam. This may also allow you to work on something a little bit more fun for a while to break the monotony. The big thing is that you be prepared for changes on previous seam numbers to potentially propagate through to higher number seams.

#### Tips

* Don't let your issues build up: A project with thousands of back-logged issues is by definition not Agile. Use StarUML to backlog issues and add features in the model first before polluting the ITS.

* Only do work on the files with sections that the issue requires: while you're not an inherently bad person for doing so you do lose some useful information from the revision commit history. Some of the most important work that has occurred is the work that occurred directly before what you're doing, so if you make that information harder for the team to see, it greatly increases the chance they won't see the information and make some choice that slows the team down or at worst causes irreparable damage. This, however, does not apply to work done on sections not addressed by the issue that are in the same file because it would not alter the file commit log.

* Organize your Major Seams using a UML Package Diagram that visibly separates the packages based on seam: UML Package Diagrams are useful because they are a dependency diagram, which helps put the hoarse in front of the cart and decouple the seam layers as much as possible.

![Kabuki Toolkit UML Seam and Package Diagram.](images/kabuki_vm_package_diagram.jpg)

* Keep your issue titles as short as possible: if your issue title is so long it doesn't fit in the one line, break it up into smaller issues. You need to be able to click on the issue ticket number to take you to the issue and you can explain the work in more detail on the issue description.

### 2.4.h AStar Method

The approach used throughout this book is called AStar Driven Development (or MDD) and Astartup, which are a combination of the industry standard development processes with artificial intelligence. MDD gets it's name from the AStar function, a famous greedy lookahead game theory algorithm that is a fundamental theorem of Artificial Intelligence. It is at it's essence a variation of Dijkstra's Shortest Path Algorithm combined with some statistics. The essence of the algorithm is to minimize cost and maximize reward, so it is a suiting name.

#### Tradeoffs

##### Pros

1. Built on industry standard AI and Machine Learning techniques.
2. Good a minimizing cost and maximizing reward.
3. Works with existing startups to allow them to transition into a lean state.
4. Can work by using a pen-and-paper development log.

##### Cons

1. Some startup companies make it more expensive to get user analytics.

## 2.5 Development Styles

There are two distinct types of development styles; vertical development, and horizontal development.

### 2.5.a Vertical Development

### 2.5.b Horizontal Development

### 2.5.c Top Down vs Bottom Up

## 2.6 Project Management

### 2.6.a Common Charts

#### Gantt Charts

#### Shortest-time Graph

### 2.6.b Project Management Software

Project management software (PMS) comes in three flavors, offline app-based, online app-based and web-based PMS(s). *Offline app-based project management software* uses a project file stored on the local computer, and is mainly suitable for single administrator projects and very small teams. *Online app-based PMS* functions as offline project management software but it has a central server that allows for multiple administrators but no web app. *Web-based PMS* primarily uses web apps, may also have a downloadable app, and is suitable for multi-administrator projects with many employees.

#### Microsoft Project

Microsoft Project is a classic industry standard Online App-based PMS. The main usefulness of Project is to get a timeline of how long projects will take and plan the execution of resources. Project at it's core is an Offline App-based PMS with a very clean interface and robust feature set. Project makes it easy to plan tasks and assign tasks to people.

Microsoft Project Server, Project's Online App-based PMS component, is good for non-programming tasks such as managing startups, businesses, and projects with an Admin department Project has a server software that assists in synchronizing client apps so everyone stays up to date. This design method predates web 2.0 and is no longer as useful as the web based tools, but is still useful.

#### ProjectLibre

ProjectLibre was the first big open source Offline App-based PMS replacement for MS Project. If you don't have a multi-million dollar budget or work with others who use Mac or Linux, it's best to not spend too much time in the project software so ProjectLibre may be a better option for startups. For what Microsoft Project is good for, it's not really worth paying money for most people, ProjectLibre does everything you would probably need to do, and if doesn't than you probably need a Web-based PMS.

#### GanttProject

GanttProject is a Java based Offline App-based PMS replacement for Microsoft Project that markets themselves as a simplified MS Project alternative. If all you need to do is the basic project management tasks, GanttProject may be the de facto tool as of 2018. As of the writing of this project GanttProject had active development on GitHub and ProjectLibre did not.

#### Redmine

Redmine is a world-class Ruby-on-Rails based Web-based PMS that is very useful for contractors and consultants. Redmine's prominent features include Gantt charts, multi-project support with unique support ticket IDs global to all projects, issue tracking, wiki, email-based issue creation, time tracking, news, documents, email notifications, and a lot more features that make it perfect for both small and large teams. Redmine is really useful for keeping track of man hours for tax purposes, especially if you're doing consulting or contracting with many clients.

#### Slack

Slack does not provide Gantt charts but it is exceptionally useful for development. Slack gives you just enough free features to get startups going to the point where they can startup making money, but then you'll be forced to upgrade to save your data. Slack is mostly useful for sharing information in chat such as code snippets and documents. Other than working well with high tech chat needs, there is little else that separates Slack from a traditional chat application.

## 2.7 Summary

* [Chapter 3: Documentation.md](03-documentation.md.md)
* [Content Table](01-overview.md#11-content-table)

## 2.7 Exercises

**1.**
**A.** Sign up for accounts with BitBucket and GitHub.
**B.** Create

1. Download ProjectLibre and GanttProject and play around with them.

**2.** Download and install the Slack client for all of your computers.

# The License

Copyright 2014-2018 (C) [Cale McCollough](https://calemccollough.github.io).

Astartup Copyright (C) 2014-8 Cale McCollough. All rights reserved (R). <<[mailto:cale.mccollough@gmail.com](cale.mccollough@gmail.com)>> <<[https://calemccollough.github.io](https://calemccollough.github.io)>>

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.  If not, see <https://www.gnu.org/licenses/>.
