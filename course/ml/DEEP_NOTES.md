# Machine learning — full beginner notes

Machine learning fits a predictive or descriptive function from examples. A strong workflow begins with the real question and data, establishes a baseline, separates evaluation from fitting, and studies errors.

## 1. Problem framing and data

Define the **unit of prediction**: one customer, transaction, image, or time window. Define the **prediction moment**: which facts are actually available then? The **target** is what you want to predict; a **feature** is an input available to the model; a **label** is the known target attached to a training example.

Example: predict whether an online order arrives late. Each row is an order at checkout. Features may include destination region and chosen shipping service. The label is late/not late after delivery. A feature containing the final delivery date leaks the answer and cannot be used at checkout.

**Data leakage** occurs when training or evaluation uses information unavailable at real prediction time, or that indirectly reveals the target. **Sampling bias** means collected examples do not represent the intended population. **Missingness** may carry information or reflect a broken collection process. Document source, time period, permissions, units, and label creation.

Split data according to future use: random split for independent examples, group split when an entity must not cross partitions, and chronological split when predicting the future. Fit preprocessing only on training data and reuse that fitted transformation on validation and test data.

## 2. Supervised learning

In **supervised learning**, examples contain inputs x and known target y. The model f(x; theta) predicts y; training chooses parameters theta to reduce a **loss**. In **regression**, y is numeric. In **classification**, y is a category, often with a probability per class.

Linear regression computes a weighted sum plus bias. Mean squared error squares residuals, so large misses count heavily; mean absolute error is more robust and stays in target units. Logistic regression maps a score through a sigmoid for binary probabilities. Softmax creates multi-class probabilities. Cross-entropy strongly penalizes assigning low probability to the correct class.

A probability is not yet an action. A **decision threshold** converts a score into a choice. Choose it based on costs, capacity, and user impact. In fraud screening, a false negative misses fraud; a false positive inconveniences a legitimate customer. Those errors may not cost the same.

## 3. Model families

A **baseline** is a simple comparison: predict the mean/median, most common class, or a domain-specific rule. Without it, a complex model's score has no context. **Linear models** are fast and interpretable in many settings but need useful features. **Decision trees** split data using feature tests and are easy to visualize but can overfit. **Random forests** average randomized trees to reduce variance. **Gradient boosting** adds trees sequentially to correct earlier errors and often performs strongly on tabular data.

**Nearest neighbors** predict from similar stored examples; scaling matters because large-range features dominate distance. **Naive Bayes** uses a simplifying conditional-independence assumption and can be a useful text baseline. **Kernel methods** compare examples through a similarity function. A model family is a tool, not a universal ranking; data size, noise, latency, interpretability, and maintenance matter.

Tune **hyperparameters** (developer-selected settings such as depth or regularization) on validation data. **Parameters** (weights or split values) are learned from training data.

## 4. Unsupervised learning

Unsupervised methods work without a target label. **Clustering** groups examples under a chosen similarity and objective. K-means assigns examples to k centroids and minimizes within-cluster squared distance; it fits best when its geometric assumptions suit the data. **Dimensionality reduction** maps data to fewer dimensions to compress or visualize patterns. PCA finds orthogonal directions of high variance after appropriate centering and scaling.

An **embedding** is a vector representation; nearby vectors are similar according to a learned or defined space. A cluster is not automatically a real-world category. Inspect examples, stability across settings, and how groups will be used. **Anomaly detection** flags unusual examples relative to a reference distribution; rare does not automatically mean harmful.

## 5. Evaluation and generalization

**Generalization** is performance on new examples from the intended environment. Training data fits parameters; validation data supports model choices; test data gives a final estimate after choices are complete. Repeatedly tuning against the test set makes it a de facto validation set.

For classification, **accuracy** is the fraction correct but can mislead on imbalanced data. **Precision** is the fraction of predicted positives that are truly positive; **recall** is the fraction of positives found. **F1** balances precision and recall. **ROC-AUC** measures ranking across thresholds; **PR-AUC** can be more informative when positives are rare. A **confusion matrix** counts true/false positives/negatives. **Calibration** asks whether predicted probabilities match observed frequencies.

For regression, MAE, MSE/RMSE, and error plots answer different questions. Aggregate metrics can conceal failures by subgroup or time. Inspect slices, uncertainty where appropriate, and real error examples.

**Overfitting** means fitting quirks of training data that do not carry to new cases. **Underfitting** means the model cannot capture the needed pattern. Regularization, representative data, simpler models, and better evaluation can help. A metric is evidence, not the definition of value.

### Q&A and project

**Can I evaluate on training data?** You can measure fit, but it does not estimate unseen performance.
**Does high AUC mean probabilities are trustworthy?** No. Ranking and calibration are different.
**What is a good first project?** Predict a documented target in a public tabular dataset. State the prediction moment, build a baseline, create leakage-safe splits, compare model families, inspect errors, and write limitations.

Mastery: defend the target, features, split, baseline, metric, threshold, and intended users before training. Continue to [deep learning](../deep-learning/README.md).