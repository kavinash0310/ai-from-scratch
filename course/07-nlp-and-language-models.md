# Part 7 — Natural language processing

## Chapter 33 — What makes language data special

NLP studies computer processing of human language. Language is ambiguous, context-dependent, culturally varied, and constantly changing. A word can have several meanings; grammar and meaning depend on context; labels may differ between annotators.

Define the task carefully:
- sentiment classification predicts a label;
- named entity recognition marks spans such as people or places;
- information extraction converts text into structured fields;
- translation maps one language to another;
- summarization creates a shorter version;
- generation creates a continuation or response.

One metric does not fit all. Classification can use precision/recall; translation and generation often need human evaluation plus task-specific automatic measures.

## Chapter 34 — Text representation before transformers

Computers need numerical representations. A bag-of-words vector records word counts and ignores most word order. TF-IDF reduces the influence of words common across all documents. These methods are simple baselines and can perform surprisingly well.

An n-gram records neighboring word sequences. For example, a bigram model uses pairs of consecutive tokens. It captures local phrase patterns but grows sparse as vocabulary and sequence length increase.

Word embeddings map words to dense vectors. Similar contexts can produce similar vectors. Static embeddings assign one vector to a word; contextual models compute representations based on surrounding text, helping distinguish meanings.

## Chapter 35 — Tokenization and language-model objective

A tokenizer splits text into token IDs. Subword tokenization balances vocabulary size and handling rare words. Tokenization affects sequence length and may behave differently across languages and scripts. Always inspect examples, especially for multilingual or code data.

A language model estimates token sequences. A next-token model estimates the next token given previous tokens. A masked-language model predicts hidden parts using surrounding context. The learning objective influences what the model is naturally suited to do.

BERT used masked language modeling and bidirectional context for representation learning; GPT-style decoder models use causal next-token training. These are broad architectural families, not a claim that each family can only perform one task.

## Chapter 36 — Sequence models and transformers

Older sequence models such as recurrent neural networks process tokens sequentially. LSTMs and GRUs improve information flow over longer sequences, but parallelizing across token positions is difficult.

Transformers use attention to mix information across positions. This allows parallel training over a sequence and provides flexible context interaction, at a cost that grows with sequence length in standard dense attention. Chapter 38 covers the transformer computation in detail.

## Chapter 37 — NLP evaluation and data care

Text datasets can contain personal data, copyrighted material, dialect differences, and offensive examples. Label definitions must be consistent. Annotators may disagree, which should be recorded rather than hidden.

For classification, inspect confusion matrices and subgroup performance. For generation, check factuality, coverage, style, toxicity, and human usefulness. Overlap-based metrics can miss meaning and may reward generic outputs. Human review needs a rubric and multiple examples.

## Q&A

**Why not split text only by spaces?**  
Words may contain punctuation, suffixes, compounds, or subword units. A tokenizer maps text into the model's learned vocabulary and affects sequence length.

**Why keep a bag-of-words baseline?**  
It is fast, interpretable, and often strong on small classification tasks. A transformer should demonstrate a meaningful improvement.

**How do BERT-style and GPT-style objectives differ?**  
BERT-style masked modeling predicts hidden tokens with context on both sides. GPT-style causal modeling predicts the next token using only prior context.

**Can a text dataset represent everyone equally?**  
Usually not by default. Language, dialect, domain, time, and annotation practices shape coverage. Audit performance on relevant populations and disclose gaps.

**Why are automatic generation metrics limited?**  
They compress language quality into a number and may miss correctness, nuance, or usefulness. Combine automated checks with human review and task-specific tests.

## Practice

1. Build a bag-of-words baseline for a small text classification task.
2. Inspect how punctuation, rare words, and a multilingual sentence are tokenized.
3. Compare a static word embedding with contextual representations at a conceptual level.
4. Write a label guide and identify two examples that annotators could disagree about.
5. Evaluate per-class precision and recall and inspect error examples.

## Mastery check

You can explain how raw text becomes model input, identify the task-specific label, select an appropriate metric, and describe where language data may be unrepresentative or sensitive.