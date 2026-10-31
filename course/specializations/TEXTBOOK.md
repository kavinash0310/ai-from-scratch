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

## 8. Reinforcement learning: value update in a tiny example

Suppose an agent takes an action, receives reward r, and moves to state s'. Q-learning updates Q(s,a) toward r + gamma times the largest estimated next-action value. If current estimate is 2, observed reward is 1, gamma is 0.9, and the next state's largest estimate is 4, the target is 4.6. With learning rate 0.5, the estimate moves halfway from 2 to 4.6, reaching 3.3. The learning rate controls how quickly experience changes the estimate.

This update assumes the transition and reward are meaningful. If the reward grants points for speed but ignores collisions, a robot may learn unsafe behavior. Reward clipping, exploration schedules, and simulator fidelity affect outcomes. Evaluate with multiple random seeds and report variation, not only the most successful run.

## 9. Recommendation: exposure and experimentation

Ranking changes what users see, which changes future clicks and training data. This is a feedback loop. A system can over-recommend popular items and reduce discovery. Position bias means a top-ranked item receives more clicks partly because it is visible. Offline logs are therefore biased by the prior ranking policy.

Candidate generation and ranking have different recall and latency requirements. A candidate stage should avoid dropping relevant items; ranking can then order the candidate set. Use a time-based or user-based split that matches deployment. Online experiments can estimate the effect of a change but need guardrails for user harm, novelty, and long-term outcomes. Do not optimize engagement without defining what benefit it represents.

## 10. Forecasting: horizon, seasonality, and uncertainty

A forecast horizon is how far ahead predictions are needed. Forecast accuracy often declines with horizon. A seasonal baseline repeats an observation from the previous season, such as last week's same weekday. This baseline can be surprisingly hard to beat.

Rolling-origin evaluation simulates repeated real forecasting moments. At each origin, train only on past observations, forecast the next horizon, and record errors. Use prediction intervals and inspect whether they cover outcomes at the expected rate. Avoid leakage from centered rolling windows or revised future information. If demand has holidays or promotions, future features are usable only if known at forecast time.

## 11. Graph and robotics project boundaries

For graph prediction, decide if the target is a missing edge, node label, or future event. Build train/validation/test graphs so the target cannot leak through message passing. Compare a graph model with simple degree or neighborhood baselines. Check whether graph edges encode sensitive or inferred relationships.

For robotics, divide the problem into perception, state estimation, planning, control, and safety. Test each layer with fault injection: missing sensor, delayed packet, obstacle, motor saturation. A simulated policy should transfer to hardware only after staged validation. Safety constraints must remain active if the learned component fails.

Questions: Why not reward clicks alone? Visibility affects clicks and can harm user value. What is a forecast origin? The time at which the prediction is made using then-available information. What does message passing do? It aggregates information along graph edges.

Practice: select one area and design a baseline experiment, split policy, metric, failure analysis, and safe fallback. State the biggest assumption you are making and how you would test it.

## 12. Compare a simple RL update with supervised learning

A supervised example gives an input and a target label. An RL transition gives a state, chosen action, reward, and next state; the correct action may not be labeled. Q-learning updates an action-value estimate toward reward plus discounted future value. This is a bootstrapping target because it uses the model's own estimate of the future.

An exploration policy balances trying uncertain actions against using current knowledge. Epsilon-greedy chooses a random action with probability epsilon and otherwise selects the best estimated action. It is simple but can take unsafe actions. In offline RL, the learner uses a fixed dataset and should not assume unobserved actions have known outcomes. Evaluating a policy from historical logs requires assumptions about how those logs were collected.

## 13. Recommendation metrics and causal impact

Precision at k measures the fraction of the top k items judged relevant; recall at k measures how much of the relevant set was found. Discounted cumulative gain gives greater weight to relevant items near the top. These are ranking metrics, not user-welfare measures. Add diversity, coverage, freshness, and user-defined outcomes.

A recommendation can change user behavior, so online experiments may be needed to estimate causal impact. Random assignment helps compare alternatives but should include guardrails, adequate duration, and checks for novelty and long-term effects. Avoid optimizing clicks alone if the true aim is learning, satisfaction, or well-being.

## 14. Forecasting workflow in detail

First plot observations and identify trend, seasonal cycles, missing intervals, and outliers. Establish naive and seasonal-naive forecasts. Choose the horizon, then evaluate with rolling origins. Compare errors by horizon and slice such as weekday, region, or demand level. A model may be good for routine periods and fail on holidays.

Prediction intervals can be assessed for coverage: if a nominal 90% interval is well calibrated, approximately 90% of relevant future outcomes should fall within it under comparable conditions. Wide intervals are less useful but may be more honest. Point forecasts and uncertainty bounds serve different decision needs.

## 15. Graph and robotics diagnostics

In a graph project, compare against degree, common-neighbor, or feature-only baselines. Test whether a target label can be inferred from graph construction or user behavior. For temporal graphs, ensure only past edges are used. Neighbor sampling and graph size influence memory and representation.

A robotics test plan should inject sensor dropout, noisy location, network delay, obstacle changes, and actuator saturation. Define safe limits and stop conditions for each test. Simulation tests code logic; hardware tests validate physical assumptions. Record which behaviors are never tested and keep a physical emergency stop.

Practice: choose one specialization and define a realistic held-out test: future time, new user, unseen edge, or physical environment. Explain why it matches deployment and identify a failure that the metric might hide.
