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

## 9. Statistical interpretation without overclaiming

An observed improvement can arise from a real effect, random variation, data leakage, measurement error, or a changed evaluation protocol. Report sample size and uncertainty. If multiple models or prompts were tried and only the winner is reported, the apparent improvement may be optimistic. Predefine comparisons when feasible and disclose deviations.

A p-value is not the probability that a hypothesis is true. It is calculated under a null model and assumptions. Statistical significance does not imply a practically important improvement. A one-point gain may not justify much higher latency or cost. For operational decisions, report effect size, uncertainty, and practical trade-offs.

## 10. Dataset and split audit

For each data source, record how examples were collected, who is represented, what labels mean, how missingness occurs, and any known exclusions. Check duplicates and near-duplicates before splitting. If the same person contributes several records, a random row split may leak identity. If predicting future events, preserve time order. If data comes from multiple sites, consider a held-out site to assess transfer.

Keep a test set untouched by iterative choice. If the sample is too small for a stable holdout, use cross-validation or a carefully designed resampling plan and state limitations. A split should match the generalization claim: new examples, new people, future time, or new sites are different targets.

## 11. Reproduction versus replication

Reproduction attempts to obtain the same result using the original data and method. Replication tests whether a claim holds in a new setting or with an independent implementation. Both require precise details. Missing preprocessing or undocumented filtering may explain why a paper's headline number cannot be reproduced.

Record exact library versions, checkpoint identifier, preprocessing, compute, seeds, prompts, and metric implementation. Preserve raw outputs and environment manifests. If the result differs, investigate systematically rather than adjusting until the number matches.

## 12. Capstone quality rubric

A strong capstone:
- defines a real task and affected users;
- documents provenance and rights for data;
- includes a simple baseline;
- uses a split that prevents leakage;
- selects metrics tied to decision costs;
- analyzes representative mistakes and relevant slices;
- explains security, privacy, and misuse risks;
- provides reproducible setup and a usable demo;
- states limits and gives a justified release recommendation.

A weak capstone often has a flashy interface but no held-out evaluation, unclear labels, or no baseline. The purpose of the rubric is to reward evidence and reasoning, not complexity.

## 13. Oral defense questions

What does one test example represent? Why was the split chosen? What result would falsify the claim? Which failure is most costly? How would the system behave if evidence is missing? What part of the pipeline is hardest to reproduce? What would change your deployment decision? A learner should answer from project evidence, not from general slogans.

Practice: write a one-page proposal, then ask a peer to find leakage and alternative explanations. Revise the protocol before running expensive experiments. At the end, publish a short report with one successful result, one failed result, and one important uncertainty.

Further reading: [Stanford CS229](https://cs229.stanford.edu/), [ACM artifact review guidance](https://www.acm.org/publications/policies/artifact-review-and-badging-current), and [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework).

## 14. A week-by-week capstone plan

**Week 1: proposal and scope.** Interview or study the intended user needs without collecting unnecessary sensitive information. Write the task, constraints, baseline, success metric, and failure costs. Decide whether the project is feasible with available data and compute.

**Week 2: data audit.** Record sources, permissions, label meanings, missingness, duplicates, and group structure. Inspect examples. Write the split rule before modeling. If the data is too small or unsuitable, narrow the question.

**Week 3: baseline.** Build the simplest useful method. Save predictions and errors. A baseline may be a rule, keyword search, majority class, last-value forecast, or existing human process.

**Week 4: candidate method.** Implement one improvement and keep other conditions controlled. Record parameters, versions, runtime, and failures.

**Week 5: evaluation and error analysis.** Run the planned validation and final test. Inspect examples, subgroups, and uncertainty. If you change the method after seeing test results, mark that test as no longer untouched.

**Week 6: product and report.** Build a reproducible interface, document limitations, and present the deployment or non-deployment decision. A realistic capstone may take longer; schedule is an example, not a quality shortcut.

## 15. Make claims proportional to evidence

A descriptive claim says what happened in the observed data. A predictive claim says how well a method predicts under a defined evaluation. A causal claim says an intervention changed an outcome and requires a causal design. Do not use “because” when the study only shows association.

Report the baseline, sample size, protocol, uncertainty, and errors. If many configurations were tried, describe the search and selection process. If human ratings are used, explain annotator instructions, disagreement, and whether raters were blinded to system identity. If an evaluation set was generated by the same model being evaluated, recognize possible judge bias and supplement it with independent review.

## 16. Open research artifacts responsibly

A reproducibility package might include source code, environment file, configuration, synthetic or permitted data sample, instructions, evaluation script, and expected outputs. It should not include personal data, secrets, unauthorized checkpoints, or licensed material that cannot be redistributed. If data cannot be shared, provide a data-access description and a safe mock fixture.

A clean repository has a clear README, one-command setup where feasible, documented assumptions, and stable links. Reproducibility is more than a notebook that runs on its author's machine. Another learner should know which commands to run and what output to expect.

Practice: write a two-paragraph abstract for a hypothetical project. The first paragraph states question, data, and method. The second reports the actual result, uncertainty, key limitation, and what evidence would be needed next. Avoid unmeasured claims.
