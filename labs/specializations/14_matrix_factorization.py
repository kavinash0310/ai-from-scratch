"""Lab 14: a tiny matrix-factorization recommender trained with SGD.

Observed ratings are decomposed into low-dimensional user and item vectors.
A rating estimate is their dot product plus global/user/item biases. We hold
out observed interactions by index to demonstrate an offline split; real
recommendation evaluation must also account for exposure and time.
"""

import math
import numpy as np

ratings = [
    (0, 0, 5.0), (0, 1, 4.0), (0, 2, 1.0), (0, 3, 1.0),
    (1, 0, 4.0), (1, 1, 5.0), (1, 2, 1.0), (1, 3, 2.0),
    (2, 0, 1.0), (2, 1, 2.0), (2, 2, 5.0), (2, 3, 4.0),
    (3, 0, 2.0), (3, 1, 1.0), (3, 2, 4.0), (3, 3, 5.0),
    (4, 0, 5.0), (4, 1, 3.0), (4, 2, 2.0), (4, 3, 1.0),
    (5, 0, 1.0), (5, 1, 2.0), (5, 2, 4.0), (5, 3, 5.0),
]
train = [row for i, row in enumerate(ratings) if i % 4 != 0]
test = [row for i, row in enumerate(ratings) if i % 4 == 0]
users = 6
items = 4
rank = 3
rng = np.random.default_rng(5)
user_factors = rng.normal(0, 0.1, size=(users, rank))
item_factors = rng.normal(0, 0.1, size=(items, rank))
user_bias = np.zeros(users)
item_bias = np.zeros(items)
global_mean = sum(r for _, _, r in train) / len(train)
learning_rate = 0.01
regularization = 0.02

for epoch in range(1500):
    rng.shuffle(train)
    for u, i, actual in train:
        old_user = user_factors[u].copy()
        old_item = item_factors[i].copy()
        prediction = global_mean + user_bias[u] + item_bias[i] + old_user @ old_item
        error = actual - prediction
        user_bias[u] += learning_rate * (error - regularization * user_bias[u])
        item_bias[i] += learning_rate * (error - regularization * item_bias[i])
        user_factors[u] += learning_rate * (error * old_item - regularization * old_user)
        item_factors[i] += learning_rate * (error * old_user - regularization * old_item)


def predict(u, i):
    raw = global_mean + user_bias[u] + item_bias[i] + user_factors[u] @ item_factors[i]
    return min(5.0, max(1.0, float(raw)))


rmse = math.sqrt(sum((predict(u, i) - r) ** 2 for u, i, r in test) / len(test))
print(f"Training interactions: {len(train)}; held-out interactions: {len(test)}")
print("Held-out RMSE:", round(rmse, 3))
print("Example user 0 ranking:", sorted(range(items), key=lambda i: predict(0, i), reverse=True))

# This toy data is tiny and synthetic. Real systems must compare a popularity
# baseline and handle implicit feedback, item exposure, freshness, and cold start.
