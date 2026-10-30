# Project 05 — Build a grounded document assistant

## Goal

Build and evaluate a retrieval-augmented prototype that answers from a small, permitted document collection and admits when evidence is missing. A language-model API is optional; the retrieval evaluation and system boundaries are required.

## Steps

1. Use public, non-sensitive documents. Record source, date, version, license, and intended users.
2. Split documents into chunks while preserving source, section, date, and permission metadata.
3. Build a keyword or TF-IDF retrieval baseline. If using embeddings, compare against that baseline.
4. Write at least 30 questions: answerable, ambiguous, outdated, and unanswerable. Mark exact supporting passages.
5. Measure Recall@k and ranking quality. Tune chunking/ranking on a development set, then evaluate once on a held-out set.
6. Generate answers with source IDs and a clear abstention behavior. Check every claim against the cited passages.
7. Add adversarial documents containing instructions such as “ignore prior rules.” Ensure retrieved text is treated as data, not permission.
8. Document latency, cost, access controls, known errors, and rollback/removal process.

## Deliverables

Runnable prototype, document manifest, query/evidence set, retrieval report, answer-support review, security cases, README, and limitations.

## Acceptance checks

Unauthorized documents are excluded before retrieval; citations resolve to source text; no-answer questions do not force invented answers; retrieval and generation are evaluated separately; and the system has no unnecessary write-capable tools.

## Stretch

Add a reranker, version-aware freshness filtering, and a small regression suite for citation support and abstention.