# Chapter 2 — Conditions, loops, and collections

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

## Make a program choose

A conditional lets a program choose actions based on a Boolean condition. Use if for the first case, elif for additional cases, and else for the remaining case.

    score = 84
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    else:
        grade = "Review"

Order matters: the first true condition wins. Test boundaries such as 79, 80, 89, and 90 so a comparison error does not hide.

## Repeat work with loops

A for-loop visits each item in a collection. A while-loop continues while a condition is true. Use a for-loop when the number of repetitions is known or tied to a collection. A while-loop must have a clear progress rule or it can run forever.

    total = 0
    for value in [4, 7, 9]:
        total = total + value

After the loop, total is 20. The loop's state changes each time; tracing that state by hand is a useful debugging tool.

## Choose a collection

- A list is ordered and can contain repeated values.
- A tuple is ordered and often used for a fixed group.
- A dictionary maps keys to values.
- A set holds unique values and supports membership checks.

    prices = [3.5, 5.0, 3.5]
    student = {"name": "Mina", "score": 84}
    unique_prices = set(prices)

Use a list for an ordered series, a dictionary for lookup by name or ID, and a set when uniqueness or membership is the main operation. Collections can be nested, but keep the structure understandable.

## Work through a counting example

Task: count how many numbers are at least 10. Start count at zero, visit each number, compare it with 10, and increment count when the condition is true. State the input, output, and boundary condition before writing code. If the list is empty, the count should naturally be zero.

## Common mistakes

- Using = where a comparison is required.
- Forgetting that list indexes start at zero.
- Mutating a list while looping over it.
- Writing a while-loop whose condition never becomes false.
- Treating dictionary keys as if they were ordered numeric indexes.

## Questions and answers

**When should I use a dictionary instead of a list?**  
When each value should be found by a meaningful key, such as student ID or product name. A list is more natural when position or order matters.

**Why test boundary values?**  
A condition may be correct for typical values but wrong exactly at a threshold. Boundary tests expose off-by-one errors.

**What makes an infinite loop?**  
A loop condition remains true because nothing updates the values used by the condition, or updates them in the wrong direction.

**What is a set useful for?**  
Storing unique items and checking whether an item is present without needing to preserve duplicates.

## Practice

1. Count passing scores in a list.
2. Find the largest value without using a built-in maximum function.
3. Build a dictionary of product prices and print the cost of a chosen product.
4. Test empty, one-item, boundary, and ordinary inputs.

## Mastery check

Trace a conditional and a loop manually; choose an appropriate list, dictionary, or set; and explain the result for an edge case.