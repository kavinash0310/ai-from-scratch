# AI research and capstone practice: a textbook volume

Research is a disciplined process for answering a question with evidence. It need not invent a new architecture. Careful replication, error analysis, measurement, and documentation of limitations are meaningful work.

## 1. Make the question testable

“Use AI to improve education” is an interest, not a testable question. Specify a task, users or population, comparison, outcome, and conditions. For example: “On a fixed set of beginner Python questions, does a retrieval assistant cite course material more accurately than a model-only baseline?” State what result would support or weaken the hypothesis before inspecting results.

List alternative explanations. Perhaps the retrieval system wins because it receives more context, not because retrieval is inherently superior. Perhaps test questions duplicate training examples. A careful experiment isolates the intended claim and states what it cannot establish.

## 2. Read research papers

A paper usually contains an abstract, introduction, related work, method, experiments, results, limitations, and references. First identify the claim. Then inspect data, split, baseline, metric, sample size, uncertainty, code availability, and limitations. Ask what exact task and population were evaluated and whether the data resembles the intended use.

A benchmark score is evidence under a protocol, not a universal ranking. Scores from different datasets, prompts, compute budgets, or metric implementations may not be comparable. Find follow-up work and independent replications when the claim matters.

## 3. Reproducible experiments

Record code revision, dataset version or identifier, preprocessing, model, hyperparameters, seed, hardware, software versions, and evaluation procedure. Preserve all planned runs, not only the best number. Seeds help control randomness but cannot promise identical outcomes across hardware and software. Record failed runs; they can expose instability.

For pretrained models and datasets, track licenses, provenance, restrictions, and transformations. Do not publish private examples or secrets in notebooks. Avoid redistributing data without rights.

## 4. Fair comparisons and error analysis

Keep splits, tokenization, training budgets, and metrics consistent. Tune methods using comparable validation procedures. Use a suitable baseline: constant predictor, simple rule, linear model, keyword search, or existing workflow.

Repeatedly changing choices based on test performance turns the test set into validation data. If this happened, describe it and use a new holdout for a final estimate. With small samples, report uncertainty and avoid strong claims over tiny differences.

Inspect false positives and false negatives. Categorize errors and check whether labels are ambiguous. An ablation removes one component to ask whether it contributes. For a retrieval assistant, compare retrieval disabled and enabled while keeping the model and evaluation fixed.

## 5. Ethics and writing

Check whether data involves people, sensitive information, or consequential decisions. Follow relevant review, consent, privacy, and licensing rules before collecting it. Publicly accessible does not automatically mean appropriate to reuse. Minimize collection, control access, set retention, avoid identifiable examples, and consider who bears errors.

A clear report includes problem, scope, data and rights, split, baseline, method, metrics, results, uncertainty, error analysis, limitations, intended use, and reproduction instructions. Phrase claims to match evidence: “Method A scored higher on metric M on this evaluation” is more defensible than “A is smarter.”

## 6. Capstone workflow

A capstone should demonstrate an end-to-end skill: frame the task, inspect data, build a baseline, select a model, evaluate, analyze errors, document limitations, and explain a deployment or non-deployment decision.

1. Write a one-page proposal with user, problem, constraints, and success criteria.
2. Inspect data and document provenance and gaps.
3. Build a baseline and save results.
4. Create leakage-resistant train, validation, and test partitions.
5. Improve one component at a time.
6. Analyze errors and important slices.
7. Build a reproducible interface or command-line workflow.
8. Document setup, assumptions, risks, limitations, and next experiments.
9. Demo the system and answer questions about failure cases.

A project is complete when another learner can reproduce the main result and understand how it might fail. A polished interface cannot substitute for sound evaluation.

## 7. Worked capstone: course-question assistant

The goal is to answer questions using a bounded course corpus. Baseline one returns a keyword-matched passage. A second system uses semantic retrieval plus a language model. Test cases include answerable questions, missing-evidence questions, and malicious instructions inside retrieved text. Measure retrieval recall at k, answer support, citation accuracy, abstention when evidence is absent, latency, and cost.

Prevent near-duplicate questions from crossing train and test. Review document rights and private data. Categorize failures as retrieval failure, unsupported generation, or bad citation. Report which system performed better under the protocol, without claiming it can answer arbitrary questions reliably.

## 8. Questions

Must research invent an algorithm? No; replication and careful measurement can be valuable. Why have a baseline? It shows whether complexity adds value. Does statistical significance prove practical benefit? No; it depends on assumptions and does not establish impact or good data. Should only the best run be reported? No; that hides variability and selection bias.

Practice: write a research question, hypothesis, baseline, split, metric, alternative explanation, and a result that would count against your preferred method.

Further reading: [Stanford CS229](https://cs229.stanford.edu/), [ACM artifact review](https://www.acm.org/publications/policies/artifact-review-and-badging-current), and [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework).
