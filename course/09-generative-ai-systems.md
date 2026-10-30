# Part 9 — Generative AI systems

## Chapter 43 — Prompting and structured outputs

A prompt is input context, not a security boundary. State the task, provide relevant information, define output format, and give examples where useful. Ask the model to distinguish evidence from assumptions and to say when the source does not answer.

Validate structured outputs with a parser and schema. If a model returns a date, amount, or action, check type, range, permissions, and business rules in ordinary code. Do not trust formatting alone.

Prompt evaluation should include normal, ambiguous, adversarial, and out-of-scope cases. A prompt change that improves one sample can regress others.

## Chapter 44 — Retrieval-augmented generation (RAG)

RAG retrieves external text and supplies it to a language model during generation. A system can be refreshed by updating the document index rather than retraining model weights. The original [RAG paper](https://arxiv.org/abs/2005.11401) combined parametric model memory with a non-parametric document index.

```mermaid
flowchart LR
    A[Approved documents] --> B[Clean and chunk]
    B --> C[Embed and index]
    D[User question] --> E[Retrieve relevant chunks]
    C --> E
    E --> F[Compose grounded prompt]
    F --> G[Generate answer with source IDs]
    G --> H[Check evidence and format]
```

Chunk size, overlap, metadata, embedding model, filters, and reranking affect retrieval. Too-small chunks lose context; too-large chunks add noise. Evaluate retrieval recall separately from answer correctness. A citation is useful only if it supports the claim.

## Chapter 45 — Tool use and agents

A model can request a tool call, such as calculator, search, or database query. Your application executes it, returns the result, and may ask the model to continue.

An agent is often a repeated loop of goal interpretation, action selection, tool result, and next action. Loops introduce failure modes: repeated calls, wrong assumptions, prompt injection, excess cost, or unsafe side effects.

Use the least powerful tool interface that works. Limit tools, input types, time, steps, and budget. Validate every argument. For sending messages, spending money, deleting data, or changing access, require a human approval step in the product.

## Chapter 46 — Fine-tuning, adapters, and model choice

Fine-tune when you have a stable task and enough high-quality examples to demonstrate the desired behavior. LoRA freezes most base weights and learns low-rank updates, reducing the number of trainable parameters. Compare adaptation with prompting and retrieval before paying its cost.

Select models using a fixed evaluation set. Consider quality, latency, context, availability, license, data handling, and total cost. A small model with a clear workflow may be preferable to a large model for a narrow task.

## Chapter 47 — Image, audio, and video generation

Diffusion models learn to reverse a gradual corruption or noise process. At generation time, repeated denoising steps transform random noise into a sample conditioned on text or other input. The original denoising diffusion paper is one foundation; see [Ho, Jain, and Abbeel](https://arxiv.org/abs/2006.11239).

Speech systems may recognize audio, generate speech, or map between text and audio. Video generation adds time and consistency across frames. Evaluate content, identity and consent, temporal consistency, source provenance, and misuse risk as appropriate.

## Evaluation and security

Create an evaluation set before iteration. Track answer correctness, groundedness, retrieval quality, refusal, format validity, tool success, latency, and cost. Keep both successful and failed examples.

Prompt injection can appear in user messages, web pages, or retrieved documents. Treat content from those sources as untrusted. Keep secrets outside model context; enforce permissions in code.

## Q&A

**Does RAG eliminate hallucinations?**  
No. Retrieval can miss the evidence, return irrelevant material, or supply malicious content. The model can misread evidence. Measure each stage and provide fallback behavior.

**Why not let an agent call any tool?**  
The model may make an incorrect or unsafe choice. Restrict tools to the task, validate calls, and require confirmation for consequential actions.

**When is fine-tuning better than retrieval?**  
Fine-tuning can improve repeatable behavior or domain format. Retrieval is usually easier for changing facts and source citations. Some systems combine them.

**Does low temperature make an answer true?**  
No. It reduces randomness in decoding but cannot correct missing knowledge or a false pattern. Verify with evidence.

**How should an app behave when sources do not answer?**  
It should state the limitation, ask for needed information, or escalate to a human rather than inventing a response.

## Practice

1. Build a small RAG prototype over approved, non-sensitive documents.
2. Create at least 20 test questions with expected source passages, including unanswerable and ambiguous questions.
3. Measure retrieval separately from answer correctness.
4. Add an untrusted document containing malicious instructions and verify the system treats it as data.
5. For one tool call, validate the schema and permissions in ordinary code; require approval before a consequential side effect.

## Mastery check

You can justify prompting, retrieval, fine-tuning, or tool use for a task; measure the chosen system on fixed examples; and explain how it handles missing evidence and malicious input.