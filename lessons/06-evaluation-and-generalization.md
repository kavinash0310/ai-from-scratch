# Lesson 06 — Evaluation, generalization, and model errors

## Learning goals

Create a trustworthy test plan, select a metric that reflects the real task, recognize leakage, and investigate where a model fails.

## What a score can and cannot say

An evaluation score summarizes performance on selected examples under selected conditions. It is not a guarantee about every future case. The evaluation is useful only if the examples and metric represent the real decision.

Always record: dataset version, split method, preprocessing, model version, metric definition, and evaluation date. Without this, two reported scores may not be comparable.

## Confusion matrix

For binary classification, predictions can be:
- true positive: positive case correctly predicted positive;
- false positive: negative case incorrectly predicted positive;
- true negative: negative case correctly predicted negative;
- false negative: positive case missed.

**Accuracy** is the fraction correct. It can be misleading when classes are imbalanced. If only 1 in 1000 transactions is fraud, a model that always says “not fraud” has 99.9% accuracy and catches no fraud.

**Precision** asks: of cases predicted positive, what fraction were truly positive? It matters when false alarms are costly.

**Recall** asks: of truly positive cases, what fraction did we find? It matters when missing a positive case is costly.

**F1** is a combined score that balances precision and recall, but it does not encode every application cost. It is not automatically the right metric.

A threshold converts a model score into a class. Moving the threshold usually trades off precision and recall. Choose it using validation data and the consequences of errors.

## Regression metrics

Mean absolute error is the average absolute distance from target; it is easy to interpret in target units. Mean squared error penalizes large errors more strongly. Root mean squared error returns to the target's units. R-squared compares against a mean baseline under a particular definition, but can be negative on test data and should not be mistaken for percent accuracy.

Inspect error distributions and examples, not just averages. A model may be accurate on typical cases and disastrous on a small subgroup.

## Data splits and leakage

- Random train-test split: appropriate when examples are independent and identically distributed enough for the intended prediction.
- Group split: keeps the same person, device, or organization out of both train and test.
- Time split: trains on the past and evaluates on the future.
- Domain split: tests transfer to a new location, camera, hospital, or source.

Leakage occurs when information from the target or test set slips into model selection or preprocessing. Common causes include duplicate examples across splits, future features, target-derived columns, and fitting a scaler on all data.

## Cross-validation and uncertainty

Cross-validation repeats training and validation across several splits to see whether results depend heavily on one random partition. It helps model selection when data are limited, but does not remove the need for a final holdout or a realistic time/group split.

Metrics vary from sample to sample. Confidence intervals or repeated splits help communicate uncertainty. Do not report many decimal places when the sample is small or noisy.

## Robustness, calibration, and subgroup checks

A robust model behaves acceptably under realistic changes: spelling differences, lighting, device types, seasonal shifts, or other expected variations. Test these conditions deliberately.

A calibrated model's probabilities match observed frequencies over suitable groups. Calibration is different from ranking quality: a model can rank cases well but give overconfident probabilities.

Subgroup evaluation can reveal uneven error rates. Define groups with care, respect privacy, and consider how group labels were collected. A favorable average may hide harmful disparities.

## Review questions with answers

**1. Why can high accuracy be useless?**  
If one class is rare, predicting the majority class can earn high accuracy while failing the actual task. Select metrics based on meaningful error costs.

**2. What is the difference between precision and recall?**  
Precision measures how reliable positive predictions are. Recall measures how many true positive cases are found.

**3. Why keep groups separate during splitting?**  
If the same person or entity appears in both train and test, the test may measure memorization of that entity rather than generalization to new entities.

**4. What does cross-validation provide?**  
A view of how model scores vary across several data partitions. It supports model selection but cannot repair a bad dataset or an unrealistic split.

**5. What is calibration?**  
Agreement between predicted probabilities and observed frequencies. Among many cases assigned probability near 0.8, roughly 80% should be positive for a well-calibrated model in that setting.

## Practice

Take a classifier and report its confusion matrix, accuracy, precision, recall, and F1. Change the threshold and explain which errors increase. Inspect errors by at least one meaningful subgroup or condition.

## Mastery check

If someone shows you a single “99% accurate” claim, ask what examples were tested, how the split was made, what the base rate is, which errors matter, and how uncertain the estimate is.