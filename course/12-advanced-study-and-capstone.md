# Part 12 — Advanced study, research, and capstone

## Chapter 58 — Move from practitioner to advanced practitioner

Advanced ability is not knowing every architecture. It is making sound choices under uncertainty. For each method, learn:
- its objective and assumptions;
- data requirements;
- computational cost;
- known failure modes;
- comparison baselines;
- evidence for and against using it.

Deepen probability, linear algebra, optimization, numerical methods, experimental design, and software systems as your chosen specialty demands. Implement small pieces to understand mechanisms; use reliable libraries for large experiments.

## Chapter 59 — Read papers critically

Read a paper in passes:
1. abstract: question and claim;
2. introduction: problem and contribution;
3. method: what changed and what assumptions are made;
4. experiments: datasets, baselines, metrics, ablations, compute;
5. limitations: what has not been shown;
6. reproduction: whether a key result can be recreated.

Write a paper card: claim, method, strongest evidence, weakest assumption, data/compute cost, one ablation, and next question. Treat preprints as research reports, not guaranteed facts. Check later versions and independent replications where available.

## Chapter 60 — Reproducible research

Keep a fixed evaluation protocol. Record code commit, dataset version, preprocessing, model configuration, random seeds, hardware, software versions, and runtime. Run multiple seeds when randomness can change the result. Report mean and spread rather than only the best run.

An ablation removes one component to test whether it matters. A negative result can be useful when the design and evaluation are sound. Do not tune on the test set or selectively report successful runs.

## Chapter 61 — Choose a specialization and form a research question

Example specialties:
- LLM training or inference efficiency;
- NLP evaluation and multilingual models;
- computer vision robustness;
- recommendation and ranking;
- forecasting;
- reinforcement learning;
- robotics;
- causal or scientific ML;
- trustworthy AI and privacy.

Write a research question that is narrow enough to test. “Make AI better” is not testable. “Does augmentation X improve recall on camera Y without reducing precision on location Z?” is closer to an experiment.

## Chapter 62 — Capstone from question to evidence

A capstone should include:
1. user, problem, and non-goals;
2. data source, permission, and quality review;
3. baseline and model rationale;
4. evaluation split and metric;
5. failure analysis and limitations;
6. reproducible setup;
7. demo or clear usage instructions;
8. safety, privacy, and impact notes;
9. next experiment.

Do not choose a project only because it uses a large model. A well-measured small model can demonstrate more expertise than an untested chatbot.

## Suggested research reading

- [Deep Learning textbook](https://www.deeplearningbook.org/) for mathematical and conceptual depth.
- [Dive into Deep Learning](https://d2l.ai/) for interactive explanations and code.
- [ResNet](https://arxiv.org/abs/1512.03385) for residual learning in computer vision.
- [BERT](https://arxiv.org/abs/1810.04805) for bidirectional language representation pretraining.
- [LoRA](https://arxiv.org/abs/2106.09685) for parameter-efficient language-model adaptation.
- [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) for a foundational diffusion formulation.

Read after the matching course parts. Use a paper to learn experimental reasoning, not as a list of facts to memorize.

## Q&A

**When am I an expert?**  
There is no single credential or finish line. Expertise is demonstrated through repeated strong work: clear framing, reliable experiments, technical depth, responsible deployment, and contributions others can inspect.

**Why reproduce a result if the paper already reports it?**  
Reproduction reveals hidden assumptions, implementation details, data issues, and how robust the claim is. It teaches more than reading the abstract.

**How do I avoid chasing every new model?**  
Pick a user problem or research question, identify what evidence could change your decision, and study only methods relevant to that question.

**What makes a capstone convincing?**  
A clear problem, baseline, fair evaluation, reproducible work, error analysis, honest limits, and an explanation understandable to another person.

**Can I skip the math and let libraries handle it?**  
Libraries handle calculation, not judgment. Advanced practitioners need enough math to diagnose objectives, assumptions, optimization, uncertainty, and failure.