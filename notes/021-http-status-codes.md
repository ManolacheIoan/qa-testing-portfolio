# HTTP Status Codes for QA

## Why it matters
Every API test checks the status code first. Knowing what each range means helps decide whether a failure is a client problem, a server problem, or a bug.

## Ranges
- 2xx: success
- 3xx: redirect
- 4xx: client error (the request is wrong)
- 5xx: server error (the server failed)

## Codes used most in testing
- 200 OK: request succeeded
- 201 Created: a new resource was created (typical after POST)
- 204 No Content: success with no body (typical after DELETE)
- 400 Bad Request: invalid data sent
- 401 Unauthorized: not authenticated (missing or invalid credentials)
- 403 Forbidden: authenticated, but not allowed
- 404 Not Found: the resource does not exist
- 429 Too Many Requests: rate limit exceeded
- 500 Internal Server Error: unexpected server failure

## Testing tips
- A valid request should return 2xx; an invalid one should return a 4xx, not a 500.
- A 500 on bad input is usually a bug: the server should validate and answer 400.
- 401 vs 403: 401 means "who are you?", 403 means "I know you, but no".

## Seen in this portfolio
- 404 on a nonexistent user and 201 on POST in the Python API tests
- 429 rate limiting seen in the browser console on a live site (see bug-reports/)
