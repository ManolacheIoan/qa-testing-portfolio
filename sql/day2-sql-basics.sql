-- Day 2: SQL basics (practice on sqliteonline.com)

CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  name TEXT,
  city TEXT
);

INSERT INTO users (id, name, city) VALUES
  (1, 'Ana', 'Iasi'),
  (2, 'Mihai', 'Bucuresti'),
  (3, 'Ioana', 'Iasi');

CREATE TABLE orders (
  id INTEGER PRIMARY KEY,
  user_id INTEGER,
  product TEXT,
  amount INTEGER
);

INSERT INTO orders (id, user_id, product, amount) VALUES
  (1, 1, 'Laptop', 3500),
  (2, 1, 'Mouse', 80),
  (3, 2, 'Tastatura', 150),
  (4, 99, 'Monitor', 900);

-- Filtering and sorting
SELECT name FROM users WHERE city = 'Bucuresti';
SELECT * FROM users ORDER BY name;

-- JOIN: only orders that have a matching user (order 4 is missing)
SELECT users.name, orders.product, orders.amount
FROM orders
JOIN users ON orders.user_id = users.id;

-- Orphan records: orders whose user does not exist (finds order 4, user_id 99)
SELECT orders.*
FROM orders
LEFT JOIN users ON orders.user_id = users.id
WHERE users.id IS NULL;

-- Aggregations
SELECT COUNT(*) FROM orders;
SELECT SUM(amount) FROM orders;
SELECT user_id, COUNT(*) AS orders_count FROM orders GROUP BY user_id;
SELECT user_id, SUM(amount) AS total FROM orders GROUP BY user_id;
