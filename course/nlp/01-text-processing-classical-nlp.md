# Chapter 1 — Text processing and classical NLP

## Language is structured, but ambiguous

A text file is a sequence of characters; an NLP model needs numerical input. Preprocessing may normalize case, punctuation, whitespace, or Unicode, but every transformation can remove useful signals. For example, lowercasing helps combine “AI” and “ai” but loses capitalization cues for names.

Tokenization divides text into units. A token can be a word, punctuation mark, subword, or byte fragment. Sentence boundaries and contractions vary by language. Do not assume splitting on spaces is universally correct.

## Count-based representations

A bag-of-words vector counts token occurrences and ignores most order. TF-IDF raises the weight of terms frequent in one document but less common across the collection. These representations are sparse and interpretable.

N-grams record neighboring tokens, such as two-word phrases. They capture local order but become sparse as vocabulary grows. For a small topic or spam classifier, count-based features can be a strong baseline.

## Classic NLP tasks

- Text classification assigns categories, such as language or sentiment.
- Named entity recognition finds spans such as names and dates.
- Information extraction converts text into fields or relations.
- Search ranks documents for a query.
- Translation and summarization map one text to another.

Each task needs its own label definitions and evaluation. Sentiment may be ambiguous; annotator disagreement is real information about the task.

## Questions and answers

**Why preserve punctuation sometimes?**  
Punctuation can signal question intent, emphasis, code syntax, or sentence boundaries. Whether it helps depends on the task.

**What is a sparse vector?**  
A long vector where most entries are zero, common when each vocabulary term gets a feature.

**Why keep count-based baselines if transformers exist?**  
They are fast, explainable, and can be competitive on smaller tasks. They establish whether more complex methods add value.

**Is sentiment always positive, neutral, or negative?**  
No. Real text may be mixed, sarcastic, context-dependent, or outside those labels. Define the target carefully.

## Practice and mastery

Build a TF-IDF text classifier. Inspect top weighted terms, test punctuation and misspellings, and compare with a simple majority-class baseline. Write down two examples where labels are genuinely ambiguous.