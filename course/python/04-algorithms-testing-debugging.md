# Chapter 4 — Algorithms, testing, and debugging

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

## Think in steps before syntax

An algorithm is a finite method for transforming input into output. Write down its steps before choosing Python syntax. For a search task, define what counts as a match, how duplicates behave, and what to return when nothing is found.

Linear search checks each item until it finds a match or reaches the end. In the worst case it checks every item, so work grows with list length n: O(n). Binary search repeatedly halves a sorted list and takes O(log n) comparisons. It is faster for large sorted inputs, but the sorted assumption is essential.

A data structure affects how costly operations are. List membership may scan many values; set membership is usually faster on average but does not provide the same ordering semantics. Big O describes growth rate, not exact seconds.

## Test behavior with examples

A test supplies an input and checks expected behavior. Start with ordinary cases, then boundaries and edge cases. Unit tests check small functions; integration tests check components working together.

For a function that counts values above a threshold, test:
- empty list;
- values all below;
- values all above;
- value exactly at threshold;
- mixed values.

Tests document intended behavior. A failing test is useful evidence. It may reveal a code bug or an unclear requirement.

## Debug systematically

1. Reproduce the problem.
2. Read the error message.
3. Inspect the smallest failing input.
4. Print or inspect intermediate values.
5. Form one hypothesis.
6. Change one thing.
7. Run the test again.

If the program gives a wrong answer without an exception, write down the expected intermediate state and compare it with the actual state. Avoid changing many lines at once.

## Questions and answers

**Why is binary search not always preferable?**  
It requires sorted data and maintaining the sort may cost more than searching. For small lists, linear search can be simpler and fast enough.

**Does O(n) mean slow?**  
Not necessarily. Big O describes growth with input size. A simple O(n) operation may outperform a complex method for small inputs.

**What is a unit test?**  
A focused check of one small unit, often a function, using known inputs and expected outputs.

**Why test an empty input?**  
Empty data is common in real workflows. Deciding behavior early prevents accidental crashes or misleading values.

## Practice

Implement linear search and binary search. Test both on empty, one-item, sorted, duplicate, and absent-target cases. Record which assumptions binary search needs.

## Mastery check

Write an algorithm in plain words, estimate how its work grows, then convert it to a function with tests for normal and edge cases.