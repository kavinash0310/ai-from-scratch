# Chapter 4 — Calculus, derivatives, and gradients

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

## A derivative measures local change

For a function f(x), the derivative f'(x) describes how much the output changes for a small change in x near a point. For f(x)=x², the derivative is 2x; at x=3, a tiny increase in x changes the output by roughly six times that increase.

The derivative is a local slope, not an average over the whole graph. At a flat point the derivative can be zero, but that does not guarantee the function has reached the lowest possible value.

## Partial derivatives and gradients

A model has many parameters. A partial derivative measures how the loss changes when one parameter changes while others are held fixed. The gradient collects all partial derivatives into a vector.

If a loss depends on weights w₁ and w₂, the gradient tells the local direction of steepest increase. To reduce loss, optimization moves in the opposite direction.

## The chain rule

A neural network is a composition: input goes through one layer, then another, then a loss. The chain rule multiplies local derivatives to determine how an early parameter influences the final loss.

Backpropagation applies this chain rule efficiently, reusing intermediate calculations. It is not a separate mysterious learning process; it is an algorithm for computing gradients through a computational graph.

## Numerical gradients

A derivative can be approximated by changing a parameter a small amount and measuring the loss difference. This is called finite differencing. It is slower and less precise than backpropagation for large models, but useful for checking whether gradient code is plausible.

## Questions and answers

**What is a gradient?**  
A vector of derivatives, one for each parameter, describing local loss change.

**Why does backpropagation run backward?**  
The output loss is known at the end. The chain rule propagates its effect backward through earlier computations to each parameter.

**Does a zero gradient prove the optimum is found?**  
No. It may be a local minimum, maximum, saddle point, or a region with nearly flat gradients.

**Why not update by the full gradient amount?**  
The gradient is a local approximation. A large step may overshoot or enter a region where the approximation is poor.

## Practice and checkpoint

For f(w)=(w−3)², sketch the curve and compute the derivative. Mark how a gradient-descent update moves w toward 3 for w=0, then explain how the learning rate changes the step.