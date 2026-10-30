# Chapter 2 — Reproducible experiments and capstone

## Design experiments

State one hypothesis before changing a model. Use a fixed evaluation protocol. Change one major factor when possible. Run multiple seeds if randomness affects results. Report mean and spread instead of only the best run.

Record code commit, data version, preprocessing, model configuration, hardware, library versions, random seed, and runtime. Reproducibility helps distinguish real improvements from accidental changes.

## Capstone structure

A strong capstone explains:
1. user and problem;
2. data rights, source, and quality;
3. baseline and chosen method;
4. split and metric;
5. results and error examples;
6. system or demo instructions;
7. limitations, privacy, and safety;
8. next experiment.

A small, well-evaluated model can show more expertise than an untested app wrapped around a large LLM.

## Choose a specialization

After fundamentals, go deep in one area such as computer vision, NLP, LLM systems, recommendation, robotics, forecasting, reinforcement learning, causal ML, or AI infrastructure. Learn its mathematical tools, read core papers, and build a portfolio of increasingly independent work.

## Deeper walkthrough: from idea to evidence

Write a hypothesis such as: “Adding a time-of-day feature reduces next-day delivery MAE on future weeks compared with the current baseline.” Specify the cutoff dates, metric, baseline, and number of repeated runs before training.

If the result improves, inspect whether the feature is truly available when a prediction is made and whether the improvement holds on later weeks. If it fails, inspect data quality, split design, and error groups before rejecting the idea.

Keep experiment records in a table: run ID, code commit, data version, settings, seed, metric, runtime, and notes. Use a README so another person can reproduce the result. Include the failures you observed; they explain the model's boundaries.

The capstone is complete when its evidence is inspectable and the next useful experiment is clear.

## Questions and answers

**Why report multiple random seeds?**  
Training can vary due to initialization and data order. Repeating reveals whether an improvement is stable.

**Why keep negative results?**  
They prevent repeated dead ends and provide useful evidence when the experiment was well designed.

**What makes a capstone reproducible?**  
Another person can obtain the data appropriately, follow setup steps, run the method, and understand the split and metric.

## Practice and mastery

Publish a capstone with a README, environment, baseline, evaluation, error analysis, and limitations. Ask someone to reproduce one result and record what instructions were unclear.