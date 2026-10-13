# Newman: running Postman collections from CLI and CI

## Newman
Command-line runner for Postman collections.
newman run collection.json

## Lesson learned
Environment variables are not exported with the collection.
Running without base_url failed with ENOTFOUND {{base_url}}.
Fix: pass it on the command line:
--env-var "base_url=https://reqres.in"

## CI
.github/workflows/newman-api-tests.yml runs the collection on every push to main and on pull requests.

## Known gap
The login request has no assertions yet.
