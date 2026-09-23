# SQL Basics for QA

## Why it matters
As a tester, you don't rely only on what the UI shows — the UI can mask a problem, or look correct while the underlying data is wrong. Querying the database directly confirms the ground truth, which is essential for cross-layer testing (UI/API/DB).

## Core concepts
Data lives in **tables** (like spreadsheets). Tables have **columns** (fields) and **rows** (individual records). Tables link to each other via keys (e.g. a `user_id` column in an `orders` table points to the `id` in a `users` table).

## SELECT — choosing columns
```sql
SELECT * FROM users;               -- all columns
SELECT name, email FROM users;     -- only specific columns
```

## WHERE — filtering rows
```sql
SELECT * FROM users WHERE email = 'test@example.com';
```

Comparison operators: `=`, `!=` (or `<>`), `>`, `<`, `>=`, `<=`

Combining conditions:
```sql
WHERE age > 18 AND country = 'Germany'
WHERE status = 'failed' OR status = 'cancelled'
WHERE NOT status = 'active'
```

## Special operators
```sql
WHERE email LIKE '%@gmail.com'              -- ends with
WHERE name LIKE 'John%'                     -- starts with
WHERE name LIKE '%john%'                    -- contains, anywhere

WHERE status IN ('pending', 'processing', 'failed')

WHERE created_at BETWEEN '2026-01-01' AND '2026-01-31'

WHERE phone_number IS NULL                  -- NOT "= NULL", must use IS NULL
WHERE phone_number IS NOT NULL
```

## ORDER BY and LIMIT
```sql
SELECT * FROM orders ORDER BY created_at DESC;   -- newest first
SELECT * FROM orders ORDER BY created_at DESC LIMIT 10;  -- last 10 only
```

## JOIN — combining tables
Real data is always spread across multiple tables. JOIN links them together.

**INNER JOIN** — only rows that match in both tables:
```sql
SELECT users.name, orders.order_id, orders.status
FROM users
INNER JOIN orders ON users.id = orders.user_id;
```

**LEFT JOIN** — all rows from the left table, even without a match on the right (useful for testing edge cases like users with no orders):
```sql
SELECT users.name, orders.order_id
FROM users
LEFT JOIN orders ON users.id = orders.user_id;
```

## GROUP BY and aggregate functions
```sql
SELECT status, COUNT(*) as total
FROM orders
GROUP BY status;
```
Aggregate functions: `COUNT()`, `SUM()`, `AVG()`, `MIN()`, `MAX()`

## Full example combining everything
```sql
SELECT users.name, orders.order_id, orders.status, orders.price
FROM users
JOIN orders ON users.id = orders.user_id
WHERE orders.status = 'failed'
  AND orders.created_at BETWEEN '2026-01-01' AND '2026-01-31'
ORDER BY orders.price DESC
LIMIT 20;
```
Translation: "Show me the name, order, status, and price for all failed orders from January 2026, sorted by highest price, top 20 only."

## Practical QA scenario
Bug reported: "User X says they paid, but the order still shows 'pending'."

Checking the DB directly:
```sql
SELECT id, status, payment_status, updated_at 
FROM orders 
WHERE user_id = 12345 
ORDER BY created_at DESC LIMIT 1;
```
If `payment_status = 'paid'` but `status = 'pending'`, this pinpoints exactly where the bug is: the payment was processed, but the order status was never updated — much stronger evidence for a bug report than "the user says...".

## Query writing order (logical, not always execution order)
SELECT what → FROM where → JOIN what it links to → WHERE what you filter → GROUP BY if aggregating → ORDER BY how you sort → LIMIT how many
