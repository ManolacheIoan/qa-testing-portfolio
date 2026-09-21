# Testing Life Cycle, RTM & Defect Troubleshooting

Notes from Jira/Xray course (Sections 6-7).

## Why Testing Life Cycle exists

The structured process exists to reduce business risk — so a company
doesn't ship an expensive product that turns out to be broken. A
disciplined process, not luck, is what prevents that.

## Testing Life Cycle — phases

1. **Requirement Analysis** — understand how the final product should
   behave, before writing any tests
2. **Test Planning** — decide strategy: tools, automation coverage,
   timeline, risks
3. **Test Case Development** — write test cases, one or more per Story
4. **Test Environments** — code goes to a server, becomes accessible
   via URL; QA deploys to a separate environment (own database,
   isolated from production)
5. **Test Execution** — run the planned steps
6. **Test Closure** — confirm all planned tests are done, verification
   complete

## Requirement Traceability Matrix (RTM)

Maps each business requirement to the test case(s) that verify it:

| Requirement | Test Cases |
|---|---|
| Req1 | TC1, TC2 |
| Req2 | TC3 |
| Req3 | TC4 |

Purpose: confirm no requirement is left untested. A requirement with
no linked test case is a coverage gap.

## Negative Tests

Tests that verify behavior on invalid/disallowed input — the "invalid"
side of Equivalence Partitioning (Module 4), not just the happy path.

## Defect Troubleshooting — investigating before reporting

Before writing a bug report, gather evidence:
- **Network tab, Console log** (Module 1 skills, directly applicable)
- **App server log** — backend-side logs, useful when the root cause
  isn't visible from the browser alone
- **Timestamp** — exact time of the issue, for correlating with server
  logs
- **Troubleshoot thoughts** — notes on what was tried/ruled out, so
  the developer doesn't repeat the same investigation
- **Screenshots** — visual evidence (never include cookies/tokens)

## Retesting vs. Regression Testing

Two different activities that both happen after a fix:

- **Retesting (Confirmation Testing)** — re-run the exact test that
  originally failed, to confirm that specific bug is gone
- **Regression Testing** — check OTHER functionality that appeared
  unrelated, to confirm the fix didn't break something else

Example: a login fix could unexpectedly break logout — regression
testing catches this kind of unrelated side effect that retesting
alone would miss.
