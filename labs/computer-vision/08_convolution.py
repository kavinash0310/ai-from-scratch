"""Lab 08: apply an edge-detection filter to a tiny grayscale image.

A kernel slides over local pixel neighborhoods. Each output is a weighted sum.
Many deep-learning libraries call cross-correlation “convolution”; in that
operation the kernel is not flipped.
"""

import numpy as np

image = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
], dtype=float)
kernel = np.array([
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1],
], dtype=float)

height, width = image.shape
kh, kw = kernel.shape
output = np.zeros((height - kh + 1, width - kw + 1), dtype=float)

for row in range(output.shape[0]):
    for col in range(output.shape[1]):
        patch = image[row:row + kh, col:col + kw]
        output[row, col] = np.sum(patch * kernel)

print("Input image shape:", image.shape)
print("Kernel shape:", kernel.shape)
print("Valid output shape:", output.shape)
print(output)

# Tasks: rotate the kernel 180 degrees and compare signs; add padding and
# derive output dimensions; explain why learned filters share weights; explain
# why a filter response is a feature and not proof that an object is present.
