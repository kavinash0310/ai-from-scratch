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
