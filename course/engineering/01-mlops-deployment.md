# Chapter 1 — MLOps and deployment

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

## A model is one component

A deployed ML service includes input validation, preprocessing, model inference, output handling, access control, logging, and user communication. Batch inference computes results periodically; online inference responds to requests; edge inference runs on a device.

Choose based on latency, volume, privacy, and hardware. Measure cold start, throughput, memory, and cost. Accuracy alone is not a service-level objective.

## Reproducible pipeline

Record code version, data version, feature definitions, training configuration, random seed, model artifact, evaluation, and deployment version. Separate validation, training, evaluation, packaging, release, and rollback.

Automate repeatable steps, but review data and model changes. A model registry or experiment tracker helps organize work; it does not guarantee correctness.

## Release and rollback

Release to a small audience or shadow mode first when possible. Compare model outputs with existing decisions. Define a rollback owner and trigger before release. Preserve the previous working version.

## Deeper walkthrough: safe model release

Suppose a new fraud model is ready. First run it in shadow mode on incoming examples without changing decisions. Compare its predictions with the current system and review disagreements. Then release to a small traffic slice with a rollback trigger.

A release package should identify model version, data and feature versions, dependency versions, evaluation report, and owner. The service should validate input schema, handle timeouts, and provide a safe fallback if inference fails.

Measure percentile latency, not only average latency: a small fraction of very slow requests can still harm users. Also track cost per request and throughput under expected peak load. The deployment target may require a smaller or quantized model.

A rollback should restore a known-good version without rebuilding from memory. Practice that procedure before a severe incident.

## Questions and answers

**What does MLOps add to model training?**  
It makes datasets, training, releases, monitoring, and rollback repeatable and maintainable.

**Why version the data?**  
A code commit alone cannot reproduce a model if the dataset or preprocessing changed.

**What is shadow deployment?**  
The new model receives live inputs and produces outputs without affecting users, allowing comparison before activation.

## Practice and mastery

Draw your capstone from user input to output. Include validation, model version, monitoring, access control, and rollback. Estimate latency and cost for a realistic usage rate.