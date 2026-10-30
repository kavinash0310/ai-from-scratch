# Lesson 10 — Building generative AI applications

## Learning goals

Choose when to use a prompt, retrieval, tools, or fine-tuning; build an evaluation set; and identify common security and reliability failures.

## Start with a system, not a prompt

A generative AI application includes more than a model. It may include user input, validation, retrieval, tool calls, model inference, output checks, a user interface, logging, and human review.

Define the task and success criteria before selecting a model. Decide what the system may answer, what it must refuse, and how a user will verify its work.

## Prompting

A prompt provides instructions and context at inference time. Better prompts can clarify role, task, constraints, examples, and output structure. Structured output formats can make results easier to validate.

Prompts do not guarantee obedience or factuality. Try examples that are ambiguous, adversarial, out of scope, and malformed. Treat user content as untrusted data.

## Retrieval-augmented generation

Retrieval-augmented generation (RAG) finds relevant external passages and provides them to a language model as context. A basic pipeline:

1. Collect approved documents.
2. Split them into chunks with enough surrounding context.
3. Convert chunks to embeddings.
4. Index the embeddings and associated source metadata.
5. Embed a question and retrieve likely relevant chunks.
6. Optionally rerank retrieved chunks.
7. Ask the model to answer using the sources.
8. Return citations and evaluate whether they support the answer.

RAG can make a model use a curated knowledge base and can provide provenance. It does not automatically solve hallucination. Retrieval can miss the right passage, the model can misread it, and a citation can be irrelevant. Evaluate retrieval quality and answer quality separately.

## Tool use and agents

A tool-enabled model can request actions such as search, calculation, or database lookup. The application should validate tool names, arguments, permissions, and results. A model should not receive unrestricted access to secrets or irreversible actions.

An “agent” usually means a loop in which a model selects actions, observes results, and continues toward a goal. Loops can fail, spend too much, or repeat unsafe actions. Add limits on steps, time, tool scope, and spend; log important decisions; use human approval for high-impact actions.

Use a simple deterministic workflow when it meets the need. Autonomy adds complexity and attack surface.

## Fine-tuning and adapters

Fine-tuning can adapt a model to a repeated task, response format, or domain style. Parameter-efficient methods update a smaller set of weights or add adapters, reducing resource requirements. Fine-tuning is not the first choice for facts that change often; retrieval is often easier to update and cite.

A good fine-tuning dataset needs quality, permission, representative examples, clear desired behavior, and held-out evaluations. Training on synthetic examples does not remove the need to check whether those examples are correct and diverse.

## Evaluation

Build a small evaluation set before tuning the system. Include:
- normal examples;
- edge cases;
- unanswerable questions;
- ambiguous requests;
- harmful or disallowed requests;
- examples designed to trigger prompt injection;
- expected sources or actions.

Score dimensions separately: answer correctness, evidence support, relevance, format validity, refusal quality, latency, and cost. Automated evaluators can help scale checks, but validate them against human judgments.

For RAG, measure whether relevant evidence was retrieved, whether the response used it correctly, and whether citations point to support. For tool use, test permission boundaries and invalid tool results.

## Security and privacy

Treat documents and user messages as data, not trusted instructions. Retrieved content may contain prompt injection. Keep credentials outside prompts and model context. Restrict tools to the minimum permissions. Avoid logging private data unnecessarily, define retention rules, and test deletion pathways.

## Review questions with answers

**1. When might RAG be preferable to fine-tuning?**  
When answers need current or private approved documents, citations, or easy updates. RAG supplies content at inference time rather than relying only on stored weights.

**2. Does RAG guarantee a correct answer?**  
No. Retrieval can find the wrong passages, and the model can misinterpret or ignore good evidence. Evaluate each part.

**3. What is prompt injection?**  
An attack where untrusted input tries to override intended instructions or misuse tools. A prompt alone is not a security boundary.

**4. Why limit agent tools and actions?**  
Models can choose incorrect actions or loop. Least-privilege permissions, budgets, step limits, and human approval reduce possible harm.

**5. Why keep an evaluation set before improving the prompt?**  
Without fixed examples, a change may help a few visible prompts while breaking other cases. A stable evaluation set reveals regression and supports fair comparison.

## Practice

Build a question-answering prototype over a small set of non-sensitive documents. Record 20 questions, expected source passages, and acceptable answers. Include unanswerable and adversarial questions. Measure retrieval and answer quality separately.

## Mastery check

Explain why your application needs its chosen method, how each component fails, what evidence a user receives, and what the system does when it is unsure.