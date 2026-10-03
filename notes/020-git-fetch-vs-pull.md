# Git Fetch vs Pull

## git fetch
Downloads changes from the remote repository but does NOT merge them
into your local branch. Safe to run anytime — just updates your view
of what's on the remote.

```bash
git fetch origin
git log origin/main --oneline   # see what's new without merging yet
```

## git pull
Equivalent to `git fetch` + `git merge` in one step. Downloads AND
immediately merges changes into your current branch.

```bash
git pull origin main
```

## When to use which
- `git fetch` — when you want to see what changed before deciding to merge (safer in a team with active changes)
- `git pull` — the common shortcut when you just want to be up to date, which is what this portfolio's workflow has used throughout (`git pull origin main` before starting new branches)
