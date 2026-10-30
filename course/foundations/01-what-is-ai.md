# Chapter 1 — What is artificial intelligence?

## Start with a task

Artificial intelligence is a broad field about building systems that perform tasks associated with intelligent behavior: perceiving, searching, planning, learning, communicating, or acting. AI is not one algorithm, and a system does not need to be conscious to be useful.

Imagine a map application finding a route. A search algorithm explores possible roads and minimizes travel cost. A traffic model may learn travel times from past trips. A language model may explain the route. Ordinary software displays the map. The product combines methods; no single component is “all the AI.”

## The family tree

- **AI** is the broad field.
- **Machine learning (ML)** learns patterns or decision rules from examples.
- **Deep learning (DL)** is ML using neural networks with multiple layers.
- **Natural language processing (NLP)** covers computational work with human language.
- **Language models** learn probability patterns over sequences of language tokens.
- **Large language models (LLMs)** are large language models trained at scale and adapted for broad tasks.
- **Generative AI** creates outputs such as text, image, sound, or video.

These categories overlap. An LLM is usually deep learning and NLP; generative AI also includes image and audio systems. Classical search AI can be AI without ML.

## Rule-based versus learned systems

A rule-based program uses explicit instructions written by people. It is predictable when rules are clear, but exceptions grow difficult. A learned model adjusts internal parameters using examples. It can capture patterns that are hard to write down, but its behavior depends on data and may be hard to explain.

Use rules for exact constraints such as “a user cannot spend more than their balance.” Use learned predictions for uncertain patterns such as estimating delivery time from historical trips. Many products combine both.

## A model is one part of a system

A useful AI system needs:
1. a clearly defined user and task;
2. appropriate data or knowledge;
3. a model or algorithm;
4. evaluation on examples that mimic real use;
5. an interface and fallback path;
6. monitoring and an owner.

A model score does not tell you whether it is worth using. The decision, costs of errors, and system behavior matter.

## Worked example: email triage

Suppose you want to sort email into urgent and ordinary. Define the input as a message plus metadata available when it arrives. The output is a category. A baseline might be a few explicit sender or subject rules. An ML model could learn from labeled historical examples. A major risk is that the labels reflect old habits or miss urgent messages written in an unfamiliar style. Evaluation should inspect false negatives, not only overall accuracy.

## Questions and answers

**Is AI the same as ChatGPT?**  
No. ChatGPT is an application built around language models and software. AI also includes planning, search, vision, recommendation, robotics, and other fields.

**Does machine learning mean the computer learns like a person?**  
No. In ML, “learning” means adjusting a mathematical model to reduce an objective using data. It does not imply human awareness or understanding.

**Can rules and ML work together?**  
Yes. A model can estimate an uncertain quantity while rules enforce hard limits. This is often safer than asking a model to enforce every policy itself.

**Why can a fluent model still be wrong?**  
Fluency is a pattern in generated text, not a proof of truth. The model may lack evidence, combine facts incorrectly, or repeat a misleading pattern.

## Practice

For a task you know, write the user, input, output, baseline, one learned approach, and the cost of a wrong result.

## Mastery check

Explain AI, ML, deep learning, NLP, and generative AI using one example for each. If you can show how they overlap without treating them as synonyms, continue.