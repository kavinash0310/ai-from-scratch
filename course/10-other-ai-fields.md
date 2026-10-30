# Part 10 — Other AI fields and specialization paths

## Chapter 48 — Reinforcement learning

In reinforcement learning (RL), an agent observes a state, chooses an action, receives a reward, and enters a new state. A policy maps states to actions. The objective is often expected cumulative reward, not immediate reward alone.

A Markov decision process models states, actions, transition probabilities, rewards, and discount factor γ. The Bellman equation expresses the value of a state as expected immediate reward plus discounted future value.

A central challenge is exploration versus exploitation: try uncertain actions to learn, or choose actions that already appear valuable. In real systems, exploration can harm people or assets, so simulation and offline evaluation matter.

Q-learning estimates action values from experience. Policy-gradient methods directly adjust a policy. RLHF applies preference-based training to language-model behavior, but it is not equivalent to all of RL and can have reward misspecification issues.

## Chapter 49 — Recommendation and ranking

A recommendation system ranks items for a person or context. Candidate generation narrows millions of items; ranking orders a manageable set; the interface controls what users see and click.

Collaborative filtering uses user-item interaction patterns. Content-based methods compare item features. Hybrid systems combine them. Challenges include sparse data, cold start, popularity bias, feedback loops, diversity, novelty, and changing interests.

Clicks are not pure preference labels: users can only click items shown to them. Evaluate beyond click prediction when possible, using quality, satisfaction, diversity, and longer-term user outcomes.

## Chapter 50 — Time series

Time series observations are ordered and often seasonal. Forecasting includes a horizon and information cutoff. Preserve chronological order in evaluation. Naive baselines such as last-value and seasonal repeat are essential.

Use rolling-origin evaluation: train on a past interval, predict a future interval, advance the cutoff, and repeat. Report error by horizon and period. Sudden policy or market changes can break historical patterns.

## Chapter 51 — Graphs and relational learning

A graph is a set of nodes and edges. It can represent people and relationships, chemicals and bonds, roads and connections, or software dependencies. Graph neural networks update node representations by aggregating information from neighbors.

Graph data may be directed, weighted, temporal, or heterogeneous. Evaluation must prevent target or future edges leaking into training. Connections can encode sensitive relationships even when node attributes are removed.

## Chapter 52 — Robotics and embodied AI

Robotics connects perception, state estimation, planning, and control to physical action. Sensors are noisy and delayed. The world can change between observation and action. Safety constraints must be explicit and tested in simulation and carefully controlled environments.

A useful pipeline is: observe → estimate state → plan action → control → observe again. A model that works on static images may fail when lighting, movement, calibration, or actuation changes.

## How to choose a specialty

Pick one track after the core ML and evaluation chapters. Choose a problem with a safe dataset or simulation, a simple baseline, and a measurable outcome. Finish a small end-to-end project before studying every advanced method in that field.

Possible tracks:
- NLP and LLMs;
- computer vision;
- recommender systems;
- forecasting;
- robotics and control;
- reinforcement learning;
- graph and scientific machine learning;
- AI engineering and deployment.

## Q&A

**Why can reinforcement learning learn a bad goal?**  
It optimizes the specified reward, which may be an imperfect proxy for the real objective. The agent can exploit gaps between reward and intent.

**Why are click logs biased?**  
A user can only click items that were shown. The recommendation policy affects the data it later learns from, creating a feedback loop.

**Why not randomly split time-series rows?**  
That can train on the future and test on the past, unlike the real deployment direction. Use chronological or rolling splits.

**What is neighbor aggregation in a graph neural network?**  
A node combines information from connected nodes to update its representation. This makes connectivity part of the model input and can spread both useful signals and harmful noise.

**Why is robotics harder than a static prediction task?**  
The system acts in a changing physical world with sensing uncertainty, latency, safety constraints, and consequences for mistakes.