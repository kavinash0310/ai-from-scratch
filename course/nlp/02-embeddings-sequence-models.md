# Chapter 2 — Embeddings and sequence models

> **Book-length subject volume:** For expanded explanations, worked examples, review questions, and practice, read the [nlp textbook](TEXTBOOK.md).

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

## From sparse counts to dense vectors

An embedding maps an item to a dense numeric vector. Word embeddings can learn from co-occurrence patterns: words appearing in similar contexts may have nearby vectors. Static embeddings assign one vector per word, so polysemous terms share a representation.

Contextual embeddings compute representations based on surrounding tokens. “Bank” in “river bank” and “bank account” can receive different vectors. Embeddings are useful inputs for similarity search and neural tasks, but they are not dictionaries and their dimensions may not have simple human meanings.

## Sequence models

Language is ordered. A recurrent neural network (RNN) processes one token at a time, passing a hidden state forward. This state summarizes earlier input but can struggle to retain long-range information and is difficult to parallelize across positions.

LSTM and GRU gates regulate information flow and improve long-range learning. Encoder-decoder models map one sequence to another, such as translation. Attention mechanisms allow an output step to reference relevant input positions.

Transformers later replaced recurrence with attention-based blocks, allowing more parallel sequence processing during training. They still have context and compute limits.

## Similarity and retrieval

Vector search can find embeddings close to a query. Cosine similarity compares direction; Euclidean distance compares geometric distance. Normalize or select metrics according to how embeddings were trained. Evaluate retrieval by whether useful items appear near the top, not by vector distance alone.

## Questions and answers

**How is a contextual embedding different from a static word vector?**  
It depends on surrounding tokens, which helps represent different meanings of the same word.

**Can vector similarity prove two documents are equivalent?**  
No. It is a learned similarity signal. It can be useful for retrieval, but candidates must be evaluated for the actual task.

**Why are RNNs sequential?**  
Each step uses the hidden state from the previous step, creating a dependency that limits parallel processing across time.

**What problem does attention address?**  
It lets a prediction combine information from relevant positions rather than relying only on one compressed state.

## Practice and mastery

Compare a bag-of-words baseline with an embedding-based classifier or retrieval task. Inspect nearest neighbors for several ambiguous queries and note where similarity fails.