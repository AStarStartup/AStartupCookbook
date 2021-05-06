# [Astartup Cookbook](../)

## [Development](./)

### Development Patterns

Development patterns are patterns to follow while developing a product, and are not to be confused with design patterns.

#### Waterfall Development

The Waterfall Development Pattern is where a project progresses sequentially through development stages without working on any prior stages. This is the fastest possible time-to-market development pattern, but is not flexible to incorporate knowledge learned during the development process. For some projects this may or may not matter or be a good or bad thing, it all depends of if the correct user requirements where collected ahead of time. More about this will be elaborated upon in Chapter 8: Design.

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

#### Issue Driven Development

Issue Driven Development (IDD) is a method that relies on a Kanban board and issue tracking system (ITS) to keep you on track by you only working on a single issue at a time, and no work is allowed to happen without an issue first being inputted into the ITS.

The process starts anytime you are doing work on code, you first create an Issue in the ITS. This issue gets associated with a Project Kanban board. When work begins you place the issue in the todo . The issue needs to be small enough that one or more issues can be tackled per day. If an issue is so big that it takes more than one day to complete then that issue is said to be an *Out of Control Issue*.

When the developer wishes to commit files, the developer then copies and pastes the title of the issue from the ITS along with the issue's unique ID (UID), and submits the commit with the issue a message consisting of the title and the UID. In GitHub, clicking on the UID in the commit log will take you to the issue page, which allows developers to chat about the issue and for teams and solo developers to use a digital development log.

IDD may make use of multiple enumerated seams, borrowed from Agile Development. Seams may be enumerated as Minor Seams, which are a group of one or more files of code that have specific debug information needs associated with them; and Major Seams, which are groups of one or more Minor Seams that have related debug information needs. Major and Minor Seams are useful because they allow you to target Unit Test information. When something breaks, the seam layers may be pealed back and only the debug information the developer needs shows up in the unit test script.

IDD's most useful feature is that any project can start using it right away and it helps projects transition into an Agile state where the product always works and new features and changes can be made without breaking everything. The amount of overhead time managing IDD is far less than the time wasted with IDD, I was even able to write books in the extra saved time!

##### Working on Non-contiguous Seams

Seams must be tested in a specific order, or combination of orders, to ensure they are working, do not require that you only work on that seam. It may be advantageous to work on seams that are one or more major seams away from the code you are working on because it helps to avoid reworking the same files because you didn't look ahead. It works best to create a prototype of the work on the higher seam numbers, then go back to working on the sequential seam. This may also allow you to work on something a little bit more fun for a while to break the monotony. The big thing is that you be prepared for changes on previous seam numbers to potentially propagate through to higher number seams.

##### Tips

* Don't let your issues build up: A project with thousands of back-logged issues is by definition not Agile. Use StarUML to backlog issues and add features in the model first before polluting the ITS.

* Only do work on the files with sections that the issue requires: while you're not an inherently bad person for doing so you do lose some useful information from the revision commit history. Some of the most important work that has occurred is the work that occurred directly before what you're doing, so if you make that information harder for the team to see, it greatly increases the chance they won't see the information and make some choice that slows the team down or at worst causes irreparable damage. This, however, does not apply to work done on sections not addressed by the issue that are in the same file because it would not alter the file commit log.

* Organize your Major Seams using a UML Package Diagram that visibly separates the packages based on seam: UML Package Diagrams are useful because they are a dependency diagram, which helps put the hoarse in front of the cart and decouple the seam layers as much as possible.

![Kabuki Toolkit UML Seam and Package Diagram.](images/kabuki_package_diagram.jpg)

* Keep your issue titles as short as possible: if your issue title is so long it doesn't fit in the one line, break it up into smaller issues. You need to be able to click on the issue ticket number to take you to the issue and you can explain the work in more detail on the issue description.

#### Old Astartup Method @todo Fix me!

The approach used throughout this book is called AStar Driven Development (or MDD) and Astartup, which are a combination of the industry standard development processes with artificial intelligence. MDD gets it's name from the AStar function, a famous greedy lookahead game theory algorithm that is a fundamental theorem of Artificial Intelligence. It is at it's essence a variation of Dijkstra's Shortest Path Algorithm combined with some statistics. The essence of the algorithm is to minimize cost and maximize reward, so it is a suiting name.

##### Tradeoffs

###### Pros

1. Built on industry standard AI and Machine Learning techniques.
2. Good a minimizing cost and maximizing reward.
3. Works with existing startups to allow them to transition into a lean state.
4. Can work by using a pen-and-paper development log.

###### Cons

1. Some startup companies make it more expensive to get user Analytics.

## License

Copyright  2014-21 © [Cale McCollough](https://cookingwithcale.org); most rights reserved, Third-party commercialization prohibited, mandatory improvement donations, licensed under the Kabuki Strong Source-available License that YOU MUST CONSENT TO at <https://github.com/CookingWithCale/AStartupCookbook>.
