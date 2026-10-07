---
layout: page
title: "UX Principles"
---

# [Astartup Cookbook](../)

## [Design](./)

### UX Principles

User experience design is the discipline of making a product usable, useful, and pleasant. The eight principles below, drawn from Dan Brown's work on information architecture, are the foundation for any interface, from a single-page website to a full SaaS platform.

#### 1. Object Principle

View your content as living. It changes and grows over time. Do not design a static structure and expect it to hold. Design the object, the thing itself, and let the structure around it adapt as the content evolves. A product feature is an object. A customer account is an object. A document is an object. Design the object's interface first, then design how objects relate to each other.

Practical application: when you add a new feature, you should not have to redesign the navigation. The feature should slot into the existing object structure. If adding a feature requires a navigation redesign, the information architecture is wrong.

#### 2. Choice Principle

People think they want many choices, but they actually need fewer choices that are well-organized. Every additional option on a screen increases cognitive load and decreases the probability that the user picks the right one. The goal is not to remove choice; it is to organize choice so the right option is obvious.

Practical application: a signup form with twelve fields has a lower completion rate than one with four. Collect the minimum information needed to get the user to their first "aha" moment, then ask for more later. A pricing page with eight plans is a pricing page with no plan. Three plans, clearly differentiated, is the ceiling.

#### 3. Disclosure Principle

Information should not be unexpected or unnecessary. Show the user only what they need at the current step. Reveal more as they progress. A user who is choosing a plan does not need to see the API documentation. A user who is writing their first document does not need to see the advanced formatting options.

Practical application: progressive disclosure. The default view shows the common case. The advanced options are one click away for the user who needs them, but they do not clutter the interface for the user who does not. This is the difference between a tool that feels simple and a tool that feels shallow.

#### 4. Exemplar Principle

Humans categorize. They group similar things together and use examples to understand categories. When designing a system, make the categories obvious. Use consistent naming, consistent placement, and consistent visual treatment for items in the same category.

Practical application: if your product has "projects," "workspaces," and "folders," the user needs to understand the difference immediately. Use one clear example of each on the onboarding screen. If the user cannot tell the difference after seeing the example, the categories are not distinct enough and you should merge them.

#### 5. Front Door Principle

The home page does not need to do everything. Users arrive at your site through many doors: a search result for a specific feature, a blog post, a friend's recommendation, a direct URL. Design each entry point to be a valid front door. The user who lands on your pricing page should be able to buy without ever visiting the home page. The user who lands on your API documentation should be able to start building without reading the marketing copy.

Practical application: every page should be reachable and useful on its own. Do not create a linear funnel where the user must pass through the home page to get to anything. Test your information architecture by asking: "If a user lands on this page from a Google search, can they accomplish their goal without getting lost?"

#### 6. Multiple Classification Principle

People search for information in different ways. One user searches by category, another by feature, another by use case, another by what the product is not. Design your navigation and search to support multiple paths to the same content.

Practical application: a documentation site should be navigable by task ("how do I deploy"), by concept ("what is a pipeline"), by reference ("API for webhooks"), and by search. If your documentation only works by browsing a tree, you have failed the users who think in tasks.

#### 7. Focused Navigation Principle

Navigation is a promise. Every item in the navigation menu is a promise that the user can get there in one click. If you have twenty items in the main navigation, you have made twenty promises and the user has to evaluate all twenty to find the one they want. The navigation should reflect the primary task structure of the product, not the organizational chart of the team that built it.

Practical application: the main navigation should have no more than five to seven items. Anything else goes into a secondary menu, a search, or a context-sensitive action. If you cannot describe the primary tasks of your product in five to seven words, the product scope is too large.

#### 8. Growth Principle

The amount of content in a design will grow over time. Design for the version of your product that has ten times the features it has today. This does not mean building the structure for ten times the features; it means designing the information architecture so that growth does not break the navigation.

Practical application: use a flat structure with clear categories rather than a deep hierarchy. A flat structure with six top-level categories that each contain ten items is easier to navigate than a four-level hierarchy with three items per level. When a category grows beyond ten items, consider splitting it into sub-categories, but do not add a new level of hierarchy until you have to.

#### Applying the Principles to a Startup MVP

When you are building a minimum viable product, the UX principles are not optional. A confusing MVP kills the product before the feature set does. The customer who cannot figure out how to use the product does not care that the product has great features. They bounce.

The MVP test: can a new user, with no instructions, complete the primary task in under two minutes? If not, the UX is the problem, not the feature set. Simplify the interface, reduce the choices, make the primary action obvious, and test again.

#### Local LLM and UX

When using a local LLM to generate or review UI code, feed it the eight principles as a system prompt constraint. The model will produce interfaces that are more usable if you explicitly tell it to apply the choice principle (fewer options, well-organized), the disclosure principle (progressive disclosure), and the front door principle (every page is a valid entry point). Without the constraint, the model tends to generate interfaces that are feature-complete but cognitively overloaded.
