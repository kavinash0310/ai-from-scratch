# Chapter 1 — Neural networks: neurons, layers, and representations

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

## The artificial neuron

A neuron receives numeric inputs x, multiplies them by weights w, adds a bias b, and applies an activation:

z = w·x + b  
output = activation(z)

A weight controls how strongly an input affects the weighted sum. The bias shifts the threshold. ReLU returns max(0,z); sigmoid maps a scalar to (0,1). Hidden layers use nonlinear activations so the entire network can represent complex functions.

## Layers compose functions

A neural network applies one transformation after another. The first layer receives raw features; intermediate layers produce learned representations; the final layer produces scores or predictions.

Without nonlinear activations, composing linear layers is still equivalent to one linear transformation. Depth alone would not provide additional expressive power.

For a batch of examples X, a layer may compute XW+b. Matrix shapes must align: examples by input features, multiplied by input features by output units, gives examples by output units.

## Output layers and losses

For a numeric target, the output may be a direct value and use mean squared or absolute error. For binary classification, one logit can pass through sigmoid and use binary cross-entropy. For multiple classes, softmax and cross-entropy are common.

Logits are raw scores before a probability transformation. Training often combines a stable logits-aware loss with raw scores to avoid numerical problems.

## Representations are learned, not guaranteed meanings

A hidden unit can respond to a pattern, but it may not map neatly to one human concept. Feature visualization and attribution are diagnostic methods, not proof that the representation is understood.

## Questions and answers

**What is a bias term?**  
An additive parameter that lets a neuron shift its response independently of the weighted input.

**Why are nonlinear activations essential?**  
They prevent many layers from collapsing into a single linear function and allow richer decision boundaries.

**What is a logit?**  
A model's raw score before conversion to a probability or class prediction.

**Do neural networks understand their hidden features?**  
The network calculates learned representations. Human interpretation may be partial and should be supported by experiments.

## Practice and mastery

Compute one neuron by hand for two inputs. Change one weight and explain the output change. Draw a two-layer network with tensor shapes and identify where the nonlinearity occurs.