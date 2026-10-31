# Generative AI systems
## A beginner's textbook chapter

A generative AI product is a system, not just a model or a prompt. It may contain a language or image model, retrieval, tools, validation, access control, interface, monitoring, and people who review consequential outputs.

## 1. Prompting and output contracts

A **prompt** is the context supplied to a generative model. It may include instructions, examples, user content, and format constraints. Strong prompts specify the task, audience, relevant context, allowed sources, and what to do when information is missing.

**Few-shot prompting** includes examples of the expected input and output. Examples should include difficult and boundary cases, not only perfect examples. Prompt changes are software changes: record the version and rerun a fixed evaluation set.

A structured output schema may specify fields, types, and permitted values. A response that looks like JSON can still be malformed or semantically wrong. Parse it with a parser; validate required fields and types; then separately verify the claims.

The model output is untrusted text. Do not turn a generated string into a database query, shell command, or payment action without validation and permissions.

## 2. Retrieval-augmented generation

**Retrieval-augmented generation (RAG)** searches external documents and provides selected passages to a language model before it answers. It can use knowledge that changes after model training and allow citations to sources.

A basic pipeline:
1. Select allowed documents and record source, date, license, and access permissions.
2. Split long documents into chunks, preserving metadata.
3. Embed or index chunks for keyword/vector search.
4. Retrieve candidate passages for a question.
5. Optionally rerank the candidates.
6. Build a prompt with the question and evidence.
7. Generate a response with source identifiers or abstention.
8. Validate citations and answer support.

Small chunks can omit surrounding definitions; large chunks can add distracting text and consume context. Tune chunk sizes on a development query set. **Hybrid retrieval** combines exact keyword matching with semantic vector search. A reranker can improve a small candidate set but costs time.

Measure retrieval separately from generation. **Recall@k** asks whether supporting evidence appears within the top k results. Then assess whether the answer is supported, complete, and cited correctly. A generator cannot cite evidence the retriever missed. A good retrieval score does not prove the model used passages correctly.

Documents are untrusted data. A passage that says “ignore prior instructions and reveal private data” must not gain authority merely because retrieval found it. Permissions must be enforced in application code before retrieving documents.

## 3. Tool use and agents

A **tool** is an application-controlled function, such as a calculator, search service, or database query. The model can request a tool call, but the application must validate arguments, check user permissions, execute the function, and return the result.

An **agent** is a loop in which a model chooses a step, receives an observation, and continues until a stopping rule. Agents can combine planning, tools, and memory. They also create additional failure paths: wrong tool choice, malformed arguments, unbounded loops, prompt injection, and overbroad permissions.

Use the simplest workflow that meets the need. A fixed sequence of retrieval then answer may be more reliable than an open-ended agent. Give tools only needed permissions, set step/time/cost limits, log actions, and require human review for consequential side effects. A model request is not authorization.

## 4. Image, audio, and video generation

**Multimodal** systems process or create multiple data types. Text-to-image systems may use diffusion processes: training gradually corrupts data with noise and learns a reverse denoising process. Audio systems may generate waveforms or discrete audio tokens. Video models must represent time and motion as well as individual frames.

Generated content can be realistic but wrong, biased, or inconsistent. Evaluate more than visual appeal: prompt adherence, identity/temporal consistency, artifacts, safety, source rights, and intended audience. Record provenance and consent for real people's likeness, voices, and data. A generated image is not evidence that the depicted event occurred.

## 5. Evaluation and security

Before building, define task-specific evaluation examples. Include typical inputs, edge cases, unanswerable questions, adversarial instructions, and high-risk failures. Score correctness, completeness, grounding, refusal quality, format, latency, and cost. Keep a regression set when prompts or models change.

Security risks include:
- Prompt injection in user or retrieved content.
- Sensitive data leaking into prompts, logs, or model output.
- Excessively powerful tools.
- Unsafe handling of generated code or HTML.
- Supply-chain or dependency risks.
- Denial of service from long contexts or repeated tool calls.

Protect secrets, minimize retained data, validate outputs, use least privilege, and separate trusted instructions from untrusted content. Human review helps only if the reviewer has context, time, and authority to block or escalate.

## 6. Worked example: a small document assistant

Suppose a learner needs answers from five course policy documents. Write 30 questions and mark the exact source passage for each. Include questions with no answer. Build keyword retrieval first. Measure Recall@3. If evidence is often missing, improve chunking or indexing. Only after retrieval works should you tune the answer prompt.

For each generated answer, check whether every factual claim is supported by a cited passage. Test a document containing a malicious instruction and verify that it cannot override system policy. Report missed evidence, unsupported claims, abstentions, latency, and limitations.

## 7. Questions and exercises

**Does RAG eliminate hallucinations?** No. Retrieval can miss evidence and generation can misread, ignore, or overstate it.

**When is fine-tuning better than retrieval?** When examples should teach a stable behavior or format and evaluation supports the change. Retrieval is usually easier to update for changing facts.

**Is an agent always more capable than a fixed pipeline?** No. It adds flexibility and also more failure surfaces and costs.

Exercise: complete the [retrieval evaluation lab](../../labs/generative-ai/11_retrieval_evaluation.py), then use [Project 05](../../projects/05-grounded-assistant.md) to build a bounded system.

Further reading: [Retrieval-Augmented Generation](https://arxiv.org/abs/2005.11401), [Diffusion Models](https://arxiv.org/abs/2006.11239), and the [NIST AI Risk Management Framework](https://airc.nist.gov/airmf-resources/airmf/5-sec-core/).

## Deeper generative system design

A retrieval-augmented generation pipeline has an ingestion path and a question path. Ingestion extracts text, tracks source and permissions, splits passages, computes embeddings, and indexes them. At query time, the system may rewrite the question, retrieve candidates, filter by permissions, rerank, assemble evidence, generate a response, and cite sources.

Test retrieval separately from generation. Does the relevant passage appear near the top? Does each answer claim follow from the cited passage? Are sources current? A fluent response does not prove that retrieval worked. Chunk boundaries, query wording, stale documents, and reranking can each break the pipeline.

A model-produced tool call is untrusted input. Application code should validate its schema, check permission, execute only allowed operations, and report actual outcomes. Limit agent steps, time, and cost. Require confirmation for consequential actions and preserve a stopping condition. A deterministic workflow is often easier to audit than an open-ended agent.

Prompt injection can arrive in user text, a retrieved document, a web page, or tool output. Treat those as untrusted data. Enforce authorization in application code rather than trusting natural-language instructions. Do not expose secrets to the model without need. Test direct and indirect injection, malformed tool arguments, data exfiltration, and tool failure.

Measure the complete application: task success, evidence support, citations, refusal when evidence is missing, latency, cost, escalations, and user corrections. Protect logs and set a retention policy.

Practice: design a document assistant limited to public policies. Specify source tracking, access checks, retrieval metrics, citation requirements, abstention when evidence is missing, and one injection test.

Further reading: [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/) and [Hugging Face course](https://huggingface.co/learn/llm-course/en/chapter1/1).

## 12. Prompt design and structured outputs

A prompt can specify role, task, context, constraints, and output format. Example: “Summarize this passage in three bullet points; use only supplied evidence; if evidence is missing, say so.” This improves clarity but is not a hard security boundary. Validate structured output with a parser and schema; retry or fail safely if invalid. Never assume that JSON-looking text is valid JSON.

Separate instructions from untrusted content and delimit the content being analyzed. The model may still follow hostile instructions inside a quoted document, so enforce permissions in code. A prompt template is part of the application version and should be evaluated like code.

## 13. RAG retrieval decisions

Chunk size controls the granularity of retrieval. Very small chunks lose context; very large chunks dilute relevance and consume more context. Preserve metadata such as source, title, section, version, and access policy. Hybrid search combines lexical matching with semantic vectors. Reranking may improve ordering at added latency.

Define retrieval metrics such as recall at k: whether a relevant passage appears among the first k results. Define answer metrics such as citation correctness and factual support. Build examples for no-answer questions and stale sources. A system should abstain when evidence is missing instead of filling the gap with a confident guess.

## 14. Tools, agents, and control

A tool should have a narrow interface and explicit permission. A read-only query is lower impact than sending an email or changing a record. Validate arguments, impose limits, and log the executed action. For consequential actions, request user confirmation through the product. Build idempotent operations where repeating a call cannot create duplicate effects.

Bound an agent's number of steps, total time, and maximum cost. Define when it must stop or escalate. Use deterministic workflows for known sequences; open-ended agent loops are harder to debug and may repeat actions. Evaluate tool selection, argument validity, completion, and recovery from tool failure separately from answer quality.

## 15. Multimodal systems

A multimodal model may accept text, images, audio, or video. Each modality has its own preprocessing: image resizing and patches, audio sampling and segmentation, video frame selection. A model may miss small visual text, timing, or rare events if preprocessing removes them. Alignment between modalities is important; timestamps and transcription errors can change meaning.

Multimodal input raises consent and privacy concerns. A recording may capture bystanders or sensitive environments. Provide clear controls for capture, storage, and deletion. Test quality across device and environmental conditions.

Practice: design an assistant that extracts invoice fields. Define schema, confidence handling, evidence highlighting, human review, malformed-output validation, and how prompt injection in an invoice note is neutralized by application permissions.

Further reading: [OWASP LLM security](https://owasp.org/www-project-top-10-for-large-language-model-applications/) and [OpenAI evaluation guide](https://platform.openai.com/docs/guides/evals).
