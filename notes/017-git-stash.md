# Git Stash

## Why it matters
Sometimes you need to switch branches urgently (e.g. to fix something on `main`) but have unfinished, uncommitted changes that would conflict. `git stash` temporarily sets those changes aside without committing them, so the working tree is clean and free to switch branches.

## Core commands

```bash
git stash              # set aside current uncommitted changes
git stash list          # view all stashed changes
git stash pop            # restore the most recent stash and remove it from the list
git stash apply          # restore the most recent stash but keep it in the list
git stash drop            # delete a stash without applying it
```

## Practical flow

1. Make changes to a file (uncommitted)
2. `git stash` — changes are set aside, working tree becomes clean
3. Switch to another branch freely, do whatever is needed
4. Switch back to the original branch
5. `git stash pop` — changes are restored exactly as they were, stash is removed from the list

## Real-world scenario
Working on a feature branch mid-task, an urgent bug needs fixing on `main`. Instead of committing half-finished work just to switch branches, `git stash` sets it aside cleanly, allowing a quick detour to fix the bug, then returning to pick up exactly where things were left off.
