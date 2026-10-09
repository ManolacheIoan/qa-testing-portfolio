# pytest: fixtures and parametrize

## Fixture
Reusable setup/teardown. Code before `yield` is setup, code after is cleanup.
Tests receive it by naming it as an argument.

## parametrize
Runs one test with several inputs. Each input shows as a separate test in the report.
Good for boundary values: valid ids, ids just outside the range, very large values.

## Why it matters
- Less duplicated code
- A failing input is easy to spot
- Same idea as boundary value analysis, automated

## Practice
python-practice/api-testing/test_api_parametrized.py (10 test cases from 3 functions)
