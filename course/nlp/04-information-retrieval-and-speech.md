# NLP extensions: information retrieval and speech

> **Place in the course:** Optional specialization after NLP foundations. Search and speech have distinct inputs, methods, and evaluation.

## Information retrieval

Information retrieval (IR) finds and ranks documents for a query. A pipeline parses the query, retrieves candidates, ranks them, and presents results. An inverted index maps words to documents. BM25 scores lexical overlap while accounting for term frequency, document length, and word rarity. It is an effective baseline for exact names and identifiers.

Dense retrieval maps queries and passages to vectors. It can match paraphrases but may return semantically related passages that do not answer the question. Hybrid retrieval combines lexical and vector signals. A reranker scores query-passage pairs more precisely, usually over a smaller candidate set.

Recall at k asks whether relevant evidence appears among the first k results. Mean reciprocal rank rewards placing the first relevant item near the top. NDCG gives graded relevance more credit near the top. Evaluate with real user questions, including ambiguous and unanswerable ones.

## Speech recognition and synthesis

Automatic speech recognition (ASR) converts audio into text; text-to-speech (TTS) generates audio from text. Audio is a sampled signal. Sample rate is measurements per second; channel count distinguishes mono and stereo. Incorrect resampling changes timing or pitch. Noise, microphones, accents, overlap, and speaking speed influence recognition.

Word error rate is (substitutions + deletions + insertions) / reference words. It treats all word errors equally and can behave poorly for languages without whitespace-separated words. Evaluate task impact too, especially for names, numbers, medication, and spoken commands.

Streaming recognition must respond quickly; partial transcripts may change as more audio arrives. Speech recordings may contain sensitive conversations, so define consent, retention, access, and deletion. Check accent and code-switching performance directly.

**Worked search example:** Search a course library with BM25. For 30 beginner questions, note whether a correct passage appears in the top five and its rank. Add dense retrieval and compare recall at five, including exact-code queries. Add a reranker only if the improvement justifies latency.

**Questions:** Why combine lexical and dense search? They make different errors. Why is WER insufficient? Errors have unequal consequences. Why check permissions during retrieval? Search should not expose inaccessible documents.

**Practice:** Create an evaluation set with exact terms, paraphrases, misspellings, multilingual questions, and no-answer cases. Define relevance judgments and a latency-quality trade-off.

Further reading: [BM25 overview](https://doi.org/10.1561/1500000019) and [Whisper speech-recognition paper](https://arxiv.org/abs/2212.04356).

## Worked ranking metrics

Suppose a query has three relevant documents, and a system returns five results with relevant items at ranks 1 and 4. Recall at 5 is 2/3 because two of three relevant items appeared. Reciprocal rank is 1 because the first relevant result is at rank 1. If the first relevant result were at rank 4, reciprocal rank would be 1/4. NDCG can use graded judgments, giving more credit to highly relevant documents near the top.

These measures do not define relevance. Human annotators need a rubric, and disagreements should be recorded. For a troubleshooting search, a passage that contains the exact error code may outrank a generally similar article. For broad discovery, semantic matches may matter more.

## Lexical and dense search errors

BM25 works from term matching and is robust for rare exact terms. Dense retrieval maps text into vectors and can find paraphrases. But embeddings may match topic rather than answer; “how to reset a password” may retrieve “how to change a username.” Hybrid systems combine scores after normalization or use one method to retrieve candidates for another to rerank. Evaluate each component independently to locate failure.

## Speech example and metric limitation

If a reference transcript contains 100 words, and recognition makes 3 substitutions, 2 deletions, and 1 insertion, WER=(3+2+1)/100=6%. Yet one substituted drug name could be more important than six punctuation differences. Normalize transcripts consistently, document how numbers and disfluencies are handled, and review consequential errors with qualified people.

Streaming ASR produces partial hypotheses, so measure latency and revision behavior as well as final WER. TTS evaluation may consider intelligibility, naturalness, speaker consent, and whether synthetic voices could mislead listeners. Audio systems also need environmental tests for background noise and microphones.

Practice: create a ten-query search set with relevance grades 0, 1, or 2. Calculate recall at 5 and reciprocal rank for two systems. Then identify one query for which automated relevance labels may be insufficient.

Further reading: [Whisper paper](https://arxiv.org/abs/2212.04356) and [Hugging Face audio task documentation](https://huggingface.co/docs/transformers/tasks/asr).
