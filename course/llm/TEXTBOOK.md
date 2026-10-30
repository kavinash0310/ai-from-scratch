# Large language models
## A beginner's textbook chapter

A large language model predicts or represents sequences of tokens. Many modern LLMs use Transformer architectures and are pretrained on large text collections, then adapted for tasks. They can write fluent responses, but fluency alone does not guarantee truth, reasoning, or reliable memory.

## 1. Tokenization and embeddings

A tokenizer maps text into a sequence of integer IDs. A token may be a word, subword, punctuation mark, or byte-like unit. Token ID is an index, not a meaningful numerical amount; token 700 is not “more” than token 20.

The tokenizer vocabulary constrains how text is segmented. Uncommon names, code, numbers, and multilingual writing can split into many tokens. This affects context length, serving cost, and what text is visible in one model call. A token embedding maps each ID to a learned vector. Position information helps the model represent order.

## 2. Transformer attention

Self-attention lets each position mix information from other positions. Learned projections create query, key, and value vectors. Queries are compared with keys to calculate attention weights; values carry the information being combined.

Scaled dot-product attention is:

    softmax(Q*K-transpose / sqrt(key_dimension) + mask) * V

The mask blocks positions that should not be visible. Scaling keeps dot-product magnitudes manageable. Softmax turns each row into weights that sum to one. The weighted values become context-enriched representations.

Multi-head attention performs several such calculations in parallel. A Transformer block also includes a feed-forward network, residual paths, and normalization. Attention allows parallel processing during training, but standard dense attention compares every pair of positions. Its score matrix grows approximately with sequence length squared, making long contexts memory- and compute-intensive.

A causal decoder masks future tokens. An encoder can use both left and right context. An encoder-decoder model reads an input with an encoder and generates an output with a decoder. These architectures support different patterns of use.

Read the [Transformer chapter](01-transformers-attention.md) for tensor shapes and a worked numerical calculation.

## 3. Pretraining objective and inference

An autoregressive language model predicts the next token given earlier tokens. Training compares its predicted distribution with the observed next token, often using cross-entropy. This objective teaches statistical patterns that help predict text. It does not guarantee factual recall or human-like understanding.

During training, parameters are updated. During ordinary inference, model weights stay fixed. The model produces a next-token distribution; a decoding procedure chooses a token; the chosen token joins the context; the cycle repeats.

- **Greedy decoding** selects the most likely next token.
- **Temperature** changes the distribution's concentration before sampling.
- **Top-p sampling** restricts choices to a likely cumulative-probability set.
- **Beam search** tracks several high-scoring partial sequences.

These methods change output variation and search; they do not add evidence or factuality. A low-temperature answer can be confidently wrong.

The **context window** limits tokens in one call. It is not a guarantee that every detail in a long prompt will be attended to or recalled. Relevant evidence may be ignored or diluted. Retrieval can be more efficient than placing every document in the prompt.

## 4. Adaptation methods

**Prompting** gives instructions and examples without updating weights. **Supervised fine-tuning** continues training on desired input-output examples. **Preference optimization** uses comparisons or preference signals to shape behavior. **Parameter-efficient fine-tuning**, such as LoRA, trains a small set of added parameters while leaving most base weights fixed.

**Quantization** stores weights with fewer bits, often reducing memory and sometimes speeding inference at a quality tradeoff. **Distillation** trains a smaller model to imitate a larger one. **Pruning** removes or reduces components. These are engineering methods that need evaluation; they are not automatic free improvements.

Choose the intervention that matches the problem:
- Use prompting for clear instructions and examples.
- Use retrieval for changing, source-based knowledge.
- Use fine-tuning for stable patterns that examples can teach.
- Use validated tools for exact calculations or authorized actions.
- Use quantization or smaller models when serving resource limits justify the tradeoff.

## 5. Evaluation and limitations

A benchmark score applies to a test set and setup. **Perplexity** measures how surprised a language model is by a text sequence; it is not a complete measure of user-answer quality. **Contamination** occurs if test material appeared in training data, which can make results optimistic. Evaluation sets should include ordinary, ambiguous, unanswerable, and adversarial cases.

Measure factual support, instruction following, format correctness, harmful errors, latency, memory, and cost. Check citation quality when answers use sources. Keep raw examples of failure. Confident tone is not a probability estimate. Use abstention when evidence is missing, and human review for high-impact actions.

## 6. Worked example: next-token prediction

For the prefix “The cat sat on the,” a model might assign the next-token probabilities “mat” 0.45, “floor” 0.20, “chair” 0.10, and other tokens 0.25. The model does not choose a complete sentence in one step. It selects one token, appends it, recalculates a distribution, and continues. The output depends on tokenizer units and the decoding rule.

If the training text often contains a false statement, next-token training may also learn that continuation pattern. Improving fluency is not equivalent to checking facts against evidence.

## 7. Questions and exercises

**Does a model store facts like a database?** Learned parameters encode patterns, but retrieval is not a transparent exact lookup. Use a database or retrieval for current verifiable facts.

**Does a larger context window create better memory?** No. It allows more tokens, but use of relevant details still must be measured.

**Does fine-tuning keep facts current?** Not reliably. A changing fact store is usually better handled with retrieval or structured data.

Exercise: run the [attention lab](../../labs/llm/10_attention.py). Confirm causal weights for future positions are zero and every row sums to one. Then contrast the lab's numerical operation with the repeated next-token inference loop described above.

Further reading: [Attention Is All You Need](https://arxiv.org/abs/1706.03762), [BERT](https://arxiv.org/abs/1810.04805), and [LoRA](https://arxiv.org/abs/2106.09685).