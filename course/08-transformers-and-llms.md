# Part 8 — Transformers and large language models

## Chapter 38 — Attention and transformer blocks

The transformer was introduced as an architecture that uses attention rather than recurrence for sequence transduction. Read the original [Attention Is All You Need](https://arxiv.org/abs/1706.03762) after this chapter.

Input text becomes token IDs, then embeddings. Positional information gives the model a way to represent order. A transformer block combines attention, a feed-forward network, residual connections, and normalization.

For each token, learned projections form a query (what this position seeks), key (what it offers for matching), and value (the information it carries). Attention scores compare queries with keys; softmax turns scores into weights; weighted values are combined:

Attention(Q, K, V) = softmax(QKᵀ / √dₖ) V

A causal mask prevents a decoder position from seeing future tokens. Multi-head attention runs several learned projections in parallel. It does not mean each head has a stable, simple human interpretation.

## Chapter 39 — Pretraining and next-token prediction

An autoregressive language model predicts a distribution over the next token. Given “A triangle has”, it assigns scores to possible continuations. Training increases probability for the observed next token across many sequences.

The loss is typically cross-entropy between the predicted distribution and the actual next token. Repeating this process teaches language regularities and information present in training data. It also teaches artifacts and biases in those data.

Pretraining is expensive because it uses large models, data, and accelerator time. A learner should study tokenization, training objectives, small models, and inference; training a production-scale LLM is not required.

## Chapter 40 — Context, decoding, and inference

The context window is the amount of tokenized input the model can attend to in one call. More context can include more material but raises memory and compute needs; it does not guarantee better attention to every detail.

At inference, the model generates a next-token distribution. Greedy decoding selects the most likely next token. Sampling draws from a distribution, with temperature and top-p altering randomness. These settings influence style and variety; they do not make unsupported facts reliable.

A response may be plausible but false. The model's internal weights are not a transparent, current database. Use retrieval, tools, citations, or abstention where evidence matters.

## Chapter 41 — Model families and adaptation

Encoder models create contextual representations and are often useful for classification or extraction. Decoder models generate continuations. Encoder-decoder models map one sequence to another, such as translation.

Adaptation options:
- prompting: supply instructions/examples at inference;
- supervised fine-tuning: train on input-output examples;
- preference training: shape behavior using comparisons;
- parameter-efficient fine-tuning: update a small adapter or low-rank parameterization;
- distillation: train a smaller model to imitate a larger model's outputs.

LoRA is one low-rank adaptation approach; see the [original paper](https://arxiv.org/abs/2106.09685). Each choice has data, compute, evaluation, and licensing implications.

## Chapter 42 — LLM limitations and evaluation

Measure task performance, factual support, refusal behavior, robustness, cost, and latency. Use examples beyond those shown to the prompt author. Evaluate per language and domain if the system claims to support them.

Do not treat fluent language as evidence of reasoning or knowledge. Model outputs can depend on phrasing and decoding settings. Build deterministic checks around structured outputs and tools where possible.

## LLM data flow

```mermaid
flowchart LR
    A[Text] --> B[Tokenizer]
    B --> C[Token IDs]
    C --> D[Embeddings plus positions]
    D --> E[Transformer blocks: attention and MLP]
    E --> F[Next-token probabilities]
    F --> G[Decoding selects token]
    G --> H[Append token and repeat]
```

## Q&A

**Does the attention equation mean the model consciously focuses?**  
No. “Attention” is a name for a learned weighted calculation. It can be inspected mathematically, but should not be equated with human attention or complete understanding.

**Why divide by the square root of key dimension?**  
Dot-product magnitudes tend to grow with dimension. Scaling helps keep softmax inputs in a useful range for optimization.

**Does a larger context window guarantee a better answer?**  
No. The model may miss or underuse relevant details, and long context costs more. Retrieval and careful prompt structure may help.

**How is pretraining different from instruction tuning?**  
Pretraining learns broad sequence patterns from a large corpus. Instruction tuning trains responses to follow task-style examples. They have different objectives and data.

**When should facts be stored in a retrieval system instead of fine-tuned into weights?**  
When facts change, need citations, or come from private approved sources. Fine-tuning is more suitable for repeated behavior or style than for maintaining a current reference database.

## Practice

1. Draw the Q, K, and V flow for a sentence and explain each role.
2. Calculate a tiny two-token attention example using scores and normalized weights.
3. Explain why causal masking is required for next-token training.
4. Compare a decoder language model and an encoder model by objective and typical use.
5. Read the abstract of Attention Is All You Need and summarize the contribution without claiming the model understands like a person.

## Mastery check

You can trace text through tokenization, embeddings, transformer blocks, next-token probabilities, and decoding; explain the training objective; and name a failure that evaluation must catch.