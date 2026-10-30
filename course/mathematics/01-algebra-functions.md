# Chapter 1 — Algebra, functions, and logarithms

> **Book-length subject volume:** For expanded explanations, worked examples, review questions, and practice, read the [mathematics textbook](TEXTBOOK.md).

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

## Why algebra appears in AI

A model calculates outputs from inputs using functions. Parameters control the shape of those functions. Training searches for parameter values that make predictions fit examples.

A simple line is y = wx + b. x is an input, y is a prediction, w is slope, and b is intercept. If w = 3 and b = 2, then input 4 gives prediction 14. The parameters w and b can be learned from data.

A feature is information about an example; a parameter is an internal value of the model. For house-price prediction, area is a feature and its learned coefficient is a parameter.

## Functions and graphs

A function maps each allowed input to an output. A graph helps see shape, range, and behavior. Linear functions change at a constant rate. Quadratic functions curve. Exponential functions change by repeated multiplication.

Domain means allowed inputs. Range means possible outputs. These ideas matter when a model is applied outside its training range. A model trained on houses from 30 to 200 square metres may behave unpredictably at 2,000 square metres.

## Powers and logarithms

Powers represent repeated multiplication. Logarithms answer: “To what power must this base be raised to get this value?” They appear in probability, information, and loss functions.

The logarithm turns multiplication into addition and compresses large ranges. In cross-entropy, log probability strongly penalizes assigning very small probability to the true answer. This makes a model learn not only the most likely class, but to avoid confident mistakes.

## Rearranging equations

If y = wx + b, then solving for w gives w = (y-b)/x when x is nonzero. Rearranging helps understand what a formula implies. In ML, formulas are often implemented by libraries, but algebra lets you inspect dimensions and assumptions.

## Worked example

Suppose a trip costs a fixed 5 units plus 2 units per kilometre. Cost(d) = 5 + 2d. The fixed part is the intercept; the per-kilometre rate is the slope. If trips at long distances systematically cost more than predicted, a straight-line model may be missing a relevant feature or curve.

## Questions and answers

**What does a model parameter mean?**  
It is a value the training procedure adjusts. Its practical meaning depends on the representation and data scale.

**Why look at a graph instead of only a formula?**  
A graph reveals nonlinearity, thresholds, extrapolation, and outliers that may be difficult to notice from a list of numbers.

**What is extrapolation?**  
Using a model outside the input range represented in training. Predictions may be mathematically defined but not reliable.

**Why do logarithms appear in ML loss?**  
They transform probabilities into a penalty that strongly discourages assigning near-zero probability to the correct outcome and make products easier to work with mathematically.

## Practice and checkpoint

Plot y = 3x + 2 and y = x² for several values. Explain which one grows faster for large x and why a model's predictions outside observed data deserve caution.