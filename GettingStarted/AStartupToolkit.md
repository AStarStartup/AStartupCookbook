---
layout: page
title: "AStartup Toolkit"
---

# [Astartup Cookbook](../)

## [Getting Started](./)

### AStartup Toolkit

The cookbook explains procedures. Companion projects provide templates and interfaces. Do not assume a feature is implemented because a chapter or issue describes it.

#### Components and evidence

| Component | Role | What to verify before relying on it |
|---|---|---|
| [AStartup Toolkit](https://github.com/AStarStartup/AStartupToolkit) | Markdown documentation templates and a Jekyll documentation site | Current README, template files, layout dependencies, installation steps, and project terms |
| [AStartup Mission Control Center](https://github.com/AStarStartup/AStartupMCC) (MCC) | Companion browser extension; its repository also contains a separate OBS plugin project | Extension manifest, implemented screens, permissions, tests, and release/installation status |
| MCP integration | Proposed agent interface in the Toolkit planning material and cookbook issue #26 | Actual server implementation, launch command, tool schemas, authentication, permissions, and an exercised tool call |

The inspected Toolkit checkout contains `Templates/App/RAD`, `Templates/App/SDD`, `Templates/Game/GDD`, `Templates/BMC`, and UX material. Those are template families, not proof that every startup document or automation exists. The former `templates/`, `mcp/`, and `extension/` tree in this chapter was not the inspected layout.

Do not describe active-session dashboards, issue writes, CI control, or automatic overnight execution as released MCC/MCP features without verifying them. An intended companion is not a tested deployment.

#### Use a template without copying its assumptions

1. Read the chosen template and its project's current instructions. Check permitted use with the owner or `attorney` if the terms are unclear.
2. Copy only needed content into an authorized destination. Keep the source repository and its Git history intact; do not delete `.git` to make an existing checkout into a new project.
3. Replace placeholders with evidence or clearly labeled assumptions. A generated persona is a scenario, not an interview finding.
4. Software templates cover requirements and design; game templates cover game design. For hardware, explicitly add safety, physical constraints, bill of materials, manufacturing, and test requirements. Do not claim a hardware template exists until you locate it.
5. Retain useful document structure, adapt metadata to the target site, and run that repository's checks. Toolkit layouts may not be named `page`; cookbook front matter is not a universal Jekyll contract.

#### Startup syndication handoff

For an agent or collaborator to find a startup's records, maintain a compact index: organization/repository identifiers, mission, current decision, canonical evidence paths, owner, permissions, and last verification date. Link to the source records rather than copying customer data into several dashboards. This is a proposed handoff format, not a claim about an implemented MCC protocol.

#### Locality and permissions

Local inference can reduce exposure of the prompt, but browser extensions, GitHub APIs, hosted models, telemetry, and remote CI may send data off-machine. Network latency does not consume context tokens. Evaluate latency, token usage, privacy, and permissions separately.

Use [Local LLM Tasks](../Dev/LocalLLM.md) for a read-only workflow. Grant tool access only after inspecting the actual server and testing its limits; a model is not given filesystem or production authority by mentioning MCP in a prompt.
