# Lesson 05 — Machine-learning foundations

## Learning goals

Understand what it means to learn from examples, distinguish common learning tasks, and build a simple training workflow.

## What learning means

A machine-learning model is a function with adjustable parameters. Training searches for parameters that make predictions fit observed examples according to an objective.

A supervised dataset contains inputs X and targets y. The model calculates predictions from X. A loss function measures disagreement between predictions and y. An optimizer changes parameters to reduce loss.

This is not the same as copying answers into a table. The goal is to learn a pattern that generalizes to examples not seen during training.

## Main task types

**Regression** predicts a numerical value, such as trip duration. A common objective is mean squared error. Large errors receive a larger penalty because the difference is squared.

**Classification** predicts a category, such as whether a message is spam. Models often produce a score or probability for each class; a decision threshold converts scores into a final label.

**Unsupervised learning** looks for structure without a provided target. Clustering groups similar examples; dimensionality reduction creates a smaller representation. These outputs need interpretation and do not automatically reveal meaningful real-world categories.

**Self-supervised learning** creates training targets from the input itself, such as hiding words and asking a model to recover them. It allows models to learn from large unlabelled collections, though the data still needs quality and provenance checks.

## A small regression model

Suppose we want to estimate house price from area. A line predicts price = w × area + b. Training examples contain an area and known sale price. We choose w and b to reduce a loss such as mean squared error.

This model may be too simple if location, condition, and property type matter. Adding relevant features may help, but features must be available at prediction time and represented accurately.

## Why compare multiple model families?

- **Linear models** are fast and interpretable, and provide strong baselines.
- **Decision trees** split data into rule-like regions but can overfit when too deep.
- **Random forests** average many trees and reduce variance.
- **Gradient-boosted trees** build trees sequentially to correct prior errors and work well on many tabular tasks.
- **Nearest-neighbor methods** predict using similar examples; feature scaling and distance matter.
- **Support vector machines** find separating boundaries with margins and can use kernels.
- **Neural networks** learn flexible representations, especially useful for complex or unstructured data.

No model is best for every problem. Start simple, use a validation plan, and compare the result against the baseline.

## The training workflow

1. Define the prediction task and collect data.
2. Separate training, validation, and test examples.
3. Fit preprocessing only on training data.
4. Train a baseline.
5. Train a candidate model.
6. Tune choices using validation data or cross-validation.
7. Make one final evaluation on test data.
8. Inspect failures and document limitations.

Hyperparameters are settings chosen by the practitioner, such as tree depth or learning rate. Model parameters are values learned from data. Confusing these terms can make experiments harder to reason about.

## Generalization and bias-variance intuition

A model that is too simple may miss real patterns; this is underfitting. A model that is too flexible may fit noise or quirks in its training examples; this is overfitting.

More model complexity can reduce bias but increase variance. Regularization discourages overly complex fits. More representative data, better features, and a correctly framed task often help more than a fancier algorithm.

## Review questions with answers

**1. What does the loss function do?**  
It turns the difference between predictions and targets into a quantity the training process tries to reduce.

**2. What is the difference between a parameter and a hyperparameter?**  
A parameter is learned during fitting. A hyperparameter is a choice made to configure the learning procedure, often selected using validation data.

**3. Why is a baseline important?**  
It establishes the minimum useful performance. If a model does not improve on a sensible baseline, adding complexity may not be justified.

**4. Is a cluster a discovered truth?**  
No. Clustering groups data according to a chosen representation and distance. The grouping needs interpretation and validation for the intended use.

**5. Why not tune directly on the test set?**  
Repeated decisions based on test results gradually adapt the project to that test set. The reported score then becomes optimistic.

## Practice

Use one public tabular dataset. Make a majority-class or mean-prediction baseline. Train a linear model and a tree-based model. Record data split, preprocessing, metric, scores, and two examples of errors.

## Mastery check

Explain the inputs, target, loss, training procedure, and baseline of your model without saying only “the library did it.”