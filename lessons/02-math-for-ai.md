# Lesson 02 — Math for AI, built gradually

## Learning goals

Connect algebra, statistics, probability, linear algebra, and calculus to what a model actually computes. The goal is useful intuition first; depth comes with practice.

## 1. Algebra describes relationships

A model often receives numbers and calculates a new number. A **function** describes this relationship. For example, if a taxi charges a base fare plus a fee per kilometre, then cost = base fare + fee × distance.

A prediction model is also a function. It maps input features to an output. Learning means choosing values inside that function so its predictions fit examples well.

A **parameter** is a value the model can adjust. A feature is information supplied to the model. Do not confuse them: a feature comes from the example; a parameter is learned by the model.

## 2. Statistics describes observed data

A dataset is a collection of observations, not a perfect view of reality.

- The **mean** is the arithmetic average. A few extreme values can move it strongly.
- The **median** is the middle value after sorting. It is more resistant to extreme values.
- **Variance** and **standard deviation** describe spread around the mean.
- A **distribution** describes which values occur and how often.
- A **sample** is the part of a population we observed.

If the sample is unrepresentative, a model trained on it can systematically fail for people or conditions missing from the data. A large sample does not automatically fix a biased sampling process.

## 3. Probability describes uncertainty

A probability is a number from 0 to 1 used to express uncertainty under a model or assumption. A prediction of 0.8 does not mean “the model is right 80% of the time in every situation.” It means the model assigns that probability according to its learned behavior. Calibration tests whether predictions near 0.8 are correct about 80% of the time across a suitable group.

Conditional probability asks how likely A is when B is known. In classification, we often care about the chance of a label given observed features. Changing the population or measurement process can change that probability.

## 4. Vectors and matrices represent many values

A **scalar** is one number. A **vector** is an ordered list of numbers. A **matrix** is a grid of numbers. A dataset with rows as examples and columns as features is naturally represented as a matrix.

A dot product multiplies corresponding vector values and adds the results. It is a weighted sum. A linear model uses weights to decide how strongly each feature affects a prediction.

Example: prediction = 2 × bedrooms + 0.5 × area. The numbers 2 and 0.5 are weights. Real models learn such weights from examples.

Vector and matrix operations let libraries process many examples efficiently. They also make neural-network computations concise.

## 5. Derivatives describe change

A derivative tells how quickly a function changes when its input changes. If a prediction error is high, we want to know which parameter changes would reduce it.

Picture a hill where height is error. The slope points uphill; move in the opposite direction to go downhill. The **gradient** is the collection of slopes for all model parameters.

**Gradient descent** updates parameters in the direction that should reduce error. A learning rate controls step size. Too large can overshoot; too small can make learning very slow.

Backpropagation is an efficient application of the chain rule that calculates how each neural-network parameter contributed to the final error. The computer does not magically know a better answer; it calculates local gradients and repeats updates.

## 6. Loss and optimization

A **loss function** turns prediction errors into a number to minimize. Mean squared error penalizes large numerical errors strongly and is commonly used for regression. Cross-entropy loss is commonly used when predicting a probability distribution over classes.

Optimization means searching for parameter values that reduce the chosen objective. Minimizing training loss alone is not enough: the model could memorize training examples. We care about performance on new examples too.

## Worked example: fit a simple line

Suppose house area is the input x and price is the target y. A simple model predicts y = w × x + b. The parameter w is the slope and b is the intercept.

1. Start with guesses for w and b.
2. Predict a price for each training example.
3. Compare predictions with known prices using a loss.
4. Calculate how changing w and b changes the loss.
5. Adjust w and b a little to reduce the loss.
6. Repeat, then evaluate on houses not used for fitting.

This tiny example contains the central loop of many learning algorithms.

## Review questions with answers

**1. What is the difference between a feature and a parameter?**  
A feature describes an input example, such as area. A parameter is an adjustable model value, such as the learned weight on area.

**2. Why can the mean be misleading?**  
Extreme values can pull it far from what is typical. Looking at the median and distribution often provides context.

**3. What does a derivative tell us?**  
It describes how a function changes near a point. During learning, derivatives help estimate which direction to change parameters to reduce loss.

**4. Does lower training loss guarantee a better model?**  
No. The model may memorize training examples. We need a fair evaluation on data that was not used to fit it.

**5. What does a learning rate do?**  
It controls how large a parameter update is. If too large, optimization can jump around or diverge; if too small, it can take a long time.

## Practice

- Calculate mean and median for a small list containing an extreme value.
- Draw y = 2x + 1 for several x values and explain slope and intercept.
- Calculate a dot product by hand.
- On paper, draw a bowl-shaped loss curve and show how repeated downhill steps approach a minimum.

## Mastery check

Describe how a model can use a weighted sum, measure an error, and adjust weights. You do not need to derive every gradient yet.