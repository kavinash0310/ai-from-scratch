# Advanced ML: learning theory and probabilistic models

> **Place in the course:** Optional advanced study after the core machine-learning chapters and mathematics.

## Goals

Explain why training error is not enough; distinguish fit from generalization; describe Naive Bayes and Gaussian mixture models; explain the Expectation-Maximization loop; and recognize when PCA or independent component analysis may help.

## Generalization and model capacity

A model is fit on a finite sample but is intended to work on new examples. Its empirical risk is average loss on observed training rows; its population risk is expected loss on the real distribution. We can compute the first and must estimate the second using valid held-out evidence.

A flexible model can fit noise. A restrictive model can miss the pattern. This is one view of the bias-variance trade-off: high bias reflects restrictive assumptions; high variance means the fitted model changes a lot when the sample changes. Learning theory asks what conditions let a model generalize. VC dimension is one measure of classifier capacity: roughly, how many points a class can label in every possible way. It gives bounds under assumptions, not an exact test score.

Worked comparison: a shallow decision tree may miss a complex rule but vary little across samples. A deep tree can memorize rows and change when a few rows change. Pruning limits capacity. Compare both with the same split and metric.

## Probabilistic classifiers

Naive Bayes uses Bayes' rule and assumes features are conditionally independent given the class. For text, features might indicate whether words occur. The assumption is often false, yet the classifier can be a fast baseline. It combines a class prior with feature likelihoods. Log probabilities avoid multiplying many tiny numbers. Smoothing assigns nonzero probability to unseen words.

Gaussian discriminant analysis models each class with a Gaussian distribution. A shared covariance assumption creates linear boundaries; different covariances create quadratic boundaries. These methods expose assumptions and uncertainty, but the real data may not be Gaussian.

## Gaussian mixtures and EM

A Gaussian mixture assumes data came from one of several Gaussian components. Component membership is hidden. Expectation-Maximization (EM) alternates:
1. **Expectation:** estimate each point's probability of belonging to each component.
2. **Maximization:** update component weights, means, and covariances using those soft assignments.

EM often increases likelihood but can reach a local optimum. Initialization matters. Repeat initializations and inspect degenerate components. A cluster is a mathematical group under the model, not automatically a natural category.

PCA projects data along directions of greatest variance. It can compress or visualize data, but it does not know which directions matter for a label. ICA seeks statistically independent components under its assumptions and is useful in some signal-separation settings. Neither guarantees human-interpretable concepts.

## Selection and practice

Feature selection must happen inside training or cross-validation. Selecting features after repeatedly inspecting test results leaks information. Hyperparameter searches also consume evidence: the more configurations tried, the more likely the best score is partly luck.

**Questions:** Does VC dimension predict an exact score? No. Why repeat EM initialization? Different starts can lead to different local optima. Does PCA find the most predictive direction? Not necessarily; it maximizes variance, not target relevance.

**Practice:** Generate two overlapping point clouds. Compare k-means with a Gaussian mixture. Inspect hard labels versus soft membership, then test an elongated cluster. Explain what a cluster score cannot prove.

Further reading: [Stanford CS229 schedule](https://cs229.stanford.edu/materials/Handout2.pdf) and [scikit-learn mixture models](https://scikit-learn.org/stable/modules/mixture.html).
