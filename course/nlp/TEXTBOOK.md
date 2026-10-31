# Natural language processing
## A beginner's textbook chapter

Natural language processing (NLP) builds systems for analyzing, classifying, searching, translating, summarizing, or generating human language. Language is ambiguous and context-dependent. A word can have multiple meanings, different dialects express the same idea differently, and a dataset can represent some groups better than others.

## 1. Text is converted into units

A **document** is one text item; a **corpus** is a collection of documents. **Tokenization** splits text into sentences, words, subwords, characters, or bytes. The choice depends on the task and model. A basic word tokenizer may treat punctuation separately. A subword tokenizer can split rare words into familiar pieces.

**Normalization** changes surface form. Lowercasing can merge “Apple” and “apple,” which may be useful for general sentiment but harmful for company/entity identification. Stemming removes endings with a heuristic; lemmatization maps a word to a dictionary base form. Removing stop words may improve some tasks, but removing “not” can reverse sentiment.

Text cleaning should be measured, not applied automatically. Preserve information needed by the task: punctuation for tone, casing for entity names, digits for identifiers, and ordering for negation.

## 2. Classical text representations

A **bag-of-words** representation counts token occurrences but ignores order. It is simple and fast, yet “dog bites person” and “person bites dog” can have similar counts.

**Term frequency-inverse document frequency (TF-IDF)** weights terms by how frequent they are in a document and how uncommon they are across the corpus. A common word such as “the” receives little emphasis; a word distinctive of one document receives more. The result is usually a sparse vector: most vocabulary entries are zero for any given text.

TF-IDF paired with logistic regression or a linear SVM is a strong, inexpensive baseline for many text classification tasks. It is easy to train and inspect. It cannot represent subtle context as effectively as contextual neural models.

## 3. Embeddings represent similarity

A **word embedding** maps a token to a dense vector. Training can make words used in similar contexts nearby. Nearby does not mean identical or true. An embedding space reflects the data and objective used to learn it.

A **contextual embedding** depends on neighboring tokens. In “river bank” and “bank account,” the word “bank” receives different contextual representations. Transformers produce contextual representations using attention.

For search, an embedding model maps queries and documents into a vector space. A similarity metric, often cosine similarity, ranks candidates. The embedding is useful only if relevant content tends to be near the query. Evaluate retrieval on real queries with known evidence.

## 4. Sequence models and Transformers

A **recurrent neural network** processes tokens in sequence while maintaining a hidden state. LSTM and GRU architectures add gates that control which information is retained. Recurrence supports variable-length input but processes steps sequentially, which limits parallelism and may struggle with long-range dependencies.

A Transformer uses attention to compare sequence positions. The query-key match creates weights, and value vectors supply information to be mixed. Position information lets the architecture distinguish word order. See the [Transformer lesson](../llm/01-transformers-attention.md) for the full calculation.

A bidirectional encoder can use both left and right context for understanding tasks. A causal decoder predicts the next token from earlier tokens. Architecture and training objective affect common use, but do not by themselves prove capability.

## 5. NLP tasks and metrics

- **Sentiment analysis:** classify opinion or emotional polarity.
- **Named-entity recognition:** identify spans such as people, places, dates, and organizations.
- **Question answering:** return an answer from language input, sometimes grounded in documents.
- **Machine translation:** generate text in another language.
- **Summarization:** compress a document while preserving important content.
- **Information extraction:** convert text into structured fields or relations.

Label definitions should specify difficult cases: sarcasm, mixed sentiment, quoted opinions, and neutral text. For classifiers, precision, recall, F1, and calibration measure different properties. For generation, lexical overlap measures such as BLEU or ROUGE may miss valid paraphrases or factual errors. Human evaluation needs a rubric and examples of disagreement.

Splits must avoid leakage from duplicated text, same authors, conversations, or near-identical templates. Evaluate across languages, dialects, domain, and time when relevant. Report limitations.

## 6. Worked baseline: review sentiment

Create a small set of reviews labeled positive or negative. Define how to handle mixed opinions before labeling. Use TF-IDF plus logistic regression as the baseline. Split by source or author if repeated examples exist. Inspect false positives such as “good acting but boring story.” The model may learn that “good” usually signals positive even when the full sentence is mixed.

Next, compare a pretrained encoder and look for improvements on the difficult cases, not just the average. If it improves only on familiar writing but fails on a particular language variety, record that limitation.

## 7. Questions and exercises

**Does token count equal word count?** No. A word may be split into subwords; punctuation and scripts affect tokenization.

**Do similar embeddings prove synonyms?** No. Similarity reflects a learned geometry and task; antonyms can appear in similar contexts.

**Can high F1 prove a text model is fair?** No. It may hide subgroup gaps, label bias, or differences in how errors affect users.

Exercise: run the [TF-IDF lab](../../labs/nlp/09_tfidf_classifier.py). Inspect the vocabulary and every held-out error. Then explain why the tiny report should not be treated as a reliable product benchmark. Continue to [LLMs](../llm/README.md).

## Deeper text processing and evaluation

A tokenizer maps text to units and integer IDs. Word tokenization is easy to inspect but struggles with unknown words and languages without spaces. Character tokenization avoids unknown whole words but creates long sequences. Subword units are a compromise. Token IDs are addresses, not meanings; an embedding table learns vectors for them. Inspect punctuation, emoji, code, long words, and target languages.

A bag-of-words model counts terms and discards order. TF-IDF emphasizes terms frequent in one document but uncommon in the corpus. It is a valuable baseline for classification and search, but cannot naturally understand synonymy or word order. N-grams preserve short sequences such as “not good.”

Metrics must reflect the task. Classification needs valid labels and splits without duplicate leakage. Translation scores based on word overlap may penalize a valid paraphrase. Summarization should be checked for factual support, coverage, omissions, and readability. Retrieval needs relevance judgments at the ranking positions that matter. Inspect errors by language, dialect, length, code-switching, and formatting.

Text can reveal names, addresses, health details, and confidential work. Removing direct identifiers does not guarantee anonymity. Collect only necessary information, control access, decide retention, and check rights and permissions. Moderation models can over-flag dialects; review false positives and false negatives.

Questions: Why can static embeddings miss sentence meaning? A token's vector alone does not express how context changes its meaning. Why keep classical NLP baselines? They are fast, useful, and show whether complexity is earning a gain.

Further reading: [NLTK book](https://www.nltk.org/book/) and [Hugging Face Tokenizers](https://huggingface.co/docs/tokenizers/).

## 12. A text-processing pipeline

A text system may normalize Unicode, segment sentences, tokenize, map tokens to IDs, pad or truncate sequences, and build features. Each operation changes information. Lowercasing can merge proper names; removing punctuation can erase sentiment or code structure; stemming may conflate distinct forms. Preprocessing should be justified by the language and task, then kept consistent at training and inference.

A vocabulary maps tokens to integer identifiers. Unknown-token handling matters for unseen words. Subword tokenizers break uncommon strings into known pieces and can represent many languages with a fixed vocabulary, but tokenization quality varies. Inspect accented text, scripts, emoji, URLs, and domain-specific terms.

## 13. Classical baselines and embeddings

Bag-of-words represents term counts without order. TF-IDF downweights terms common across documents. N-grams represent short sequences and can capture phrases such as “not safe.” These models are efficient and often competitive for small supervised datasets.

An embedding is a learned vector. Similarity, often measured by cosine similarity, can identify related terms, but vector proximity is not proof of equivalence or fairness. Static embeddings assign one vector per token; contextual models compute representations influenced by surrounding words. The word “bank” in a river sentence and a finance sentence may need different contextual representations.

## 14. Language tasks need distinct evaluation

Classification uses labels; named-entity recognition tags spans; information extraction builds structured fields; translation maps between languages; summarization compresses content; retrieval ranks documents. A metric designed for one task may not reflect another. For generation, human assessment often needs a rubric for factuality, completeness, and clarity. For retrieval, judge relevance at useful ranks.

Annotation instructions should define ambiguous cases. Check inter-annotator agreement, but remember disagreement can reflect a genuinely ambiguous task. Evaluate across language, dialect, domain, text length, and code-switching. Near-duplicate documents can inflate scores if split across partitions.

Privacy and rights are central because text often contains personal or copyrighted content. Determine collection provenance, allowed use, retention, and access before training. De-identification does not ensure anonymity.

Practice: build a TF-IDF baseline for sentiment, inspect false positives and false negatives, then add bigrams. Explain which examples changed and why. Compare results on a separate test set and include class counts.

Further reading: [NLTK Book](https://www.nltk.org/book/) and [Hugging Face Datasets](https://huggingface.co/docs/datasets/).

## 15. Sequence-to-sequence learning and context

A sequence-to-sequence model reads an input sequence and produces an output sequence. Translation is an example. An encoder can build contextual representations of the source; a decoder generates target tokens while attending to source information. Teacher forcing trains the decoder using correct previous tokens, while inference conditions on tokens it generated itself. This difference can cause exposure bias: small generation errors can change later inputs.

A Transformer replaces recurrent step-by-step processing with attention across positions, which allows parallel training and long-range relationships. Positional information represents order. A causal decoder mask prevents looking at future output tokens. Attention weights are useful computation but should not automatically be presented as faithful human explanations.

## 16. Multilingual and domain language

Tokenizers may split a low-resource language into many small pieces, increasing sequence length and cost. A model trained mostly on one language may have weak vocabulary, factual coverage, or safety behavior in another. Test the actual languages, scripts, code-switching, and dialects that users rely on. Translation from a high-resource language is not a substitute for evaluation with fluent speakers.

Domain jargon and abbreviations may differ from web language. A glossary, domain-adapted corpus, or retrieval system may help, but check data rights and privacy. Distinguish terminology errors from reasoning errors.

Practice: design a multilingual sentiment evaluation set. Specify annotation instructions, language coverage, split policy, false-positive review, and how you would compare a TF-IDF baseline with a contextual model.
