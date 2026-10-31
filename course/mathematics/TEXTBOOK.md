# Mathematics for AI
## A beginner's textbook chapter

You do not need to become a mathematician before using machine learning. You do need to understand the calculations a model makes, the assumptions behind them, and how to recognize an invalid result. This chapter builds a practical bridge from algebra to optimization.

## 1. Algebra and functions describe a model

A **variable** is a symbol whose value can change. A **constant** is fixed for a calculation. A **parameter** determines the behavior of a function. A function takes an input and returns an output. In y=f(x), x is the input and y is the output.

A line is a simple model:

    y = w*x + b

Here w is the slope: how much y changes when x increases by one. b is the intercept: the output when x is zero. For w=2 and b=1, x=3 gives y=7. A house-price model might use floor area as x, but price also depends on location, age, and market conditions. The equation is a model of selected effects, not reality itself.

A **linear transformation** preserves addition and scaling. In applied ML, “linear model” often includes an added bias, so it is affine mathematically. A model can represent nonlinear patterns by transforming inputs, for example x squared, or by composing layers with nonlinear activations.

A **logarithm** reverses exponentiation. If 2 raised to the third power is 8, log base 2 of 8 is 3. Natural logarithms appear in likelihoods and cross-entropy. They turn products of probabilities into sums of log probabilities, which is more numerically stable and easier to optimize.

## 2. Vectors, matrices, and shapes

A **scalar** is one number. A **vector** is an ordered list of numbers. A **matrix** is a two-dimensional grid. A **tensor** is an array with any number of axes. Data and neural-network activations are usually tensors.

A vector can represent a point, a row of features, or a learned embedding. A dot product multiplies matching entries and adds them:

    [1, 2] dot [3, 4] = 1*3 + 2*4 = 11

A dot product can be thought of as combining input features with weights. If a weight is large and positive, that feature can strongly increase the score; if it is negative, it can reduce the score.

Matrix multiplication combines rows and columns. If a dataset has 100 examples and 3 features, its matrix X has shape 100 by 3. If a model maps each example to one prediction, its weight vector has length 3 and the prediction vector has 100 values. Shapes tell you which dimension means examples and which means features.

Common operations:
- **Transpose:** swap rows and columns.
- **Norm:** measure the size or length of a vector.
- **Distance:** quantify how far two vectors are under a chosen metric.
- **Projection:** express one vector's component along another direction.
- **Cosine similarity:** compare vector directions, often used for embeddings.

A shape mismatch is not merely a coding nuisance; it often reveals a conceptual mistake about which axis is examples, features, channels, or time.

## 3. Probability models uncertainty

Probability assigns a number from 0 to 1 to an event under a specified model or experiment. Mutually exclusive outcomes whose possibilities cover every case should sum to 1. A **random variable** maps outcomes to numeric values.

Conditional probability means “the probability of A given that B is known.” It is not generally the same as the probability of B given A. This distinction matters for medical tests, fraud detection, and search.

Suppose 1% of a population has a condition. A test correctly identifies 90% of people with it, but 10% of people without it also test positive. Out of 10,000 people:
- about 100 have the condition; about 90 test positive;
- about 9,900 do not; about 990 still test positive.
Only 90 of about 1,080 positives truly have the condition. A seemingly accurate test can have low precision when the event is rare. This is the **base-rate effect**.

## 4. Statistics summarize samples

A **population** is the set we want to understand. A **sample** is the data we actually observe. A statistic calculated from a sample is uncertain because another sample may differ.

The **mean** is the sum divided by count. The **median** is the middle sorted observation. **Variance** measures average squared spread around the mean; **standard deviation** is the square root of variance and uses the original units. A few extreme values can move the mean strongly, while the median is more robust.

**Correlation** measures association. It does not establish that one variable caused another. A third variable, selection process, or time trend may influence both. **Confidence intervals** describe uncertainty from a statistical procedure under assumptions; they are not guarantees about a single future prediction.

## 5. Calculus and gradients

A derivative measures local rate of change. For f(x)=x squared, the derivative is 2x. Around x=3, increasing x a tiny amount changes f by approximately six times that amount. The word local matters: the derivative is an approximation near the point, not an average across the entire curve.

For a function of many parameters, the **gradient** contains one partial derivative per parameter. It points in the direction of locally fastest increase in the objective. To reduce a loss, gradient descent moves in the opposite direction.

A neural network is a composition of functions. The **chain rule** computes how an early quantity affects a final result through intermediate steps. If z depends on y and y depends on x, then the effect of x on z is the effect of y on z multiplied by the effect of x on y. Backpropagation applies this rule efficiently through a network.

### Worked derivative and update

Let L(w)=(w−3) squared. The derivative is 2(w−3). At w=0, the gradient is -6. With learning rate 0.1:

    new_w = old_w - learning_rate * gradient
    new_w = 0 - 0.1*(-6) = 0.6

The parameter moved toward 3, where loss is zero. If the learning rate is too large, updates can leap over the minimum and oscillate or diverge.

## 6. Optimization and numerical computation

**Optimization** searches for parameters that minimize or maximize an objective. A training loss is an objective, but it is only a proxy for actual user value.

Gradient descent repeatedly calculates predictions, loss, gradients, and parameter updates. **Stochastic gradient descent** estimates gradients from small batches. **Momentum** smooths update directions. **Adam** adapts update sizes using running gradient statistics. These optimizers do not make poor labels or leakage safe.

A **convex** function has a bowl-like shape with a global minimum under standard conditions. Deep neural-network objectives are generally non-convex. In practice, initialization, data order, learning rate, regularization, and numerical precision affect results.

Computers represent many numbers using finite-precision floating point. This creates rounding error; very large values can overflow and very small values can underflow. For example, directly exponentiating large softmax scores can overflow. Subtracting the row maximum before exponentiation preserves the resulting probabilities and improves numerical stability.

## 7. Common mistakes

- Treating a probability as certain fact.
- Confusing a parameter learned from data with a hyperparameter chosen by a practitioner.
- Ignoring tensor shapes and then applying an operation along the wrong dimension.
- Thinking a small training loss proves good unseen performance.
- Using correlation to make a causal claim.
- Treating a gradient as an explanation of a feature's meaning.
- Forgetting that numeric calculations can be unstable.

## 8. Questions and worked checks

**Why does matrix multiplication require matching dimensions?** Each output sums products of aligned entries; the inner dimensions must represent the same feature space.

**If gradient is positive, which way does gradient descent move?** It subtracts a positive step, so the parameter decreases. If gradient is negative, subtraction increases the parameter.

**Does PCA preserve the information most useful for a target?** Not necessarily. PCA preserves directions of high variance without using the target labels.

**Why can mean and median differ?** A skewed distribution or outliers may pull the mean far from the middle observation.

Exercise: predict y for x=4, w=2, b=1; calculate dot product [2,1] dot [3,-1]; compute an update for gradient 5 and learning rate 0.2. Answers: 9; 5; subtract 1 from the current parameter.

## 9. How math connects to the course

Algebra describes simple predictors. Linear algebra describes batches of features and model weights. Probability and statistics describe data uncertainty and evaluation. Calculus provides gradients. Optimization uses gradients to fit parameters. These topics recur in logistic regression, neural networks, attention, embeddings, and many other areas. Continue to [machine learning](../ml/README.md) and the [gradient-descent lab](../../labs/math/02_gradient_descent.py).

## Deeper probability, derivatives, and numerical thinking

Conditional probability asks how likely A is when B is known. Bayes' rule reverses a conditional relationship: P(A given B) = P(B given A) P(A) / P(B). The base rate matters. If only 1% of 10,000 messages are phishing, a detector with 90% sensitivity catches about 90 phishing messages. With a 5% false-positive rate, it also flags about 495 ordinary messages. Only about 15% of the 585 alerts are phishing. “90% accurate at catching phishing” does not mean “90% of alerts are phishing.”

A sample statistic estimates a population property. A result measured on a small sample has uncertainty; a difference between 91% and 92% may reflect which examples were sampled. A confidence interval is produced under assumptions about sampling and the statistic. It does not repair biased data or a test set that influenced model choice.

The chain rule explains backpropagation. If a = f(z), z = wx+b, and loss L depends on a, then dL/dw = (dL/da)(da/dz)(dz/dw). Since dz/dw=x, the gradient combines the effect of changing the output, activation, and weight. A computation graph makes these dependencies explicit; automatic differentiation applies the chain rule to the operations in code. If labels or loss are wrong, correct gradients still optimize the wrong goal.

Shapes are part of algebra. If X is examples-by-features and w has one value per feature, Xw produces one score per example. Transpose swaps axes; matrix multiplication is not generally commutative. Check dimensions as you would check units in physics.

Computers use finite precision. Very large exponentials may overflow; tiny values may underflow. Stable softmax calculations subtract the largest score before exponentiation. Feature scaling can improve optimization when units differ greatly, but learned scaling statistics must be fit only on training data.

Questions: What direction does a gradient point? Toward the steepest local increase of a differentiable scalar function. Why update opposite it? To reduce loss locally. Does a smaller loss prove a useful model? No: leakage, a wrong split, or a mismatched objective can yield low loss and poor real-world decisions.

Practice the base-rate example with a prevalence of 0.1%, sensitivity of 95%, and false-positive rate of 1%. Compute the approximate number of true and false alerts among 100,000 cases, then explain why precision differs from sensitivity.

Further reading: [Seeing Theory](https://seeing-theory.brown.edu/) and [3Blue1Brown linear algebra](https://www.3blue1brown.com/topics/linear-algebra).

## 15. Matrices as batches of examples

Let X contain m examples and n features, so X has shape (m,n). Let w contain n weights, and let b be one scalar. The expression Xw+b produces m predictions. A row of X is one example; a column is one feature. If a library expects data shaped (channels,height,width), feeding (height,width,channels) may be wrong even if the same numbers are present.

For a linear prediction yhat = Xw+b and squared-error loss L = (1/m) sum((yhat-y)^2), the gradient with respect to w is proportional to X transpose times the residual. This says each feature's update depends on how that feature co-varies with the prediction error. Matrix notation is compact because it applies the same calculation to every row.

## 16. Distributions and expectation

A probability distribution assigns probability mass or density to possible outcomes. A Bernoulli variable represents a yes/no outcome with parameter p. A categorical variable selects one of several classes. A normal distribution is often used as an approximation for continuous noise, but it is not automatically appropriate for every dataset.

The expectation is a probability-weighted average. For outcomes 0 and 10, with probabilities 0.9 and 0.1, expected value is 1. It does not say the outcome will be 1; it summarizes repeated uncertainty. Variance measures spread around the mean. In decision-making, expected loss weighs possible errors by their probability and cost.

A dataset is a sample from a collection process. If collection excludes some groups or records outcomes differently, statistical calculation cannot make that sample representative by itself. Document sampling and missingness before interpreting estimates.

## 17. Derivatives and optimization step by step

For f(w)=(w-3)^2, derivative is 2(w-3). If w=0, derivative is -6, so moving opposite the gradient increases w and approaches the minimum at 3. A gradient-descent update is w_new=w_old-learning_rate*gradient. With learning rate 0.1, the update is 0 - 0.1*(-6)=0.6. Too large a rate can jump back and forth or diverge; too small a rate makes progress slow.

In many dimensions, the gradient is a vector of partial derivatives. The learning rate controls step size. Momentum smooths updates using a running direction; adaptive optimizers scale coordinates using gradient history. These optimizers do not fix a bad loss, mislabeled data, or invalid evaluation.

## 18. Metrics as mathematical definitions

For binary classification, precision=TP/(TP+FP), recall=TP/(TP+FN), and specificity=TN/(TN+FP). Accuracy=(TP+TN)/all examples. Each answers a different question. If the denominator is zero, the metric is undefined and software may return a convention; inspect counts rather than accepting the number blindly.

A threshold changes TP, FP, TN, and FN. The ROC curve compares true-positive rate against false-positive rate across thresholds; the precision-recall curve emphasizes the positive class and can be more revealing when events are rare. AUC summarizes ranking behavior across thresholds but does not select an operating point.

Practice: derive the precision, recall, and accuracy for TP=40, FP=10, TN=900, FN=50. Then explain which metric matters if false negatives are most costly and why a decision threshold still needs review.

Further reading: [Khan Academy linear algebra](https://www.khanacademy.org/math/linear-algebra) and [Seeing Theory](https://seeing-theory.brown.edu/).
