# Full AI Course: organized by subject

This course is for a learner starting with little or no AI background. Each subject has its own folder so you can see what belongs to Python, mathematics, AI, ML, NLP, LLMs, and other fields.

There are **13 subject folders and 46 detailed chapter files**, covering the 62 topics in the [progress tracker](../PROGRESS.md). Each chapter is a lesson with explanations, examples, Q&A, practice, and a mastery check. Some technical topics include diagrams.

## Learning path

```mermaid
flowchart TD
    A[Foundations] --> B[Python and software skills]
    B --> C[Mathematics]
    C --> D[Classical AI]
    D --> E[Machine learning]
    E --> F[Deep learning]
    F --> G[Computer vision and NLP]
    G --> H[Transformers and LLMs]
    H --> I[Generative AI systems]
    I --> J[Specialization]
    J --> K[Deployment and responsible AI]
    K --> L[Research and capstone]
```

## Subject folders

| Subject | Main topics |
| --- | --- |
| [Foundations](./foundations/README.md) | AI basics, terminology, task framing, study method |
| [Python and software foundations](./python/README.md) | Python, algorithms, Git, SQL, environments, APIs |
| [Mathematics](./mathematics/README.md) | Algebra, linear algebra, probability, statistics, calculus, optimization |
| [Classical AI](./ai/README.md) | Search, planning, logic, constraints, uncertainty, game reasoning |
| [Machine learning](./ml/README.md) | Problem framing, supervised and unsupervised learning, evaluation |
| [Deep learning](./deep-learning/README.md) | Neural networks, backpropagation, regularization, transfer learning |
| [Computer vision](./computer-vision/README.md) | Images, CNNs, vision tasks, transfer learning, evaluation |
| [Natural language processing](./nlp/README.md) | Text processing, embeddings, sequence models, language tasks |
| [Large language models](./llm/README.md) | Transformers, tokenization, pretraining, inference, adaptation |
| [Generative AI](./generative-ai/README.md) | Prompting, RAG, tool use, agents, image/audio/video, evaluation |
| [AI specializations](./specializations/README.md) | Reinforcement learning, recommendations, time series, graphs, robotics |
| [AI engineering and responsibility](./engineering/README.md) | MLOps, deployment, monitoring, security, privacy, governance |
| [Research and capstone](./research/README.md) | Paper reading, reproducible experiments, advanced study, capstone |


## Practice, projects, and mastery

- [Runnable labs](../labs/README.md) — 22 local exercises, from Python and gradient descent through attention, retrieval, and monitoring.
- [Project ladder](../projects/README.md) — six staged projects with acceptance criteria and a [shared grading rubric](../projects/RUBRIC.md).
- [Mastery checks](../assessments/MASTERY_CHECKS.md) and [100-point scorecard](../assessments/MASTERY_SCORECARD.md) — answer explanations and evidence-based gates.

## Expanded notes and vocabulary

The chapter pages link to long-form, beginner-oriented explanations in [Expanded deep-study notes](DEEP_GUIDES.md). Each subject folder has its own guide with topic explanations, definitions, worked examples, Q&A, and practice. Use the cross-course [AI glossary](GLOSSARY.md) when you meet an unfamiliar term.

## AI/ML field reference

Use the [AI/ML Field Reference](AI-ML-FIELD-REFERENCE.md) for a cross-course glossary, a practical guide to major model families, their strongest use cases, and the tradeoffs behind data, training, inference, memory, and engineering efficiency.

## Which programming languages?

Start with **Python**. Learn **SQL** for databases and basic shell commands for running projects. Add JavaScript/TypeScript if you want a web interface. C/C++ are optional for performance, embedded AI, or robotics. Do not try to learn all languages at once.

## How to use the course

1. Start with [Foundations](./foundations/README.md).
2. Complete each folder's chapters in order and do the practice before moving on.
3. Use the topic checklist in [PROGRESS.md](../PROGRESS.md).
4. Read the folder README to see prerequisites and next steps.
5. Use the [source guide](./SOURCES.md) for official documentation and primary research papers.

The core beginner-to-builder route takes roughly **9–15 months at 6–8 focused hours per week**. Advanced specialization and expertise require continuing projects, deeper theory, paper reading, and experience with real data and users over time. This course prepares you for that work; it does not promise expertise from reading alone.

## What counts as learning

For each chapter, aim to explain the idea in plain language, solve a small example, implement or use the method, evaluate it fairly, and name a failure mode. Finishing a page without being able to do those things is a signal to practice more.