# Chapter 5 — Generative system evaluation and security

## Build a fixed test set

A generative app needs examples of ordinary, ambiguous, unanswerable, malformed, adversarial, and high-risk inputs. Define expected behavior, not only expected text. Measure correctness, grounding, format validity, refusal, tool success, latency, and cost separately.

Keep a record of model and prompt versions. A change should run through the same test set to reveal regression. Human reviewers need a rubric, examples, and a process for disagreements.

## Prompt injection and data handling

User messages, web pages, and retrieved documents are untrusted. Instructions embedded in content may try to override system behavior. Separate trusted instructions from data, restrict tool permissions in code, and never place secrets in prompts.

Minimize logs, redact sensitive information, set retention periods, and control access. Model outputs may reproduce sensitive training data or harmful associations; test plausible abuse and apply appropriate limits.

## Questions and answers

**What is prompt injection?**  
Untrusted text attempts to manipulate the model into ignoring intended instructions or misusing tools.

**Can system prompts alone secure an agent?**  
No. Security depends on permissions, validation, isolation, monitoring, and human review, not just instructions.

**Why separate quality dimensions?**  
A response can be correct but poorly cited, safe but unhelpful, or formatted correctly but false. One score hides these distinctions.

**What should happen when the model is uncertain?**  
The system should request more information, retrieve additional evidence, abstain, or escalate, depending on the task.

## Practice and mastery

Write a threat model and evaluation plan for a RAG or agent prototype. Include expected misuse, sensitive data, tools, permission boundaries, test cases, reviewer, alert, and rollback step.