# Day 6: Git history and diff

## What I learned
- `git log --oneline` shows the commit history in one line per commit.
- `git show --stat HEAD` shows which files the last commit changed.
- `git diff` shows unstaged changes; `git diff --staged` shows what is already added.
- `git add` takes a snapshot, so later edits need another `git add`.
- `.gitignore` keeps files like `.pytest_cache/` and `.venv/` out of the repo.

## Mistake and fix
I committed on `main` instead of the feature branch. Fix:
1. `git branch -f day6/git-history main`
2. `git reset --hard origin/main`
3. `git checkout day6/git-history`
4. `git push`

## Rule
Run `git branch` before every `git add`. Never commit on main.
