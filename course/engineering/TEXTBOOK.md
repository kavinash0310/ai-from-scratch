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
