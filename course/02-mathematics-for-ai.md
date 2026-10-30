# Part 2 — Mathematics for AI

## Chapter 8 — Numbers, algebra, and functions

Math in AI describes how inputs relate to outputs and how model parameters change. Begin by reviewing arithmetic, fractions, percentages, negative numbers, powers, and logarithms. Then practice rearranging equations, reading coordinate graphs, and understanding functions.

A function maps an input to an output. For example, f(x) = 3x + 2 takes x, multiplies by 3, then adds 2. A model is often a function with parameters that can be learned from data.

A linear model for house prices might be prediction = w₁ × area + w₂ × bedrooms + b. The input features are area and bedroom count; w₁, w₂, and b are parameters. The model's flexibility depends on the features and form we chose.

## Chapter 9 — Linear algebra: vectors and matrices

A scalar is one number. A vector is an ordered list. A matrix is a rectangular grid. A dataset with n examples and d features is commonly represented as an n-by-d matrix.

The dot product multiplies matching vector elements and sums them. It computes a weighted combination. Matrix multiplication performs many dot products at once; this is why it appears in neural networks and why GPUs accelerate it.

A vector's length and direction can be described geometrically. Distance and angle are useful for comparing examples, but the result depends on scale. If one feature is measured in dollars and another in years, distances can be dominated by dollars unless features are scaled appropriately.

A basis is a set of directions used to represent vectors. A change of basis changes coordinates, not the underlying object. Principal component analysis (PCA) finds directions that explain large variance under a linear projection; it does not automatically discover meaningful causes.

## Chapter 10 — Statistics and probability

Statistics summarizes samples and helps us reason about populations. Mean, median, quantiles, variance, and standard deviation describe different aspects of a distribution. Always plot and inspect data: one summary number can hide skew, outliers, or multiple groups.

Probability describes uncertainty. A random variable is a quantity whose value can vary. A conditional probability P(A|B) asks how likely A is when B is known. Bayes' rule connects prior belief, likelihood, and updated belief:

P(A|B) = P(B|A) × P(A) / P(B)

In a rare-event problem, even a strong detector can produce many false alarms because the negative class is much larger. Base rates matter.

An estimate from a sample has uncertainty. Confidence intervals describe a procedure's long-run coverage under assumptions; they are not a guarantee that a specific interval contains the true value. Randomization, sampling process, dependence, and measurement quality matter.

## Chapter 11 — Calculus and gradients

A derivative measures how much a function changes for a small change in input. The derivative of x² is 2x. At x = 3, a small change in x changes x² at about six times that change.

For many parameters, the gradient contains one derivative per parameter. The chain rule lets us calculate how changes pass through a composition of functions. Neural networks are compositions, so the chain rule can send error information backward from output to earlier layers.

## Chapter 12 — Optimization and the learning update

Gradient descent uses the gradient to reduce an objective. If loss is L(w), update w by w ← w − η × gradient(L), where η is the learning rate.

For linear regression with prediction y_hat = wx + b and mean squared error L = average((y_hat − y)²), the gradient points toward parameters that raise loss. Subtracting a small fraction of that gradient tends to reduce loss locally.

- Too-large learning rate: updates overshoot, bounce, or diverge.
- Too-small learning rate: training progresses slowly.
- Noisy mini-batches: updates fluctuate but can be efficient.
- Poor scaling: parameters may change at very different effective rates.

Optimization can reach a good solution without proving it is the only or global best solution. The objective may be non-convex, and model quality on training data may not reflect generalization.

## A diagram of model learning

    examples + targets
          ↓
    model makes predictions
          ↓
    loss measures prediction error
          ↓
    gradient estimates how parameters affect loss
          ↓
    optimizer updates parameters
          ↓
    repeat; evaluate on unseen examples

## Q&A

**Do I need to finish calculus before machine learning?**  
No. Learn the derivative and gradient intuition first, then practice calculations as models require them. The ML path can begin alongside gradual math study.

**What does a vector represent in a model?**  
It can represent one example's feature values, one learned parameter set, or an internal representation. The meaning depends on where it appears.

**Why scale features?**  
Many algorithms use distances or gradient-based optimization. Features with large numerical ranges can dominate even when their real importance is not greater.

**What does a probability of 0.8 mean?**  
It is the model's assigned probability under its training and calibration conditions. It does not guarantee correctness for this individual case. Check calibration on representative data.

**Why does gradient descent subtract the gradient?**  
The gradient points toward the direction of greatest local increase. Moving in the opposite direction tends to reduce the objective for a small enough step.