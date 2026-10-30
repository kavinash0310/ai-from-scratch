# Natural language processing — full beginner notes

NLP is the study and engineering of systems that analyze or generate human language. Language is ambiguous, contextual, multilingual, and constantly changing, so the dataset and evaluation setup matter as much as the model.

## 1. Text processing and classical NLP

A **document** is a text item; a **corpus** is a collection of documents. **Tokenization** splits text into units such as sentences, words, subwords, punctuation, or characters. **Normalization** changes surface forms, for example lowercasing; use it only when the distinction is unimportant. **Stop words** are common words sometimes removed for a task, but they can carry meaning: “not” is critical for sentiment.

A **bag of words** counts terms and ignores order. **TF-IDF** increases the weight of terms frequent in one document but less common across the corpus. These representations support simple search or baseline classification. They are sparse: most vocabulary positions are zero for a given document.

Classical methods such as Naive Bayes, logistic regression, and support-vector machines are useful baselines. They are often faster to train and easier to inspect than deep models. Preprocessing can accidentally remove negation, names, accents, or language-specific structure, so inspect examples after every transformation.

## 2. Embeddings and sequence models

A **word embedding** maps a token to a dense vector. In a useful embedding space, words used in similar contexts may be nearby, but similarity does not mean identical meaning or truth. A **contextual embedding** depends on surrounding tokens; the same word can receive different representations in different sentences.

A **sequence model** processes ordered tokens. Recurrent neural networks maintain a hidden state as they read; LSTMs and GRUs add gates to preserve or discard information. They handle variable-length text but process tokens sequentially, which can limit parallelism and make very long-range dependencies difficult. Transformers use attention to compare positions directly; see the [Transformer chapter](../llm/01-transformers-attention.md).

An embedding model used for search maps a query and documents into vectors, then retrieves close candidates. **Cosine similarity** compares vector direction. It is useful only if the embedding model and data make relevant items close. Validate retrieval with real queries and known relevant passages.

## 3. Language tasks, data, and evaluation

Common tasks include **sentiment analysis** (opinion or emotion labels), **named-entity recognition** (spans such as people and organizations), **question answering**, **summarization**, **translation**, and text generation. Each task needs precise label definitions. “Positive sentiment” must be defined for sarcasm, mixed reviews, and neutral text.

Train/test examples should not share near-duplicate passages, authors, or conversations when that would make evaluation too easy. For translation and summarization, automatic metrics compare references but may miss meaning or valid alternate wording. Human evaluation needs a rubric, independent raters, and examples of disagreement. Track performance by language, dialect, domain, and writing style where relevant.

A classifier's **precision**, **recall**, and **F1** summarize different error tradeoffs. For generation, evaluate factual support, completeness, style constraints, and harmful errors—not only fluency. Keep raw examples and label provenance so a score can be audited.

### Q&A and practice

**Does stemming preserve meaning?** Not always; it heuristically strips word endings.
**Why does tokenization affect cost?** Models usually process token IDs, so different scripts and words can use different token counts.
**Can a language benchmark prove broad language understanding?** No. It measures a specific collection under specific conditions.

Practice: create a small labeled sentiment set, write labeling rules, train a TF-IDF baseline, inspect errors, then compare a pretrained model. Explain which differences came from representation, data, or evaluation. Continue to [LLMs](../llm/README.md).