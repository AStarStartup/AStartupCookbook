# [Astartup Cookbook](../../)

## [Development](../../)

### [Issue-driven Development](./)

#### Parking Tickets

An Parking Ticket is a standard tree markdown template for IDD that helps clarify the details of an issue. It is called a Parking Ticket as a pun on Driven Development. An Parking Ticket is composed of a one-sentence mission statement title, an Issue Type as the H1 heading and there is one H2 heading for the Problem, Solution, Mission Details, and Hierarchy.

#### One-sentence Mission Statement

Every Issue should have for it's title a one-sentence mission statement. A mission is easiest to describe in terms of a milliary combat operation. You don't just want to go out fighting the enemy in the abstract, you need to target specific parts of the enemy and attack the enemy until it is defeated. If possible every issue should only address one discrete mission; this however is not possible without addressing a coupled issue, or sometimes you're just too lazy to make an extra issue ticket, so when there is more then a one mission, they should be separated by a semicolon. In IMUL every mission starts with a verb, such as Rename, Add, Delete, etc.

***Example***

`Title:Lib.ModuleXYZ.Add feature ABC; Rename Foo bar.`

#### Issue Type

The Issue type describes what type of issue this is. The goal of the Issue Type is to express in as few of words as possible what type of work needs to be done. Common Issue types are:

* Feature Request
* Bug Report
* Bug Fix
* Implementation
* Design Tweak
* Design Iteration
* Breaking Change
* Legal
* Typos
* FAQ
* Organize
* Partnership Request

#### Problem

Every issue must address a problem. Sometimes the problem is the same as the one-sentence mission statement. We only want to go on a mission if there is a problem, and if there isn't a problem then the mission itself is a problem. A problem statement should be as short as possible to express why we're going on the mission.

#### Solution

For every problem, there should be *AT LEAST** one solution. A good solution statement should address why this is the appropriate solution for the problem statement. You should describe what are the properties of a solution that will achieve the affect desired. When you're mapping out and prioritizing issues you might not know which solution you'll use, so you should use one H2 heading for each solution.

#### Mission Details

The Missions Details section details about the mission you can't fit in the one-sentence mission statement, such as filenames of affected files, procedures required to perform changes, pre and post conditions, conditions for success, and quality assurance instructions.

#### Hierarchy

If an issue is part of a hierarchy of issues it can help developers by linking to the parent and child issues. Hierarchies are very useful for breaking up larger issues into more manageable sub-issues. If an issue tree doesn't contain a Hierarchy section it is assumed to be a flat hierarchy.

## License

Copyright 2014-20 (C) [Cale McCollough](https://cookingwithcale.org).

This is an open-source document, the Document, that was written by and contains intellectual property. The Document consists of documents, files, source code, technology design files, art, and other content contained this file, folder and the GitHub repository located at <https://github.com/AStarStartup/AstartupCookbook>, the Repository. The Document is published under a generic non-commercial open-source license, the License, and is for educational and demonstration purposes only. You may use, reproduce, publicly display, and modify the Document so long as you submit and donate fixes and derived intellectual property, the Donated Ideas, to the Repository as an Issue ticket to become part of the Document. You may not sell the Document or otherwise profit from derivative works created from the Document without the expressed written permission of the copyright holder. Unless required by applicable law or agreed to in writing, the Document distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
