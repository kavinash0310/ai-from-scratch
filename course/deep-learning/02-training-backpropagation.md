# Chapter 2 — Training, loss, and backpropagation

> **Book-length subject volume:** For expanded explanations, worked examples, review questions, and practice, read the [deep-learning textbook](TEXTBOOK.md).

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

## One training step

Training repeats a loop:
1. take a batch of examples;
2. run a forward pass;
3. compare predictions with targets using a loss;
4. calculate gradients with backpropagation;
5. update parameters with an optimizer.

An epoch is one full pass through the training set. Batch size controls examples per update. Too-small batches are noisy; very large batches need memory and may have different optimization behavior.

## Backpropagation

The network is a composition of functions. The chain rule calculates how each parameter changes the final loss. Backpropagation walks from loss toward earlier layers, reusing intermediate derivatives efficiently.

The gradient does not say what the parameter “means”; it says how a small local parameter change affects loss at the current model and batch.

## Optimizers and learning rates

Stochastic gradient descent uses noisy mini-batch gradients. Momentum smooths update direction. Adam maintains running estimates of gradient and squared gradient. These methods can make training easier, but learning rate and schedule still matter.

Track training and validation loss. If training loss falls while validation loss rises, the model may overfit. If neither falls, inspect learning rate, data scaling, labels, loss, and gradient flow.

## Deeper walkthrough: a one-parameter gradient step

Let prediction be wx for a single example with x=2 and target y=6. Mean squared error is L=(wx−6)². At w=1, the prediction is 2 and loss is 16. The derivative with respect to w is 2(wx−6)x, which is −16 at w=1.

With learning rate 0.1, update w to 1 − 0.1×(−16) = 2.6. The new prediction is 5.2 and loss is 0.64. This simple example shows why subtracting a negative gradient increases the weight and reduces error.

For neural networks, backpropagation applies the same chain rule through many layers. Real training averages gradients over batches and updates millions of parameters.

## Questions and answers

**What changes during inference?**  
The model calculates outputs with fixed parameters. It does not update weights unless training or adaptation is explicitly run.

**What is backpropagation not?**  
It is not the optimizer, not the loss, and not a guarantee of a good solution. It computes gradients used by the optimizer.

**What does exploding or vanishing gradient mean?**  
Gradient magnitudes can grow too large or shrink toward zero across layers, making training unstable or slow.

**Why use validation loss?**  
It estimates performance on unseen examples during development and helps detect overfitting or choose settings.

## Practice and mastery

Train a small network on a digit dataset. Plot both losses across epochs. Deliberately use a poor learning rate and observe instability. Identify the forward pass, loss, backward pass, and update in the training code.