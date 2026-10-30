# Lesson 00 — A map of artificial intelligence

## Learning goals

By the end, you should be able to explain what people mean by AI, distinguish several important subfields, and describe the path from a problem to a working AI system.

## Start with the everyday meaning

Imagine asking a computer to sort your photos into “cat” and “not cat.” A computer could follow a list of hand-written rules, such as “if the image has pointy ears and whiskers, call it a cat.” That is an AI-like system built from explicit rules. It may work on easy pictures and fail when the cat is hidden, facing away, or drawn as a cartoon.

Another approach is to show the computer many example pictures and the correct answers. A learning algorithm adjusts an internal model until it becomes good at predicting answers for examples it has not seen. This is machine learning.

**Artificial intelligence (AI)** is the broad field of designing systems that perform tasks associated with intelligent behavior: perception, language, planning, decision-making, or learning. AI is not one particular technique.

**Machine learning (ML)** is a family of methods in which a system uses data to improve a task instead of relying only on hand-written rules. A model is the learned function that turns inputs into outputs.

**Deep learning (DL)** is machine learning that uses neural networks with many layers. The layers learn useful internal representations from data. Deep learning is especially useful with images, audio, language, and other complex inputs.

**Generative AI** creates new outputs such as text, images, audio, or code. A large language model (LLM) is a generative model trained on sequences of tokens. Generative AI is one branch of AI, not the whole field.

## One problem, several possible methods

Suppose you want a program to find a route across a map.

- A search algorithm can examine possible roads and choose a low-cost route. It follows a defined map and does not need to learn from examples.
- A machine-learning model can estimate traffic or travel time from past trips.
- A generative model might explain the route in natural language.
- A complete product might combine all three, plus ordinary software that displays the map.

AI projects often combine learned components with normal code. The model is rarely the whole system.

## A useful map of the field

- **Search and planning:** find a sequence of actions that reaches a goal.
- **Knowledge and reasoning:** represent facts, rules, constraints, or uncertainty.
- **Machine learning:** learn patterns from examples.
- **Computer vision:** interpret images and video.
- **Natural language processing:** work with human language.
- **Speech and audio:** recognize, classify, or generate sound.
- **Recommender systems:** rank items for a person or context.
- **Reinforcement learning:** learn actions through rewards and interaction.
- **Robotics:** connect perception, planning, and action in the physical world.
- **Generative modeling:** create new samples that resemble learned patterns.

## The basic learning loop

A machine-learning project usually has these steps:

1. Define a task that matters to someone.
2. Collect examples that represent the task.
3. Choose what information is available at prediction time.
4. Split examples so some remain unseen during training.
5. Train a simple baseline.
6. Measure errors on held-out data.
7. Decide whether the results are useful and safe enough.
8. Improve data, model, or product design.
9. Monitor the system after release.

A model can be mathematically impressive and still be useless if the task is poorly defined, the data is misleading, or the output is not actionable.

## Important vocabulary

- **Input:** information given to a system.
- **Output or prediction:** what the system returns.
- **Data:** recorded examples or observations.
- **Algorithm:** a procedure for calculating an answer or learning from examples.
- **Model:** a learned set of values and rules used to produce predictions.
- **Training:** adjusting model values using examples and an objective.
- **Inference:** using a trained model to make a prediction.
- **Evaluation:** measuring behavior on examples that were not used to fit the model.
- **Deployment:** making a model available in a real workflow.

## Common misunderstandings

- AI is not automatically conscious or human-like. A system can perform a narrow task well without understanding it the way a person does.
- More data is not always better. Data can be irrelevant, duplicated, biased, mislabeled, or unlawful to use.
- A fluent answer is not proof of truth. Generative models can produce plausible mistakes.
- High test accuracy is not the same as usefulness. The test may not represent the real world, or the cost of a particular mistake may be high.
- “From scratch” does not mean reinvent every tool. Learn the mechanism, implement small examples, then use tested libraries for larger work.

## Review questions with answers

**1. Is every AI system a machine-learning system?**  
No. A route-search program or rule-based expert system can be part of AI without learning from data. Machine learning is one major approach within AI.

**2. How are deep learning and machine learning related?**  
Deep learning is a subset of machine learning. It uses multi-layer neural networks to learn representations and predictions.

**3. Is ChatGPT the same thing as AI?**  
No. It is one type of product built around generative language models and software systems. AI also includes search, vision, robotics, recommendation, planning, and many other areas.

**4. Why do we need test data?**  
Training data tells the model what patterns to fit. Test data estimates how the model behaves on examples it did not train on. Reusing training examples for the final score can make performance look better than it is.

**5. What is the difference between training and inference?**  
Training adjusts model values using data and an objective. Inference applies the fixed trained model to new input.

## Practice

Choose a task from daily life, such as sorting email or finding a bus route. Describe:
- the user and desired outcome;
- the input and output;
- a rule-based solution;
- a solution that could learn from examples;
- one possible failure and its cost.

## Mastery check

Explain AI, ML, deep learning, and generative AI to a friend using one example. If you can show how they relate without calling them synonyms, continue to Lesson 01.