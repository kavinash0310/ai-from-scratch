"""Lab 10: scaled dot-product self-attention with a causal mask.

Queries are compared with keys. Softmax turns scores into weights, then the
weights mix value vectors. A causal mask blocks future positions so a
next-token model cannot see the answer it is meant to predict.
"""

import numpy as np

X = np.array([[1.0, 0.0], [0.0, 1.0], [1.0, 1.0]])
Wq = np.array([[1.0, 0.0], [0.0, 1.0]])
Wk = np.array([[1.0, 0.0], [0.0, 1.0]])
Wv = np.array([[1.0, 0.2], [0.3, 1.0]])

Q, K, V = X @ Wq, X @ Wk, X @ Wv
scores = (Q @ K.T) / np.sqrt(K.shape[1])
future_positions = np.triu(np.ones_like(scores, dtype=bool), k=1)
scores = np.where(future_positions, -1e9, scores)

# Stable softmax subtracts the largest score before exponentiating.
scores -= np.max(scores, axis=1, keepdims=True)
weights = np.exp(scores)
weights /= np.sum(weights, axis=1, keepdims=True)
output = weights @ V

np.set_printoptions(precision=3, suppress=True)
print("Attention weights; each row is one query position:")
print(weights)
print("Row sums:", weights.sum(axis=1))
print("Output representation shape:", output.shape)
print("Future-position weights, which should be zero:")
print(weights[np.triu(np.ones_like(weights, dtype=bool), k=1)])

# Change X or projection matrices. Compare masked and unmasked results.
# Real Transformers repeat this across multiple heads and learned layers.
