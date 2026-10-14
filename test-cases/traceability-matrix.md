# Traceability Matrix (example: login feature)

Links each requirement to the test cases that verify it and to the result.
It shows coverage: a requirement with no test case is a gap.

| Req ID | Requirement | Test case | Result |
|--------|-------------|-----------|--------|
| REQ-01 | A valid user can log in | TC-LOGIN-01 | Pass |
| REQ-02 | An invalid password shows an error | TC-LOGIN-02 | Pass |
| REQ-03 | A locked user cannot log in | TC-LOGIN-03 | Pass |
| REQ-04 | Empty fields show a validation message | TC-LOGIN-04 | Not run |
| REQ-05 | Session ends after logout | (none) | Gap |

## Why it matters
- Shows coverage per requirement
- Makes gaps visible (REQ-05 has no test)
- Standard practice in automotive validation, where each requirement must be traceable to a test
