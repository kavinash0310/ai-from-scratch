# Chapter 3 — Responsible AI, security, and privacy

> **Book-length subject volume:** For expanded explanations, worked examples, review questions, and practice, read the [engineering textbook](TEXTBOOK.md).

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

## Map impact through the lifecycle

Ask who uses the system, who is affected, who benefits, who bears errors, and who can contest a decision. Validity, reliability, safety, security, privacy, transparency, and fairness are ongoing concerns.

The NIST AI Risk Management Framework organizes activities as Govern, Map, Measure, and Manage. It supports structured risk work; check the current version and companion resources because the framework evolves.

## Privacy and security

Collect the minimum data needed. Document source, permission, retention, and deletion. Restrict access and protect secrets. Avoid storing private prompts unless there is a justified and protected purpose.

Threat-model data poisoning, prompt injection, unauthorized tool use, model inversion, membership inference, and exposure of confidential information. Enforce permissions in code, not prompts.

## Human oversight

Human review only helps when reviewers have time, training, authority, and evidence. Define escalation and appeal paths. Communicate limitations in terms users can act on.

## Deeper walkthrough: risk analysis for an AI support assistant

Map who interacts with the assistant, what documents it can read, and which tools it can call. A prompt injection in a retrieved page could ask it to reveal private instructions or send customer data elsewhere. The system should treat retrieved text as untrusted, limit tools to read-only when possible, and enforce access in code.

For privacy, identify personal information in prompts and logs. Remove what is unnecessary, set a deletion schedule, and restrict log access. For fairness, test quality across languages and user groups the product claims to support.

Governance needs owners: who approves a model update, handles a complaint, investigates an incident, and can disable the system? A risk register should have likelihood, impact, mitigation, evidence, and residual risk.

Risk review is continuous because data, users, model versions, and external threats change.

## Questions and answers

**Does fairness have one universal metric?**  
No. Metrics can conflict and depend on context, group definitions, and policy choices. Explain the selected criteria and limitations.

**Why does prompt injection count as a security issue?**  
Untrusted content can try to alter model behavior or induce tool misuse. System instructions alone are not an authorization boundary.

**What is meaningful human oversight?**  
A reviewer can understand relevant evidence, disagree, and change the outcome, with enough time and accountability.

## Practice and mastery

Write a risk register for one project: affected people, harms, controls, measurement, owner, appeal path, and shutdown trigger. Add one adversarial security test and one privacy check.