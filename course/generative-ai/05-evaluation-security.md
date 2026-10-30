# Chapter 5 — Generative system evaluation and security

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

## Build a fixed test set

A generative app needs examples of ordinary, ambiguous, unanswerable, malformed, adversarial, and high-risk inputs. Define expected behavior, not only expected text. Measure correctness, grounding, format validity, refusal, tool success, latency, and cost separately.

Keep a record of model and prompt versions. A change should run through the same test set to reveal regression. Human reviewers need a rubric, examples, and a process for disagreements.

## Prompt injection and data handling

User messages, web pages, and retrieved documents are untrusted. Instructions embedded in content may try to override system behavior. Separate trusted instructions from data, restrict tool permissions in code, and never place secrets in prompts.

Minimize logs, redact sensitive information, set retention periods, and control access. Model outputs may reproduce sensitive training data or harmful associations; test plausible abuse and apply appropriate limits.

## Deeper walkthrough: score a document assistant

Create a small gold set with questions, relevant passages, acceptable answers, and cases that cannot be answered. For each question, measure whether retrieval included the needed passage, whether the generated claims are supported, and whether the citation points to the right section.

Include adversarial cases: a document asks the model to ignore its rules; a question requests another user's private record; a query contains unsupported assumptions. The expected behavior may be refusal, permission check, or explicit uncertainty.

Run the same suite after changing prompt, model, chunking, or embedding model. Track regressions by category rather than averaging them away. A single unsafe permission failure may matter more than many low-risk wording improvements.

Keep evaluation documents synthetic or approved; do not copy private user records into a public test suite.

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