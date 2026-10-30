# Chapter 2 — Supervised learning: regression and classification

## The basic setup

Supervised learning uses examples with known targets. A model f(x; θ) maps features x to a prediction. Training adjusts parameters θ to minimize a loss on training examples. The real goal is performance on new examples from the intended use environment.

## Regression

Regression predicts a number. A linear regression model computes a weighted sum plus bias. Mean squared error averages squared differences between predicted and true values, penalizing large errors strongly. Mean absolute error is less sensitive to outliers and remains in target units.

Linear regression is a useful baseline, but assumes a linear relationship in the chosen feature representation. Adding transformations or interactions can capture some curvature, but increases modeling choices.

## Classification

Classification predicts categories. Logistic regression applies a sigmoid to a linear score to produce a value between zero and one. For multiple classes, softmax can produce a distribution over classes.

Cross-entropy loss penalizes assigning low probability to the correct class. A threshold converts a probability into a yes/no decision. The threshold is a product decision based on false-positive and false-negative costs; 0.5 is not a universal rule.

## Training and validation

Train parameters on training data. Use validation data to choose features, model family, and hyperparameters. Keep test data for a final estimate after choices are complete. Fit scaling and imputation on training data only, preferably inside a pipeline.

## Worked example

To predict ride duration, define features available at dispatch time and a duration target. Predict the training median as a baseline. Fit a linear model and compare mean absolute error on a time-based validation split. Inspect long trips where errors are large; traffic, route, or events may explain the failure.

## Questions and answers

**What is the difference between regression and classification?**  
Regression predicts a numeric quantity; classification predicts a category or category probabilities.

**Why can a classifier output a probability but still be miscalibrated?**  
The score may rank examples but not match observed frequencies. Evaluate calibration on held-out representative cases.

**What is a hyperparameter?**  
A setting selected by the practitioner, such as regularization strength or tree depth. Model parameters are fitted from training data.

**Why use the training median as a baseline?**  
It is simple, robust to extreme values, and reveals whether feature-based modeling improves prediction.

## Practice and mastery

Train a baseline, linear model, and logistic classifier on separate appropriate tasks. Record splits, loss, metrics, threshold, and error examples. Explain what the model can infer and what information it never received.