# Project 02 — Build and evaluate a tabular prediction model

## Goal

Complete one leakage-aware supervised ML workflow and defend the model choice. Use a public, licensed dataset with an explicit target.

## Steps

1. Define the unit of prediction, prediction time, target, allowed features, and user decision.
2. Check duplicates, missingness, class balance, label meaning, time ordering, and possible leakage.
3. Choose a split that matches future use: random, group-aware, or time-ordered. Set it aside before tuning.
4. Create a naive baseline, then compare at least two model families, such as regularized logistic regression and boosted trees.
5. Put preprocessing inside a pipeline fitted on training data only. Tune on validation or cross-validation, not the final test set.
6. Choose metrics from the error costs. Inspect a confusion matrix, threshold effects, and at least ten wrong predictions.
7. Document performance by meaningful slices where the dataset permits and state uncertainty/limitations.

## Deliverables

A runnable project, data dictionary, saved split strategy, baseline comparison table, error analysis, README, and responsible-use note. Do not upload a restricted dataset.

## Acceptance checks

The model beats the baseline on the chosen metric without leakage; the test set was not repeatedly used for choices; another person can recreate the reported result; and the report explains which errors matter.

## Stretch

Calibrate probabilities, estimate variation across folds, test a simple drift scenario, and measure inference latency and model size.