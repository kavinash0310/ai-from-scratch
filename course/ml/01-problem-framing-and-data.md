# Chapter 1 — Problem framing and data

## Frame a decision

“Use AI to improve support” is not a trainable task. Define who needs help, what decision is changing, what information exists at decision time, and what errors cost.

For supervised learning, define one example, features X, and target y. In a late-delivery task, one row might be one shipment; features are known at acceptance time; the target says whether delivery was late. Actual arrival time is unavailable at prediction time and leaks the answer.

Write the prediction time explicitly. For each feature ask, “Would we know this value then?” Identify unit of analysis: customer, order, message, or day. Repeated entities may need group-aware splits.

## Data provenance and quality

Document source, permission, collection process, label definition, missingness, duplicates, time span, and known gaps. Labels can be noisy or reflect historical decisions rather than ground truth. Data quality is part of model quality.

Check distributions and examples before modeling. Plot target balance, missingness, feature ranges, and time patterns. Investigate impossible values. Do not remove unusual values until you know whether they are errors or important rare cases.

## Baseline and objective

A baseline is a simple comparison: majority class, historical average, current business rule, or previous system. Decide a success metric before tuning. A model is valuable only if it improves the decision enough to justify operational costs and errors.

## Questions and answers

**What is a feature?**  
An input attribute representing an example. It should be available and valid when the prediction is made.

**What is target leakage?**  
Using information that reveals the answer or would not exist at prediction time, producing unrealistic evaluation.

**Why document labels?**  
Different people may interpret categories differently. A written labeling rule supports consistent data and meaningful error analysis.

**Why make a baseline before a model?**  
It shows whether the model improves on a simple approach and reveals whether the task has usable signal.

## Practice and mastery

Write a one-page specification for a prediction task. Include user, action, example unit, prediction time, feature list, target, data source, baseline, metric, error costs, and split strategy. Identify one feature that must be excluded because it appears after prediction time.