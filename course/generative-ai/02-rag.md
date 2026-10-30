# Chapter 2 — Retrieval-augmented generation (RAG)

## Why retrieve

A language model may not contain current, private, or verifiable knowledge. RAG searches an approved document collection and provides relevant passages at inference. The original RAG research combines parametric model memory with an external vector index; see [Lewis et al.](https://arxiv.org/abs/2005.11401).

## Pipeline

```mermaid
flowchart LR
    A[Approved documents] --> B[Clean and split into chunks]
    B --> C[Embed and index with metadata]
    D[Question] --> E[Retrieve and optionally rerank]
    C --> E
    E --> F[Build evidence prompt]
    F --> G[Generate answer and source IDs]
    G --> H[Validate support and format]
```

Chunk length and overlap balance context with retrieval precision. Metadata can filter by date, permissions, or source. Embeddings retrieve semantic neighbors; keyword search may better find exact names or numbers. Hybrid retrieval combines signals. Reranking reorders candidates with a more targeted model.

## Evaluate each stage

Measure retrieval recall: did useful evidence appear among the retrieved passages? Then measure answer quality: is the answer supported, complete, and correctly cited? A good answer model cannot use evidence that retrieval missed.

A citation should point to the exact source supporting a claim. Test unanswerable and outdated questions and provide an abstention path. Retrieved documents are untrusted input: prompt injection can be embedded inside them.

## Questions and answers

**Does RAG eliminate hallucination?**  
No. Retrieval can miss evidence and generation can misread or ignore it. Evaluate retrieval and generation separately.

**Why keep source metadata?**  
It enables filtering, citations, version checks, and permissions. Without metadata, a similar passage may come from an outdated or unauthorized source.

**Are embeddings the only retrieval method?**  
No. Keyword, vector, structured database, and hybrid search each suit different queries.

**Why test questions with no answer?**  
The system must learn to say it cannot find evidence instead of fabricating a plausible answer.

## Practice and mastery

Create a small knowledge base and 30 queries with expected source passages. Report recall at k, answer support, citation quality, and abstention behavior. Add an adversarial instruction to a source document and confirm it is treated as content, not authority.