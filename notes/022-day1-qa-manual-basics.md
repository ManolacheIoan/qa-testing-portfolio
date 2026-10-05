# Day 1: QA manual basics

## Testing vs QA
- Testing: running the software to find defects and to check that it meets the requirements.
- QA: the process that prevents defects (planning, reviewing requirements, agreed rules).
- Example: reviewing an unclear requirement before coding is QA. Running the finished app is testing.

## The 5 stages of testing
1. Analysis: read the requirements and understand what correct behaviour is.
2. Design: write test cases (steps and expected result).
3. Execution: run the tests and record what happens.
4. Reporting: log defects with clear steps to reproduce.
5. Closure: retest fixes, check nothing else broke, summarise results.

## Test case
- Parts: ID, title, preconditions, steps, expected result (plus actual result and status when run).
- One test case checks one thing. Steps are actions, not observations.
- The expected result comes from the requirements, not from guesses.

## Bug report
- Parts: ID, title, environment, test data, preconditions, steps to reproduce, expected result, actual result, severity, priority, evidence, status.
- A good title says what is wrong and where. Steps must be clear enough for someone else to repeat them.

## Severity vs priority
- Severity: how serious the defect is for the product (set by the tester).
- Priority: how soon it should be fixed (set by the team, based on business needs).
- A typo on a company's home page: low severity, high priority.

## Equivalence partitioning and boundary value analysis
- Equivalence partitioning: group inputs that behave the same, test one value per group.
- Boundary value analysis: test the edges of each range.
- Example: password length 8-12. Classes: <8 invalid, 8-12 valid, >12 invalid. Boundaries: 7, 8, 9 and 11, 12, 13. Also test empty (0) and one value from the middle (10).

## Decision table
- Used when the result depends on a combination of conditions. N yes/no conditions give 2^N rules.
- Example: discount only if the customer has a loyalty card AND spends over 100. 4 rules, only one gives a discount.
- Combine with boundary values: what happens at exactly 100?

## State transition testing
- Test the valid transitions between states and try the invalid ones.
- Example: cart states Empty, With items, Paid. Valid: Empty to With items, With items to Paid, With items to Empty. Invalid: Empty to Paid.

## Types of testing
- Smoke: quick check that the main functions work, before deeper testing.
- Retest: verify that a specific fixed bug is really fixed.
- Regression: verify that a change or fix did not break what worked before.
- Exploratory: explore the app freely, without a script, to find unexpected problems.

## Practice done today
- Test cases TC-02 and TC-03 for the saucedemo login (empty password, empty username).
- BUG-01 and BUG-02 found with problem_user on saucedemo.com.
