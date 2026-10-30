# Lesson 08 — AI specializations and how to choose

## Learning goals

Understand the main data types and methods behind common AI specialties, then choose a project that fits your interests and resources.

## Computer vision

Computer vision systems work with images or video. A digital image is a grid of pixel values, often with color channels. Convolutional neural networks use local filters to detect patterns; modern vision systems also use transformers and pretrained encoders.

Common tasks include image classification, object detection, segmentation, and image generation. A label for a whole image is different from a box around every object or a pixel-level mask. Choose the task that matches what a user needs.

**Starter project:** classify a small set of plant or household images. Split by source or photographer if near-duplicate images could leak across splits.

## Natural language processing

Language is represented as sequences. Earlier approaches used hand-built features, counts, or vector representations. Neural networks learned contextual representations. Transformers now provide a common architecture for many language tasks.

Tasks include classification, translation, information extraction, summarization, and generation. Language data can contain private information, stereotypes, or annotation ambiguity. Define whose language and which context the system is expected to support.

**Starter project:** categorize a small collection of public short texts, document the label definitions, and inspect errors across writing styles.

## Recommendation and ranking

A recommender estimates which items may be useful to a person or context. Collaborative filtering uses patterns in user-item interactions; content-based methods use item properties; modern systems can combine both.

The key challenge is not just prediction accuracy. Feedback is selective: users only interact with items shown to them. Popularity bias, cold-start users, changing tastes, and the effects of ranking all matter.

**Starter project:** recommend books using descriptions or a small public interaction dataset. Compare with “most popular” and explain the cold-start problem.

## Time series and forecasting

Time series are observations ordered in time. A random train-test split can leak future information, so preserve chronology. Baselines include last value, seasonal average, and moving average.

Forecasts should include a horizon and uncertainty range. A prediction for tomorrow is different from one for a year from now. Sudden structural changes can make old patterns unreliable.

**Starter project:** forecast a public monthly series using a seasonal naive baseline, then compare one model over several rolling-origin test windows.

## Reinforcement learning

An agent observes a state, takes an action, receives a reward, and transitions to another state. It tries to learn a policy that maximizes future reward. Exploration gathers information about actions; exploitation uses what is already known.

Rewards are proxies for goals. Poorly designed rewards can cause an agent to exploit the scoring rule in an unwanted way. Simulations can differ from the real world, and exploration can be unsafe in physical settings.

**Starter project:** train an agent in a tiny grid-world, then change the reward and see how behavior changes.

## Graph machine learning

A graph has nodes and edges. Social networks, molecules, roads, and dependencies are naturally graph-shaped. Graph algorithms can analyze structure; graph neural networks learn representations by combining information from neighbors.

The definition of nodes and edges encodes assumptions. Leakage can occur when future edges or target-linked structure are present in training.

## Selecting your specialty

Ask:
1. What data type interests me?
2. Who would use the result?
3. Is there a safe, lawful, small dataset?
4. What is a simple baseline?
5. Can I evaluate the task realistically with my available time and compute?

Choose one specialty for a first project. Breadth is useful, but a finished project with an honest evaluation teaches more than shallowly sampling many libraries.

## Review questions with answers

**1. Why should a time-series split preserve time order?**  
In deployment, the model predicts future values using past observations. Random splitting can let future patterns influence the training estimate.

**2. What is cold start in recommendation?**  
The system has little or no interaction history for a new user or item, making collaborative signals weak.

**3. Why is a reward function a safety concern in reinforcement learning?**  
The agent optimizes the reward as written, not the human intention behind it. A flawed reward can encourage undesirable behavior.

**4. Why check image duplicates across splits?**  
Near-duplicates can make test results look strong even though the model has effectively seen the same image during training.

**5. Must I study every specialty to become advanced?**  
No. Build broad foundations, then develop depth in one or two domains. Expert skill includes knowing the boundaries of your chosen methods.

## Practice

Choose one specialty and write a small project brief using the template. Include data provenance, baseline, evaluation split, expected errors, and a meaningful limitation.

## Mastery check

Explain what makes the data in your chosen specialty different from a simple spreadsheet and how that changes the model and evaluation plan.