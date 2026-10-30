# Chapter 2 — Monitoring and model maintenance

Monitor software health: errors, latency, throughput, and spend. Monitor data: missing fields, ranges, and input distribution. Monitor model quality: delayed labels, error rates, confidence, and overrides.

Data drift means input distribution changes. Concept drift means the relationship between inputs and outcomes changes. A shift alert is not proof of failure; investigate examples and outcomes before retraining.

Retraining can make things worse if data labels are delayed, contaminated, or reflect a harmful feedback loop. Define when to retrain, who reviews it, and how to compare it with the current model.

## Deeper walkthrough: detect a real service change

Suppose a delivery model predicts lateness. Monitor latency and service errors, but also compare predicted lateness rates and input distributions with recent training data. When next-day outcomes arrive, calculate recall and calibration by route and week.

If predictions shift after a new logistics provider is introduced, that is a signal to inspect. It is not proof that the model is worse: the provider could have improved delivery. Delayed outcome labels are needed to measure actual quality.

Use a response ladder: alert the owner, inspect examples and data pipeline, compare outcomes, restrict use if risk is high, then retrain or rollback if evidence supports it. Keep the current model until the replacement passes the same fixed evaluation protocol.

A dashboard without an owner and response threshold is not monitoring. Write what each alert means, who investigates, and what action is allowed.

## Questions and answers

**Why can an online model become worse without code changes?**  
Users, data collection, environment, or the relation between features and outcomes can change.

**Should every drift alert trigger retraining?**  
No. Drift signals guide investigation. Retraining on poor or biased data can worsen behavior.

**Why monitor overrides and complaints?**  
They can provide early evidence of errors that aggregate metrics or delayed labels miss.

## Practice and mastery

Define three service alerts and three model-quality signals for your capstone. For each, specify threshold, owner, investigation, and rollback action.