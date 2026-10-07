---
layout: page
title: "Documentation Checks"
---

# [Astartup Cookbook](../)

## [Documentation](./)

### Documentation Checks

The offline checker verifies the source Markdown, not the truth of every sentence. Run it before submitting book edits and retain its output with the review.

#### Setup and commands

From this repository, use Python 3.10 or later and an isolated virtual environment. The requirements pin the parsers used by the gate. Do not overwrite an existing environment without checking it.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r tools/requirements.txt
.venv/bin/python -m unittest discover -s tools -p 'test_*.py' -v
.venv/bin/python tools/check_docs.py .
.venv/bin/python tools/check_docs.py . --json
.venv/bin/python tools/check_docs.py . --strict-content
```

On Windows use the environment's `Scripts/python.exe` instead of `.venv/bin/python`. A normal run fails on structural errors or unmarked incomplete content. It reports declared drafts but allows a clearly labeled draft book. `--strict-content` additionally fails while any draft/incomplete page remains; that is a publication-readiness check, not a reason to remove honest draft markers.

#### Scope

The checker parses `.md` files, including GitHub issue templates, while skipping Git internals, virtual environments, dependencies, build output, and bytecode caches. It checks:

* YAML front matter with an exact closing delimiter and no duplicate keys; content pages need `layout: page` and a nonempty string `title`.
* Closed code fences, so an unclosed example cannot silently hide later links.
* Relative Markdown links and images, including reference-style destinations and encoded paths. Case checking follows the host filesystem; run on a case-sensitive filesystem before publishing.
* Links to Markdown heading fragments using GitHub-style IDs, including duplicate headings. Directory fragments resolve to `README.md` or `index.md` when present.
* Local destinations that escape the repository, including symlink targets.
* Obvious unfinished prose or empty outlines that need `status: draft`.

Root `README.md`, `AGENTS.md`, `BacklogTriagePlan.md`, `RepoSyncPlan.md`, and `license.md` are utility exceptions to the page-layout rule. GitHub issue templates retain GitHub metadata rather than becoming Jekyll pages. Both sets are still checked for parseable metadata and local Markdown links.

Examples inside code fences are not treated as live links or research findings. JSON output includes file and link counts, draft paths, errors, and warnings. Exit status zero means the selected structural gate passed, not that a startup task has been completed.

#### What it does not prove

It does not fetch external URLs, inspect embedded HTML link destinations, evaluate Liquid templates, certify legal or financial conclusions, assess complete coverage of a topic, or prove customer demand. It is not a Jekyll build. A hosting configuration can generate different URLs or heading IDs; test the actual rendered site separately before publishing it.

A page without `status: draft` is not automatically fact-checked. Read new factual claims against their primary evidence. For source changes, record the source, claim, relevant excerpt, and retrieval limits. Recalculate every worked example with units and assumptions. Preserve author notes without presenting them as verified benchmarks.

Executable recipes need syntax checks, failure-path checks, and a real run on an appropriate environment before claiming they work there. If a runtime, dependency, or input is unavailable, report that limitation rather than fabricating output.

#### Change discipline

Run the baseline and current gate when reviewing a large change. Keep known draft findings visible instead of filling gaps with generic text. Check the diff for scope and provenance, then hand off results to the authorized integration owner. Do not add remote CI configuration, change branch protection, commit, push, or close issues merely because the offline check passes.
