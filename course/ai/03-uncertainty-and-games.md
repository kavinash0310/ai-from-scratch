# Chapter 3 — Uncertainty, Bayesian reasoning, and games

> **Book-length subject volume:** For expanded explanations, worked examples, review questions, and practice, read the [ai textbook](TEXTBOOK.md).

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

## Reason under uncertainty

A rule may say “if evidence A, conclude B.” Real evidence is rarely perfect. Probability represents uncertainty under a model. Bayes' rule updates belief when evidence arrives:

P(H|E) = P(E|H)P(H) / P(E)

H is a hypothesis and E is observed evidence. The prior P(H) matters. A rare condition can remain unlikely after a positive test if false positives are common relative to the base rate.

A Bayesian network represents variables and conditional dependencies as a directed graph. It provides a compact factorization only when its independence assumptions are appropriate. A graph of statistical dependency is not automatically a causal graph.

## Game search

In a two-player zero-sum game, one player's gain is the other's loss. Minimax searches a game tree: the current player chooses a move that maximizes value, while the opponent is assumed to minimize it.

Searching to the end can be too expensive. A depth limit and evaluation function estimate the position. Alpha-beta pruning skips branches that cannot change the selected move. The agent's quality depends on legal-move representation, search depth, and the evaluation function.

## Decisions and expected utility

When outcomes differ in value, choose actions by expected utility: sum of outcome probabilities times their utilities. Probability describes uncertainty; utility describes preference. A high-probability outcome is not always the best choice if its cost is severe.

## Questions and answers

**Why does the prior matter?**  
The evidence must be interpreted relative to how common the hypothesis was before observing it. Ignoring the prior can badly misread rare events.

**What does minimax assume?**  
Both players act optimally according to the modeled utility. If an opponent, environment, or game includes randomness, represent that uncertainty explicitly.

**What does alpha-beta pruning change?**  
It avoids exploring parts of the tree that cannot affect the final minimax decision. It does not change the answer when implemented correctly.

**Is expected utility just probability?**  
No. Probability describes likelihood; utility represents the value or cost of an outcome.

## Practice and mastery

Create a tiny game tree with two choices at each turn. Label leaf values, calculate minimax by hand, then apply alpha-beta pruning. For a separate rare-event example, compute posterior probability from prior and test rates.