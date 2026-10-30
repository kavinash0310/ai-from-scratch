# Mathematics for AI — full beginner notes

Math is a language for describing patterns precisely. For AI, first learn what each tool calculates, what its symbols mean, and how a small numerical example behaves.

## 1. Algebra, functions, and logarithms

A **variable** is a symbol whose value can vary. An **equation** says two expressions are equal; solving finds values that make it true. A **function** maps an input to an output. In y = f(x), x is the input and y is the output. A **parameter** defines a function's behavior; training often changes parameters.

For the line y = wx + b, w is the slope and b is the intercept. If w=2 and b=1, input x=3 gives output 7. A model might use this to predict house price from area, but price may also depend on location, age, and market conditions.

A **linear relationship** changes at a constant rate in the represented variables. A **nonlinear transformation** such as x squared or a sigmoid lets a model represent curves. A **logarithm** is the inverse of exponentiation: log base 2 of 8 is 3 because 2 to the power 3 is 8. Natural logarithms often appear in probability and loss. Log probabilities turn products into sums and penalize confident wrong predictions.

**Order of operations** prevents ambiguity. **Function composition** feeds one function's output to another. Neural networks are compositions. Practice rearranging formulas and substituting numbers before advanced proofs.

## 2. Vectors, matrices, and geometry

A **scalar** is one number. A **vector** is an ordered list of numbers; it can represent coordinates or features. A **matrix** is a rectangular array and can represent a dataset or linear transformation. A **tensor** generalizes arrays to more dimensions. **Shape** gives the number of elements along each axis and must agree for operations.

The dot product multiplies matching entries and sums them: [1,2] dot [3,4] = 1×3 + 2×4 = 11. It measures aligned weighted contributions; with normalized vectors, it relates to cosine similarity. Matrix multiplication combines rows and columns and applies a linear map. If X has shape (examples, features) and W has shape (features, outputs), XW has shape (examples, outputs).

**Transpose** swaps rows and columns. **Norm** measures vector size. **Basis** is a set of directions used to express vectors. **Projection** expresses how much of one vector points along another. An **eigenvector** is a direction preserved by a square transformation, scaled by its eigenvalue; it is useful in some methods but not a prerequisite for first ML models.

Shape check: 100 houses with 3 features forms X with shape (100,3). One weight per feature gives W shape (3,1); XW gives 100 predictions. If dimensions do not match, check which axis represents examples and which represents features.

## 3. Probability and statistics

Probability describes uncertainty under an experiment or model. It lies between 0 and 1. Probabilities of mutually exclusive exhaustive outcomes sum to 1. A **random variable** assigns a number to possible outcomes. **Conditional probability** asks for the chance of A given B; it is not generally equal to the chance of B given A.

**Mean** is the arithmetic average; **median** is the middle sorted value; **variance** measures squared spread around the mean; **standard deviation** is its square root and returns to the original units. Outliers can strongly move the mean, so robust summaries may help.

A **sample** is the observed subset; a **population** is the group we want to reason about. A statistic estimated from a sample has uncertainty. **Correlation** measures association, not causation. A **confounder** can create or hide an association. **Distribution shift** occurs when future data differs from development data.

For a fair six-sided die, probability of an even result is 3/6 = 1/2. For a classifier, predicted probability 0.8 should mean roughly 80% of comparable cases are positive if it is calibrated; a model may rank well but be poorly calibrated.

## 4. Calculus and gradients

A **derivative** measures the local rate at which an output changes as an input changes. For f(x)=x squared, derivative is 2x; at x=3, a tiny increase in x changes f by about six times that increase. The derivative is a local approximation, not an average across all values.

For many parameters, the **gradient** is a vector of partial derivatives, one per parameter. It points toward locally fastest increase of a scalar function. To reduce loss, gradient descent steps in the opposite direction. The **chain rule** computes a derivative of composed functions: change through the outer function times change through the inner function.

A neural network's forward pass computes predictions; backpropagation applies the chain rule efficiently from the loss backward through the computation. A gradient says how a small parameter change affects current loss, not what a parameter means in human language.

Finite-difference check: approximate derivative with [f(x+h)-f(x-h)]/(2h) for small h, then compare it with an analytic derivative. This helps debug tiny models.

## 5. Optimization and numerical thinking

An **objective function** is what we seek to minimize or maximize. A **loss** measures model error on examples. **Optimization** searches for parameter values that improve the objective. Gradient descent updates theta to theta minus learning-rate times gradient. A rate too large can overshoot; one too small can make progress slow.

A **convex** objective has a bowl-like geometry with no bad local minima under the usual idealized definition; neural-network objectives are generally non-convex. **Regularization** adds a preference for simpler parameter values. A **constraint** restricts allowed solutions. **Convergence** means updates approach a stable solution or stopping condition; it does not guarantee usefulness.

Numerical computation uses finite precision. Floating-point rounding, overflow, underflow, and unstable operations can cause surprises. For softmax, subtract the largest score before exponentiating; probabilities remain the same and calculation is more stable. Track loss and metrics, but also inspect predictions and data.

Worked optimization: for L(w)=(w−3) squared, derivative is 2(w−3). At w=0 and learning rate 0.1, update to 0.6. Repeating moves w toward 3. With a much larger rate, updates can leap from one side to the other.

## Self-check

Explain why a dot product needs matching vector lengths, why a gradient is not an accuracy metric, and why correlation does not prove causation. Solve shape, probability, derivative, and update examples by hand. Continue to [machine learning](../ml/README.md).