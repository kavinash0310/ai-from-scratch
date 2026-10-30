# Chapter 2 — Training, loss, and backpropagation

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