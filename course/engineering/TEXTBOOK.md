# AI engineering and responsible deployment: a textbook volume

A trained model is not yet a dependable product. Its behavior depends on data, preprocessing, code, infrastructure, people, and operational decisions. This chapter follows a model from experiment to release and maintenance.

## 1. The lifecycle

A practical cycle is define the need, govern data, build a baseline, train, evaluate, review risks, deploy, monitor, maintain, and retire. Monitoring may reveal that the original task itself was framed incorrectly. A data pipeline collects and validates examples. A training pipeline creates an artifact. An inference service returns predictions. A registry records model versions and evidence. These can be separate systems or simple scripts, but their responsibilities should be clear.

Record the code revision, data identifier, preprocessing, model, settings, dependencies, and evaluation. Large or private data need controlled storage, not casual source control. Without a link between configuration and result, an experiment is difficult to reproduce.

## 2. Data contracts and tests

Define a training-serving contract for feature names, types, units, order, missing-value handling, and transformations. Validate raw input schema, ranges, missing rates, categories, duplicates, and feature distributions. Validate transformed features too: a correct raw row can become incorrect after preprocessing.

Fit scalers and imputers on training data, then reuse them. Group related examples by person or device when the real task predicts unseen groups. Use chronological splits for future forecasting. A random split is not automatically valid.

## 3. Deployment patterns

Batch inference scores many rows on a schedule and is often easy to retry. Online inference answers one request with low latency and needs timeouts, capacity, and failure behavior. Streaming inference processes continuous events and must handle duplicates, late arrivals, and ordering.

A service contract says what inputs are accepted, what outputs mean, which model version was used, and what happens on timeout or invalid input. A shadow release runs a candidate alongside the current system without changing user decisions. A canary release exposes a small fraction of traffic first. Keep a rollback path and know how downstream actions are reversed.

## 4. Monitoring

Monitor infrastructure: latency, errors, throughput, memory, availability. Monitor data: missing fields, ranges, categories, and distribution changes. Monitor model behavior: prediction distributions and, when labels arrive, real quality. Data drift means the input distribution changed; concept drift means the relationship between inputs and outcomes changed. Drift is a signal to investigate, not automatic proof of failure.

Overall metrics can hide weak slices. Evaluate relevant groups, languages, devices, or conditions, with privacy safeguards and enough sample size. Google production guidance recommends schemas, feature checks, slice metrics, and real-world metrics because the deployed pipeline is larger than the model.

## 5. Security, privacy, and fairness

Threats include poisoned data, stolen credentials, unauthorized access, prompt injection, data exfiltration, model theft, and denial of service. Use least privilege: each system gets only the permissions it needs. Keep secrets out of prompts and repositories. Validate model-produced tool arguments in application code.

Privacy begins at collection. Decide which data is necessary, who can access it, the lawful basis or permission, retention period, and deletion process. Removing names does not guarantee anonymity. Evaluate whether a model can reproduce sensitive training data when relevant.

Fairness requires identifying affected groups and harms with domain expertise. Compare meaningful slice outcomes and error rates. No single metric captures every fairness question; some criteria conflict under differing base rates. Human oversight is useful only if reviewers have context, expertise, time, and authority to change the decision. A model card documents intended use, evaluations, and limits; documentation supports but does not replace safeguards.

## 6. Incident response and change

Before launch, name the owner, pause mechanism, communication path, and evidence needed for an incident review. After a failure, distinguish data, software, model, environment, and product causes. Add a regression check. Retraining should follow evidence and review; new data may introduce bias, licensing issues, or label changes.

## 7. Worked example: ticket priority

A support team wants to rank urgent tickets. Start with the existing queue policy as a baseline. Define costs of missing an urgent issue and the capacity of the review team. Split by time so future tickets remain unseen. Report recall of urgent cases and precision among the top tickets, plus subgroup examples. Run the model in shadow mode and compare its ranking with the existing process. If released gradually, monitor latency, input mix, correction rate, and delayed outcomes. Preserve manual prioritization and rollback.

The launch decision depends on error costs and workflow, not a single metric. A model can be statistically accurate and still be unacceptable if the wrong people bear its errors.

## 8. Questions and practice

Does deployment finish the project? No; data, users, and software change. Is drift the same as failure? No; outcome evidence is needed. Does “human in the loop” guarantee safety? No; oversight needs context and authority.

Practice: make a launch checklist for a maintenance-request ranking model. Include data tests, time and group splits, error costs, slices, service limits, monitoring, escalation, and rollback.

Further reading: [Google ML monitoring](https://developers.google.com/machine-learning/crash-course/production-ml-systems/monitoring), [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework), and [OWASP LLM security](https://owasp.org/www-project-top-10-for-large-language-model-applications/).

## 9. A model release checklist explained

Before release, answer these questions in writing:
- What user need does this address, and what is the existing baseline?
- What input schema and prediction contract does the service guarantee?
- What data and model versions produced this artifact?
- Does evaluation simulate deployment and include meaningful slices?
- What error costs, privacy risks, security threats, and licensing restrictions remain?
- Who owns the system and receives alerts?
- Can the service be paused or rolled back?
- What human process handles uncertainty and appeal?

A checklist does not make every answer good, but it prevents hidden assumptions from becoming permanent production behavior. For a high-impact system, domain and legal review may be needed before any technical release decision.

## 10. Data and model versioning

Version code in Git, data with an immutable identifier or snapshot, and model artifacts with a registry or checksum. Record preprocessing alongside the model because a model without the transformation pipeline is incomplete. Keep evaluation reports linked to the exact artifact. A registry can track candidate, approved, deployed, and retired states.

Do not silently overwrite a model. A versioned release supports rollback and lets investigators reconstruct which output was produced by which model. Preserve only logs needed to diagnose the system, with appropriate access and retention controls.

## 11. Reliability and service-level thinking

A service-level objective might state that 99% of valid requests complete within a latency budget. The objective should reflect user need, not an arbitrary dashboard target. Define timeouts, retries, circuit breakers, and fallback responses. Retrying a non-idempotent tool call can create duplicate actions. Load testing should include realistic input sizes and concurrent traffic.

A model endpoint can be unavailable while a product remains useful if a fallback exists: a rules-based path, cached result, manual queue, or clear error. A stale result should be labeled as stale. Monitor both successful request rate and the quality of the returned result.

## 12. Monitoring and retraining triggers

Monitor input schema violations, shifts in important features, output distribution, human overrides, delayed labels, and outcome metrics. Data drift and concept drift are diagnostic signals. Define thresholds and an owner for investigation. An alert without an action plan creates noise.

Retraining requires fresh representative data and valid labels. New data may encode changed policies or historical harm. Compare the new candidate with the current model on a fixed evaluation, inspect slices, and review downstream behavior. Do not automatically retrain and deploy without validation merely because a schedule fired.

## 13. Responsible-AI review

Identify affected people, potential benefits and harms, who can contest an outcome, and how the system affects access or opportunity. Review performance across relevant slices, privacy, security, transparency, human oversight, and accessibility. A model card describes intended use and limits; a data sheet describes collection and composition. These documents are useful only if maintained as the system changes.

Questions: What does least privilege mean? Grant only necessary permissions. Why use shadow deployment? It tests a candidate on live-like inputs without changing decisions. Why can monitoring an average be insufficient? A subgroup can fail while the overall metric looks stable.

Practice: write a release review for a ticket triage model, including rollback owner, metric thresholds, slice monitoring, privacy, and appeal.

Further reading: [Google production ML monitoring](https://developers.google.com/machine-learning/crash-course/production-ml-systems/monitoring) and [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework).

## 14. Continuous integration for ML

A CI pipeline can run code style checks, unit tests, data-schema tests on a small fixture, model-loading checks, and evaluation regression tests. It should not require private production data. A candidate model can be compared against a fixed baseline and held-out evaluation. A regression threshold should account for normal variability and should not automatically approve a deployment.

Data tests should validate feature transformations, missing values, category ranges, and output shapes. Integration tests can verify that a request moves through preprocessing, model inference, and response serialization. Security checks should reject unauthorized fields and malformed tool requests. Keep a reproducible artifact so a released version can be rebuilt or retrieved.

## 15. Model-serving architecture

A typical path is client request → authentication and validation → feature transformation → model inference → policy layer → response. Each boundary should have a clear schema and failure mode. A policy layer may apply thresholds, constraints, access checks, or human review. Do not embed authorization only in the model prompt.

For online systems, plan capacity using traffic and model latency. Batching can increase throughput but may delay a request while waiting for a batch. Quantization or smaller models can reduce serving cost but require quality evaluation. Cache only outputs whose freshness and permissions permit reuse. Include model version in internal logs for diagnosis.

## 16. Monitoring, fairness, and feedback loops

Prediction monitoring alone is not outcome monitoring. Confidence may stay stable while actual quality deteriorates. Labels can arrive months later; define a proxy carefully and update it when real outcomes become available. Human overrides may signal problems but are also influenced by workload and policy.

When a recommendation changes exposure, that exposure affects future data. When an eligibility model changes who receives an offer, the labels observed later are selected by prior decisions. This feedback loop means future training data is not a neutral sample. Record interventions and design monitoring to distinguish model behavior from policy behavior.

## 17. Security review for LLM applications

Treat prompts, retrieved documents, and tool outputs as untrusted. Apply least-privilege credentials, enforce authorization outside the model, validate outputs, constrain network access, and prevent secret leakage. Tool execution should be allow-listed and bounded. Store sensitive logs only when necessary and protect them.

Test indirect injection from documents, attempts to reveal hidden prompts, unauthorized tool calls, malicious file contents, and denial-of-service inputs. A refusal on a test prompt does not prove the app is secure; verify the underlying service rejects unauthorized actions.

Questions: Why use CI for models? It catches code and data-contract regressions before release. Why do outcomes arrive late? Many real labels are only observed after the prediction's consequence. Why is model confidence not sufficient monitoring? Calibration and real-world outcomes can change while score distributions look similar.

Practice: draw a serving architecture for an LLM assistant and label trust boundaries, credentials, permission checks, logging, failure modes, and rollback.
