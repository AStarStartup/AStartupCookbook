---
layout: page
title: "AStartup Toolkit"
---

# [Astartup Cookbook](../)

## [Getting Started](./)

### AStartup Toolkit

The AStartup Toolkit is the companion to this cookbook. It is a collection of markdown templates, an MCP server, and a browser extension that together form the operating system for building a startup with AI agents.

#### What the Toolkit Does

1. **Markdown Templates** — pre-built templates for every common startup document: mission tickets, session tickets, business plans, customer interview guides, CI pipeline configs, deployment runbooks. The templates encode the best practices from this cookbook so you do not have to remember them.
2. **MCP Server** — a Model Context Protocol server that connects AI agents to the AStartup workspace. The agent can read issue tickets, update the kanban board, create branches, and run the CI pipeline through the MCP server. This is the bridge between the agent and the startup infrastructure.
3. **Browser Extension: AStartup Mission Control Center (MCC)** — a browser extension that shows the state of your startup at a glance. Open issues, active sessions, CI pipeline status, milestone progress. The MCC is the dashboard. You open it in the morning, see what the agents did overnight, and direct the next session.

#### How It Is Organized

```
AStartupToolkit/
  templates/
    mission_ticket.md       # Mission ticket template
    session_ticket.md       # Session ticket template
    business_plan.md        # Business plan template
    customer_interview.md   # Customer interview guide
    ci_pipeline.md          # CI pipeline template
    deployment_runbook.md   # Deployment runbook template
  mcp/
    server/                 # MCP server source
    config/                 # MCP configuration
  extension/
    src/                    # Browser extension source
    public/                 # Extension assets
  docs/
    README.md               # Toolkit documentation
    CONTRIBUTING.md         # Contribution guide
```

The templates folder is the most important part. Every template is a markdown file that you copy into your repo and fill in. The templates are DRY: one template for a mission ticket, not seven variants. If you need a different format, you fork the template and create your own variant in your repo.

#### Using the Markdown Templates

To use a template:

1. Copy the template file into your repo.
2. Rename it to match the naming convention: `CamelCase.md` for content files.
3. Fill in the placeholders. Every placeholder is in angle brackets: `<Problem>`, `<Solution>`, `<FilesAffected>`.
4. Remove any sections that do not apply to your use case.
5. Add the Jekyll front matter at the top.

The templates are starting points, not rigid forms. If a section does not make sense for your project, remove it. If you need a section that is not in the template, add it. The template encodes the minimum; your project defines the maximum.

#### The MCC and the Agent Loop

The MCC is the human's interface to the agent loop. The agents work autonomously during the day: they pick up issues from the kanban board, create branches, write code, run tests, open pull requests. The MCC shows the state of this loop:

* **Active sessions** — which agents are working, on which issues, for how long.
* **CI status** — which pull requests have green pipelines, which are red.
* **Milestone progress** — which milestones are complete, which are in progress.
* **Open issues** — the kanban board, sorted by priority.

In the morning, you open the MCC, review what the agents did overnight, merge the green pull requests, and set the direction for the day. In the evening, you review the day's work, update the session tickets, and set up the next three tasks for the morning.

The MCC does not replace the kanban board. It is a view of the kanban board plus the CI status plus the milestone progress. The kanban board is the source of truth. The MCC is the dashboard.

#### Local LLM and the Toolkit

The MCP server is designed to work with local LLMs. The agent runs on your machine, the MCP server runs on your machine, and the communication is local. No data leaves your machine. The agent reads the issue ticket, writes the code, runs the tests, and pushes the branch. The CI pipeline runs on your CI runner, which can also be local.

The advantage of a local setup: the context window is not consumed by network latency. The agent reads a file, processes it, writes a file, in milliseconds. The round-trip time is the speed of your NVMe, not the speed of the internet. For a solo founder running a small team of agents, this is the difference between a responsive workflow and a sluggish one.
