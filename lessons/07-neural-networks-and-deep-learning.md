# Lesson 07 — Neural networks and deep learning

## Learning goals

Understand a neuron as a weighted calculation, learn how layers build representations, and explain how loss and gradients update model parameters.

## A neuron is a calculation

A neuron receives numbers x₁, x₂, and so on. It multiplies each by a weight, adds a bias, then applies an activation function:

z = w₁x₁ + w₂x₂ + … + b  
output = activation(z)

The weights determine influence; the bias shifts the result. An activation such as ReLU introduces non-linearity. Without non-linear activations, stacking many linear layers still gives one linear function, so the network could not express richer patterns.

## Layers build representations

A layer applies many neuron calculations. The first layers may detect simple combinations; later layers combine them into more abstract patterns. In an image model, early features might respond to edges and later features to shapes or objects. This is an intuition, not a guarantee that every neuron has a clean human-readable meaning.

A neural network is a composition of functions. Its parameters are all the weights and biases. Deep learning means using networks with multiple layers and learning useful internal representations from data.

## Loss, backpropagation, and gradient descent

The model predicts, a loss compares the prediction with the target, and backpropagation calculates how each parameter affected that loss. An optimizer uses those gradients to update parameters.

At a high level:

1. Forward pass: calculate predictions from inputs.
2. Loss: compare predictions with targets.
3. Backward pass: calculate parameter gradients using the chain rule.
4. Optimizer step: update parameters.
5. Repeat across batches and epochs.

A **batch** is a small group of examples used for one update. An **epoch** is one pass through the training set. A learning rate controls update size. Training too long or with an unsuitable setup can overfit or diverge.

## Common activations and outputs

ReLU outputs zero for negative inputs and the input itself for positive values. It is simple and widely used in hidden layers.

For classification, a sigmoid can map one logit to a value between 0 and 1. Softmax converts several logits into values that sum to 1. The resulting numbers can be treated as class probabilities only with suitable assumptions and calibration checks.

A loss and output activation should match the task. Multi-class classification often uses softmax with cross-entropy; regression often uses a direct numeric output with a regression loss.

## Why data scale and compute matter

Neural networks can have many parameters. Training them involves repeated matrix operations, which can be accelerated by GPUs. A GPU is helpful but not required for small learning tasks. Start with small models and datasets so experiments finish quickly enough to understand.

More parameters and data do not automatically mean better results. Data quality, objective choice, optimization, architecture, compute budget, and evaluation all matter.

## Regularization and transfer learning

Ways to reduce overfitting include more representative data, weight decay, dropout, data augmentation, early stopping, or a smaller model. Each method has assumptions and should be validated.

**Transfer learning** starts from a model trained on a related, larger dataset. Reusing learned representations can reduce data and compute needs. Fine-tuning adjusts some or all model parameters for a new task. Always compare with a simpler baseline and ensure the pretrained model's license and intended use fit your project.

## Review questions with answers

**1. Why does a neural network need non-linear activation functions?**  
Without non-linearity, a stack of linear transformations can be simplified to a single linear transformation. Non-linear activations let the network represent more complex functions.

**2. What does backpropagation calculate?**  
It efficiently calculates how the loss changes with respect to each parameter, using the chain rule through the network.

**3. What is the difference between an epoch and a batch?**  
A batch is a group of examples used for one update. An epoch is one full pass over the training examples.

**4. Why can training accuracy keep increasing while test performance gets worse?**  
The model may be fitting noise or special details of training examples rather than a general pattern. This is overfitting.

**5. What is transfer learning?**  
Reusing parameters or representations from a model trained on one task or dataset, then adapting them to a related task.

## Practice

Train a small PyTorch classifier. Plot training and validation loss over epochs. Deliberately train longer or increase model size and observe when validation performance stops improving. Change one setting at a time.

## Mastery check

Draw the forward and backward passes, label the input, weights, prediction, target, loss, gradients, and update. Explain what changes during inference: predictions are calculated, but the model's parameters are not being trained.