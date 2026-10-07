---
layout: page
title: "Continuous Integration"
---

# [Astartup Cookbook](../)

## [Development](./)

### Continuous Integration

Continuous integration, CI, is the practice of automatically building and testing your code every time you push a change. The goal is to catch errors the moment they are introduced, not days later when the change is tangled with ten other changes and nobody remembers what broke.

For a solo founder running agents, CI is not optional. The agents write code faster than you can review it. If the only quality gate is "the founder looks at the code," the agents will produce more bugs than the founder can catch. CI is the quality gate that runs automatically, every push, every time, without the founder needing to remember to run it.

#### The CI Pipeline

A CI pipeline is a sequence of automated steps that run on every push to the repository. The standard pipeline has four stages:

1. **Lint** — check the code for style violations, unused imports, and common mistakes. This is the fastest stage and catches the most frequent errors. A linter runs in seconds and prevents the "I forgot to remove a debug print" class of bug.
2. **Build** — compile the code or install the dependencies. This catches syntax errors, missing dependencies, and version conflicts. If the build fails, nothing else runs.
3. **Test** — run the test suite. Unit tests, integration tests, and any end-to-end tests that can run in the CI environment. This is the stage that catches logic errors.
4. **Package** — build the deployable artifact: a Docker image, a binary, a wheel, a bundle. This stage only runs if the previous three pass. The artifact is tagged with the commit hash and stored in a registry.

Each stage must pass for the pipeline to be green. A red pipeline blocks the merge. No exceptions. If the pipeline is red, the code does not go to production, period.

#### CI as a TDD Tool

CI is the enforcement mechanism for test-driven development. TDD says: write the test first, watch it fail, write the code, watch it pass. CI automates the "watch it pass" part for every push. The agent writes code, pushes it, and the CI pipeline runs the tests. If the tests fail, the agent sees the failure and fixes the code. The agent does not need to run the tests locally; the CI pipeline is the test runner.

This works because the feedback loop is tight. The agent pushes, the pipeline runs in two to five minutes, the agent reads the result. The reward loop is the green checkmark. The agent reinforces the code patterns that produce green pipelines.

For ex post facto testing, where you add tests after the code is already written, CI is even more important. The tests are the specification. If you write the tests after the code, the tests define what "done" means, and CI verifies that the code meets the specification on every push.

#### Minimal CI for a Solo Founder

You do not need a complex CI setup. The minimum viable CI pipeline:

* A linter that runs on every push.
* A test suite that runs on every push.
* A build step that produces a deployable artifact.
* A branch protection rule that requires the pipeline to pass before merging to the default branch.

This is four lines of configuration in most CI systems. The linter catches style errors. The tests catch logic errors. The build catches packaging errors. The branch protection rule enforces that none of these errors reach the default branch.

#### CI with Local LLM

When running a local LLM as a coding agent, the CI pipeline is the agent's primary feedback mechanism. The agent does not need to run tests locally; it pushes and reads the CI output. This has two advantages:

1. **The agent does not burn local compute on tests.** The local machine is for editing and thinking, not for running the full test suite. The CI runner does the heavy lifting.
2. **The CI environment is deterministic.** The agent's local environment might have a different Python version, a different library version, a different OS. The CI environment is fixed, pinned, and reproducible. If the tests pass in CI, they pass everywhere.

The practical workflow:

1. The agent writes code and runs the linter locally (fast, immediate feedback).
2. The agent pushes the branch.
3. The CI pipeline runs lint, build, and test.
4. The agent reads the CI output.
5. If green, the agent opens a pull request.
6. If red, the agent reads the failure, fixes the code, and pushes again.

The agent loops until the pipeline is green. This is the reward loop: green pipeline is the reward, red pipeline is the error signal. The agent does not stop at the first push; it iterates until the CI is green.

#### Branch Protection

The single most important CI configuration is branch protection. The default branch (main, master) must not accept direct pushes. All changes must go through a pull request, and the pull request must have a green CI pipeline. This one rule prevents the entire class of "I pushed broken code to main" incidents.

For a solo founder, the branch protection rule is:

* Require a green CI pipeline before merging.
* Require the branch to be up to date with the default branch before merging.
* Do not allow force pushes to the default branch.
* Do not allow deletion of the default branch.

These four rules, configured in five minutes, prevent the majority of CI-related incidents.
