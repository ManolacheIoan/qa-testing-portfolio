# Linux Basics for QA

## Why it matters
Many test environments, CI/CD runners (including the GitHub Actions pipeline in this repo), and server logs run on Linux. Being comfortable navigating a terminal and searching through logs is a core QA skill, not just a "nice to have."

## Core commands practiced

- `pwd`, `cd`, `ls` — navigation
- `touch`, `mkdir`, `echo >>` — creating files/folders, appending content
- `cat` — reading a full file
- `grep "pattern" file` — searching for matching lines (e.g. filtering error logs)
- `grep -c "pattern" file` — counting matching lines
- `tail -f file` — following a log file live, as new lines are written (essential for watching server logs while reproducing a bug in real time)
- `|` (pipe) — chaining commands, e.g. `cat file | grep "ERROR" | wc -l`
- `chmod +x script.sh` — making a script executable
- `wc -l` — counting lines

## Practical QA scenario
Given a server log (`server.log`) with mixed INFO/ERROR entries, the goal is to quickly answer "how many errors happened" without manually reading the whole file:

```bash
grep -c "ERROR" server.log
```

Or chained through a pipe:
```bash
cat server.log | grep "ERROR" | wc -l
```

## check_errors.sh
A simple bash script that automates this check — counts ERROR lines in `server.log` and prints the result. Demonstrates the full loop: writing a script, hitting a "Permission denied" error, understanding why (`ls -l` shows no execute permission), fixing it with `chmod +x`, then running it successfully.

```bash
#!/bin/bash
echo "Checking server.log for errors..."
ERROR_COUNT=$(grep -c "ERROR" server.log)
echo "Found $ERROR_COUNT errors."
```
