"""Lab 07: train a tiny neural network on XOR with NumPy.

XOR returns 1 when its binary inputs differ. One linear boundary cannot solve
it. The two-layer network below uses tanh in a hidden layer and sigmoid at
the output. It performs forward propagation, backpropagation, and updates.
"""

import numpy as np

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]], dtype=float)
y = np.array([[0], [1], [1], [0]], dtype=float)
rng = np.random.default_rng(3)
W1 = rng.normal(0, 0.7, size=(2, 4))
b1 = np.zeros((1, 4))
W2 = rng.normal(0, 0.7, size=(4, 1))
b2 = np.zeros((1, 1))


def sigmoid(z):
    z = np.clip(z, -30.0, 30.0)
    return 1.0 / (1.0 + np.exp(-z))


rate = 0.5
for step in range(12000):
    hidden = np.tanh(X @ W1 + b1)
    probabilities = sigmoid(hidden @ W2 + b2)

    # Mean squared error keeps the derivative walkthrough compact.
    error = probabilities - y
    d_output = (2.0 / len(X)) * error * probabilities * (1.0 - probabilities)
    dW2 = hidden.T @ d_output
    db2 = np.sum(d_output, axis=0, keepdims=True)

    # Chain rule carries the output gradient back through tanh and layer one.
    d_hidden = (d_output @ W2.T) * (1.0 - hidden**2)
    dW1 = X.T @ d_hidden
    db1 = np.sum(d_hidden, axis=0, keepdims=True)

    W1 -= rate * dW1
    b1 -= rate * db1
    W2 -= rate * dW2
    b2 -= rate * db2

hidden = np.tanh(X @ W1 + b1)
probabilities = sigmoid(hidden @ W2 + b2)
print("XOR inputs and predicted probabilities:")
for row, probability in zip(X.astype(int), probabilities[:, 0]):
    print(row.tolist(), "->", round(float(probability), 3))
print("Predicted classes at threshold 0.5:", (probabilities[:, 0] >= 0.5).astype(int))

# This tiny dataset demonstrates a mechanism, not generalization. Vary hidden
# width, initialization, learning rate, and activation; draw the computation graph.
