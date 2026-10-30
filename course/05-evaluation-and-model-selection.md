# Part 5 — Evaluation and model selection

## Chapter 23 — Train, validation, and test

Training data fit parameters. Validation data support choices such as model family and hyperparameters. Test data estimate final performance after those choices are fixed. Repeatedly inspecting test results turns the test set into part of the tuning process.

The split should resemble future use:
- random split for independent examples;
- group split for repeated users or devices;
- time split for future prediction;
- domain split for new locations or sources.

If a user has many records, placing some in train and others in test may exaggerate generalization. If the model predicts next month, training on later months is a serious leak.

## Chapter 24 — Metrics are choices about error

For binary classification, a confusion matrix counts true positives, false positives, true negatives, and false negatives.

- Accuracy: total correct divided by total examples.
- Precision: true positives among predicted positives.
- Recall: true positives among actual positives.
- Specificity: true negatives among actual negatives.
- F1: harmonic mean of precision and recall.
- ROC-AUC: ranking quality over thresholds; can look strong on highly imbalanced data while precision is poor.
- PR-AUC: focuses on precision-recall behavior and is often informative for rare positives.

For regression, mean absolute error is in the target's units and less sensitive to extreme errors than squared error. RMSE penalizes large errors more strongly. Always include a baseline and explain the unit.

Metric selection should reflect what a user cares about. If missing a positive is costly, optimize for recall subject to an acceptable precision or review budget. Do not select metrics after seeing which one flatters the model.

## Chapter 25 — Leakage and mistakes in evaluation

Leakage gives a model access to information it would not have at prediction time or contaminates the test. Examples:
- target-derived fields;
- future information;
- duplicates across splits;
- preprocessing fitted on the full dataset;
- selecting features based on test performance;
- user or patient identity indirectly repeated across train and test.

A pipeline fits transformations only on training folds. A time-aware or group-aware split addresses dependence that random splitting misses.

## Chapter 26 — Uncertainty and calibration

A score is an estimate from finite examples. Use repeated splits or confidence intervals when sample size permits. Large swings across folds indicate instability or heterogeneous examples.

Calibration asks whether predicted probabilities correspond to observed frequencies. A model may rank examples well but be overconfident. Reliability diagrams compare predicted probability buckets to observed outcomes. Calibration must be evaluated on representative held-out data.

For high-impact decisions, an uncertainty estimate should connect to an action: human review, abstention, or additional evidence. A number without a decision policy may not help.

## Chapter 27 — Robustness, fairness, and explanation

Test likely shifts: different cameras, seasons, locations, spelling, accents, or input quality. A model can fail outside training coverage. Report where it was tested.

Evaluate meaningful subgroups when lawful and appropriate. Group metrics may conflict; no single fairness number resolves all policy choices. Seek affected perspectives, inspect data collection, and explain tradeoffs.

Explanations can help debugging and communication, but approximate feature importance is not proof of causality. Correlated features can divide or distort importance. Use explanations as evidence to investigate, not as unquestionable reasons.

## Q&A

**Why is the test set used once?**  
It is meant to remain independent from model choices. Repeated tuning against it gradually adapts decisions to its quirks and makes the score optimistic.

**Why can accuracy be deceptive?**  
A majority-class predictor can score highly when positives are rare while failing every positive case. Check class balance and error types.

**When should I use a time split?**  
When future predictions are the goal and data have temporal order or drift. Train on earlier periods and validate/test on later periods.

**Does calibration mean the model is correct?**  
No. It means predicted probabilities align with observed frequencies over a suitable population. The model can still be wrong on an individual case or on a changed population.

**Are explanations proof of fairness?**  
No. They can reveal patterns but do not establish fairness or causality. Combine subgroup evaluation, data review, domain knowledge, and affected-user feedback.