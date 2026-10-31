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

## Worked example: Naive Bayes with smoothing

Suppose a tiny spam dataset has 4 spam and 6 ordinary messages, so the class priors are 0.4 and 0.6. The word “prize” occurs in 3 of 4 spam messages and 1 of 6 ordinary messages. With a simple presence feature, the likelihoods are 0.75 and about 0.17. For a message containing “prize,” the unnormalized class scores are 0.4*0.75=0.30 for spam and 0.6*0.17=0.10 for ordinary. Normalizing gives an approximate spam probability of 0.75.

With only six ordinary examples, the estimate is fragile. If a word never appeared in one class, its raw likelihood would be zero; Laplace smoothing adds pseudo-counts so one absent observation does not rule a class out. The numerical probability should still be checked for calibration because the independence assumption and small sample can make confidence misleading.

## EM in words, then in equations

Imagine measurements from two overlapping groups, but group identities are hidden. EM first assigns each point a soft responsibility for each Gaussian based on the current means and variances. It then updates each Gaussian using those weighted points. Repeat until likelihood changes little or a stopping limit is reached.

The expectation step does not discover a single “true” label. A point near two components may receive responsibility 0.55 and 0.45. Initialization, number of components, covariance restrictions, and scaling affect the result. Compare several starts and inspect the fitted distributions, not only a scalar clustering score.

## Generalization checks

A theoretical capacity measure explains why very flexible classes may need more examples; it does not replace measurement. For practical work, compare training and validation curves, use nested validation if selecting many hyperparameters, and preserve the final test set. If samples share people, time, sites, or near-duplicate records, split by that structure.

**Key terms:** empirical risk is measured training loss; population risk is expected loss on the target distribution; capacity describes the range of functions a model class can express; soft assignment gives fractional membership; likelihood measures how well a model assigns probability to observed data.

**Check your understanding:** Why can an EM clustering score improve while cluster meaning remains poor? The score is tied to model fit, while usefulness depends on whether the components support the intended interpretation or decision. Why can a high-capacity model still generalize? With suitable data, regularization, and assumptions, complexity alone does not determine failure.
