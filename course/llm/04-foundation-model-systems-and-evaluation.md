# LLM systems: pretraining, scaling, and reliable evaluation

> **Place in the course:** Advanced LLM study after attention, inference, and adaptation. A foundation model is both a learned function and a data-processing system.

## Pretraining data

A corpus can contain licensed, public, and curated sources. Collection does not establish permission. Deduplication reduces repeated examples; filtering attempts to remove low-quality material; normalization and tokenization form sequences. These choices influence language coverage, memorization, bias, and contamination of later benchmarks.

Training examples are token sequences with next-token targets. Packing long documents reduces wasted context but boundaries must not accidentally leak across examples. Data mixtures and sampling weights affect what is learned. Capability cannot be inferred from parameter count alone.

## Compute and distributed concepts

Training repeatedly performs matrix operations, gradient computation, and optimizer updates. Data parallelism replicates a model and synchronizes gradients. Tensor parallelism splits large operations; pipeline parallelism splits layers across devices. Sharding reduces memory per device. Communication, utilization, checkpointing, and fault recovery become part of the system.

Cost depends on model parameters, tokens, context length, batch, precision, hardware, and training efficiency. Most learners should train a tiny language model on a toy corpus to see tokenization, causal masks, loss curves, checkpoints, and sampling. That teaches mechanics without implying a reproduction of frontier-scale training.

## Scaling and evaluation

A scaling trend is empirical under a particular regime; it is not a guarantee outside the measured range. Benchmarks can be contaminated by training data. Prompt formatting, answer extraction, tools, and judge quality affect scores.

Evaluate the application with representative users, answerable and unanswerable cases, adversarial inputs, evidence requirements, latency, and cost. Use human review when automatic metrics are weak. Preserve model identifiers and prompt versions because hosted systems may change.

Worked example: For a course tutor, ask held-out questions with supporting passages, uncovered questions, and hostile instructions inside retrieved text. Score correctness, evidence support, citation precision, abstention, and latency. Measure retrieval separately from generation.

**Questions:** Why deduplicate? Repeated content can dominate learning and distort evaluation. Why are benchmark scores protocol-dependent? Data, prompts, scoring, and tools change results. Why train a tiny model? It makes the mechanics observable.

**Practice:** Compare two assistants on the same test cases. Report model version, test design, citations, refusal behavior, injection results, p95 latency, and per-task cost.

Further reading: [Stanford CS324](https://stanford-cs324.github.io/winter2022/) and [NIST Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf).
