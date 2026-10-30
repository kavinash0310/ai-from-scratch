# Transformers and attention — from first principles

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

This chapter builds the Transformer one idea at a time: text becomes tokens, tokens become vectors, attention mixes context, and repeated blocks transform those vectors into useful predictions.

## What you should know first

It helps to know Python lists and functions, vectors and dot products, matrix multiplication, and the idea of a neural-network layer. If any of those are new, study [Python](../python/README.md), [linear algebra](../mathematics/02-linear-algebra.md), and [neural networks](../deep-learning/01-neural-networks.md) first. You can still read this chapter now; return to the prerequisites when a term feels unclear.

By the end, you should be able to explain the purpose of tokens, embeddings, positions, queries, keys, values, attention weights, heads, residual connections, and causal masks. You should also be able to trace one token through an attention calculation.

## 1. Why a Transformer needs representations

A computer program cannot multiply the word “cat” directly. Neural networks operate on numbers, so text must be converted into numbers in a repeatable way.

A **tokenizer** divides text into units. A token may be a whole word, part of a word, punctuation, or a byte-like unit. For example, a rare word may be split into several common pieces. Each distinct token is assigned an integer ID. The ID is an index, not a meaningful measurement: token 500 is not “larger” or “more important” than token 40.

An **embedding table** maps each token ID to a learned vector. If the model width is 512, each token becomes a vector of 512 numbers. Those numbers are learned during training. They give the model a numerical space in which it can transform and compare token representations.

A vector by itself does not tell the model where a token appeared. Transformers therefore add or otherwise represent **position information**. This lets the model distinguish “dog bites person” from “person bites dog,” even if both contain the same words.

### Vocabulary for this step

- **Vocabulary:** the set of token IDs a tokenizer can produce.
- **Token ID:** an integer that selects a row in an embedding table.
- **Embedding:** a learned vector representation of a token or other object.
- **Position encoding:** information that tells the network where a token occurs in a sequence.
- **Context:** the other tokens and information available when a representation is calculated.

## 2. Attention answers “which other positions should contribute?”

Self-attention lets each token build a new representation using information from other positions in the same sequence. “Self” means the queries, keys, and values all come from the current sequence.

For every token vector, learned linear transformations create three vectors:

- A **query (Q)** represents what this position is looking for.
- A **key (K)** represents what this position can be matched on.
- A **value (V)** carries the information that can be passed along.

A query is compared with keys. A strong match gives that key's value more influence on the query token's new representation. The model learns the projections that create Q, K, and V; people do not write a hand-made dictionary of which words should attend to which others.

The standard scaled dot-product attention equation is:

Attention(Q, K, V) = softmax(QKᵀ / √dₖ) V

Read it left to right:

1. **QKᵀ** calculates a compatibility score between each query position and each key position.
2. **Divide by √dₖ** (the square root of the key-vector width) to keep scores in a useful numerical range as vectors get wider.
3. **Softmax** turns the scores for a query into weights that add up to 1.
4. **Multiply by V** to calculate a weighted mixture of the value vectors.

The output is a context-enriched vector for each query position.

## 3. A tiny numerical attention example

Use two toy positions. These numbers are made up to demonstrate the calculation; a trained model learns its own vectors.

Let the first query be q = [1]. Let the two keys be k₁ = [1] and k₂ = [0]. Their dot-product scores are 1 and 0. Softmax of [1, 0] is approximately [0.731, 0.269]. This says the first position receives about 73% of its information from position one and 27% from position two.

Let the corresponding values be v₁ = [2] and v₂ = [4]. The output is:

0.731 × 2 + 0.269 × 4 = 2.538

The new representation is a weighted blend of information from both positions. If the query or keys changed, the weights would change. In a real model, vectors have many dimensions, there are many positions, and learned projections produce the vectors.

For a key width of 1, √dₖ is 1, so scaling did not change the example. With wider keys, the scale helps keep the softmax from becoming extremely sharp too early in training.

## 4. Shapes: what is being multiplied?

Let B be batch size, T be the number of tokens, and D be the model width. An input batch can be written as a tensor with shape B × T × D. A tensor is a multi-dimensional array.

After projection, each token has query, key, and value vectors. With H attention heads and head width Dh, the internal shape can be represented as B × H × T × Dh. The score matrix has shape B × H × T × T: for every query token, it holds a score for every key token.

This T × T part matters. Standard dense self-attention computation and memory grow roughly with the square of sequence length. Doubling T can require roughly four times as many pairwise scores. This is one reason long contexts are expensive.

## 5. Multi-head attention

A single attention operation learns one set of query/key/value projections. **Multi-head attention** runs several smaller attention operations in parallel. Each head has its own learned projections; their outputs are combined and projected back to the model width.

Different heads can learn different useful patterns, such as nearby relationships, matching references, or more distant dependencies. But do not assume that every head has one simple, stable meaning. Head analysis is a research question, not a guaranteed interpretation.

## 6. What is inside a Transformer block?

A common Transformer block contains:

1. a self-attention sublayer;
2. a **residual connection** that adds the input to the sublayer output;
3. **normalization** to keep activation scales manageable;
4. a **feed-forward network**, usually applied separately at every token position;
5. another residual path and normalization.

The attention sublayer mixes information across positions. The feed-forward network transforms each position's representation. Repeating blocks allows later layers to work with representations produced by earlier layers.

A residual connection has the form “input + transformed input.” It gives information and gradients a more direct path through a deep network. Normalization controls activation scale and can make optimization more stable. Exact ordering varies by architecture, so follow the specific model's design.

## 7. Encoder, decoder, and causal masks

An **encoder** can let a position use context on both its left and right. BERT is a well-known encoder-style model trained with masked-token prediction.

A **decoder** used for next-token generation must only use previous tokens. A **causal mask** hides future positions from attention. Without it, during training the model could see the token it is supposed to predict and cheat.

An **encoder-decoder** model has an encoder that reads an input and a decoder that generates an output while attending to the encoded input. This structure has been used for translation and other sequence-to-sequence tasks.

These are common patterns, not absolute limits on every later use. The training objective and system design matter as much as the label “encoder” or “decoder.”

## 8. Training is different from generation

During training, the model sees token sequences and learns parameters that reduce a loss. A causal language model predicts the next token at many positions. Cross-entropy loss penalizes assigning low probability to the observed next token.

During generation, the parameters are usually fixed. The model processes the prompt, creates a distribution over possible next tokens, selects one according to a decoding rule, appends it to context, and repeats. Training adjusts weights; inference uses those weights to calculate outputs.

An attention mechanism is a learned numerical operation. The word “attention” does not mean that a model has human awareness, and an attention map alone does not fully explain why a final answer was produced.

## Common mistakes to avoid

- Treating token IDs as meaningful numeric quantities.
- Forgetting that position information is needed.
- Assuming an attention score proves a human-readable reason.
- Mixing up the model's training objective with its inference procedure.
- Assuming a longer context automatically yields a better answer.
- Ignoring the quadratic cost of dense attention as sequence length grows.
- Assuming all Transformers are decoder-only language models.

## Questions and answers

**Why are there three vectors called query, key, and value?**  
The query-key comparison determines how much one position uses each other position. The value vectors contain the information being mixed. Separating matching from content gives the model flexibility.

**Why does softmax appear?**  
It converts a row of scores into non-negative weights that sum to one. The attention output can then be interpreted as a weighted combination of values.

**Why divide by the square root of key width?**  
Dot-product magnitudes tend to grow as vector width grows. Large scores can make softmax overly saturated, with very small gradients. Scaling helps training remain numerically useful.

**What does a causal mask prevent?**  
It prevents a position from attending to future tokens. That keeps next-token training honest: the model must predict the next token from the prefix.

**Does self-attention mean every token always uses every other token?**  
Not necessarily. The score weights can be small, masks can block positions, and different heads and layers compute different mixtures.

**Why is attention expensive for long inputs?**  
Each token position scores against many other positions. The pairwise score matrix has T × T entries, so cost rises roughly quadratically with sequence length in standard dense attention.

**Does a Transformer understand language like a person?**  
The architecture calculates learned vector transformations and predictions. It can perform useful language tasks, but that does not establish human-like experience or understanding.

## Practice

1. Draw a three-token sentence and show which positions can attend to which others for an encoder and a causal decoder.
2. Repeat the two-position numeric example using scores [2, 0]. Calculate softmax weights and the weighted value.
3. Label Q, K, V, attention weights, residual connection, normalization, feed-forward network, and causal mask in a Transformer block diagram.
4. Explain why the model needs both token identity and position information.
5. Read the architecture diagram and abstract of [Attention Is All You Need](https://arxiv.org/abs/1706.03762), then summarize what the paper changed and what it did not prove.

## Mastery check

Without looking at the page, trace text through tokenization, embeddings, position information, Q/K/V projections, attention weights, Transformer blocks, and output. Explain one reason the architecture is useful and two limitations that need separate engineering or evaluation.