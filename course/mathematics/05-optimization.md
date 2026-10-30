# Chapter 5 — Optimization and numerical thinking

## Minimize an objective

Optimization chooses parameter values to minimize or maximize an objective. In ML, the objective is often average loss over training examples plus regularization.

Gradient descent updates parameters:

    new_parameter = old_parameter - learning_rate × gradient

The learning rate controls step size. Too large can cause oscillation or divergence; too small can make progress very slow. Learning-rate schedules vary the step size during training.

## Batches and stochastic gradients

Full-batch gradient descent calculates gradients using all training examples each update. Stochastic gradient descent uses one example; mini-batch methods use a subset. Mini-batches reduce compute per update and introduce gradient noise, which can help or complicate optimization.

An epoch is one complete pass through the training data. A batch is the examples used for one update. These terms describe different scales.

## Loss landscape and local solutions

Neural-network objectives are usually non-convex: the loss surface can contain many valleys and saddle regions. Optimization typically seeks a useful low-loss solution, not a proof of the unique global minimum.

For a convex objective such as ordinary least squares under standard conditions, optimization has more useful global guarantees. Understand which assumptions your method relies on.

## Numerical issues

Floating-point numbers have finite precision. Very large or small values can cause overflow, underflow, or unstable calculations. Normalize inputs where appropriate, monitor loss, and use numerically stable library implementations.

## Questions and answers

**Why is the learning rate important?**  
It controls how far parameters move per update. The same optimizer can fail with a poor rate.

**What is mini-batch training?**  
Updating parameters from a subset of examples. It balances compute efficiency with a noisy estimate of the full-data gradient.

**Does lower training loss mean the system is better?**  
No. It can overfit. Evaluation on data not used for fitting or tuning is required.

**Why use a library optimizer?**  
Optimizers include tested details such as momentum and numerical handling. Learn the basic update first, then rely on reliable implementations for larger experiments.

## Practice and checkpoint

Use a simple quadratic loss and compare several learning rates. Plot loss by step. Explain why one rate diverges and another progresses slowly. Then relate that behavior to training loss curves in a neural network.