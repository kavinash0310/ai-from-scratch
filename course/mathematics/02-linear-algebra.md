# Chapter 2 — Vectors, matrices, and geometry

## Represent many numbers together

A scalar is one number. A vector is an ordered list of numbers. A matrix is a grid. A tensor generalizes arrays to multiple dimensions.

If a dataset has 100 examples and 4 numeric features, it can be represented as a 100-by-4 matrix X. Row i describes one example. Column j contains one feature. A target vector y contains the desired output for each row.

Shape matters: adding a 100-by-4 matrix to a length-4 vector may broadcast the vector across rows in numerical libraries. Many bugs are shape mismatches, so inspect array dimensions.

## Dot products and weighted sums

For vectors a and b, dot product is a·b = sum of matching products. Example: [2, 3]·[4, 5] = 2×4 + 3×5 = 23.

A linear model uses a dot product between input features and learned weights, then adds a bias. This is why matrix multiplication runs the same model over many examples efficiently.

The dot product is also related to angle and similarity. If vectors point in similar directions, their cosine similarity is high. But similarity depends on representation: semantically similar text vectors may be close because of how they were trained.

## Scaling and geometry

Distance formulas assume a measurement scale. If one feature ranges from 0 to 1 and another from 0 to 100,000, Euclidean distance may be dominated by the large-range feature. Standardization or normalization can help, but fit scaling statistics on training data only.

Normalization does not automatically make data fair or meaningful. It changes coordinates and may remove useful absolute magnitude.

## Matrix multiplication

A matrix-vector multiplication creates a weighted sum for each row. A neural-network layer is often a matrix multiplication plus bias, followed by a nonlinear activation. GPUs accelerate these operations because they perform many similar arithmetic operations in parallel.

## Dimensionality reduction

Principal component analysis (PCA) rotates coordinates to directions that capture as much variance as possible, then may keep only the top directions. It can compress data and reveal structure, but high variance is not always task-relevant, and components may be hard to interpret.

## Questions and answers

**What is a vector in a dataset?**  
It often represents one example's feature values or a learned parameter set. Its meaning comes from the chosen columns or model layer.

**Why do matrix shapes matter?**  
Operations require compatible dimensions. A shape error can reveal that examples, features, and parameters have been arranged incorrectly.

**Does a high cosine similarity prove two texts mean the same thing?**  
No. It indicates geometric closeness in a learned representation, which can be useful but depends on the model and context.

**Does PCA find the most important features?**  
It finds directions of greatest variance, not necessarily causal or predictive importance.

## Practice and checkpoint

Compute a dot product by hand, then explain how a matrix of example rows multiplied by a weight vector produces one prediction per row. Standardize two differently scaled features and explain what changed.