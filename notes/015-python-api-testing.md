# API Testing with Python (requests + pytest)

## Why it matters
Manual API testing with Postman is useful for exploration, but automated API tests (using Python's `requests` library + `pytest`) are what most real QA/test automation roles expect — this sits at the middle layer of the Test Pyramid, complementing the UI tests already automated with Playwright in this repo.

## Core concepts

- `requests.get(url)` / `requests.post(url, json=payload)` — the main HTTP verbs used in testing
- `response.status_code` — the HTTP status returned (200 OK, 201 Created, 404 Not Found, etc.)
- `response.json()` — parses the response body into a Python dict/list, so individual fields can be checked directly

## Test structure
Each test follows the same shape as the Playwright/pytest UI tests already in this repo — a function starting with `test_`, using `assert` to verify expected behavior.

```python
def test_get_user_returns_200():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
```

## Testing both valid and invalid cases (EP/BVA applied to APIs)
A good API test suite doesn't just check the happy path — it also verifies the API fails correctly on bad input, the same Equivalence Partitioning / Boundary Value Analysis logic used for UI test design.

```python
def test_get_nonexistent_user_returns_404():
    response = requests.get(f"{BASE_URL}/users/99999")
    assert response.status_code == 404
```

## test_api.py
A small test suite (see `python-practice/api-testing/test_api.py`) covering:
- GET requests — verifying status code and response content on a valid user
- GET on a nonexistent resource — verifying a proper 404 is returned
- POST requests — verifying a resource is created (201) and the response contains the expected fields

Built against `jsonplaceholder.typicode.com`, a free fake API made for practicing exactly this kind of testing without any real backend risk.

Run with:
```bash
pytest test_api.py -v
```
