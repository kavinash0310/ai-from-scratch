# Chapter 3 — NLP tasks, evaluation, and data

## Define language labels carefully

Text labels are judgments. “Toxic,” “helpful,” or “urgent” need written criteria and examples. Different annotators may disagree. Record disagreement and determine whether the task should allow multiple labels or uncertainty.

Language coverage varies by dialect, script, domain, age, code-switching, and time. A model trained on one variety may perform poorly on another even if aggregate evaluation appears strong.

## Match metrics to outputs

Classification uses precision, recall, F1, and calibration. Information extraction may measure span-level precision and recall. Translation or summarization needs automatic metrics plus human assessment of meaning, completeness, and factual support.

Generation overlap metrics may reward shared words without recognizing correctness, and may penalize valid paraphrases. Use task-specific rubrics and inspect examples.

## Data protection

Text often contains names, health details, addresses, or private conversations. Minimize collection, document permission and retention, and avoid exposing sensitive text in notebooks or logs. Published data may still carry license restrictions or social risks.

## Deeper walkthrough: disagreement is task information

Suppose annotators mark a message as “urgent.” One may mean safety-critical, another may mean “needs a reply today.” Before training, define the label with examples and borderline cases. Measure agreement and review disagreements.

If reasonable annotators continue to disagree, the target may be subjective. The product may need multiple labels, calibrated confidence, or a human decision rather than forcing one ground-truth category.

Create a time-based test set if language and policy change. Remove duplicates across splits. Evaluate false negatives and false positives separately, and inspect language varieties the product claims to support.

Text may contain sensitive content even in public forums. Data provenance, consent, and retention should be part of the dataset card.

## Questions and answers

**Why can an NLP model fail on a new dialect?**  
Its training data may not cover that language variety, vocabulary, or syntax. It learned statistical patterns from the data it received.

**Why document annotator disagreement?**  
Disagreement can reveal ambiguous labels or multiple valid interpretations. Hiding it can make a model appear more certain than the task allows.

**Is BLEU or another generation score enough?**  
No. Automatic metrics are useful signals but may miss factuality, completeness, or human usefulness.

**What is a good test set?**  
One representative of the intended use, separated by time, source, or user when needed, with labels reviewed and privacy constraints respected.

## Practice and mastery

Create a labeling guide for a small text dataset. Have two people label the same examples, compare disagreements, revise the guide, then evaluate per-class performance and examples from different language varieties.