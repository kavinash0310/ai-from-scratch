"""Lab 01: Python values, collections, loops, and functions.

Run from the repository root:
    python labs/python/01_values_functions.py

Change the transaction data and predict the new totals before running again.
"""

transactions = [
    {"item": "notebook", "quantity": 2, "unit_price": 3.50},
    {"item": "pen", "quantity": 5, "unit_price": 0.80},
    {"item": "folder", "quantity": 1, "unit_price": 2.25},
]


def line_total(transaction):
    """Return quantity times unit price for one dictionary."""
    return transaction["quantity"] * transaction["unit_price"]


def summarize_orders(rows):
    """Use a loop and accumulator to calculate total and per-item costs."""
    total = 0.0
    by_item = {}
    for row in rows:
        cost = line_total(row)
        total += cost
        by_item[row["item"]] = cost
    return total, by_item


total, details = summarize_orders(transactions)
print("Cost by item:")
for item, cost in details.items():
    print(f"  {item}: USD {cost:.2f}")
print(f"Order total: USD {total:.2f}")

empty_total, empty_details = summarize_orders([])
print(f"Empty order total: USD {empty_total:.2f}; details: {empty_details}")

# Learner tasks:
# 1. Add a discount_percent field and apply it safely.
# 2. Reject negative quantities instead of charging a negative cost.
# 3. Explain the difference between printed output and a returned value.
# 4. Predict what changes if transactions is a tuple rather than a list.
