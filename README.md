# QA / Test Automation Portfolio

Hands-on QA / test automation practice — bug investigations, API testing,
SQL, test automation, CI/CD, and formal test design techniques, built
while training for a Junior QA / Test Automation role in Germany.

## Structure

- **bug-reports/** — real bugs found and documented on live sites,
  following a structured format (Environment, Steps to Reproduce,
  Actual/Expected Result, Severity, Evidence)
- **notes/** — deeper investigations and concept notes: API
  authentication behavior, Jira/Xray workflows, Linux basics, SQL
  basics, Docker basics, Git stash and merge conflicts, bug report
  anatomy, Severity vs Priority, the Test Pyramid, and Story Points
- **postman-collections/** — exported Postman collections used during
  API investigations
- **python-practice/** — API testing automation with `requests` and
  `pytest`
- **playwright-practice/** — UI test automation with Playwright,
  including Page Object Model, login and checkout flow scenarios
  mapped directly to the test plans below, and a documented
  exploratory testing session with confirmed bugs (via `xfail`)
- **sql-scripts/** — SQL practice covering JOINs, aggregation, and data
  integrity validation queries
- **test-cases/** — worked examples of formal ISTQB test design
  techniques (Equivalence Partitioning, Boundary Value Analysis,
  Decision Tables, State Transition Testing) and locator strategy
  examples for test automation (CSS Selectors, XPath, data-testid)
- **test-plans/** — written test plans for login and checkout flows
- **.github/workflows/** — CI/CD pipeline (GitHub Actions) running the
  automated Playwright test suite on every push

## Workflow

Every addition to this repo goes through a standard feature-branch
workflow: branch → commit → pull request → code review → merge —
matching real team practices rather than direct commits to `main`.

## Engineering foundations

Alongside this portfolio, I bring foundational coursework in C/C++ and
MATLAB/Simulink from my Engineering degree, in addition to the
hands-on Python-based QA/automation skills demonstrated here.

## About

Built by Ioan Manolache as part of a structured transition into
Software QA / Test Automation, targeting entry-level roles in Germany.
GitHub: [github.com/ManolacheIoan](https://github.com/ManolacheIoan)
