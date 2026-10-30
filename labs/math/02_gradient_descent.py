"""Lab 02: fit a straight line by gradient descent using plain Python.

The data follows approximately y = 2x + 1. The model predicts y_hat = w*x+b.
Mean squared error is the objective. Each step computes its gradient, then
moves parameters against it. This is the central optimization idea in neural
network training.
"""

xs = [0.0, 1.0, 2.0, 3.0, 4.0]
ys = [1.0, 3.0, 5.0, 7.0, 9.0]
weight, bias = 0.0, 0.0
learning_rate = 0.01
examples = len(xs)


def mean_squared_error(w, b):
    total = 0.0
    for x, y in zip(xs, ys):
        error = (w * x + b) - y
        total += error * error
    return total / examples


for step in range(2000):
    gradient_w = 0.0
    gradient_b = 0.0
    for x, y in zip(xs, ys):
        error = (weight * x + bias) - y
        gradient_w += 2.0 * error * x
        gradient_b += 2.0 * error
    gradient_w /= examples
    gradient_b /= examples
    weight -= learning_rate * gradient_w
    bias -= learning_rate * gradient_b

print(f"Learned weight: {weight:.3f} (target about 2)")
print(f"Learned bias:   {bias:.3f} (target about 1)")
print(f"Final MSE:      {mean_squared_error(weight, bias):.6f}")

# Experiments:
# - Change learning_rate to 0.5. Does training converge or overshoot?
# - Add noise to one target. What does the fitted line do?
# - Explain why low training error does not prove generalization.
