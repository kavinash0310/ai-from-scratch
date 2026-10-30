# Chapter 3 — Probability and statistics

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

## Describe data before modeling

Statistics summarizes observations and helps estimate properties of a larger population. The mean is sensitive to outliers; the median is more robust. Variance and standard deviation describe spread; quantiles describe cut points. Histograms and scatter plots reveal shapes and relationships.

A dataset is a sample, not the world itself. If the sample excludes certain groups or conditions, a model cannot reliably learn performance for them merely by being complex.

## Probability and conditional probability

Probability ranges from 0 to 1. A random variable represents a quantity that may take different values. Conditional probability P(A|B) means the probability of A given B.

Bayes' rule is:

P(A|B) = P(B|A)P(A) / P(B)

It combines prior probability, evidence likelihood, and the probability of the evidence. This helps explain why rare events can be hard to detect accurately even when a test is fairly good.

## Base-rate example

Suppose a condition affects 1 in 1,000 people. A test catches 99% of true cases but returns positive for 1% of unaffected people. Among 1,000 people, about 1 has the condition and is likely caught; about 10 of 999 unaffected people may be false positives. Most positive results can therefore be false even with seemingly strong test properties. The base rate matters.

## Sampling and uncertainty

An estimate from a finite sample varies. If we take different samples, we can get different averages or model scores. Standard errors, confidence intervals, and bootstrap estimates describe some of this uncertainty under assumptions.

A confidence interval is produced by a procedure with long-run coverage properties. It is not a statement that a particular interval has a 95% chance of containing the fixed true value in a frequentist interpretation.

## Correlation and causation

Correlation measures association. It does not prove that changing one variable will change another. A third variable, selection process, or measurement method can explain the relationship. Prediction may use correlations; intervention decisions require causal reasoning.

## Questions and answers

**Why can the average be misleading?**  
A few extreme values can pull it away from what is typical. Look at median, quantiles, and a plot.

**What is a base rate?**  
The prevalence of an event before considering a particular test result. Rare events create many false positives unless specificity is extremely high.

**Does a probability of 0.8 mean this case is 80% certain?**  
It is the model's probability assignment. Its reliability depends on calibration and whether the current case resembles the evaluation population.

**Does correlation imply cause?**  
No. Association alone cannot rule out confounding, selection, or reverse direction.

## Practice and checkpoint

Construct the rare-event example with counts for 10,000 people. Compute mean and median for a skewed dataset. Explain one place where a correlated feature might be unavailable or misleading at prediction time.