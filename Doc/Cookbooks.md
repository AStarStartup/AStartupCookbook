---
layout: page
title: "Cookbooks"
---

# [Astartup Cookbook](../)

## [Documentation](./)

### Cookbooks

A cookbook is a set of practical procedures with inputs, outputs, limits, and checks. It can help people and agents use a project, but usefulness must be tested rather than inferred from the number of pages.

#### Create an agent-readable cookbook

1. State the decisions and tasks it supports, the audience, and the boundary between advice and permission to act.
2. Organize each procedure around prerequisites, steps, a checkable result, failure handling, and a source record where facts depend on external evidence.
3. Use Markdown links and stable identifiers. Keep one canonical procedure and point related pages to it instead of copying slightly different rules.
4. Preserve author notes as notes. Mark incomplete pages `status: draft`, distinguish examples from findings, and never fabricate case studies to make the outline look finished.
5. Test links, metadata, worked calculations, and executable recipes. See [Documentation Checks](./DocumentationChecks.md). An offline check is not a factual audit or a rendered-site build.
6. Ask an agent to use one procedure on permitted test inputs and explain the result to a human. Record what it misunderstood, then fix the procedure.

If adapting existing material, confirm the permitted use and ownership before copying or publishing it; ask the owner and `attorney` when unclear. Public access does not establish permission to sell derivative work or change its terms. Do not delete a source checkout's `.git` history or mass-rename every file as a quickstart shortcut.

The companion [AStartup Toolkit](../GettingStarted/AStartupToolkit.md) contains documentation templates. Inspect the actual template and its current build instructions rather than assuming a model file or editor extension exists.
