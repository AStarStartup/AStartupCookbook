---
layout: page
title: "Workspace Structure"
---

# [Astartup Cookbook](../)

## [Getting Started](./)

### Workspace Structure

`Workspace1`, `Workspace2`, and `Workspace3` are this method's labels for first-, second-, and third-party material. They describe ownership and collaboration, not grammatical tenses, filesystem permissions, or a required Git topology.

* `Workspace1`: material your organization maintains.
* `Workspace2`: collaboration projects, tutorials, or other work where responsibility is shared.
* `Workspace3`: vendor code, dependencies, references, and tools with their own upstream owners.

A common root folder can contain independent Git repositories. That is a multi-repository workspace, not a monorepo. A monorepo stores multiple projects in one Git repository. The current AStarStartup workspace uses independent project repositories; verify the root and origin before each Git operation.

#### Illustrative layout

```text
Workspace/
  Workspace1/
    CompanyDocs/       # independent administrative repository
    Product/           # independent product repository
  Workspace2/
    Collaboration/    # agreed owner and remote
  Workspace3/
    VendorLibrary/    # reference or explicitly maintained fork
```

This is an example, not the literal AStartup Toolkit directory tree. Existing projects do not need a mass move to adopt the ownership labels. Large datasets or build caches can live on another drive with documented paths.

#### Boundaries

Keep administrative coordination and product history distinct. Discover the organization's actual coordination repository, session-log location, and board from its instructions; do not assume an organization always has a repository with the same name.

A workspace root helps search and backup planning, but one folder is not a backup. Test restoration and include data outside that root. Do not vendor or modify a dependency unless the project defines that policy; use its package manager, pinned upstream version, or an explicit fork.

#### Agents and local models

Start a task in the target project and pass only the relevant files. A working directory is not a security sandbox. Enforce filesystem, network, and tool permissions separately. Reading a shared dependency can be necessary; permission to read it is not permission to edit it.

See [Agent Operations](../Dev/AgentOperations.md) and [Context Window Engineering](../Productivity/ContextWindowEngineering.md).
