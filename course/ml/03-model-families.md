# Chapter 3 — Trees, ensembles, and other model families

> **Book-length subject volume:** For expanded explanations, worked examples, review questions, and practice, read the [ml textbook](TEXTBOOK.md).

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

## Decision trees

A decision tree asks a sequence of feature questions, splitting examples into regions. A shallow tree can be inspected as rules. A deep tree can memorize training data. Maximum depth, minimum leaf size, and pruning constrain complexity.

## Ensembles

A random forest trains many varied trees and averages their predictions. This reduces variance compared with one unstable tree, at the cost of less simple interpretation.

Gradient boosting builds weak learners sequentially, each focusing on residual errors from earlier learners. It performs strongly on many tabular datasets, but careful validation and tuning are needed.

## Distance and margin methods

k-nearest neighbors predicts using nearby training examples. Feature scales and distance choice strongly influence results; prediction may be expensive because many examples must be compared.

Support vector machines seek a boundary with a margin between classes. Kernels can model non-linear boundaries by calculating similarities in an implicit transformed space. They can be effective on small/medium datasets but require scaling and tuning.

Naive Bayes uses Bayes' rule with simplifying conditional-independence assumptions. It is computationally light and can provide a strong text baseline despite those assumptions being unrealistic.

## Choose for evidence

No family is always best. Compare on the same split with the same data handling. Consider latency, memory, interpretability, missing values, update frequency, and the quality of probabilities. Do not select based on training score alone.

## Questions and answers

**Why does a deep tree overfit?**  
It can create very narrow regions matching individual training examples, including noise.

**What does a random forest average?**  
Predictions from trees trained with varied data samples and feature subsets, reducing sensitivity to one tree's quirks.

**Is feature importance causal?**  
No. Importance describes model behavior under a method; correlated features can distort attribution and do not establish intervention effects.

**When might k-nearest neighbors be a poor choice?**  
With many dimensions, unscaled features, huge datasets, or expensive low-latency prediction.

## Practice and mastery

Compare a shallow tree, random forest, boosted trees, and a linear baseline on one tabular dataset. Keep the split fixed, inspect errors, and explain operational tradeoffs rather than reporting only a winner.