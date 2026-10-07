---
layout: page
title: "Workspace Structure"
---

# [Astartup Cookbook](../)

## [Getting Started](./)

### Workspace Structure

Your workspace is the root folder that contains every file you work on for your startup, your side projects, and your third-party dependencies. The folder structure is a mono-repo: one root, multiple workspaces, clear boundaries between what you own, what you collaborate on, and what you depend on.

#### The Three Tenses

The workspace uses three tenses to separate first-party, second-party, and third-party code:

1. **Workspace1 (first person)** — your company's code. Everything you own. The startup's product, its tooling, its documentation, its infrastructure. This is the folder you push to your company's GitHub organization.
2. **Workspace2 (second person)** — collaboration projects. Tutorials you are writing for someone else, a project you are contributing to as a guest, a joint venture with a partner. These are projects where you are not the sole owner but you are an active participant.
3. **Workspace3 (third person)** — dependencies. Libraries, frameworks, vendor code, anything you use but do not own. This folder is for reference and version pinning. You do not edit files in Workspace3; you pin them to a version and let the build system resolve them.

The naming is intentional: first, second, third. It maps to the grammatical tenses of ownership. You write in the first person. You collaborate in the second person. You consume in the third person.

#### Folder Layout

```
Workspace/
  Workspace1/
    astartup/              # company admin repo
    astartup.toolkit/      # product repos
    astartup.net/          # website
  Workspace2/
    tutorial.project/      # collaboration projects
    joint.venture/
  Workspace3/
    dependencies/          # vendored libraries
    references/            # documentation, specs
    tools/                 # build tools, CI runners
```

#### Why a Mono-Repo

A mono-repo, one root folder for all workspaces, has three advantages for a solo founder or a small team:

1. **One backup.** You back up one folder, not five scattered directories. If the drive dies, you lose one folder, not five.
2. **One search.** When you need to find a file, you search one root. `grep -r "pattern" ~/Workspace/` finds it regardless of which project it is in.
3. **Cross-project context.** When you are working on a feature in Workspace1 that depends on a library in Workspace3, the library is one `../` away. You do not need to clone it, symlink it, or remember where it lives.

The disadvantage is that the root folder can get large. The mitigation is to keep Workspace3 on a separate drive or a separate mount point if the dependencies are large (game engines, machine learning datasets). The code you write in Workspace1 should be small enough to live on the boot drive.

#### The Workspace Repo

Each workspace has a corresponding GitHub repository. The Workspace repo shares the name of the GitHub organization. For the AStartup organization, the Workspace repo is `AStarStartup/AStarStartup`. The Workspace repo contains:

* The administrative files for the organization: AGENTS.md, the kanban board configuration, the contributing guide.
* The session tickets: the daily development logs for every project in the organization.
* The coordination files: AGENT_PLAN.md, COORDINATION.md, any multi-agent task assignments.

The Workspace repo is not a product repo. It is the operating system for the organization. Product code lives in its own repo. The Workspace repo is where the agents and the founder coordinate.

#### Workspace and Local LLM

When running a local LLM, the workspace structure matters for context management. The agent should only see the files it needs for the current task. If the agent is working on a feature in `Workspace1/astartup.toolkit/`, it should not be reading files from `Workspace3/dependencies/` unless the task requires it.

The practical rule: the agent's working directory is the project folder, not the workspace root. `cd ~/Workspace/Workspace1/astartup.toolkit/` before starting the agent session. The agent sees the project, not the entire mono-repo. If the agent needs a file from Workspace3, you pass it explicitly: "Read `~/Workspace/Workspace3/dependencies/llama.cpp/README.md` for the build instructions."

This keeps the context window clean and the agent focused. The mono-repo is for your convenience as a human who needs to search across projects. The agent does not need the convenience; it needs the constraint.
