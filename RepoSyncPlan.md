# AStartup Cookbook — Repo Sync Plan (NOT executed)

Prepared 2026-10-03 by biz-master (kanban task t_c8272729).
**The Captain drives all git/MDD commits; the human is the merge gate. Nothing in this plan was executed.**

## Situation (verified 2026-10-03)

- Local repo: `/home/astarcale/AStarStartup/AStartupCookbook/`
- Branch: `Issue88` (uncommitted working-tree diff: dozens of modified/deleted `.md`, all `.github/ISSUE_TEMPLATE/*.md` changed, `ReadMe.md`→`README.md` renames in progress).
- `origin` points at the OLD org (`CookingWithCale/...`), not `AStarStartup`.
- GitHub `AStarStartup/AStartupCookbook` default branch `master`, last pushed Dec 2022; local is AHEAD and unpushed.
- 49 open issues (#26–#109) drive the overhaul.
- This plan's own file edits (ADD rename + MissionTickets chapter + template fixes) sit uncommitted on top of the Issue88 working tree.

## Why the current state is wrong (three entangled problems)

1. **Wrong remote.** `origin` → `CookingWithCale` is the pre-2022 personal-namespace address. The live repo is `AStarStartup/AStartupCookbook`. Any push to `origin` today lands in the old org.
2. **Work sits on a branch whose ticket scope is already stale.** The uncommitted diff on `Issue88` spans the whole book (rename + README moves + template rewrites) — that is not one mission. Per the ADD protocol, one ticket = one coherent solution step; the `Issue88` diff is several missions stacked together, so it cannot be committed as a single honest `#88` sub-commit.
3. **Local is ahead of GitHub with no pushed history.** The last push was Dec 2022. Everything since is only local. If the machine dies, it is gone.

## Ordered plan (Captain executes; each step = one MDD commit on an `Issue<N>` branch)

### Phase 0 — Protect the work (no commit, no push)
1. Snapshot the current dirty state so nothing can be lost:
   - `git stash create` (records a dangling commit id) **and** `git diff > /tmp/issue88-diff.patch` + `git status --short > /tmp/issue88-status.txt`. Keep the patch file outside the repo.
2. Read the full `Issue88` working-tree diff and `git status` and note which files belong to which logical mission (this is the input to Phase 2).

### Phase 1 — Point `origin` at the real repo (remote config, NOT a push)
3. `git remote set-url origin https://github.com/AStarStartup/AStartupCookbook.git` (or the org's token-auth URL, e.g. `https://x-access-token:<GH_TOKEN>@github.com/AStarStartup/AStartupCookbook.git` — token never committed).
4. `git remote -v` to verify. **Do not push yet** — pushing now would ship the mixed Issue88 diff.
5. `git fetch origin` to bring down any remote refs since Dec 2022 and learn the true ahead/behind split (`git rev-list --left-right --count origin/master...HEAD`).

### Phase 2 — Re-baseline onto `master` and split Issue88 into honest tickets
6. `git checkout -b Issue<new> origin/master` — start each mission from the real published base branch, never from a stale local `master`.
7. **Decompose the Issue88 diff into per-mission working sets.** For each logical mission, stage only its files and commit on its own `Issue<N>` branch with the MDD grammar. Suggested first splits (numbers are the real ticket ids to be confirmed against the 49-issue backlog; see Backlog Triage Plan):
   - **`Issue88` → split** (the original diff was too big to be one mission):
     - Rename/branding batch → map to the rename/overhaul tickets.
     - `ReadMe.md`→`README.md` renames → their own ticket.
     - `.github/ISSUE_TEMPLATE/*.md` rewrites → template tickets.
   - Each becomes `#<N>.A`, `#<N>.B`, … on its own `Issue<N>` branch, in issue order, one coherent step per commit.
8. Update each mission ticket's `### Files Affected` to the real staged list (replace `?`) before committing that step.

### Phase 3 — Land the new ADD-overhaul work (this task's file edits)
9. Commit the ADD rename + `MissionTickets.md` + template reconciliation as their own mission(s) on `Issue<N>` branches (numbers per the triage table), base `origin/master`.
10. Each commit: `<title> #<N>.<Letter>`; stage only the files that mission touches; never the whole dirty tree.

### Phase 4 — Publish (Captain's call)
11. Push only the `Issue<N>` branches: `git push -u origin Issue<N>` (never `master`, never force).
12. Open a Pull Request per mission branch → `master`. Human verification is the merge gate; a green run is evidence, not permission.
13. After a mission is merged and closed, `git branch -d Issue<N>` **only** with explicit Captain authorization for that exact deletion.

## Guardrails (from `~/AStarStartup/AGENTS.md`)
- Verify `git remote get-url origin` belongs to `AStarStartup` before any remote write; a legacy/foreign owner is a hard stop requiring the Captain.
- No force-push, no rewriting published history, no merging, no direct pushes to the default/protected branch.
- No deleting branches/issues without explicit Captain authorization for the exact action.
- Stage explicit paths; avoid blanket staging while the worktree holds unrelated edits.
- Token lives only in the astartup profile's own `.env`; never in git config, the remote URL in a commit, source, or chat.

## Risks / unknowns (need Captain input)
- **Ahead/behind magnitude is unverified** (could not run `git rev-list` from this agent). Phase 1 step 5 resolves it; if local and `origin/master` have diverged on the same files, a reconcile/merge decision is needed before Phase 2.
- **The Issue88 diff's true scope is unverified line-by-line** here. Phase 0 step 2 is required before any commit so the split in Phase 2 is honest, not guessed.
- **Ticket numbers for the split missions must come from the 49-issue backlog** — see the Backlog Triage Plan for the recommended mapping.
