"""Lab 20: build a count-based next-word model from a tiny text corpus.

A bigram language model estimates a next word from the previous word. It is
not a Transformer and cannot use long context, but it exposes the basic
probability idea behind next-token prediction. Add-one smoothing gives unseen
transitions a nonzero probability.
"""

from collections import Counter, defaultdict
import random

sentences = [
    "ai learns patterns from data",
    "machine learning uses data",
    "ai models predict useful patterns",
    "language models predict the next token",
    "models learn patterns from examples",
    "the next token depends on context",
]
start, end = "<START>", "<END>"
transitions = defaultdict(Counter)
vocabulary = set()

for sentence in sentences:
    words = [start] + sentence.lower().split() + [end]
    vocabulary.update(words)
    for previous, current in zip(words, words[1:]):
        transitions[previous][current] += 1

vocabulary_size = len(vocabulary)


def next_word_distribution(previous):
    counts = transitions[previous]
    denominator = sum(counts.values()) + vocabulary_size
    return {
        word: (counts[word] + 1) / denominator
        for word in vocabulary
    }


previous = "models"
distribution = next_word_distribution(previous)
print(f"Most likely next words after {previous!r}:")
for word, probability in sorted(
    distribution.items(), key=lambda item: item[1], reverse=True
)[:5]:
    print(f"  {word:12s} {probability:.3f}")

rng = random.Random(2)
generated = []
previous = start
for _ in range(12):
    candidates = list(vocabulary)
    probabilities = [next_word_distribution(previous)[word] for word in candidates]
    following = rng.choices(candidates, weights=probabilities, k=1)[0]
    if following == end:
        break
    generated.append(following)
    previous = following
print("Sample continuation:", " ".join(generated))

# Small data produces repetitive and unreliable text. A neural language model
# learns richer representations, but still predicts token distributions rather
# than guaranteeing factually correct statements.
