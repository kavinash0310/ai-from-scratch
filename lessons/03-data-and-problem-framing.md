# Lesson 03 — Data and problem framing

## Learning goals

Turn a vague wish for “AI” into a concrete task, identify the data needed, and prevent mistakes that make a model seem more successful than it is.

## Begin with a decision, not an algorithm

“Use AI to improve customer service” is too vague to train or evaluate. Ask:
- Who needs help?
- What decision or action should change?
- What input exists at decision time?
- What output would help?
- What happens when the output is wrong?
- Is machine learning necessary, or would a rule or search method work better?

A good ML framing says what one example is, what information is available, and what target should be predicted.

## Examples, features, labels

An **example** is one unit of observation: one email, transaction, patient visit, image, or time period. A **feature** is a measurable input about that example. A **label** is the known answer used for training or evaluation.

For spam detection, one example might be one email. Features could include words and sender information. The label says spam or not spam.

A model should not receive information that would be unavailable when the real decision is made. If an email was marked “spam” after a human reviewed it, a feature recording that review is unavailable at prediction time and leaks the answer.

## Decide the unit and prediction moment

A common source of error is mixing units. If a person has ten transactions, should the model predict one result per transaction or one result per person? If multiple rows from the same person appear in both training and test sets, the model may recognize that person's pattern instead of learning a general rule.

For time-dependent decisions, use only information available before the prediction moment. A model that predicts tomorrow’s demand must not see tomorrow’s sales.

Write down the prediction moment explicitly. Then audit each feature: would this value exist at that moment?

## Data quality and provenance

Before modeling, ask:
- Where did the data come from?
- Was it collected for this purpose?
- Do you have permission to use it?
- What does a missing value mean?
- Were labels assigned consistently?
- Are some groups, locations, or time periods absent?
- Are duplicates present?
- Did the data collection process change?

Data are produced by people and systems. The pattern a model learns can reflect the measurement process or historical decisions, not an objective truth.

Keep a small data dictionary: name, meaning, type, unit, source, collection time, and known caveats for each column.

## Split before you learn from the data

A training set is used to fit model parameters. A validation set supports model choice and tuning. A test set is reserved for a final estimate.

Do not choose preprocessing rules using the full dataset before splitting. For example, if you calculate averages or scaling values using every row, information from the test set has influenced training. Fit those transformations on training data only, then apply them to validation and test data.

The split must match the real use:
- Random split can suit independent examples.
- Group split keeps related examples together.
- Time split trains on the past and tests on the future.
- Location or domain split can test transfer to new environments.

## Build a baseline

A baseline is a simple comparison point. It might always predict the most common class, the historical average, or a transparent rule. If a complex model cannot beat a reasonable baseline, it may not add value.

Choose the metric before looking at final test results. If a false negative is much more costly than a false positive, accuracy alone is inadequate.

## Worked example: predict late deliveries

- Unit: one shipment.
- Prediction time: when the shipment is accepted.
- Candidate inputs: origin, destination, weekday, package type, and weather forecast available then.
- Target: whether delivery is late.
- Leakage risk: actual arrival timestamp or a field updated after delivery.
- Baseline: fraction late overall or by route.
- Evaluation: test on a later time period to mimic future shipments.
- Error impact: the business may promise a delivery time, so false confidence can harm customers.

This description is already valuable before selecting any model.

## Review questions with answers

**1. Why is “improve customer service” not a sufficient ML task?**  
It has no precise input, prediction moment, target, or success measure. A team needs to specify the decision and its consequences.

**2. What is target leakage?**  
It occurs when training or evaluation includes information that would not be available at prediction time, often directly or indirectly revealing the answer.

**3. Why split data before fitting a scaler or imputer?**  
Those transformations learn statistics from data. If test data contributes, the final evaluation is no longer fully independent.

**4. When is a random split inappropriate?**  
When examples are linked by person, device, location, or time. Random splitting can place near-duplicates or future observations in both train and test.

**5. Why make a baseline?**  
It tells you whether the model adds value over a simple or existing approach. A sophisticated model is not useful just because it is sophisticated.

## Practice

Write a one-page problem brief for a task you care about. Specify the user, action, example unit, prediction moment, input fields, target, baseline, metric, data source, and failure cost.

## Mastery check

For every feature you propose, answer: “Would this be known at the exact moment this prediction is needed?” If you cannot answer, investigate before modeling.