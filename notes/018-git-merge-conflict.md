# Git Merge Conflicts

## What causes a conflict
Two branches modify the same line of the same file, so Git cannot decide automatically which version to keep.

## What it looks like
- Between `<<<<<<< HEAD` and `=======`: the version from the current branch
- Between `=======` and `>>>>>>>`: the version from the branch being merged

## How to resolve
1. Open the conflicted file and decide which version to keep (or write a new one)
2. Delete the conflict markers
3. `git add <file>` to mark it as resolved
4. `git commit` to finish the merge

## Useful commands
```bash
git status                    # shows "both modified" files
git merge --abort             # cancel the merge and return to the pre-merge state
git log --oneline --graph     # visualize how branches were joined
```

## Practice
Reproduced in a throwaway repo: two branches (`colleague-a`, `colleague-b`) changed the same line of `status.txt` differently. Merging both into `main` triggered a conflict, resolved manually by keeping the FAILED status, then committed as a merge commit.

## In a real team
Do not just pick a version blindly: ask the colleague who wrote the other change, since the "right" answer depends on intent, not on Git.
