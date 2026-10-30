"""Lab 15: one GraphSAGE-like neighborhood aggregation step.

A graph stores entities as nodes and relationships as edges. Each node has a
feature vector. Message passing forms a new vector from the node and its
neighbors. This example only demonstrates aggregation; it does not train a
full graph neural network or establish that connected nodes are alike.
"""

import numpy as np

features = np.array([
    [1.0, 0.8], [0.9, 1.0], [0.8, 0.7],
    [-0.8, -1.0], [-1.0, -0.7], [-0.7, -0.9],
])
neighbors = [
    [1, 2], [0, 2], [0, 1],
    [4, 5], [3, 5], [3, 4],
]

updated = []
for node, adjacent_nodes in enumerate(neighbors):
    neighbor_mean = features[adjacent_nodes].mean(axis=0)
    # Combine self information with the average neighborhood message.
    updated.append(0.5 * features[node] + 0.5 * neighbor_mean)

updated = np.asarray(updated)
print("Original node-feature shape:", features.shape)
print("After one aggregation:", np.round(updated, 3))
print("Nodes 0-2 and 3-5 form two connected groups in this toy graph.")

# Tasks: remove an edge, add a misleading edge, or replace the mean with max.
# Explain how missing edges, noisy links, and graph-aware data splits can alter
# a learned node prediction.
