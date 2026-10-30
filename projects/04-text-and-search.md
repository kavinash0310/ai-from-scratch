# Project 04 — Compare text classification and retrieval

## Goal

Learn how text cleaning and representation affect two tasks: assigning labels and finding relevant passages.

## Steps

1. Select a permitted text corpus and document language, source, collection date, label method, and privacy limits.
2. Create a split that prevents near-duplicate documents, authors, threads, or sources from appearing on both sides.
3. For classification, build a TF-IDF plus linear model baseline. Compare with a suitable pretrained encoder only if feasible.
4. For retrieval, write at least 30 queries and mark the evidence passages that answer each. Compare keyword search with embedding retrieval if available.
5. Report F1 or PR-AUC for classification. Report Recall@k and ranking quality for retrieval. Inspect errors rather than relying on one average.
6. Test negation, names, numbers, multilingual text if relevant, and unanswerable queries.
7. Explain how tokenization, normalization, and label definitions change the result.

## Deliverables

Dataset notes, split strategy, baseline and comparison, query/evidence set, metrics, ten error examples, setup steps, and limitations.

## Acceptance checks

No test examples were used for repeated tuning; each query has judged evidence; language varieties are described; and the report separates classification results from retrieval results.

## Stretch

Add a cross-encoder reranker to a small candidate set and calculate whether quality gains justify latency.