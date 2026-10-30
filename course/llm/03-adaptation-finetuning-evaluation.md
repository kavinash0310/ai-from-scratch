# Chapter 3 — Fine-tuning, adapters, and LLM evaluation

## Adaptation methods

Prompting supplies instructions and examples at inference. Supervised fine-tuning updates model weights using input-output examples. Preference training shapes behavior using comparisons or feedback. Distillation trains a smaller model to imitate outputs from a larger one.

Parameter-efficient fine-tuning updates fewer weights. LoRA adds low-rank trainable matrices while keeping most base weights fixed; see the [original LoRA paper](https://arxiv.org/abs/2106.09685). It can reduce training memory but still requires quality data and evaluation.

Use retrieval when facts change or need sources. Fine-tuning may help stable formats, domain style, or repeated behavior. Choose by experiment, not trend.

## Evaluation

An LLM evaluation set should include normal, ambiguous, adversarial, and out-of-scope inputs. Measure task correctness, factual support, refusal, format, latency, and cost. Compare model versions with a fixed set.

Human evaluation requires a rubric, blind comparisons where practical, multiple examples, and attention to disagreement. An automatic judge is another model with its own failure modes; calibrate it against people and known examples.

## Deeper walkthrough: choose an adaptation method

Use prompting when instructions and a few examples reliably shape one task. Use retrieval when answers need changing documents, citations, or private approved knowledge. Use fine-tuning when you need repeated behavior, format, or style that prompts do not reliably produce. Consider a smaller distilled model when latency or cost dominates.

Build the same evaluation set for each candidate. Include quality, latency, cost, privacy, and operational updates. A method that scores slightly higher but cannot meet privacy or latency requirements is not suitable.

For fine-tuning, split by source and time where appropriate; near-duplicate training examples can make evaluation optimistic. Keep a held-out set untouched by prompt and hyperparameter iteration.

## Questions and answers

**When should I fine-tune instead of prompt?**  
When prompting cannot reliably produce a repeated desired behavior and you have sufficient high-quality examples. Test both approaches.

**What is LoRA's tradeoff?**  
It trains fewer parameters than full fine-tuning, reducing resource needs, but does not remove data requirements or evaluation.

**Why use a fixed evaluation set?**  
It makes model changes comparable and exposes regressions. Keep a separate final test set if you are making repeated development decisions.

**Can an LLM grade itself reliably?**  
Not automatically. Model judges may favor fluent answers, share blind spots, or be inconsistent. Validate them against human judgments.

## Practice and mastery

Create 30 test prompts for a narrow task, define a scoring rubric, and compare prompt-only with one adaptation method. Include unsupported questions and measure when each system should abstain.