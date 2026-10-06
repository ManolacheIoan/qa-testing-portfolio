# Day 2: API basics and first Postman tests

## What an API is
- Two programs talking: a client sends a request, a server sends a response.
- Request: method, URL, headers, body. Response: status code, headers, body (usually JSON).

## HTTP methods
- GET reads data, POST creates, PUT/PATCH update, DELETE removes.

## Status codes
- 2xx success (200 OK, 201 Created), 4xx client error (400, 401, 404), 5xx server error (500).

## JSON
- Key/value pairs in { }. Value types: number, string, array, object.
- When testing an API, compare fields and their types with what is expected.

## Practice done (jsonplaceholder.typicode.com)
- GET /posts/1: 200 OK, fields userId, id, title, body.
- GET /posts/9999: 404 Not Found, empty JSON (negative test).
- POST /posts: 201 Created, server adds id 101. The API only simulates, so GET /posts/101 returns 404.
- Postman tests: status code check, id check, title check in the POST response. Changed the expected value on purpose to see a test fail, then fixed it.

## Lesson
- A test that never failed does not prove it can catch a bug. Check that the test can fail.

## SQL basics (sql/day2-sql-basics.sql)
- Tables, rows, primary key, foreign key. SELECT, FROM, WHERE, ORDER BY.
- JOIN keeps only rows with a match. LEFT JOIN + WHERE ... IS NULL finds orphan records.
- Found an orphan order (user_id 99 does not exist in users): a data integrity defect to report, not to delete.
- COUNT, SUM and GROUP BY give totals per group.
