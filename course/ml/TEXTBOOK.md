# Machine learning
## A beginner's textbook chapter

Machine learning fits a function from examples. The difficult work is not only selecting an algorithm: define the task, collect valid data, prevent leakage, compare with a baseline, and measure behavior on cases that represent future use.

## 1. Define the learning problem

For each example, define inputs x and target y. A **feature** is an input available at prediction time. A **label** is the known target attached to a training example. A model f(x; theta) maps features to a prediction, with theta representing learned parameters.

The **prediction moment** is when the model must act. It determines which features are legal. To predict delivery delay at checkout, the delivery timestamp is unavailable. If it appears in training data, it leaks the answer.

Before modeling, ask:
- What is one row or example?
- How is the target defined and who labels it?
- Which facts exist at prediction time?
- Are data points independent, grouped, or time-ordered?
- Which errors are costly?
- Does the collected data represent intended use?

**Data leakage** includes direct target leakage and indirect leakage across related records or time. **Sampling bias** occurs when the data collection process excludes or overrepresents important examples. A model can only learn from what is represented.

## 2. Supervised learning

In **supervised learning**, examples include a target. **Regression** predicts a number, such as a price. **Classification** predicts a category, such as spam/not spam.

### Linear regression

A linear model computes a weighted sum plus bias:

    prediction = w1*x1 + w2*x2 + ... + b

The weights represent how the model combines features. They do not automatically describe causal influence. Mean squared error averages squared differences between predictions and targets. Large errors receive disproportionate weight. Mean absolute error averages absolute differences and stays in target units.

If an outlier is a data error, both models may be misleading until the data is investigated. Metrics do not repair wrong labels.

### Logistic regression

For binary classification, logistic regression first computes a linear score z, then applies the sigmoid:

    p = 1 / (1 + exp(-z))

The result is between zero and one. Training commonly uses binary cross-entropy, which penalizes low probability assigned to the observed class. The score is not automatically calibrated; calibration must be checked on held-out examples.

The predicted probability and decision threshold are separate. If false negatives are costly, a product may choose a lower threshold to flag more positives, accepting more false positives. The right operating point depends on context.

For multiple classes, softmax converts scores into values that sum to one. The model chooses the largest score by default, but a real product may need abstention or costs that differ by class.

## 3. Compare model families

A model family carries an **inductive bias**: assumptions about what patterns are easy to represent.

- **Linear models** are fast, compact, and useful as interpretable baselines. Feature engineering can add interactions or nonlinear effects.
- **Decision trees** split examples by feature conditions. They are easy to visualize but can be unstable.
- **Random forests** average many randomized trees, often reducing variance. They can model nonlinear interactions with limited scaling.
- **Gradient boosting** adds small trees sequentially to improve earlier errors. XGBoost, LightGBM, and CatBoost are common implementations for tabular work.
- **Support-vector machines** seek separating margins and can use kernels; kernel methods can become costly with many examples.
- **Nearest neighbors** predict from similar stored examples; distance choice and scaling matter.
- **Naive Bayes** uses a simplified conditional-independence assumption and can be a useful text baseline.
- **Neural networks** compose nonlinear functions and may learn complex representations, but often need more data and tuning.

There is no universal ranking. A tree ensemble can be an efficient choice for medium-sized tabular data. A neural network may be better with large-scale image, speech, or text data and suitable compute. Compare methods on the same data, split, metric, and tuning budget.

## 4. Unsupervised learning

**Unsupervised learning** seeks structure without target labels.

**K-means** assigns points to a chosen number of centroids, minimizing within-cluster squared distance. It is efficient for large datasets with compact, similarly sized groups, but assumes a useful distance geometry. Scale features before distance-based grouping when units differ.

**DBSCAN** groups dense regions and can mark isolated examples as noise. It can find irregular cluster shapes but depends on density parameters. **Hierarchical clustering** builds nested groups and can be useful for small datasets where relationships matter. **Gaussian mixture models** estimate soft membership under distributional assumptions.

**Principal component analysis (PCA)** projects numeric features into directions of high variance. It can compress or visualize data, but high variance is not synonymous with target usefulness. **Anomaly detection** flags unusual records relative to a reference; an unusual example is not automatically an error or threat.

## 5. Build a valid training workflow

Separate examples into:
- **Training set:** fit model parameters.
- **Validation set:** choose model family, features, and hyperparameters.
- **Test set:** estimate final performance after choices are made.

Repeatedly tuning on the test set makes it part of the development process and makes the reported score optimistic. Use group splits when a person/device can create correlated records across sets. Use chronological splits when predicting future events.

Fit transformations only on training data. A scaler learns means and standard deviations; an imputer learns replacement values; a vocabulary learns from text. Use a pipeline so the transformation is fitted within each training fold.

First build a baseline. For numeric outcomes, predict a training mean or median. For classification, predict the majority class or use a domain rule. The baseline tells you whether model complexity adds useful signal.

## 6. Metrics must match error costs

A **confusion matrix** counts true positives, false positives, true negatives, and false negatives.

- Accuracy is fraction correct; it can hide failure on rare classes.
- Precision asks: among predicted positives, how many are positive?
- Recall asks: among actual positives, how many did we find?
- F1 combines precision and recall but does not represent all costs.
- ROC-AUC summarizes ranking over thresholds.
- PR-AUC emphasizes precision/recall and is often informative for rare positives.
- Calibration asks whether predicted probabilities match observed rates.

For regression, MAE is robust to outliers and easy to interpret. MSE/RMSE penalize large errors more. Plot errors and inspect outliers. An average can hide subgroup harm or poor performance at a particular time.

## 7. Diagnose fit

**Overfitting** means the model fits idiosyncrasies of training data that do not transfer. **Underfitting** means the model cannot represent the needed pattern. A learning curve plots performance as training data or model complexity changes.

If training and validation performance are both poor, investigate labels, features, model capacity, optimization, and data quality. If training is strong but validation weak, use more representative data, regularization, simpler models, or leakage checks. Do not change several things at once if you want to learn what caused the improvement.

## 8. Worked example: a late-delivery classifier

At order placement, one row is one order. The target is whether it arrives later than the promised date. Candidate features include distance, service type, weekday, and region. The actual delivery time is not a feature because it is unknown when making the prediction.

First train a majority baseline. Split by date so the test period is later. Fit imputation and categorical encoding on training data. Compare logistic regression with boosted trees. Report recall for late orders, precision, confusion matrix, and threshold. Inspect false negatives and determine whether certain routes or seasons account for them. Only then decide whether a support team should use the score.

## 9. Questions and answers

**Why is a baseline mandatory?** It shows whether the proposed model adds value beyond a cheap, transparent method.

**What is the difference between a model parameter and a hyperparameter?** Parameters are fit from examples; hyperparameters are chosen by practitioners during development.

**Can a model with high ROC-AUC still make bad decisions?** Yes. The threshold, calibration, error costs, and population shift matter.

**Can unsupervised clusters be treated as known customer types?** No. They are groups under a chosen representation and distance; validate their stability and meaning.

**Why not simply use the largest model?** It may cost more, be harder to maintain, and perform worse on the task than a simpler approach.

## 10. Exercises with answer guidance

1. Find a dataset and define the prediction moment. List features that would leak future information.
2. Compare a baseline and two models using a group- or time-aware split.
3. Choose a threshold based on an explicit false-positive and false-negative tradeoff.
4. Inspect at least ten errors and write what additional data might distinguish them.
5. Save preprocessing, model, split, metric, and limitation notes.

A strong solution makes its assumptions visible and does not use the test set to tune repeatedly. Continue to the [deep-learning textbook](../deep-learning/README.md), or use the [ML model comparison lab](../../labs/ml/19_model_family_comparison.py).

## Deeper evaluation: objective, threshold, and leakage

A loss function gives the learner a training penalty. A metric summarizes behavior for comparison. A threshold turns a score into an action. Calibration asks whether predictions stated as probabilities match observed frequencies. These are related but different. If missing a machine failure costs 100 and inspecting costs 5, a predicted risk of 0.3 may justify inspection even though it is below 0.5. A threshold depends on error costs and capacity, not a universal convention.

Training data fit parameters. Validation data guide model choices. A test set estimates final performance after choices are complete. Repeatedly tuning against the test score turns it into validation data. Cross-validation rotates validation folds; it does not fix leakage or an inappropriate split.

Leakage occurs when the training process uses information unavailable at prediction time or lets evaluation data influence choices. Examples: a post-outcome field used as a feature; scaling the entire dataset before splitting; the same person appearing in both train and test; repeated test-score tuning. Ask whether each field would really exist at the moment the prediction is needed. Keep related people, devices, documents, or time periods grouped when deployment requires that separation.

Accuracy can mislead on rare events. If one in 1,000 transactions is fraud, predicting “not fraud” every time yields 99.9% accuracy while catching zero fraud. Precision asks what share of alerts are true positives; recall asks what share of actual positives are caught. A confusion matrix gives counts at one threshold. Review actual counts, alert capacity, and costs alongside rates.

A robust evaluation states sample size, split rule, metric, uncertainty where possible, and important slices. Keep a simple baseline. A complex model should earn its complexity with a meaningful improvement.

Questions: Why can training loss fall while test performance worsens? The learner may fit noise or exploit a mismatch. Why compare slices? An aggregate average can hide a subgroup failure. Why is a score not itself a decision? Someone must choose an action policy and threshold based on costs.

Further reading: [scikit-learn model evaluation](https://scikit-learn.org/stable/modules/model_evaluation.html), [cross-validation](https://scikit-learn.org/stable/modules/cross_validation.html), and [Google dataset splitting](https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets).
