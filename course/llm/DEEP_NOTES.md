# Large language models — full beginner notes

An LLM is a trained model that assigns probabilities to token sequences or produces representations useful for language tasks. This guide expands the three LLM chapters; use the dedicated [Transformer and attention lesson](01-transformers-attention.md) for the full architecture walkthrough.

## 1. Tokenization, pretraining, and inference

A **tokenizer** converts text into token IDs from a fixed vocabulary. A token can be a word, part of a word, punctuation, or byte-like unit. Token IDs are indices, not semantic measurements. Token count differs from word count and affects context use, latency, and cost.

During **pretraining**, an autoregressive model sees a prefix and predicts the next token. **Cross-entropy loss** rewards probability assigned to the observed next token. A **parameter** is a learned numeric value; billions of parameters do not form a searchable database with guaranteed factual recall. Training data influences patterns and errors the model learns.

At **inference**, weights are generally fixed. The model calculates next-token scores; a decoding rule chooses one token; that token is appended and the process repeats. **Greedy decoding** chooses the highest-scoring token. **Temperature** reshapes the distribution before sampling; **top-p** restricts sampling to a cumulative-probability set. Neither establishes truth. A **context window** is the maximum sequence considered by a call; it is not perfect memory.

## 2. Adaptation and fine-tuning

**Prompting** gives task instructions and examples at inference without changing model weights. **Fine-tuning** trains on task-specific examples. **Supervised fine-tuning (SFT)** teaches desired input/output patterns. **Preference optimization** uses comparisons or preference signals to shape responses. **Parameter-efficient fine-tuning** updates a small added parameter set instead of all model weights.

**LoRA** represents an update through low-rank matrices added to selected weight transformations. It can reduce trainable parameters and memory, but still requires careful data, evaluation, and versioning. **Quantization** stores weights at lower numerical precision to reduce memory or speed computation, with possible quality tradeoffs.

Choose adaptation based on evidence: prompting for clear instructions, retrieval for changing knowledge, fine-tuning for stable response patterns or task behavior, and tools for actions or exact computation. Fine-tuning is not a reliable way to keep an ever-changing database current.

## 3. Evaluation and deployment

A language model can be evaluated on held-out tasks, but one benchmark score is not a universal capability measure. Build a task-specific test set from intended use, including easy, typical, ambiguous, and adversarial examples. Measure factual correctness, instruction following, format validity, latency, cost, and failure severity.

**Perplexity** summarizes predictive uncertainty on a token dataset; lower values do not necessarily mean better user answers. **Human evaluation** needs a rubric and multiple raters for subjective properties. **Contamination** occurs when evaluation material appeared in training, making results overly optimistic. **Distribution shift** means deployment requests differ from test cases.

Track model identifier, prompt, decoding settings, dataset version, and evaluator version. Keep a refusal and escalation path for unsupported or high-impact questions. Confident wording is not a confidence estimate.

### Q&A and practice

**Does temperature improve correctness?** No; it changes sampling.
**Does a larger context window guarantee recall?** No; relevant evidence may still be missed or diluted.
**When is RAG preferable to fine-tuning?** Often when the system needs changing, attributable source material; evaluate retrieval quality and permissions.

Practice: inspect tokenization, compare greedy and sampled output on a fixed prompt, make an evaluation set, record failures, and explain which qualities need human review.