# Day 3: Python and pytest basics

## Variables and types
- A variable holds a value: str (text), int (whole number), float (decimal), bool (True/False).
- type() shows the type. str() converts a number to text so it can be joined with a string.

## Conditions
- if / elif / else. Comparisons: ==, !=, >, <, >=, <=. Combine with and, or, not.
- Indentation (4 spaces) defines the block. = assigns, == compares.

## Lists and loops
- A list holds several values, indexed from 0. for loops repeat code for each element.

## Functions
- def creates a function, return gives back a result. A test calls a function and checks the result.

## First pytest tests (python-practice/day3)
- validators.py: is_valid_password (8 to 12 characters, both included) and is_adult (18 or more).
- test_validators.py: boundary tests for password length (7, 8, 12, 13) and age (17, 18).
- Test names must start with test_. assert checks the result.

## Lesson: a test must be able to fail
- On a copy, I changed <= 12 to < 12. The boundary test for 12 characters failed (assert False is True), the other four passed.
- Boundary tests catch off-by-one bugs.
