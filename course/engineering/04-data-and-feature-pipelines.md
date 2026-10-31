# AI engineering: data and feature pipelines

> **Place in the course:** Advanced practical study after the core ML workflow. Production performance depends on reliable data definitions and transformations.

## A pipeline is an executable data contract

A data pipeline extracts, validates, transforms, and delivers data. A feature is an input used by a model. Document its name, definition, unit, source, timestamp, missing-value meaning, and allowed range. “Customer activity” is ambiguous; “completed sessions in the 30 days before prediction time” is testable.

A schema contract checks names and types. Semantic checks verify meaning: age is nonnegative, timestamps are valid, and categories are allowed. Check raw data and transformed features because a valid row can become invalid later.

## Point-in-time correctness

For each training row, features must reflect information available at its prediction time. Predicting loan default at application time using “days past due” recorded afterward leaks the outcome. Historical joins must select the record as of the decision time, not the latest current value.

A rolling demand average must end at the forecast moment; a centered window sees future data. A promotion field is valid only if the schedule was already known. Record event time, processing time, and label horizon, then hand-check a row before scaling to millions.

## Offline and online parity

Training may compute features in batch while a service computes them online. Differences create training-serving skew. Reuse transformations when feasible, or create parity tests that compare both outputs on identical examples.

A feature store can centralize definitions and online/offline values, but adds infrastructure and governance cost. A small project may use versioned pipeline code. The important property is a tested contract.

## Lineage and operations

Lineage records where data came from, what transformations occurred, and which version produced a model. Keep stable references for large datasets rather than committing sensitive raw data. Track schema versions; changes need migration plans. Handle retries, duplicates, late data, and failed jobs. Make steps idempotent when possible and preserve only necessary logs.

Worked example: At 8 p.m., predict tomorrow's product demand. The seven-day average may use data through today, but not tomorrow. A feature generated from later corrections is not available at the prediction moment. The target must not be included in the rolling aggregate.

**Questions:** Why can current customer status leak into old training rows? It may include post-outcome information. Why specify units? “Income” is unclear without currency and period. Why test parity? Different preprocessing changes model inputs.

**Practice:** Define three features for a delivery-time prediction: timestamp, unit, missing behavior, validation, and leakage risk. Draw ingestion → validation → transformation → training → inference.

Further reading: [Google dataset splitting](https://developers.google.com/machine-learning/crash-course/overfitting/dividing-datasets) and [Google production monitoring](https://developers.google.com/machine-learning/crash-course/production-ml-systems/monitoring).
