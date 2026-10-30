"""Lab 18: relational tables, joins, aggregation, and safe parameters.

SQLite is included with Python, so this lab needs no database server. The
example creates a tiny database in memory, joins orders to customers, and
uses a placeholder rather than concatenating user input into a query.
"""

import sqlite3

connection = sqlite3.connect(":memory:")
connection.execute("""
    CREATE TABLE customers (
        customer_id INTEGER PRIMARY KEY,
        name TEXT NOT NULL
    )
""")
connection.execute("""
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        customer_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        FOREIGN KEY(customer_id) REFERENCES customers(customer_id)
    )
""")
connection.executemany(
    "INSERT INTO customers(customer_id, name) VALUES (?, ?)",
    [(1, "Asha"), (2, "Ravi"), (3, "Noor")],
)
connection.executemany(
    "INSERT INTO orders(order_id, customer_id, amount) VALUES (?, ?, ?)",
    [(101, 1, 25.0), (102, 1, 10.0), (103, 2, 40.0)],
)
connection.commit()

rows = connection.execute("""
    SELECT customers.name, COUNT(orders.order_id), COALESCE(SUM(orders.amount), 0)
    FROM customers
    LEFT JOIN orders USING (customer_id)
    GROUP BY customers.customer_id, customers.name
    ORDER BY customers.name
""").fetchall()
for name, number_of_orders, total in rows:
    print(f"{name}: {number_of_orders} orders, total {total:.2f}")

# Bind values through placeholders. Do not build SQL by concatenating user text.
name = "Asha"
safe_rows = connection.execute(
    "SELECT order_id, amount FROM orders WHERE customer_id = "
    "(SELECT customer_id FROM customers WHERE name = ?)",
    (name,),
).fetchall()
print("Parameterized lookup:", safe_rows)
connection.close()

# Tasks: add a date column, filter by a date range, and explain why LEFT JOIN
# keeps a customer who has no matching order.
