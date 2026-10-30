# Mastery checks with answer explanations

Use these after studying the linked stages. First answer without looking below the questions. Score 2 points for a correct answer with reasoning, 1 for partial understanding, and 0 if guessed or incorrect. A score of 8/10 means revisit the missed concept and redo its lab before moving on.

## Check 1 — Python and math

1. What is the difference between assignment and equality comparison?
2. Why does a loop need a stopping condition or finite collection?
3. If a line predicts y = wx+b, what do w and b control?
4. A model's loss is 16 and its gradient is -4. With learning rate 0.1, what is the gradient-descent update to the parameter?
5. What does a vector's shape tell you?

## Check 2 — Classical AI and data framing

6. What four parts define a basic search problem?
7. When does BFS guarantee a least-cost path?
8. What does A* combine, and what property should its heuristic have for optimality?
9. Why does a wet road not prove it rained?
10. Give an example of a feature that leaks a delivery prediction.

## Check 3 — Machine learning

11. Distinguish supervised and unsupervised learning.
12. Why compare with a baseline?
13. How do parameters differ from hyperparameters?
14. Name one suitable time-aware split and why a random split may fail.
15. What is overfitting?

## Check 4 — Evaluation and statistics

16. Define precision and recall in words.
17. When can accuracy look high while a classifier is poor?
18. Why should the test set not be used for repeated model tuning?
19. What is calibration?
20. Does correlation show that one variable caused another? Explain.

## Check 5 — Deep learning

21. What does a non-linear activation add to a stack of neural layers?
22. What does backpropagation calculate, and what does an optimizer do?
23. What changes in training but usually stays fixed in inference?
24. What is a batch and what is an epoch?
25. Why can training loss fall while validation loss rises?

## Check 6 — NLP, Transformers, and LLMs

26. Is a token ID a semantic measurement? Why not?
27. What are queries, keys, and values used for in attention?
28. What future information does a causal mask block?
29. Does lower temperature make a generated claim more factual?
30. What is the difference between a context window and reliable memory?

## Check 7 — Generative AI applications

31. What are the retrieval and generation stages in RAG, and why evaluate them separately?
32. Why must generated structured output be parsed and validated?
33. How should a retrieved instruction inside a document be treated?
34. Give one situation where retrieval is preferable to fine-tuning.
35. What does abstention mean?

## Check 8 — Specialization, deployment, and research

36. Why can a click not be treated as an unbiased recommendation label?
37. Why use chronological backtesting for forecasting?
38. What is a data-drift alert evidence of, and what does it not prove?
39. What is an ablation?
40. What should another person need in order to reproduce a capstone?

## Answer key

1. Assignment binds a name to a value; equality comparison asks whether two values match.
2. Without a stopping rule, repetition may never end; finite iteration bounds the work.
3. w controls slope/feature effect, while b shifts the prediction baseline.
4. Update parameter to old value minus 0.1 times -4, so it increases by 0.4.
5. The number of entries along each axis; compatible shapes are required for operations.
6. Initial state, actions, transition rules, and a goal test; path cost is also needed when routes have different costs.
7. When each action has equal cost (or an equivalent condition); otherwise BFS counts steps, not actual cost.
8. Cost already spent plus estimated remaining cost; for optimal A* under standard assumptions the heuristic is admissible and does not overestimate.
9. Other causes, such as a sprinkler, can wet a road; implication cannot be reversed without more evidence.
10. The actual delivery timestamp when prediction is supposed to occur at checkout.
11. Supervised uses input-target examples; unsupervised seeks structure without target labels.
12. A baseline shows whether extra model complexity adds useful value.
13. Parameters are learned from training data; hyperparameters are selected by the practitioner.
14. Train on earlier periods and validate/test on later periods; random splitting can let future patterns leak into training.
15. Fitting accidental training details that do not carry to relevant new data.
16. Precision: how many predicted positives are truly positive. Recall: how many actual positives are found.
17. If the majority class dominates, predicting it for every case can yield high accuracy while missing the rare class.
18. Repeated decisions adapt to the test set and make its score optimistic.
19. Predicted probabilities match observed frequencies among similar cases.
20. No. A confounder, selection effect, or coincidence can cause association; causality requires assumptions and design.
21. Without non-linearity, stacked linear transformations collapse to one linear transformation; activation lets the network represent curves and interactions.
22. Backpropagation computes gradients by the chain rule; the optimizer uses them to update parameters.
23. Training updates learned parameters; ordinary inference uses fixed parameters.
24. A batch is the examples in one update; an epoch is one pass through the training set.
25. The model may start fitting training-specific noise or quirks.
26. No. It is an index into a tokenizer vocabulary, not an ordered measure of meaning.
27. Query-key compatibility determines attention weights; value vectors carry information mixed by those weights.
28. It blocks a position from attending to future tokens so next-token training cannot read its target.
29. No. Temperature changes sampling variability, not evidence or factuality.
30. The context window is a token limit; reliable memory means the model actually uses relevant information, which is not guaranteed by length.
31. Retrieval selects evidence; generation writes a response from it. Separate measures identify whether failure came from missing evidence or poor use of evidence.
32. Plausible-looking text may be malformed, missing fields, wrong types, or factually unsupported.
33. As untrusted data, not as an instruction with authority to override the application.
34. When facts change often or answers must cite source documents.
35. Deliberately declining or deferring when evidence or confidence is insufficient under the system's policy.
36. Users click only what was displayed; lack of a click may mean no exposure, not dislike.
37. The real task predicts future values from past data; a chronological split reflects that direction.
38. Evidence that input distributions changed; it does not itself prove performance or harm worsened.
39. A controlled removal or change of a component to test its contribution.
40. Code, data access/license/version, preprocessing, environment, settings, split, metrics, and run instructions.

For practical skill, pair this check with the labs and [project ladder](../projects/README.md). Recall alone is not mastery.