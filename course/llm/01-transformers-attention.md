# Chapter 1 — Transformer architecture and attention

## Why transformers

Before transformers, many sequence models processed tokens step by step. The Transformer paper proposed an architecture based on attention without recurrence, allowing parallel processing across sequence positions during training. Read the [original paper](https://arxiv.org/abs/1706.03762) after this explanation.

Text is tokenized into IDs. An embedding table maps each ID to a vector. Positional information distinguishes token order. Transformer blocks apply attention and feed-forward transformations, with residual connections and normalization.

## Query, key, and value

Each token vector is projected into:
- query Q: what this position seeks;
- key K: what each position offers for matching;
- value V: information to combine.

Scaled dot-product attention is:

Attention(Q, K, V) = softmax(QKᵀ / √dₖ) V

QKᵀ computes pairwise compatibility scores. Dividing by the square root of key dimension keeps magnitudes manageable. Softmax turns each row into weights that sum to one. Multiplication by V combines information from positions.

Multi-head attention repeats these learned projections in parallel, then combines the results. A causal mask blocks future positions for next-token generation.

## The transformer block

A block commonly has attention, a position-wise feed-forward network, residual paths, and normalization. Residual paths add an input to a transformed output, helping information and gradients flow through depth.

The architecture is a computation graph, not a human-like reading process. Attention weights are one part of the calculation and should not be treated as complete explanations.

## Questions and answers

**Why does attention scale the dot product?**  
Large dot products can push softmax into very sharp regions with small gradients. Scaling helps maintain a useful numerical range.

**Why add position information?**  
Self-attention alone does not inherently know sequence order. Position signals help distinguish different arrangements.

**What does a causal mask do?**  
It prevents a token from using future tokens, so training matches the information available when generating left-to-right.

**Do attention maps explain a model's decision?**  
They show one component of information mixing, not a complete causal explanation of the final output.

## Practice and mastery

Draw a three-token attention calculation. Mark Q, K, V, scores, normalized weights, and output. Read the original paper's architecture diagram and identify encoder, decoder, attention, and feed-forward blocks.