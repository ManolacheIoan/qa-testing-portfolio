# Testing Types: Functional vs Non-Functional

## Functional Testing
Verifies WHETHER the system does what it's supposed to do, according to requirements.
- Unit Testing — tests the smallest unit of code (a function/method), in isolation
- Integration Testing — tests how multiple components/modules interact with each other
- System Testing — tests the entire system end-to-end, as a whole
- Acceptance Testing (UAT) — verifies whether the system satisfies business/client requirements, usually performed by the client or by QA on their behalf

## Non-Functional Testing
Verifies HOW the system behaves (not what it does), under various conditions.
- Performance Testing — speed, response time under normal load
- Load Testing — system behavior under an expected load (e.g. 1000 concurrent users)
- Stress Testing — pushes the system beyond its limits, to see where/how it fails
- Usability Testing — how easy/intuitive the system is for the end user
- Security Testing — vulnerabilities, unauthorized access, injections, etc.

## Why the distinction matters
A system can pass 100% of its functional tests (does exactly what it should) and still be unusable in production — e.g. it's slow (performance), crashes at 50 users (load), or has a security hole. That's why a complete test plan covers both categories, not just functional.
