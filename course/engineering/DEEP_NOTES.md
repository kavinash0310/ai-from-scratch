# AI engineering and responsible deployment — full beginner notes

An ML model becomes a dependable service only when software, data, permissions, evaluation, and operations work together.

## 1. MLOps and deployment

**MLOps** applies software and operations practices to ML systems. A pipeline may collect and validate data, train a model, evaluate it, register artifacts, deploy a version, and monitor outcomes. An **artifact** is a versioned output such as weights, tokenizer, schema, or report. A **model registry** records versions and metadata. **Deployment** makes a version available to an application.

Training code should record data version, preprocessing, random seeds, dependencies, configuration, and metrics. A model file without its tokenizer and preprocessing may be unusable. Use a reproducible environment and automate checks. A **canary release** sends a small share of traffic to a new version; **rollback** returns to a previous safe version.

Latency, throughput, memory, availability, and cost are product constraints. Batch processing and online prediction have different needs. Secure secrets and limit service permissions. Separate model output from application decisions so thresholds and policy can be reviewed.

## 2. Monitoring and maintenance

Monitoring has three layers: service health (errors, latency, uptime), data health (schema, missingness, ranges, distribution changes), and model/product outcomes (quality, subgroup impact, user corrections). **Data drift** is input distribution change; **concept drift** is change in the relationship between inputs and target. Drift alerts do not prove quality is worse; validate with labels and context.

A **feedback loop** collects new outcomes, triages them, updates data, retrains if justified, evaluates, and rolls out a new version. Keep a fixed evaluation suite to catch regressions. Monitor meaningful slices without exposing private data unnecessarily. Define an owner and incident response procedure before deployment.

## 3. Responsible AI, security, and privacy

**Fairness** concerns whether errors and benefits are distributed acceptably; no single metric answers every fairness question. Define affected groups, harms, obligations, and context with stakeholders. **Explainability** can mean global behavior, local explanations, or actionable reasons; an explanation method can be approximate.

**Privacy** protects people and sensitive information. Minimize collection, restrict access, define retention, and assess whether training or prompts could reveal personal data. **Security** includes poisoning, extraction, prompt injection, unauthorized tool access, and supply-chain risks. Apply least privilege, validate input/output, and isolate untrusted content.

A **risk assessment** documents intended use, affected people, foreseeable misuse, severity, likelihood, mitigations, owners, and residual risk. Human review helps when reviewers have context, authority, and time to act. A checkbox is not a safety program.

### Q&A and deployment exercise

**Should every drift alert trigger retraining?** No. Investigate whether the shift is real, relevant, and supported by enough labels.
**Is a human reviewer automatically protective?** No. Design clear criteria, manageable workload, and an escalation route.
**What should a release record include?** Model/data versions, tests, known limitations, owners, monitoring, and rollback instructions.

Exercise: deploy a small model behind a test API. Add input validation, version metadata, latency logging, a fixed evaluation set, a rollback plan, and a short risk review. Continue to [research and capstone](../research/README.md).