# Chapter 4 — Unsupervised learning

> **Book-length subject volume:** For expanded explanations, worked examples, review questions, and practice, read the [ml textbook](TEXTBOOK.md).

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

## Learn without a target

Unsupervised learning seeks structure when no known label y is provided. The goal may be grouping, compression, anomaly scoring, or exploration. Since there is no answer key, validation requires domain judgment, stability tests, and downstream usefulness.

## Clustering

k-means assigns examples to one of k clusters by minimizing squared distance to cluster centers. It works best when clusters are compact and roughly spherical in the chosen feature space. Initialization, scale, outliers, and k change the result.

Hierarchical clustering builds nested groups using pairwise distance. Density-based methods can find irregular shapes and mark isolated points as noise, but depend on neighborhood and density settings.

A cluster is a grouping induced by representation and algorithm, not a discovered natural category. Name clusters only after inspecting examples and checking whether the grouping is useful.

## Dimensionality reduction and anomalies

PCA projects data into directions of high variance. It helps visualize or compress but may discard low-variance signals that matter for a target. Anomaly detection assigns unusualness scores. Rare does not automatically mean wrong or harmful.

## Evaluation

Check whether clusters are stable across seeds or samples, whether they correspond to useful distinctions, and how they compare with simple rules. For anomaly systems, examine false alarms and missed incidents with domain experts.

## Deeper walkthrough: validate a clustering result

Suppose a retailer asks to group customers. Standardize numeric inputs, choose a small k, and inspect cluster sizes and representative examples. If one cluster contains nearly everyone and several contain single points, check scale, outliers, initialization, and k.

Repeat clustering across random seeds or bootstrap samples. If assignments change dramatically, the groups are unstable. Compare with a simple business segmentation and ask whether each group supports a different action.

Do not name clusters “loyal customers” or “price sensitive” based only on their averages. Those interpretations need validation and may reflect confounding factors. A cluster is an algorithmic partition, not a discovered human type.

For anomaly detection, review alerts with domain experts and estimate false-alarm costs before using them operationally.

## Questions and answers

**How do I know the right number of clusters?**  
There is no universal answer. Use domain purpose, stability, interpretability, and downstream impact. A score alone does not define meaningful clusters.

**Why scale features before k-means?**  
Euclidean distance can otherwise be dominated by a large-range feature.

**Is an anomaly a data error?**  
Not necessarily. It may be a rare valid event, an emerging pattern, or a measurement problem. Investigate before discarding.

## Practice and mastery

Cluster a small dataset after plotting and scaling. Inspect representative examples from each cluster, repeat with different initialization, and explain which groupings are stable and useful.