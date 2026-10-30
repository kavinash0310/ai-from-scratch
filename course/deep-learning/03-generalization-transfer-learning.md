# Chapter 3 — Generalization, regularization, and transfer learning

> **Book-length subject volume:** For expanded explanations, worked examples, review questions, and practice, read the [deep-learning textbook](TEXTBOOK.md).

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

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

## Deeper walkthrough: freeze or fine-tune

Start with a pretrained image model as a frozen feature extractor: compute representations and train a small classifier head. This is fast and helps reveal whether the representation separates the task. If validation performance plateaus and the new images differ from pretraining, unfreeze some layers and fine-tune with a smaller learning rate.

Compare both approaches on the same train/validation split. Watch for overfitting when the labeled dataset is small. Fine-tuning can adapt representations, but also erase useful features or learn dataset shortcuts.

A frozen model still carries its training data and limitations. Check license, intended use, and evaluation coverage. Never treat pretraining as a substitute for inspecting errors on your own domain.

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