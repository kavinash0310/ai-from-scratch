# Foundations of artificial intelligence
## A beginner's textbook chapter

This chapter gives you a map of the field before asking you to memorize model names. AI is a collection of ways to make systems perceive, reason, learn, plan, communicate, and act. The central question is always concrete: **what information does the system receive, what must it do, and what evidence would show that it did it well?**

## 1. What counts as artificial intelligence?

A route planner, spam filter, chess engine, speech recognizer, and language model may all be described as AI. They do not work in the same way. A chess program can search possible moves using hand-written rules. A spam filter can learn patterns from labeled email. A language model can predict likely text continuations. A robot can combine sensors, geometry, planning, control, and learned perception.

The word **intelligence** in AI does not mean that a program is conscious, experiences emotion, or understands a situation as a person does. In this course, call a system AI when it uses computational methods to produce behavior that solves an intelligent-seeming task. Study what it does, how it works, and where it fails before making claims about its inner experience.

Think of an AI system as a function plus its surrounding environment:

- It receives **inputs**, such as an image, message, sensor reading, or database record.
- It performs **computation**, such as searching, applying rules, or evaluating a learned model.
- It produces an **output**, such as a label, score, sentence, or action.
- A product may convert the output into a **decision**, such as block, approve, route, or ask a human.
- Evaluation checks whether the behavior is useful under realistic conditions.

The final decision can have greater impact than the model score. A spam detector may output a probability of 0.82; an application decides whether to block the message. The **threshold** is a product choice based on the cost of blocking legitimate mail versus allowing spam. A probability is not itself a policy.

### Worked example: a map route

Suppose a map receives a starting location and destination. Its output is a route. A classical search system can represent intersections as states and roads as actions. It can minimize travel time if edge costs represent current travel time. A learned system may predict traffic from past and live observations. A complete route product combines the search, traffic predictions, map data, GPS, interface, and fallback behavior. Calling the whole product “an AI model” hides these distinct parts.

Questions to ask:
1. What location data is current and available?
2. Does the route optimize time, distance, safety, or something else?
3. What happens when a road closes or the GPS is inaccurate?
4. How does the system communicate uncertainty?

These questions are more useful than simply asking whether the app is AI.

## 2. How the main fields fit together

**Artificial intelligence** is the broad field. **Machine learning (ML)** is a set of methods that fit patterns from data. **Deep learning (DL)** is ML with neural networks made from multiple learned layers. **Natural language processing (NLP)** studies language tasks and methods. **Computer vision (CV)** concerns images and video. **Generative AI** describes models or systems that create new content. A **large language model (LLM)** is a language model trained at large scale; many current LLMs use Transformer neural networks.

These are different kinds of labels:

- AI is the umbrella field.
- ML and deep learning are families of methods.
- NLP and CV are application areas.
- Generative AI describes a kind of output or task.
- Transformer is an architecture.
- LLM describes the scale and role of a language model.

A single system can belong to several categories. An image captioner is a generative system in computer vision, may use deep learning, and can include a Transformer. A question-answering service is an NLP application that might use an LLM plus a search index and ordinary application code.

**Symbolic AI** represents knowledge as explicit rules, facts, or constraints. **Machine learning** represents patterns through fitted parameters. **Hybrid AI** combines these approaches. A useful system may use a model to parse a request, a search algorithm to find a valid route, and explicit code to enforce permission rules.

## 3. How a learning system differs from a rule system

A rule system behaves according to rules a developer specifies. For example:

    if account_age_days < 2 and transaction_amount > 5000:
        review_transaction = True

The behavior can be easy to inspect, but people must anticipate useful rules and exceptions. A learned system receives examples such as transaction features and prior outcomes. It adjusts internal **parameters** to reduce an **objective** or **loss**. The model may identify combinations of patterns that were not written as rules, but it can also learn biases or collection artifacts present in the examples.

**Training** is the process of fitting parameters. **Inference** is using the fitted model to calculate a result. **Model** means the fitted mapping from input to output. **Algorithm** means the procedure used to fit it or search through possibilities. Do not confuse an application with its model: preprocessing, permissions, business rules, databases, and human review are often outside the model.

### When not to use ML

If a task has exact rules, a deterministic program may be simpler. If you need to add two numbers, use arithmetic; training a model is wasteful. If the available data is too small or biased to support learning, a model may provide false confidence. ML is especially useful when the input-to-output mapping is hard to specify directly but representative examples exist, such as classifying varied images or recognizing speech.

## 4. Turn a vague need into an AI task

A responsible task definition answers:

1. **User and purpose:** who uses the result and what decision follows?
2. **Unit:** one email, one customer, one image, or one time window?
3. **Prediction time:** what information is available at the exact time of use?
4. **Input:** which data is allowed and relevant?
5. **Output:** category, number, ranking, generated text, or action?
6. **Target:** what outcome counts as correct?
7. **Error costs:** which mistakes matter and how much?
8. **Evaluation:** how will behavior be measured on cases not used to build it?
9. **Boundary:** when should the system abstain or ask for human review?

Example: “Predict customer churn” is vague. A better definition is: “For each active subscription at the start of a month, estimate whether it will be cancelled in the next 30 days, using only information recorded before that month, so a support team can offer voluntary help.” This clarifies timing, target, unit, and user action.

**Data leakage** occurs when information unavailable at prediction time slips into training or evaluation. If the churn model uses the cancellation timestamp as an input, its test score can be excellent and its actual usefulness zero. Think about the real process before selecting features.

## 5. A map for a complete beginner

A strong learning path builds prerequisites gradually:

1. Learn Python values, control flow, functions, files, and debugging.
2. Learn algebra, vectors, matrices, probability, and statistics alongside code.
3. Study problem framing, data quality, classical search, and rule-based reasoning.
4. Learn supervised and unsupervised ML, baselines, splits, and metrics.
5. Study neural networks, gradients, and training behavior.
6. Choose an area such as vision, NLP, recommendation, forecasting, graphs, or robotics.
7. Learn Transformers, LLMs, retrieval, and generative applications.
8. Build a system, evaluate it, document limitations, and maintain it.
9. Read primary research and reproduce a small claim before advancing to research work.

You do not have to master all mathematics before running a simple model. But do not skip the math forever. A spiral works well: use a concept, encounter a limitation, return to the theory, and deepen your implementation.

## 6. Questions and answers

**Does AI always learn from data?** No. Search, planning, logic, and manually written rules can be AI without learning from examples.

**Does a large model know facts the way a database does?** No. Its parameters encode patterns learned from training. Exact retrieval is not guaranteed. Use a database or retrieval system when current, attributable evidence matters.

**If a model is accurate, is the product safe?** Not necessarily. Averages can hide subgroup errors, and a high score on the wrong split can be misleading. Product rules, interfaces, permissions, monitoring, and escalation also matter.

**Can AI replace expertise in a domain?** A model can support a task, but its limitations and the consequences of error must be evaluated. Domain knowledge helps define useful targets and detect implausible outputs.

## 7. Chapter exercise with model answers

Choose a familiar product feature, such as a photo tagger or recommendation feed. Write its input, output, user decision, two possible errors, and one success measure.

Example answer for a photo tagger:
- Input: one image selected by a user.
- Output: likely object labels and scores.
- Decision: suggest labels that the user can accept or edit.
- Errors: miss a relevant object; suggest an offensive or incorrect label.
- Measure: per-class recall and precision on representative images, plus the rate at which users accept or correct suggestions.

The answer is good because it distinguishes a suggestion from an irreversible action and proposes measurements tied to errors.

## 8. What to remember

AI is a field, not one algorithm. Always define the task before choosing a model. Distinguish training from inference and model from application. A benchmark measures behavior on a particular dataset; it does not automatically prove real-world usefulness. Continue with [Python](../python/README.md), [mathematics](../mathematics/README.md), or the [course index](../README.md).