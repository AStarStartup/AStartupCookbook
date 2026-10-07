---
layout: page
title: "Continuous Integration"
---

# [Astartup Cookbook](../)

## [Development](./)

### Continuous Integration

Continuous integration runs repeatable checks when changes enter the shared development workflow. Configure triggers and required checks explicitly; a green icon only describes the checks that actually ran.

#### Define the pipeline before copying configuration

Record the repository's runtime versions, dependency installation command, lint/check commands, test commands, build command (if any), triggers, timeouts, and artifact policy. Use the project manifest and lockfile; do not invent `npm test` or a build step for a documentation repository.

A practical order is dependency setup, fast static checks, relevant tests, then build or package if required. Some stages can run in parallel. Package publishing and production deployment are separate, approval-gated actions. Pin dependencies and keep runner permissions minimal. Untrusted pull requests must not receive production secrets.

#### TDD and existing code

For a new behavior or bug fix, run a focused test locally, observe the expected failure, implement the change, and rerun it plus relevant regression checks. CI repeats the passing checks in the runner environment; it does not replace observing the initial failure.

For code without tests, first characterize the current behavior and add regression coverage around the change. Tests written after implementation may preserve a bug, so compare them with the intended behavior and acceptance criteria. Passing tests are not the whole specification.

#### Agent feedback is not model training

An agent can read a failed test and revise its next attempt. Ordinary inference does not update the model's weights. A green test result is feedback in the current workflow, not reinforcement learning or evidence that a local model has learned permanently.

Run relevant local checks before a permitted push. Use CI for a clean environment, broader matrices, or expensive checks; it need not rerun every possible check for every edit. A pinned runner reduces variation but does not prove the software works on every platform.

#### Solo-founder quality gate

Start with the checks that catch your costly failure modes. For this book, [Documentation Checks](../Doc/DocumentationChecks.md) provides an offline gate. It is not a deployed CI pipeline or a Jekyll build.

Before relying on branch protection, inspect the actual rules: triggers, required check names, bypasses, and review requirements. Report missing enforcement to the owner rather than changing permissions yourself. A successful pipeline is not permission to merge.

#### Pipeline instruction template

```text
Repository and supported environments:
Triggers and paths covered:
Dependency installation and lockfile:
Local check commands:
Runner check commands and timeouts:
Expected artifacts (or none):
Required check names and authorized merge gate:
Permissions and secret restrictions:
Failure owner, logs, and recovery procedure:
Checks intentionally omitted and residual risk:
```

Verify a real successful run and a deliberately failing fixture or test before claiming the gate catches errors. Record the commit, command, exit status, and log location. Do not promise a universal duration, cost, or failure-prevention rate.
