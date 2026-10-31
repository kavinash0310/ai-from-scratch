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

## Data contamination and benchmark interpretation

A benchmark may overlap with pretraining or fine-tuning data. Exact overlap is not the only concern: paraphrases or explanations may have been seen. Contamination can inflate scores without the model being able to generalize as intended. Use newly written or private evaluation examples when a decision depends on them, and vary wording while preserving the task.

A benchmark score also depends on prompting, context, decoding, tool access, answer extraction, and judge model. Keep a reproducible harness and report these details. Automated judges can favor stylistic similarity or share errors with the model being evaluated; audit a sample with independent human reviewers.

## End-to-end assistant evaluation

For a course assistant, separate:
1. retrieval quality: did the correct passage appear in top k?
2. answer support: does each claim follow from the retrieved evidence?
3. citation correctness: does each link support the attached claim?
4. abstention: does the system say evidence is missing?
5. behavior: does it resist instructions inside untrusted documents?
6. operation: are latency, availability, and cost acceptable?

This decomposition turns a vague “quality” failure into an actionable diagnosis. Keep held-out examples, but add new regression cases when real failures occur.

## Model and dataset documentation

Record model identifier, version or revision, tokenizer, context limit, modality, license, source of fine-tuning data, and known evaluation limits. A hosted endpoint may change without local code changing, so capture an evaluation snapshot and date. Do not assume open weights imply open data or unrestricted use.

Practice: prepare 20 questions: five directly answerable, five requiring synthesis across passages, five outside the corpus, and five with malicious retrieved instructions. Set pass criteria for answer support, citation, abstention, tool use, latency, and cost before testing.

Further reading: [Stanford HELM benchmark](https://crfm.stanford.edu/helm/latest/) and [NIST Generative AI Profile](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf).
