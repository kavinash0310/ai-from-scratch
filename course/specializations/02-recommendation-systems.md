# Chapter 2 — Recommendation and ranking

A recommender selects or ranks items for a person or context. Candidate generation finds a manageable set from a large catalog; ranking orders those candidates; the interface controls what is actually shown.

Collaborative filtering uses user-item interaction patterns. Content-based methods use item attributes. Hybrid systems combine both. New users and items create a cold-start problem. Popularity bias can cause already popular items to receive more exposure and feedback.

Clicks are selective observations: users can only click items they saw. The existing ranking policy shaped the dataset, so click prediction may reinforce earlier choices.

Evaluate offline with careful historical splits, but also consider diversity, satisfaction, user outcomes, and exploration. Online experiments need ethical design and guardrails.

## Questions and answers

**Why isn't a click a simple preference label?**  
The user may not have seen alternatives, may click accidentally, or may click to inspect an item they dislike.

**What is cold start?**  
The system lacks interaction history for a new user or item.

**Why measure diversity?**  
A ranking can maximize likely clicks while repeatedly showing similar items and reducing user choice.

## Practice and mastery

Create a popularity baseline and a content-based recommender over a small catalog. Compare ranking quality, diversity, and new-item behavior. Explain what your logs cannot tell you.