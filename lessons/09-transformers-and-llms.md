# Lesson 09 — Transformers and large language models

## Learning goals

Understand how text becomes numbers, what attention does, why a transformer can process context, and how next-token prediction creates a language model.

## Text becomes tokens

A computer model operates on numbers. A **tokenizer** turns text into token IDs. A token may be a word, part of a word, punctuation, or another byte-like unit. Tokenization is not identical to splitting by spaces.

A token ID is mapped to a learned **embedding** vector. The vector gives the model a numerical representation it can transform. Similarity between embeddings can reflect learned patterns, but no single coordinate has a guaranteed human interpretation.

Tokenization affects cost, context length, and handling of unusual text. Different tokenizers divide the same sentence differently.

## Attention: context-dependent mixing

In self-attention, each token creates three vectors called query, key, and value. A query is compared with keys to calculate which other tokens should contribute information. The resulting weights mix value vectors.

The standard scaled dot-product attention is:

Attention(Q, K, V) = softmax(QKᵀ / √dₖ) V

Intuition:
- QKᵀ gives compatibility scores between token positions.
- Division by √dₖ keeps scores from becoming too large as dimensions grow.
- softmax converts scores into weights that sum to one across attended positions.
- Multiplying by V forms a weighted mixture of information.

Attention is content-dependent: a token can use different context in different sentences. It does not guarantee human-like understanding.

## Multi-head attention and position

Multi-head attention runs several attention projections in parallel. Heads can learn different relations, then their outputs are combined. This increases flexibility.

Attention by itself does not know token order. Positional information is added so the model can distinguish “dog bites person” from “person bites dog.” Modern models may use different positional schemes; learn the general purpose before memorizing variants.

Transformer blocks usually combine attention, a feed-forward network, residual connections, and normalization. Residual connections give information and gradients a path across layers. Normalization can stabilize training.

## Causal masking and next-token prediction

A decoder language model is usually trained to predict the next token from previous tokens. During training, a causal mask prevents a position from attending to future tokens. Otherwise the model could cheat by reading the answer.

Given “The sky is”, the model predicts a probability distribution over possible next tokens. Training rewards probability on the observed next token. Repeating across huge collections teaches statistical patterns of language and other training data.

At generation time, the model selects or samples a token, appends it to context, and predicts again. Temperature and sampling rules change variety and risk; they do not add knowledge.

## Pretraining, fine-tuning, and prompting

- **Pretraining** learns broad representations and next-token behavior from large data.
- **Instruction tuning** trains the model to respond to prompts in a desired format.
- **Preference optimization** uses comparisons or feedback to shape response behavior.
- **Prompting** changes the context supplied at inference time but does not usually change model weights.
- **Fine-tuning** updates some or all weights using a task-specific dataset.

These processes solve different problems. A prompt cannot reliably add extensive reference knowledge. Retrieval can provide current documents. Fine-tuning is often useful for style or repeated behavior, but is not automatically the best way to store facts.

## Why LLMs can be useful and still fail

A model predicts plausible continuations, not guaranteed truths. It can state false information fluently, lose track of long context, overgeneralize stereotypes, or follow malicious instructions embedded in input. The output depends on training data, architecture, prompt, decoding, tools, and surrounding software.

Evaluate outputs against the task. For factual work, check evidence. For code, run it. For consequential decisions, require human oversight and define when the model must abstain.

## Review questions with answers

**1. Why are words converted to tokens and embeddings?**  
Neural networks perform numerical operations. Token IDs select learned vectors that the model can transform and combine.

**2. What do query, key, and value do intuitively?**  
Queries express what a position seeks, keys express what positions offer for matching, and values carry information to mix using the attention weights.

**3. Why use a causal mask in a next-token model?**  
It prevents a position from seeing future tokens during training, matching the information available when generating text.

**4. Does predicting likely text prove the model knows the truth?**  
No. It learns patterns that make continuations likely. Truth and evidence require separate evaluation.

**5. What is the difference between prompting and fine-tuning?**  
Prompting changes the input context for one inference. Fine-tuning changes model parameters using additional training.

## Practice

Use a tokenizer to inspect how several sentences split into tokens. Draw an attention table for a four-token sentence and explain which prior tokens a final token might use. Read the abstract and introduction of [Attention Is All You Need](https://arxiv.org/abs/1706.03762), then explain its main idea in your own words.

## Mastery check

Explain text → token IDs → embeddings → transformer blocks → next-token probabilities → generated sequence. Identify where evidence is missing and where evaluation must be added.