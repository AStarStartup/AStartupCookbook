---
layout: page
title: "Pre-push Review"
---

# Pre-push Review — 2026-10-07

## Decision

Hold publication as a complete, reference-grade cookbook. The reviewed decision/agent guides and offline checks are ready for the Captain's review, but the book still contains 89 declared draft or incomplete pages. A clearly labeled working-draft release is a different decision from claiming the book or all tickets are finished.

This replaces the earlier generated Morning Briefing. Its blanket “all 37 issues addressed” and repository-wide “zero broken links” claims were not supported by adequate acceptance checks. No overnight execution is claimed.

## What changed

* Added the canonical problem–solution procedure in `Engineering/ProblemSolving.md`: rules, evidence, competing causes, winning condition, do-nothing/manual/buy/build options, scenarios, founder capacity, experiments, stop rules, and implementation handoff.
* Added a copyable decision record and a clearly hypothetical worked example. The base case has USD 516/month operating cash balance but USD -44/month after the stated founder opportunity cost. The arithmetic is covered by executable tests; it is not customer evidence or a startup forecast.
* Connected customer interviews, market validation, mission tickets, and the README agent entry point to that procedure. The original Lab-2-Market/EA Partners phone-interview notes remain verbatim and explicitly historical.
* Retained the founder's case-study narrative and added the Fertilab/Eugene interviews, composition book, missing-collaborator history, and resumed-book goal supplied by the author. No interviews, quotations, clinical findings, or study results were invented.
* Corrected unsupported forgetting/productivity/model-size prescriptions, feedback-versus-training claims, trademark terminology/anecdote, information-architecture attribution, and fictional Toolkit/MCP/extension capability claims. New source-derived explanations have citations and an evidence ledger; unreviewed legal material remains draft and legal conclusions go to `attorney`.
* Removed unsafe blanket staging, shared-branch deletion, and automatic-merge instructions. Local repository rules and distinct permissions govern edits, commits, pushes, launches, payments, and outreach.
* Fixed chapter navigation beyond the root README and misleading page titles. The initial parsed-link sweep found 143 missing targets in 22 files; nonexistent chapters were not fabricated simply to make a link check green. Most widespread page changes are one-line draft markers, not content rewrites.
* Added `Dev/LocalLLM.md`, `Doc/DocumentationChecks.md`, pinned parser requirements, a read-only offline checker, and regression tests.

## Executed verification

The isolated environment was created in the active profile's scratch area, not in another profile or the project. `tools/requirements.txt` was exercised with the installed environment.

```text
python -Werror -m py_compile tools/check_docs.py tools/test_check_docs.py tools/test_business_example.py
  exit 0
python -Werror -m unittest discover -s tools -p 'test_*.py' -v
  exit 0; 13 tests passed
python -Werror tools/check_docs.py .
  exit 0; 198 Markdown files; 780 local links; 0 structural errors; 89 draft/incomplete files
python -Werror tools/check_docs.py . --strict-content
  exit 1; expected failure because 89 draft/incomplete pages remain
git diff --check
  exit 0
```

The checker covers YAML/front matter, duplicate keys, closed fences, parsed local Markdown links/images, source heading fragments, repository boundaries including symlinks, and declared draft status. Its fixtures were observed failing before the relevant checker fixes. No independent subagent code review ran for the new helper scripts; delegation is not exposed in this profile. These are this model's review plus automated checks, not an independent-review stamp. It does not fetch external URLs, check embedded HTML destinations, certify factual correctness, or build the rendered site. Case checking follows the filesystem.

Six source-bearing pages passed citation/evidence-mapping verification. That verifies citations and attached source excerpts, not every recommendation or legacy sentence. The information-architecture publisher was blocked; the reproduced article was read and its provenance disclosed. The attention and learning discussion is limited to the retrieved abstract/review summary.

The actual Ollama recipe passed Python and Bash syntax checks. Its unavailable-runtime path was executed and exited 1 with `Connection refused`. Neither Ollama nor llama-server was installed/reachable in this environment. No successful inference, model-quality test, cloud/privacy guarantee, or simulated customer result is claimed. No Jekyll build or deployed CI run occurred. Ruff and Pyright executables were unavailable; tool edit diagnostics and warning-as-error compilation were used, not a standalone full type/lint run.

Git reports a CRLF-to-LF warning for `.gitignore`; its diff is the addition of `.venv/`, not a wholesale formatting change. The canonical `license.md` is unchanged by this review. One root README notice remains; no per-page notices were reintroduced.

## Open decisions and issue acceptance

The refreshed public API still lists 37 open non-PR issues, with no issue-body changes since the review read. `Doc/issue_review.csv` records each actual issue number/title, related content, remaining verification, and the recommendation to leave it open pending owner acceptance. This is a provisional review matrix, not automatic acceptance or a closure payload.

The Captain must resolve the conflicting/evolving bootstrap numbering in #87/#91. Use actual issue links until then; do not assume a Questions record is always #13. Toolkit/MCP/MCC feature claims in #26/#103/#108 still need actual implementation and runtime verification. The earlier canonical-license source URL/use terms in #101 need the owner and `attorney`, not an inferred legal conclusion.

Prioritize completion of the draft business-model, money-management, and operating material after the core decision guide. Add sourced procedures and auditable examples rather than generic filler. Do not remove draft markers to force a strict pass.

## Git and publication boundary

The local branch remains `Issue172`; HEAD remains `1fdd3a672d9faa87b85964277e00044cea5295f5`. The index is empty and review changes are unstaged/uncommitted. This review did not create a commit, amend/rebase/reset history, push, merge, deploy, change a board, or close an issue.

The live remote read reports `master` at `6a61d22e8a716fb3c8d4991543f47f67fdecf049` and no advertised `Issue172` branch. The earlier implementation commit was not confirmed through the public API. Do not assume stale remote-tracking refs describe publication state or that this old branch is the right integration base. The authorized integration owner should compare it with the live base before any commit/push.

Publication remains a separate approved action. The useful result of this review is a more reliable core and a visible boundary around unfinished material, not a green badge for the whole startup handbook.

