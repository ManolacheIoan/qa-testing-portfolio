# Day 5: Linux, grep and redirects

## Basic commands
- pwd: shows the current folder
- ls -la: lists files, including hidden ones
- cat: prints a file
- tail / head: show the last / first lines of a file
- wc -l: counts the lines in a file

## Searching logs
- grep ERROR file: shows only the lines containing ERROR
- grep -c: counts the matching lines
- grep -i: ignores upper and lower case

## Pipe and redirects
- | (pipe): sends the output of one command to the next
- > : writes output to a file and overwrites it
- >> : adds output to the end of a file

## Why it matters in QA
When a test fails in CI, the log can have thousands of lines. With grep I can
find the ERROR lines fast and save them to a file for the bug report.

## What I practiced
I created app.log and test.log, filtered the ERROR lines with grep, counted
them with grep -c and saved them to errors.txt with >.