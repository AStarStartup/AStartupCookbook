# AStartup Cookbook — Backlog Triage Plan (NOT executed)

Prepared 2026-10-03 by biz-master (kanban task t_c8272729).
49 open issues, #26–#109. **Ticket numbers and titles below that I could not independently read from this headless agent are marked `(verify)`; the Captain should confirm each title before the `Issue<N>` sequence is committed to.**

## Method
Each open issue is placed in one of three buckets:
- **(a) Rename / Overhaul** — the agentic-era rebranding: IDD/MDD → ADD, methodology naming, chapter/template reorganization. These are the "umbrella" missions that this task's file edits already implement.
- **(b) Content updates** — substantive new/changed book content (a principle added, a chapter filled in, a stub written, a section reworked).
- **(c) Stale / close** — duplicate, superseded-by-rename, or no-longer-wanted items to close (with a comment) rather than execute.

Recommended `Issue<N>` sequencing runs the rename/overhaul first (it is the base everything else references), then content updates in chapter order, and closes the stale items last (or first, if cheap) to shrink the 49.

## Bucket (a) — Rename / Overhaul (drive the rebrand)
| Ticket | Working title (from task brief) | Action |
|---|---|---|
| #100 | MDD → Agentic Driven Development rename | Execute — core rebrand; already done in this task's file edits. |
| #101 | Change `Dev/IDD`; delete `/d…` (stale path) | Execute — chapter rename + dead-path cleanup. |
| #102 | Rename GettingStarted, H1 | Execute — chapter H1/heading rename. |
| #103 | (verify) | Confirm title; likely a rename follow-on. |
| #104 | License rename | Execute — license/copyright wording per new brand. |
| #105 | (verify) | Confirm title. |
| #106 | DRY copyright | Execute — dedupe the License block across files. |
| #107 | (verify) | Confirm title. |
| #108 | (verify) | Confirm title. |
| #109 | (verify) | Confirm title. |
| #88 | (verify — the current branch) | The branch name implies an 88-scoped mission; per the Sync Plan its diff is too big to be one mission and must be split. |

**Note:** The rebrand is already reflected on disk (ADD rename, `MissionTickets.md`, template `Files Affected` fixes). Bucket (a) tickets become the `Issue<N>` vehicles that commit that work.

## Bucket (b) — Content updates (fill / rework the book)
| Ticket | Working title | Action |
|---|---|---|
| #47 | (verify — MDD/MissionTicket template update) | Likely template-driven; may fold into bucket (a). Confirm. |
| #60 | (verify) | Confirm. |
| #70 | (verify) | Confirm. |
| #78 | (verify) | Confirm. |
| #82 | (verify) | Confirm. |
| #85 | (verify) | Confirm. |
| #86 | (verify) | Confirm. |
| #87 | (verify) | Confirm. |
| #91 | (verify) | Confirm. |
| #95 | (verify) | Confirm. |
| #96 | UX.Add 8 basic UX design principles from Dan Brown (read in full, open, author AStarCale, 2024-08-31) | Content — add 8 UX principles to the Design/UX chapter. `### Files Affected` currently `?` → resolve to the UX chapter file before commit. |
| #98 | (verify — MDD/MissionTicket template update) | Confirm; may fold into bucket (a). |

The task brief groups #47/#60/#70/#78/#82/#85/#86/#87/#91/#95/#98 as "MDD/MissionTicket-template updates" — most are therefore candidates to **fold into the bucket-(a) rebrand** rather than stand alone, since the template itself is being rewritten now. Only keep them separate if each adds distinct content beyond the template rework.

## Bucket (c) — Stale / close (or supersede)
- Any issue whose only ask is "rename IDD→ADD" that is **duplicated** by #100 → close as duplicate of #100.
- The legacy **`Old Astartup Method @todo Fix me!`** section in `Dev/DevelopmentPatterns.md` (names "AStar Driven Development (or MDD)") is superseded by the new ADD section — close any issue tracking that old method as superseded, and remove/fold the section.
- The `ReadMe.md`→`README.md` rename work is already in flight on `Issue88`; any separate issue doing the same → close as duplicate.
- Confirm each `(verify)` ticket's title; the genuinely stale ones get a closing comment + close, not a commit.

## Recommended `Issue<N>` sequencing (Captain to confirm numbers)
1. **Phase 1 — Rebrand (bucket a).** #100 → #101 → #102 → #104 → #106, then the remaining confirmed rename tickets (#103/#105/#107/#108/#109). This lands the ADD naming everywhere first.
2. **Phase 2 — Templates (bucket a overlap).** #47/#98 (and any confirmed template tickets) to finalize `mission.md` + the rest against the new protocol.
3. **Phase 3 — Content (bucket b).** Chapter order: Design/UX (#96) first if the UX chapter is the gap, then the rest in the book's chapter sequence. Each resolves its `?` Files Affected before commit.
4. **Phase 4 — Cleanup (bucket c).** Close/supersede duplicates and the old-method section after the rebrand makes them redundant.

## What I could NOT resolve from this headless agent (needs the Captain)
- **I could not fetch the 49-issue list.** The search backend is search-only (no URL fetch) and the index had only #96. So titles for #100–#109 and most of bucket (b)/(c) are from the task brief or marked `(verify)`. **If you paste the 49 issue bodies (or hand me a PAT), I will fill the `(verify)` cells and lock the exact `Issue<N>` sequence.**
- **Ticket numbers for the Issue88 split** (Sync Plan Phase 2) depend on the real backlog numbers — confirm against the list above.
- **Which of the "template update" issues (#47/#60/#70/#78/#82/#85/#86/#87/#91/#95/#98) truly add content** vs. are just the rebrand — needs the bodies.

## No git operations performed.
This is a written plan only, per the task's hard constraints.
