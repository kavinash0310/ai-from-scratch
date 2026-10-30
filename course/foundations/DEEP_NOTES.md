# Foundations — full beginner notes

This guide expands both foundation chapters with vocabulary, examples, and mental models needed before the technical subjects. The goal is to describe what a system does in ordinary language before choosing algorithms.

## 1. What AI is and how the fields relate

### Begin with the task, not the label

Artificial intelligence (AI) is a broad engineering and research field concerned with building systems that perform tasks associated with intelligent behavior: recognizing patterns, making predictions, using language, planning actions, or perceiving the world. The label alone does not tell you how a system works. A hand-written chess search program and a neural network that recognizes cats can both be called AI, but one mainly searches explicit possibilities while the other learns numerical patterns from examples.

A useful map is:

- **Artificial intelligence:** the broad umbrella of methods for intelligent behavior.
- **Machine learning (ML):** methods that fit patterns from data instead of specifying every rule manually.
- **Deep learning (DL):** ML using neural networks with many learned layers.
- **Natural language processing (NLP):** methods for analyzing, generating, or interacting with human language. NLP can use rules, classical ML, or deep learning.
- **Generative AI:** systems that produce new text, images, audio, code, video, or other content. “Generative” describes the task rather than one architecture.
- **Large language model (LLM):** a language model with many parameters trained on large text collections. Many modern LLMs use Transformers, but language model is the task, Transformer is an architecture, and large describes scale.

A rule system receives rules written by people. A learned system receives examples and adjusts parameters so predictions fit patterns. A hybrid system can combine learned components with databases, search, constraints, and human-written safeguards. Many real products are hybrid.

### Inputs, outputs, and objectives

Describe an AI task as a contract:
1. What information is available at decision time?
2. What output must the system produce?
3. What counts as a useful or harmful error?
4. Who is affected by the result?
5. How will success be measured on cases not used to build it?

For example, a message classifier receives message text and outputs a probability that it is spam. The probability is not the same as the final action: a product chooses a threshold based on the cost of blocking a real message versus allowing spam.

**Model** means the learned or programmed mapping from inputs to outputs. **Algorithm** means the procedure used to search, train, or calculate. **Data** means recorded examples or evidence. **Parameter** means an internal value learned or set by a model. **Inference** means using a model to produce an output. **Training** means adjusting learnable parameters from examples and an objective.

### A simple worked comparison

Suppose you want to decide whether a fruit is an apple.

- A rule approach might say: if color is red and diameter is in a range, predict apple. It is interpretable but brittle when apples are green.
- A supervised learning approach sees labeled pictures of apples and other fruit, then learns visual features from examples. It may generalize to green apples if the training set represents them.
- A complete application also needs camera input, image preprocessing, an output threshold, an interface, and a way to handle uncertain cases. The neural network is only one component.

### Common confusions and Q&A

- AI does not mean a machine is conscious or human-like.
- A fluent answer is not automatically correct.
- A training score is not proof that a system works in its intended environment.
- Bigger models can represent more patterns, but size alone does not fix poor data, bad objectives, or weak evaluation.

**Is every AI system a neural network?** No. Search, planning, logic, rules, and optimization can be AI without neural networks.

**Is NLP the same as LLMs?** No. NLP is a field of tasks and methods. LLMs are one family of models used for many language tasks.

**What is the difference between a model and an application?** A model computes a mapping; an application surrounds it with data handling, decisions, safety checks, storage, interfaces, and monitoring.

Practice: choose a familiar product feature such as spam filtering, maps, or recommendations. State its input, output, possible errors, and one non-neural method that might solve it.

## 2. How to study AI and build durable skill

### Learn in a spiral

AI depends on several subjects, but you do not need to finish every subject before touching a model. Use a spiral: learn a small idea, implement it, inspect where it fails, then return to the math and theory that explain the failure. For example, use a linear classifier first; later study vectors, loss, gradients, and regularization to understand why it learned its boundary.

A productive cycle is:
1. **Predict:** write down what you think will happen.
2. **Implement:** build the smallest runnable version.
3. **Measure:** compare it with a baseline on held-out examples.
4. **Explain:** write what each important line and metric means.
5. **Break:** alter one assumption and observe the failure.
6. **Revise:** correct your explanation and record the next question.

This is active learning. Watching or reading can introduce concepts, but retrieval practice (recalling without looking), implementation, and explaining from memory reveal gaps more reliably.

### Vocabulary for learning

- **Prerequisite:** knowledge that makes a topic easier, not a gate that prevents all exploration.
- **Baseline:** the simplest reasonable method used for comparison.
- **Experiment:** a controlled change with a question and measurable result.
- **Hypothesis:** a prediction about what a change will do and why.
- **Metric:** a defined numerical summary of performance; it can still fail to capture what users care about.
- **Reproducibility:** another person can run the documented process and obtain comparable results.
- **Portfolio project:** a finished artifact showing code, data choices, evaluation, limitations, and communication—not just a screenshot.

### A sustainable routine

Choose one chapter and one small deliverable each week. Example: learn Python loops; implement a word counter; test empty input and punctuation; explain the code in a README. When you reach ML, keep a notebook of dataset, split, baseline, metric, and observed errors. When you reach LLM applications, save representative prompts and outputs, including failures.

Use this project log:

- Question:
- What I expected:
- What I changed:
- Data and split:
- Baseline:
- Result:
- Examples of errors:
- What the result does not prove:
- Next experiment:

For an equation, name every symbol, check shapes, and calculate a tiny example by hand. For code, trace one input through each line; do not treat a library call as magic. For a paper, read the abstract, problem setup, method figure, experiments, limitations, and related work before trying every proof.

When blocked, reduce scope: fewer examples, fewer parameters, a tiny synthetic dataset, or a hand-calculated case. Keep a glossary in your own words and revisit it; copying a definition is not the same as being able to use it.

### Measure progress honestly

Do not measure learning by hours watched or tutorials completed. Measure whether you can explain a concept without notes, implement a small example, predict the effect of a change, detect leakage or a misleading metric, compare against a baseline, and state limitations.

Practice: after any chapter, close it and make a one-page concept map. Mark each term green (can explain and use), yellow (recognize but cannot apply), or red (unclear). Revisit yellow and red through examples, not rereading alone.

Continue to [Python](../python/README.md), study [mathematics](../mathematics/README.md) alongside code, then visit [classical AI](../ai/README.md) and [machine learning](../ml/README.md). The [main course index](../README.md) shows the full route.