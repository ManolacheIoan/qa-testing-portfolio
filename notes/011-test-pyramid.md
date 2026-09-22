# The Test Pyramid

## What it is
A model showing the ideal proportion of different test types in a project, based on speed, cost, and reliability.
    /\
   /UI\          <- few tests, slow, expensive, brittle
  /------\
 /  API   \       <- more tests, faster, more stable
/----------\

## The three layers

- **Unit Tests (base, most numerous)** — test individual functions/methods in isolation, no dependencies (DB, network, UI). Run in milliseconds, easy to pinpoint exactly where a bug is.
- **API/Integration Tests (middle)** — test how components work together (e.g. does the backend return the right response for a given request). Slower than unit tests, but still fast and stable compared to UI.
- **UI Tests (top, fewest)** — test the full system through the actual interface, like a real user would. Most realistic, but also slowest, most expensive to maintain, and most likely to break from small UI changes unrelated to actual bugs (flaky tests).

## Why the pyramid shape (not inverted)
If a team relies mostly on UI tests ("ice cream cone" anti-pattern), the test suite becomes slow to run and fragile — a small CSS change can break dozens of tests that have nothing to do with actual functionality. Relying more on unit and API tests catches most bugs faster and cheaper, while a thin layer of UI tests still verifies the system works end-to-end from the user's perspective.

## Connection to this portfolio
The CI/CD pipeline built in this repo (GitHub Actions + Playwright/pytest) currently sits at the UI layer of the pyramid. In a real project, these UI tests would typically be complemented by unit tests (testing backend logic directly) and API tests (e.g. via Postman/pytest hitting endpoints directly, without going through the browser) — which is exactly what the API testing practice in this repo (Postman collections) represents at the middle layer.
