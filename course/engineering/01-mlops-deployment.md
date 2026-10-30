# Chapter 1 — MLOps and deployment

## A model is one component

A deployed ML service includes input validation, preprocessing, model inference, output handling, access control, logging, and user communication. Batch inference computes results periodically; online inference responds to requests; edge inference runs on a device.

Choose based on latency, volume, privacy, and hardware. Measure cold start, throughput, memory, and cost. Accuracy alone is not a service-level objective.

## Reproducible pipeline

Record code version, data version, feature definitions, training configuration, random seed, model artifact, evaluation, and deployment version. Separate validation, training, evaluation, packaging, release, and rollback.

Automate repeatable steps, but review data and model changes. A model registry or experiment tracker helps organize work; it does not guarantee correctness.

## Release and rollback

Release to a small audience or shadow mode first when possible. Compare model outputs with existing decisions. Define a rollback owner and trigger before release. Preserve the previous working version.

## Questions and answers

**What does MLOps add to model training?**  
It makes datasets, training, releases, monitoring, and rollback repeatable and maintainable.

**Why version the data?**  
A code commit alone cannot reproduce a model if the dataset or preprocessing changed.

**What is shadow deployment?**  
The new model receives live inputs and produces outputs without affecting users, allowing comparison before activation.

## Practice and mastery

Draw your capstone from user input to output. Include validation, model version, monitoring, access control, and rollback. Estimate latency and cost for a realistic usage rate.