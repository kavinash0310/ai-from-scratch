# Generative AI systems — full beginner notes

Generative AI applications combine a model with prompts, data, retrieval, tools, interfaces, policies, and evaluation. A prompt is only one part of the system.

## 1. Prompting and structured outputs

A **prompt** is the input context sent to a model. It can contain instructions, examples, user data, and formatting requirements. Clear prompts state the task, constraints, audience, and expected output. **Few-shot prompting** includes examples; examples should represent edge cases, not only ideal inputs.

A **system instruction** sets behavior at a higher level in an application; a **user message** supplies the current request. Model output is untrusted text. Validate JSON with a parser and schema rather than assuming valid-looking braces mean valid data. A **structured output** constrains fields and types, but valid structure does not prove factual correctness.

Worked example: ask for an object with fields answer, source_ids, and cannot_answer. Validate that answer is text, source_ids is a list of known IDs, and cannot_answer is Boolean. Reject malformed output and test missing, extra, and contradictory fields.

## 2. Retrieval-augmented generation

**RAG** retrieves relevant external passages and supplies them to a generation model. An index may store text, metadata, and embeddings. At query time, retrieval selects candidates; optional reranking reorders them; a prompt includes evidence; generation produces an answer. **Chunking** splits long documents into pieces. Small chunks can omit context; large chunks may distract. Tune with representative questions.

**Recall at k** asks whether useful evidence appears among the first k retrieved items. Separate retrieval evaluation from answer evaluation. A generated citation should point to evidence supporting the specific claim. Filter by permission and freshness before ranking. Retrieved text can contain malicious instructions; treat it as data, not authority.

## 3. Tools and agents

A **tool** is an application-controlled function the model can request, such as a calculator or database lookup. The application validates arguments, checks permissions, runs the function, and returns its result. The model does not magically execute reliable actions because it produced a tool-shaped string.

An **agent** is a loop that uses model decisions, tools, observations, and stopping rules to pursue a goal. Begin with deterministic workflows; add autonomy only when a measurable task needs it. Set time, tool, and cost limits; require confirmation for consequential actions; log inputs and outcomes. Test prompt injection and malicious tool outputs.

## 4. Multimodal generation

**Multimodal** systems process more than one modality: text, image, audio, or video. Image models may generate pixels from noise or latent representations; audio models may generate waveforms or discrete codec tokens. A **latent** is an internal compressed representation. **Diffusion** methods learn to reverse a noise process in steps. A generated result can be plausible yet inaccurate or biased.

Specify rights, provenance, consent, and expected use for media. For perception tasks, evaluate recognition separately from generation. For audio, test accents, background noise, speaker overlap, and transcription versus translation. For video, motion and temporal consistency matter in addition to individual frames.

## 5. Evaluation, reliability, and security

Build a **test set** of real and adversarial use cases before tuning. Compare output with a baseline and record severity. Evaluate correctness, completeness, groundedness, refusals, policy compliance, latency, and cost. **Regression testing** reruns a fixed suite after a prompt or model change. An update can improve one category and harm another.

Security risks include prompt injection, data leakage, insecure output handling, excessive tool permissions, and denial of service through expensive requests. Keep secrets out of prompts when possible, use least privilege, validate outputs, and isolate untrusted content. **Human-in-the-loop** means a person reviews or approves selected steps; it is not a substitute for a safe workflow.

### Q&A and practice

**Can prompting guarantee correct answers?** No. Treat it as behavior guidance and validate outputs.
**Does RAG eliminate hallucinations?** No. Retrieval can miss evidence and generation can misuse it.
**Why not give an agent every tool?** Excess permissions increase the impact of mistakes and attacks.

Practice: build a small FAQ assistant with citations, schema validation, unanswerable questions, and a test report. Then add one read-only tool and document its permission boundary. See [LLM notes](../llm/DEEP_NOTES.md).