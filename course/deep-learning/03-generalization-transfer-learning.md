# Chapter 3 — Generalization, regularization, and transfer learning

## Generalization

A network can memorize examples, especially when capacity is high relative to data. Generalization is performance on new examples from the target environment. Train and validation curves help diagnose but do not prove future robustness.

## Regularization tools

- Weight decay penalizes large parameter magnitudes.
- Dropout temporarily removes activations during training.
- Data augmentation creates transformations that should preserve labels.
- Early stopping halts when validation improvement ends.
- Smaller architectures reduce capacity and computation.

These are not interchangeable magic switches. Augmentation is harmful if transformations alter the correct label. Strong regularization can cause underfitting.

## Transfer learning

A pretrained model begins with representations learned on another dataset. Freeze its backbone and train a task-specific head, then optionally fine-tune some or all layers. This is often more efficient than training from random initialization on a small dataset.

Check domain match, model license, expected input preprocessing, and whether pretrained data may encode bias. Compare with a baseline and evaluate on a split that reflects future use.

## Questions and answers

**What is overfitting?**  
The model fits details of training examples that do not generalize, often shown by improving training loss while validation performance worsens.

**Why can data augmentation hurt?**  
A transformation may change the label or create unrealistic inputs. Only use transformations consistent with the task.

**When is transfer learning useful?**  
When the pretrained model learned relevant patterns and the available labeled dataset or compute is limited.

**Does a pretrained model remove the need for evaluation?**  
No. It may be mismatched, biased, or unsuitable for your data and task.

## Practice and mastery

Train from scratch and with a pretrained model on a small dataset. Keep splits fixed, compare compute and quality, inspect failures, and state what the pretrained model's license permits.