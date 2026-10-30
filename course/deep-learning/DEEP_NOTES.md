# Deep learning — full beginner notes

Deep learning is machine learning with neural networks built from layers of differentiable calculations. The central idea is not “the computer thinks like a brain”; it is that a flexible function can be adjusted from data using gradients.

## 1. Neurons, layers, and neural networks

A simple neuron receives numbers x, multiplies them by learned weights w, adds a bias b, then applies an activation: a = activation(w·x+b). The **weight** controls how strongly an input contributes; the **bias** shifts the threshold. A **layer** applies many such calculations. A **neural network** composes layers to map inputs to predictions.

If every layer were only linear, stacking layers would still produce one linear function. An **activation function** such as ReLU (max(0,x)) adds non-linearity so the network can represent more complex patterns. The final layer depends on the task: a number for regression, or class logits followed by softmax for multi-class prediction.

An image classifier may receive a structured image tensor. The first layer does not “see a cat”; it calculates weighted combinations. During training, layers together can build useful representations. A **representation** is a transformed form of data that makes task-relevant information easier to use.

Key terms: **logit** is an unnormalized class score; **activation** is a layer's output; **width** is units per layer; **depth** is number of layers; **parameter count** is learned weights and biases. More parameters increase capacity and resource needs, but do not guarantee generalization.

## 2. Training, loss, and backpropagation

Training repeats four ideas: forward pass makes predictions; a loss compares prediction with target; backpropagation computes gradients; an optimizer changes parameters. A **batch** is the examples used for one update. An **epoch** is one pass through the training set. **Learning rate** controls update size.

For a one-weight model prediction = w×x, use x=2, target y=6, and squared loss L=(wx−y)². At w=1, prediction is 2 and loss 16. The derivative with respect to w is 2(wx−y)x = -16. With rate 0.1, update w to w−0.1(-16)=2.6. Prediction becomes 5.2 and loss 0.64. The update subtracts the gradient; subtracting a negative number increases the weight.

**Backpropagation** is efficient use of the chain rule through the network graph. It calculates derivatives; it does not choose the learning rate or update weights. An **optimizer** performs updates using gradients. SGD, momentum, and Adam are common optimizers. A loss going down on training data alone does not prove useful learning; inspect validation performance too.

## 3. Generalization and transfer learning

**Overfitting** is fitting accidental details of training examples; **underfitting** is failing to represent the needed relationship. A validation curve can show when training keeps improving while unseen-data performance worsens. **Regularization** limits effective complexity: weight decay penalizes large weights, dropout randomly omits activations during training, and data augmentation creates label-preserving variations.

**Transfer learning** starts with a model trained on a broad source task and adapts it to a related target task. A **pretrained model** contains parameters learned before your task. **Fine-tuning** updates some or all of them. **Feature extraction** freezes most weights and trains a small task-specific head. This helps when labeled data is limited, but source and target data must be compatible.

A responsible experiment compares frozen features, partial fine-tuning, and a simple baseline; uses leakage-safe splits; and checks error slices. A large pretrained model can still fail on new cameras, languages, devices, or populations.

### Q&A and practice

**Does a neural network have one neuron per concept?** No. Units are numerical components; human-readable interpretations are not guaranteed.
**Does more depth always improve accuracy?** No. Training stability, data, compute, architecture, and evaluation all matter.
**What is the first deep-learning project?** Train a small classifier, compare it with a baseline, plot train/validation loss, and inspect mistakes.

Mastery: draw the forward pass, label weights, activations, loss, and gradients, and explain which values change during training versus inference. Continue to [computer vision](../computer-vision/README.md) or [NLP](../nlp/README.md).