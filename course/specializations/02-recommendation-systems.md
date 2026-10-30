# Chapter 2 — Recommendation and ranking

> **Book-length subject volume:** For expanded explanations, worked examples, review questions, and practice, read the [specializations textbook](TEXTBOOK.md).

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

A recommender selects or ranks items for a person or context. Candidate generation finds a manageable set from a large catalog; ranking orders those candidates; the interface controls what is actually shown.

Collaborative filtering uses user-item interaction patterns. Content-based methods use item attributes. Hybrid systems combine both. New users and items create a cold-start problem. Popularity bias can cause already popular items to receive more exposure and feedback.

Clicks are selective observations: users can only click items they saw. The existing ranking policy shaped the dataset, so click prediction may reinforce earlier choices.

Evaluate offline with careful historical splits, but also consider diversity, satisfaction, user outcomes, and exploration. Online experiments need ethical design and guardrails.

## Deeper walkthrough: two-stage recommendations

Suppose a music catalog has ten million tracks. A candidate generator might select a few hundred using user history, new releases, and similar artists. A ranking model orders candidates using context such as listening time and skips. The interface may reserve space for diverse or editorial items.

A logged impression is the item actually shown; a click is only observed for shown items. If the ranking system never shows a track, its click probability is unknown. This is exposure bias. Offline evaluation should account for the logging policy or be treated as approximate.

For a new user, there is no interaction history. Use onboarding preferences, contextual popularity, or content features. For new tracks, content metadata and exploration can help. Track satisfaction, repeat use, diversity, and complaint signals alongside click-through rate.

Do not equate engagement with welfare. If a metric rewards endless time in the app, the product may optimize the wrong outcome.

## Questions and answers

**Why isn't a click a simple preference label?**  
The user may not have seen alternatives, may click accidentally, or may click to inspect an item they dislike.

**What is cold start?**  
The system lacks interaction history for a new user or item.

**Why measure diversity?**  
A ranking can maximize likely clicks while repeatedly showing similar items and reducing user choice.

## Practice and mastery

Create a popularity baseline and a content-based recommender over a small catalog. Compare ranking quality, diversity, and new-item behavior. Explain what your logs cannot tell you.