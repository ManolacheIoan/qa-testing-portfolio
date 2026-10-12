# Day 7: Merge conflicts

## What I learned
- A merge conflict happens when two branches change the same line of the same file.
- Git stops the merge and marks the file with `<<<<<<<`, `=======` and `>>>>>>>`.
- The part between `<<<<<<<` and `=======` is the current branch (HEAD); the part between `=======` and `>>>>>>>` is the branch being merged.
- `git status` shows "both modified" for files with a conflict.
- `git merge --abort` cancels the merge if I want to start over.

## How I resolved it
1. Opened the file and decided what the final text should be.
2. Removed the markers and saved the final content.
3. `git add <file>` to mark it as resolved.
4. `git commit -m "..."` to finish the merge.
5. `git log --oneline --graph` to check the two branches joined.

## Rule
Always read both sides of the conflict before choosing. Never delete a side without checking what it does.
