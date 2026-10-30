# AI specializations: a textbook volume

This volume studies five areas with different data, objectives, and evaluation rules. The right first question is not “Which model is popular?” but “What kind of decision or prediction is this, and what information exists at that moment?”

## 1. Reinforcement learning

In supervised learning, an example includes a target. In reinforcement learning (RL), an agent chooses actions and receives rewards from an environment. Rewards may arrive later, so the learner must connect an earlier action with a future result.

A Markov decision process describes states, actions, transition probabilities, rewards, and a discount factor. A state is the information used to describe the situation. An action is a choice. A transition model describes how an action changes the next state. The reward is a numerical proxy for outcomes. The discount factor controls how much future reward counts. A policy maps states to actions. The goal is usually to maximize expected cumulative reward.

Worked grid example: an agent starts at one cell, moves north, south, east, or west, receives -1 for each move, and gets +10 at the goal. The negative step reward encourages short routes. If every movement instead gives +1, the agent may learn to wander forever. Reward design encodes the goal and can create unintended behavior.

Value methods estimate future return from states or state-action pairs. Q-learning updates an estimate using the reward just received and the expected value of the next state. Policy-gradient methods adjust a parameterized policy directly. Actor-critic combines a policy actor with a value critic. Exploration tries uncertain actions; exploitation uses actions already believed beneficial.

RL is hard to evaluate because actions affect future experience and rewards may be misspecified. Offline logs may lack outcomes for actions a new policy would take. Begin in simulation or a constrained environment, compare with a safe baseline, limit exploration, and measure real outcomes beyond the reward score. Do not casually experiment on people or physical systems.

## 2. Recommendation systems

A recommender ranks items for a user or context: products, music, courses, or news. Feedback may be explicit, such as a rating, or implicit, such as a click. A click is not the same as satisfaction because position and exposure affect what is seen.

Collaborative filtering finds patterns across users and items. Matrix factorization approximates a sparse user-item table with lower-dimensional user and item vectors. Content-based recommendation uses item properties and a user's history. Hybrid systems combine signals. New users and new items cause the cold-start problem.

Many recommenders use a pipeline: candidate generation selects a manageable set, ranking orders it, and policy rules constrain what may appear. Evaluate ranking with precision at k, recall at k, or discounted gain; also inspect coverage, diversity, freshness, and user outcomes. An offline ranking score does not prove that a deployed change improves user welfare. Exposure can create a feedback loop: already popular items are shown more often and get more clicks.

## 3. Time-series forecasting

A time series is ordered measurements, such as hourly energy demand. Trend is long-term movement; seasonality is a repeating pattern; noise is irregular variation. Time order changes evaluation: a random split may train on future observations and test on the past.

Start with a naive baseline, such as “next value equals the last value” or “this Monday equals last Monday.” Then test seasonal and statistical methods. Define the forecast horizon and the moment of prediction. Use rolling-origin evaluation: fit on an earlier window, forecast the next period, move forward, and repeat. Fit preprocessing only on information available at each origin.

MAE treats absolute errors evenly; RMSE penalizes large errors more; percentage errors can be unstable when actual values approach zero. Prediction intervals communicate uncertainty that a point forecast hides. Check revised historical data and features that are not actually available at prediction time.

## 4. Graph learning

A graph has nodes and edges. Nodes may represent people, pages, molecules, or devices; edges encode relationships. Edges can be directed, weighted, typed, and time-stamped. Graph algorithms include shortest paths, connectivity, and centrality. A graph neural network updates each node's representation by aggregating information from neighbors. More layers include more distant neighbors, but excessive aggregation can make representations too similar.

Graph splits need special care. If a target edge is visible during message passing, the model may leak the answer. A future relationship cannot be used to predict the past. Decide whether the task predicts unseen nodes, unseen edges, or future edges and split to match. Graphs can reveal sensitive relationships, so consider privacy and consent.

## 5. Robotics

A robot senses, estimates state, plans, acts through actuators, and observes again. Sensors are noisy; the robot's estimated position is not perfect truth. Localization estimates position. Mapping represents the environment. SLAM combines localization and mapping.

Planning chooses a path or sequence; control converts desired behavior into physical commands. Feedback control measures the error between target and observed state and adjusts action. A route valid in a map may fail due to friction, latency, obstacles, or sensing error.

Simulation enables repeatable experiments but differs from the physical world, a reality gap. Use staged hardware tests, low-energy limits, emergency stops, and safe areas. A learned policy should not be the sole safety mechanism for a real robot.

## 6. Choose an area and baseline

| Problem shape | Area | First baseline |
| --- | --- | --- |
| Actions affect future outcomes | RL | Safe scripted policy |
| Rank items for people | Recommendation | Popularity or content ranking |
| Predict ordered future measurements | Time series | Last-value or seasonal baseline |
| Relationships carry information | Graph learning | Graph statistics or classical algorithms |
| Sense and act in the physical world | Robotics | Constrained feedback controller |

The simple baseline is useful: it sets a comparison and may solve the need at lower cost.

## 7. Review questions

Why is reward only a proxy? Because it measures a chosen signal and can omit side effects. Why can clicks be biased? Exposure and position influence whether an item is clicked. Why must a forecast split respect time? The intended use predicts future observations from past information. Why can a graph model leak? Neighbor structure may contain the target information. Why test robots in stages? Physical errors can injure people or damage equipment.

Practice: choose one specialization and write the task, affected people, available-at-decision inputs, baseline, primary metric, error cost, and fallback. For RL include state, action, reward, and exploration limits. For forecasting include horizon and chronological split. For graphs include edge semantics and leakage controls.

Further reading: [Sutton and Barto](http://incompleteideas.net/book/the-book-2nd.html), [Google recommendation systems](https://developers.google.com/machine-learning/recommendation), [Forecasting: Principles and Practice](https://otexts.com/fpp3/), [PyTorch Geometric](https://pytorch-geometric.readthedocs.io/), and [ROS 2](https://docs.ros.org/).
