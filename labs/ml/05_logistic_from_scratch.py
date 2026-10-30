"""Lab 05: binary logistic regression with NumPy, not an ML library.

We fit weights to a tiny linearly separable two-feature dataset. A sigmoid
turns a linear score into a probability. Binary cross-entropy is minimized
with gradient descent so weights, loss, and gradients are visible.
"""

import numpy as np

X = np.array([
    [0.0, 0.0], [0.2, 0.1], [0.1, 0.4], [0.4, 0.2],
    [1.0, 1.0], [0.8, 1.2], [1.3, 0.9], [1.1, 1.4],
], dtype=float)
y = np.array([0, 0, 0, 0, 1, 1, 1, 1], dtype=float)


def sigmoid(scores):
    scores = np.clip(scores, -30.0, 30.0)
    return 1.0 / (1.0 + np.exp(-scores))


weights = np.zeros(X.shape[1])
bias = 0.0
rate = 0.2
n = len(y)

for step in range(3000):
    probabilities = sigmoid(X @ weights + bias)
    clipped = np.clip(probabilities, 1e-9, 1.0 - 1e-9)
    loss = -np.mean(y * np.log(clipped) + (1.0 - y) * np.log(1.0 - clipped))
    error = probabilities - y
    gradient_weights = X.T @ error / n
    gradient_bias = np.mean(error)
    weights -= rate * gradient_weights
    bias -= rate * gradient_bias

print(f"Final training cross-entropy: {loss:.4f}")
print("Learned weights:", np.round(weights, 3), "bias:", round(float(bias), 3))
for point in [np.array([0.1, 0.2]), np.array([1.0, 1.1])]:
    probability = float(sigmoid(point @ weights + bias))
    print(f"features={point.tolist()} positive_probability={probability:.3f}")

# Probability is not automatically calibrated. A threshold is a decision rule,
# not a property that makes one class universally correct. Try different
# thresholds and discuss the two types of classification error.
