# Advanced AI study path: extensions beyond the core

## Honest assessment

The existing core is a good map for a beginner and can support first projects when paired with its labs and project ladder. It is **not enough by itself to make someone an expert**. Many lesson pages are short introductions, and expertise requires deeper study, implementation, evaluation, specialization, and feedback.

The right next step is not to make the beginner sequence endless. Keep the core in order and treat this path as optional advanced study. The topic check compares the repo with published curricula: CS2023 (ACM, IEEE-CS, AAAI) includes reasoning, machine learning, perception, language, robotics, and societal impact; Stanford CS229 lists learning theory, probabilistic generative models, EM, dimensionality reduction, reinforcement learning, and control. This repo already introduces many neighboring areas; these additions make several important concepts explicit.

## Advanced core extensions

1. [Learning theory and probabilistic models](./ml/06-learning-theory-and-probabilistic-models.md) — generalization, Naive Bayes, GMM/EM, PCA/ICA, model selection.
2. [Causal inference and experiment design](./ml/07-causal-inference-and-experiment-design.md) — A/B testing, confounding, uncertainty, treatment effects, observational methods.
3. [Data and feature pipelines](./engineering/04-data-and-feature-pipelines.md) — point-in-time correctness, leakage, training-serving skew, lineage.
4. [Efficient training and inference](./engineering/05-efficient-training-and-inference.md) — GPU memory, precision, quantization, batching, distributed training.
5. [Robustness and AI safety testing](./engineering/06-robustness-and-ai-safety-testing.md) — shift, threat models, red teaming, access controls, evidence.

## Specialization electives

Choose based on your intended work:

- [Generative model families](./deep-learning/04-generative-model-families.md) — autoregressive, VAE, GAN, diffusion, and flow methods.
- [Information retrieval and speech](./nlp/04-information-retrieval-and-speech.md) — ranking, lexical and dense search, ASR, speech metrics.
- [Foundation-model systems and evaluation](./llm/04-foundation-model-systems-and-evaluation.md) — data, compute, distributed training, benchmark caveats, application evaluation.

## Completion standard

For each module, complete its practice, reproduce a small experiment, and write down assumptions, baseline, metric, failure modes, and evidence. A learner should be able to explain the method, state when it fails, and justify whether it is appropriate for a project.

## Sources for this curriculum gap check

- [CS2023 curriculum report](https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm)
- [Stanford CS229 topic schedule](https://cs229.stanford.edu/materials/Handout2.pdf)
- [NVIDIA deep-learning performance guide](https://docs.nvidia.com/deeplearning/performance/dl-performance-getting-started/index.html)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
