# Chapter 1 — Prompting and structured outputs

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

## Give the model a clear task

A prompt provides context to a generative model. Useful prompts define task, relevant inputs, constraints, audience, and output format. Examples can clarify edge cases. Ask the model to separate evidence from assumptions and identify missing information.

A prompt is not a hard policy boundary. It cannot enforce authorization, guarantee truth, or protect secrets. Put critical validation and permissions in ordinary application code.

## Structured outputs

If an application needs JSON-like output, define fields, types, required values, and allowed ranges. Parse and validate the response. Handle malformed output with a bounded retry or an error path. Never assume a syntactically valid response is factually correct.

## Prompt iteration as experiment

Write an evaluation set first. Change one prompt element at a time and compare results across normal, ambiguous, adversarial, and out-of-scope examples. A prompt that helps one example may damage another.

## Deeper walkthrough: design a prompt contract

A reliable extraction prompt can define: task, trusted context, untrusted input boundaries, required fields, permitted labels, uncertainty behavior, and output schema. The application should then parse the output and reject invalid values.

For example, extracting an invoice total should return amount, currency, source span, and a confidence or missing marker. Check that the amount is numeric, currency is allowed, and the quoted source span exists in the input. The model should not invent a missing total.

Keep instruction and user-provided document visually and structurally separate. Test a document containing “ignore previous instructions” and verify it is treated as content. Security enforcement belongs in application logic, not prompt wording.

A prompt version should be paired with an evaluation set and recorded model configuration.

## Questions and answers

**Does prompt engineering change model weights?**  
Usually no. It changes the context supplied at inference. Fine-tuning is a separate process that updates parameters.

**Can a prompt protect an API key?**  
No. Keep secrets out of model context and enforce access in secure application code.

**Why use examples in a prompt?**  
Examples demonstrate format and task boundaries, but may bias the model or consume context. Evaluate whether they help.

**Should I ask the model to think step by step?**  
It may change output behavior, but generated explanations are not proof that internal reasoning is correct. Verify the answer against task evidence.

## Practice and mastery

Write a structured extraction prompt and schema. Test with missing fields, conflicting information, malicious instructions, and valid cases. Parse the output and reject values outside the schema.