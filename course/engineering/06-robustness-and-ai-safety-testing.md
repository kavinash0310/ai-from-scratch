# AI engineering: robustness and safety testing

> **Place in the course:** Advanced deployment study. Test for accidental change and purposeful misuse; safety evidence must match the system and its impact.

## Robustness beyond an average

A held-out score describes one sample and distribution. Distribution shift occurs when deployment inputs differ. Out-of-distribution cases lie outside training support. Test realistic changes: new devices, image quality, languages, seasons, rare labels, and corrupted input. These tests can reveal failures; they cannot prove all failures are absent.

Measure subgroup sample counts with metrics. A result from five examples has high uncertainty. Define important slices before looking at results when feasible.

## Security and adversarial testing

An adversarial example is an input designed or unintentionally changed to trigger an error. In language applications, prompt injection tries to manipulate instructions or tools. Test the system boundary: can untrusted content cause unauthorized actions or disclosure?

Map assets, trust boundaries, actors, and consequences. Enforce authorization in services, validate inputs and outputs, restrict permissions, limit network access, and protect secrets. A refusal in model text is not proof that the application enforced access control.

## Red teaming and safety cases

A red-team exercise tests defined misuse and failure patterns. Set scope, collect reproducible cases, rank severity, fix issues, and retest. Cases may include data leakage, unsafe advice, discriminatory errors, denial of service, tool abuse, or supply-chain compromise.

A safety case links a claim, argument, and evidence. Claim: “The assistant cannot execute a purchase without confirmation.” Evidence: service authorization tests, adversarial tool-call tests, code review, and observed confirmation flow. This is more concrete than saying the model is safe.

NIST AI RMF organizes work around governing, mapping, measuring, and managing risk. Update evaluations when data, tools, or user groups change.

**Questions:** Does passing a red-team set prove safety? No; only the tested behaviors have evidence. Why separate refusal from tool access? The model can be manipulated; code must enforce permissions. Why report slice sample counts? They affect how much to trust subgroup results.

**Practice:** Threat-model a private document assistant. List assets, trust boundaries, attacker goals, permission controls, tests, owners, and incident response.

Further reading: [NIST AI RMF Core](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) and [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/).

## Design a threat model

List assets such as private documents, credentials, user records, and tool actions. Identify trust boundaries between user input, retrieval, model, tool, and database. For each boundary ask what an attacker or accidental failure could do, what permission is needed, and what evidence would detect it.

A useful test matrix covers:
- malformed or extreme inputs;
- data distribution shift and rare subgroups;
- direct and indirect prompt injection;
- unauthorized document retrieval;
- tool arguments outside their schema;
- secret disclosure attempts;
- denial-of-service inputs and repeated tool loops;
- dependency, model, and data provenance.

Each test should specify setup, expected behavior, actual result, severity, and owner. Repeat tests after changes to prompts, models, retrieval, tools, or access controls.

## Robustness and fairness evidence

Robustness is not a single number. Test across realistic changes and report where performance changes. For a language model, test spelling, dialect, code-switching, and long context. For computer vision, test lighting, resolution, occlusion, and camera. For a credit or eligibility model, inspect relevant groups and whether false decisions can be appealed.

Subgroup metrics require adequate sample sizes and privacy protection. A gap can arise from data quality, label definitions, measurement, or model design. The review should involve people who understand the domain and those affected by the outcome. A mitigation can shift errors elsewhere, so retest after changes.

## From finding to release decision

Classify a finding by likelihood, severity, exposure, and reversibility. A low-severity error in a reversible recommendation is different from a high-severity error in medical triage. Possible responses include fixing, restricting, adding human review, improving monitoring, delaying release, or documenting a bounded residual risk.

A safety case links a claim to arguments and evidence. Example claim: “The assistant cannot execute a purchase without user confirmation.” Evidence might include application-level permission checks, tests of malformed model output, red-team prompts, and reviewed logs. The model's verbal promise is not sufficient.

Practice: run a small red-team exercise on a document assistant. Try an instruction embedded in a retrieved document that requests another user's files. Verify the retrieval service denies access even if the model follows the malicious instruction. Record evidence and a regression test.

Further reading: [NIST AI RMF Measure](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/) and [OWASP LLM Top 10](https://owasp.org/www-project-top-10-for-large-language-model-applications).
