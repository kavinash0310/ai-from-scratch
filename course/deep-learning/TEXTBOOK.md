# Deep learning
## A beginner's textbook chapter

Deep learning is machine learning built from neural networks with many parameterized transformations. The network is a function made from arithmetic operations. Training adjusts its internal numbers so predictions fit examples under a chosen loss. The words neuron and learning can sound biological; here they refer to specific computations and optimization.

## 1. A neuron as a calculation

A simple unit receives features x1 through xn, multiplies them by weights w1 through wn, adds a bias b, and applies an activation:

    z = w1*x1 + ... + wn*xn + b
    a = activation(z)

The weights say how strongly features contribute to the score. The bias shifts it. The activation transforms the score. Without nonlinear activations, stacking linear layers would still be one linear transformation. ReLU returns max(0,z); tanh maps values to -1 through 1; sigmoid maps to 0 through 1.

A layer applies this calculation to many units. A network composes layers. The input layer receives the representation; hidden layers transform it; an output head produces scores suitable for the task. **Logits** are raw scores before a probability transformation. Regression may output a number directly. Multi-class classification may apply softmax to logits. The final activation depends on the loss and the intended interpretation.

A neural network does not automatically have one unit for “cat” or “sadness.” Units are learned numerical components, and their human interpretation can be distributed or unclear.

## 2. Forward pass and loss

The **forward pass** computes predictions. A **loss function** compares predictions with targets during training. The loss is the quantity optimized; it may not equal the product's quality metric.

For regression, mean squared error is average squared prediction error. For binary classification, cross-entropy penalizes low probability assigned to the true label. For class probabilities p and correct class y, the contribution is minus log p(y). If the model assigns probability 0.01 to the correct answer, the penalty is much larger than if it assigns 0.8.

A **batch** is the set of examples used for one gradient calculation. An **epoch** is one pass through training data. Training data fits parameters. Validation data helps choose settings. Test data gives a final estimate after choices are complete.

## 3. Backpropagation and a numerical update

A neural network is a chain of functions. The chain rule tells how a small change in an early parameter affects the final loss. **Backpropagation** calculates these derivatives efficiently from the output toward earlier layers. An **optimizer** uses the gradients to update parameters. They are different operations.

Consider a one-parameter model prediction = w*x and one example with x=2 and target y=6. Let squared loss be L=(w*x-y) squared. At w=1, prediction is 2 and loss is 16. The derivative with respect to w is 2*(w*x-y)*x, which is -16. With learning rate 0.1:

    new_w = old_w - rate * gradient
    new_w = 1 - 0.1*(-16) = 2.6

Subtracting a negative gradient increases the weight. The new prediction is 5.2 and the loss becomes 0.64. A real network repeats this chain rule over many parameters and examples.

## 4. Optimizers and training dynamics

**Gradient descent** subtracts a gradient-scaled update. **Stochastic gradient descent (SGD)** estimates gradients using minibatches. **Momentum** keeps a running direction that can smooth noisy updates. **Adam** adapts update sizes using running statistics of gradients.

The **learning rate** controls update size. Too high can cause loss to oscillate or diverge. Too low can make progress very slow. Track training and validation loss. If both stay high, inspect data, labels, architecture, initialization, loss, and learning rate. If training improves but validation worsens, suspect overfitting or a mismatch between the split and use case.

**Vanishing gradients** become too small as they pass through many layers; early layers then learn slowly. **Exploding gradients** become so large that updates destabilize training. Normalization, residual connections, activation choices, initialization, and gradient clipping address different aspects of training stability.

## 5. Generalization and transfer

A large network can memorize examples. **Overfitting** is learning accidental training detail that fails on new cases. **Regularization** discourages brittle fits:
- Weight decay penalizes large weights.
- Dropout randomly removes activations during training.
- Data augmentation creates label-preserving variants.
- Early stopping ends training when validation performance stops improving.
- More representative data can improve coverage.

**Transfer learning** starts from a model trained on a broader source task. **Feature extraction** freezes most weights and trains a small output head. **Fine-tuning** updates some or all weights on a target task. Start with a simple, frozen baseline; fine-tune only when data and validation show a benefit.

Source and target data must be compatible. A vision model trained on ordinary web photographs may not work well on medical scans. A language model may underperform on a specialized domain or language. Validate representative subgroups and inspect errors.

## 6. How to diagnose a training run

Save training and validation curves. For classification, inspect a confusion matrix and probability calibration. For regression, inspect residuals by value range and meaningful group. Record split, preprocessing, seed, model, optimizer, learning rate, batch size, and stopping rule.

Change one factor at a time when investigating. If you change the architecture, optimizer, data augmentation, and learning rate together, you may not know what helped. Keep a baseline and save the best validation checkpoint.

## 7. Questions and worked checks

**Why do activations matter?** They add nonlinearity, allowing the network to represent functions that a single linear map cannot.

**Does backpropagation update weights?** No. It computes gradients. An optimizer applies updates using those gradients.

**Why can training accuracy be high while validation accuracy is low?** The network may have memorized patterns specific to the training set or the split may not represent deployment.

**What is transferred in transfer learning?** Learned parameter values and representations from a source task are reused and optionally adapted.

Exercise: sketch input -> linear layer -> activation -> output -> loss, then draw gradient flow backward. Explain which operations occur during training and which occur during inference. Answer: inference normally computes forward outputs with fixed weights; training also calculates gradients and updates weights.

Continue to [computer vision](../computer-vision/README.md), [NLP](../nlp/README.md), and the [backpropagation lab](../../labs/deep-learning/07_backprop_xor.py).

## Deeper training loop and diagnosis

A mini-batch goes through a forward pass to produce predictions. A loss compares these predictions with labels. Backpropagation computes derivatives with respect to trainable parameters; an optimizer updates them. Many frameworks accumulate gradients, so old gradients must be cleared before the next step. Training and inference modes can differ for dropout and batch normalization.

A useful debugging sequence is: check input and output shapes; check labels and loss; verify that predictions and gradients are finite; then try to overfit a tiny subset. If a model cannot fit a few examples, first investigate data, labels, architecture, loss, and optimizer. Only then investigate generalization on larger data.

Learning curves compare training and validation performance. Low training error with high validation error may indicate overfitting. High error on both may mean underfitting, too little training, bad preprocessing, or a bug. Weight decay discourages large weights, dropout randomly removes activations during training, augmentation introduces label-preserving variations, and early stopping uses validation behavior. Every technique assumes something: flipping a medical image is invalid if orientation changes the diagnosis.

Normalization can improve optimization when feature scales differ. Batch normalization and layer normalization use different axes and statistics; neither is the same as cleaning raw inputs. Padding and masks matter in sequence models. Record architecture, optimizer, learning rate, batch size, preprocessing, seed, software, and checkpoint so a result can be interpreted.

Questions: What does batch size change? The number of examples used for each gradient estimate, affecting memory and optimization noise. Why can too-high a learning rate fail? Updates can jump past useful parameter regions. Does automatic differentiation verify the model's intended meaning? No, it differentiates the computations written.

Further reading: [PyTorch beginner tutorials](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) and [autograd tutorial](https://docs.pytorch.org/tutorials/beginner/blitz/autograd_tutorial.html).
