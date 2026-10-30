# Chapter 1 — Reading research papers

## Read in passes

Start with title and abstract: what question is being answered and what claim is made? Read the introduction for motivation and contribution. Then inspect method, assumptions, data, baselines, metrics, ablations, and limitations.

A paper's result is evidence under a particular protocol. Check whether the baseline is strong, splits are fair, test data remained untouched, and metric matches the use. A preprint can be useful but may not have peer review or independent replication.

## Paper card

For each paper, write:
- question and central claim;
- method in your words;
- data and evaluation;
- strongest evidence;
- weakest assumption;
- compute and resources;
- one ablation to test;
- one follow-up question.

## Reproduction

Try to reproduce a small part before accepting the conclusion. Note missing details, software versions, data processing, random seeds, and hardware. A reproduction that differs is not automatically a failure: investigate sources of variation.

## Deeper walkthrough: test a paper's claim

If a paper claims a new image method improves accuracy, check what was held constant: dataset split, input resolution, augmentation, compute, model size, and tuning budget. A comparison is not fair if the new method received extensive tuning while the baseline used default settings.

Separate the paper's abstract claim from the evidence. Does the experiment support all claimed settings or one benchmark? Are results averaged across runs? Is there an ablation showing which component mattered? Does the paper report failures or only best cases?

Search for later work that challenges or reproduces the result. Read code only after understanding the method; code can clarify missing details but may differ from the paper.

A good paper note ends with one question you can test, not just a list of terminology.

## Questions and answers

**Should I read every equation first?**  
No. Understand the problem and method outline, then return to equations tied to the central contribution.

**What is an ablation?**  
A controlled removal or change of one component to test whether it contributes to the result.

**Why question the benchmark?**  
A benchmark may be too narrow, contaminated, or unlike real use. Strong scores only support claims about its tested conditions.

## Practice and mastery

Read one paper related to a course project. Write a paper card and reproduce one small result or implementation detail. Identify what evidence would change your opinion.