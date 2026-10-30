# Chapter 5 — Evaluation and generalization

> **Book-length subject volume:** For expanded explanations, worked examples, review questions, and practice, read the [ml textbook](TEXTBOOK.md).

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

## Separate fitting from judging

Training data fit parameters. Validation data help choose models. Test data provide a final estimate once choices are fixed. Repeatedly tuning against test results turns the test into training-by-feedback.

Choose the split to mimic deployment:
- random for independent observations;
- group split for repeated users or devices;
- chronological split for future prediction;
- domain split for new locations or sources.

Preprocessing is learned too. Fit imputers, encoders, and scalers on training folds only. A pipeline prevents accidental leakage during cross-validation.

## Metrics describe error priorities

For binary classification, a confusion matrix counts true positive, false positive, true negative, and false negative cases.

Accuracy is overall fraction correct; it can mislead when one class is rare. Precision measures reliability of positive alerts. Recall measures how many actual positives were found. F1 combines precision and recall but does not express every real-world cost. ROC-AUC measures ranking over thresholds; PR-AUC is often more informative for rare positives.

For regression, mean absolute error is interpretable in target units; RMSE penalizes large errors more. Report a baseline and error distribution.

## Generalization and uncertainty

Overfitting means the model fits training details that do not repeat in future data. Underfitting means it is too simple to capture useful patterns. Cross-validation estimates variability across splits, but cannot fix biased or unrepresentative data.

Calibration checks whether probability predictions match observed frequencies. Distribution shift means new inputs or relationships differ from training. Monitor representative subgroups and realistic changed conditions.

## Fairness and explanations

Group averages can hide unequal error rates. Evaluate relevant groups with attention to sample size, data rights, and context. Fairness metrics can conflict; explain choices and involve affected stakeholders.

Model explanations can help debug or communicate, but they are not proof of causality or fairness. Treat feature importance as evidence to investigate.

## Questions and answers

**Why can accuracy be 99% and still fail?**  
If positives are 1% of data, always predicting negative achieves 99% accuracy while finding no positive cases.

**What is data leakage?**  
Information from test outcomes or unavailable future data influences model fitting or selection, making evaluation optimistic.

**What is calibration?**  
Among cases assigned a probability near a value, the observed fraction should be near that value under representative conditions.

**Does a good test score guarantee future success?**  
No. Future populations, devices, behavior, or data pipelines can change. Test design and monitoring matter.

## Practice and mastery

Calculate a confusion matrix and precision/recall on an imbalanced example. Evaluate a model with a group or time split, inspect errors, state uncertainty, and identify a condition under which you would not deploy it.