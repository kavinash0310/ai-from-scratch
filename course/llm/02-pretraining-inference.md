# Chapter 2 — Tokenization, pretraining, and inference

> **Book-length subject volume:** For expanded explanations, worked examples, review questions, and practice, read the [llm textbook](TEXTBOOK.md).

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

## Tokenization

A tokenizer maps text to a sequence of token IDs. Tokens can be whole words, subwords, punctuation, or bytes. Token count is not word count. Rare words or multilingual text may split into many pieces.

Tokenization influences context length, cost, and model behavior. Inspect what happens to code, numbers, names, and languages you care about.

## Pretraining objective

An autoregressive LLM predicts the next token from prior tokens. At every position, it predicts a probability distribution; cross-entropy loss rewards probability assigned to the actual next token. Large-scale training repeats this over data.

The model learns patterns and associations represented in its data, including errors, bias, and artifacts. Next-token prediction does not guarantee factual recall or human-like reasoning.

Encoder language models such as BERT use masked-token prediction to learn representations from left and right context. Decoder models use causal next-token prediction. Encoder-decoder models map an input sequence to an output sequence. These training patterns shape natural strengths but do not rigidly define every downstream use.

## Inference and decoding

At inference, the model processes input tokens and produces next-token scores. A decoder selects or samples one token; that token is appended to context, then the model repeats. Greedy decoding chooses the top token. Temperature and top-p sampling change randomness and diversity, not truth.

The context window limits input and generated tokens. Longer context costs memory and computation and can still fail to surface important details. Retrieval may be better than sending every document.

## Questions and answers

**Does the model store facts like a database?**  
Its parameters encode learned patterns, but retrieval is not transparent or guaranteed. Use external evidence for current facts and citations.

**Why does the token count surprise users?**  
Tokenizers split text according to learned vocabulary units; punctuation, symbols, and uncommon words can add tokens.

**Does a low temperature make the output accurate?**  
No. It changes sampling variation. The model can consistently produce a wrong answer.

**What is the context window?**  
The maximum token sequence considered by a model call under its implementation. It is not a guarantee of perfect memory across the whole sequence.

## Practice and mastery

Use a tokenizer to inspect several sentences and code snippets. Trace a short prompt through token IDs, next-token probabilities, and repeated decoding. Compare greedy output with sampling and explain what changed.