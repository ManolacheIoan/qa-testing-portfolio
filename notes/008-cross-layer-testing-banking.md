# Cross-Layer Testing & Applied EP/BVA (Banking Scenario)

Notes from Jira/Xray course (Section 4: QA Mindset/Strategy).

## Cross-Layer Verification (UI vs API vs Database)

When testing a displayed value (e.g. a bank account balance), never
trust the UI alone — it only displays whatever the backend sends it,
even if the backend's calculation is wrong.

**Three independent layers to check:**
1. **UI** — what's displayed on screen (e.g. "Balance: 1,500 RON")
2. **API** — the raw value returned by the backend
   (e.g. `GET /api/accounts/12345/balance` → `{"balance": 1500}`)
3. **Database** — the value calculated directly from source data
   (e.g. `SELECT SUM(amount) FROM transactions WHERE account_id = 12345`)

**Why this matters:** if all three layers agree, confidence is high.
If two layers disagree, the mismatch tells you exactly where the bug
lives:
- UI ≠ API → frontend bug (display/formatting issue)
- API ≠ Database → backend bug (calculation/business logic issue)

This combines skills learned separately (DevTools/UI testing, Postman
API testing, SQL queries) into a single cross-verification strategy.

## Applied EP/BVA — Banking Payment Scenario

Real-world example of applying Equivalence Partitioning and Boundary
Value Analysis (Module 4 techniques) to a financial domain, instead
of abstract examples.

**Balance boundaries (BVA):**
- Balance exactly enough to cover the payment (boundary: 0 remaining
  after transaction)
- Balance insufficient — payment should be rejected, not allowed to
  push balance negative
- Negative balance — should be an unreachable state; test explicitly
  that the system prevents it

**Display formatting (BVA on UI):**
- Very large amounts (8+ digits) — check the UI doesn't truncate
  incorrectly or break layout, and displays proper separators
  (e.g. 1,234,567.89)

**Card validation (Equivalence Partitioning):**
- Valid card → accepted
- Expired card → rejected, with a clear message
- Card with invalid number (failed checksum) → rejected
- Card with insufficient funds → rejected, with a message distinct
  from "invalid card" (different failure reason, different UX)

**Key takeaway:** these are not new techniques — they're the same
EP/BVA/Decision Table methods from Module 4, applied to a real
business domain (banking) instead of abstract examples (password
length, age). The reasoning process is identical; only the domain
changes.
