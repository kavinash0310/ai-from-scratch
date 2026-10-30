# Lesson 11 — Advanced topics and the path to research-level skill

## Learning goals

See the wider technical landscape, learn how to read papers critically, and build habits that distinguish an advanced practitioner from someone who only knows library APIs.

## Advanced skill is a cycle

Expertise does not mean knowing every model. It means being able to:
- formulate a useful question;
- find reliable evidence and prior work;
- create a baseline;
- design a fair experiment;
- understand mathematical and computational tradeoffs;
- analyze failure;
- reproduce results;
- communicate uncertainty and limitations.

A strong project can be simple if the experiment is rigorous.

## Topics to explore after the core lessons

### Optimization and theory
Study convexity, stochastic optimization, constrained optimization, numerical stability, initialization, learning-rate schedules, and generalization theory. Learn which guarantees apply to which assumptions.

### Self-supervised and representation learning
Models create training signals from unlabeled data, such as predicting hidden parts or matching related views. Representations can transfer to downstream tasks. Ask whether the pretraining data and learned representation actually fit the new task.

### Generative models
Autoregressive models predict sequences one step at a time. Variational autoencoders learn a probabilistic latent space. Generative adversarial networks train a generator against a discriminator. Diffusion models learn to reverse a gradual corruption process. Each approach has different training behavior, output quality, sampling speed, and evaluation challenges.

### Reinforcement learning and decision systems
Study Markov decision processes, Bellman equations, value functions, policy gradients, exploration, offline RL, and safe control. Real-world deployment is difficult because environment changes and unsafe exploration may be costly.

### Causal inference
Prediction estimates associations useful for forecasting. Causal inference asks what would happen under an intervention. A predictive model cannot by itself answer “what if we changed this policy?” Confounding, selection, and assumptions about interventions matter.

### Multimodal and structured data
Multimodal models connect text, images, audio, video, or actions. Graph models handle relational structure. Scientific ML may encode physical or domain constraints. These methods need domain-appropriate datasets and evaluation.

### Systems and scaling
Advanced practice includes distributed training, mixed precision, memory optimization, efficient data loading, inference batching, quantization, caching, and latency measurement. Optimization should follow a measured bottleneck, not a guess.

## How to read a research paper

Read in passes:

1. **Abstract:** what question and claimed result?
2. **Introduction:** why does the problem matter and what is the contribution?
3. **Method:** what is actually new? What assumptions and inputs?
4. **Experiments:** which datasets, baselines, metrics, and ablations?
5. **Limitations:** what is not tested or could fail?
6. **Reproduction:** can you implement a small version and match a key result?

Write a one-page paper note:
- question;
- central claim;
- method in your words;
- strongest evidence;
- weakest assumption;
- compute and data needed;
- one ablation you would run;
- whether the result changes your project.

Do not infer that a paper is correct because it is new, popular, or has a high benchmark score. Check whether the comparison is fair and whether the benchmark represents the intended use.

## Design better experiments

Change one important factor at a time when you want causal evidence about a design choice. Keep a validation plan fixed. Run multiple seeds when randomness matters. Report mean and spread, not only the best run. Save configuration, code version, data version, and hardware.

An ablation removes one component to test whether it contributed. A baseline tests whether complexity is necessary. A negative result is useful if the experiment was sound.

## Research reading path

- [Deep Learning](https://www.deeplearningbook.org/) by Goodfellow, Bengio, and Courville: foundational theory and methods.
- [Dive into Deep Learning](https://d2l.ai/) : interactive code, math, and discussions.
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) : the transformer architecture.
- [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401) : an influential RAG formulation.

Read these after the matching lessons, not before your foundations. New papers appear constantly, so use them to learn the method of reading and reproducing research rather than treating any one paper as the final word.

## Review questions with answers

**1. What makes a benchmark result weak evidence?**  
Possible reasons include an unrepresentative dataset, leakage, weak baselines, metric mismatch, repeated tuning on the test set, small samples, or cherry-picked runs.

**2. What is an ablation?**  
A controlled experiment that removes or changes one component to estimate whether it contributes to performance.

**3. How do prediction and causal inference differ?**  
Prediction estimates outcomes from observed patterns. Causal inference estimates the effect of an intervention under additional assumptions. Correlation alone does not establish what an intervention would do.

**4. Why record random seeds and configurations?**  
Training can vary due to data order, initialization, hardware, and software. Recording settings supports comparison and reproducibility, though a seed alone does not guarantee identical results everywhere.

**5. What should an advanced practitioner do when a model fails?**  
Reproduce the failure, categorize it, test hypotheses with controlled experiments, determine whether the issue is data, framing, model, or deployment, and report the limits honestly.

## Practice

Choose one paper from a topic you studied. Write a one-page note, implement a small component, and propose an ablation. Compare your result with a simple baseline.

## Mastery check

Can another person reproduce the central claim of your experiment from your data source, split, metric, code, and configuration? If not, improve the experiment record.