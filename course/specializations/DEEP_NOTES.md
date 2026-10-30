# AI specializations — full beginner notes

Specializations apply shared foundations to different data and decisions. Each area has assumptions that can invalidate a familiar metric or split.

## 1. Reinforcement learning

**Reinforcement learning (RL)** studies an agent that acts in an environment and receives rewards. A **state** describes the situation; an **action** is a choice; a **reward** is numeric feedback; a **policy** maps states to actions. An **episode** is interaction until termination.

The **return** is accumulated future reward. **Exploration** tries uncertain actions to learn; **exploitation** uses currently preferred actions. A **value function** estimates expected future return. A **Q-function** estimates return for a state/action pair. The **discount factor** controls how much distant rewards count.

Reward design is difficult: an agent may optimize numeric reward while violating real intent. Offline data may not cover actions a learned policy prefers. Start with a simulator, safe baseline, clear constraints, and tests for reward hacking before real-world use.

## 2. Recommendations and ranking

A recommender predicts which items may help a user. **Collaborative filtering** uses patterns in user-item interactions; **content-based filtering** uses item/user attributes. A **candidate generator** finds a manageable item set; a **ranker** orders candidates; a **re-ranking** layer can enforce freshness, diversity, or policy rules.

Interactions are not neutral labels: an item not clicked may never have been shown. This is **exposure bias**. A **cold-start** user or item has little history. Ranking metrics such as NDCG reward placing relevant results high, but online experiments should also monitor satisfaction, diversity, and long-term effects. Popularity is a valuable baseline.

## 3. Time-series forecasting

A **time series** is ordered observations indexed by time. A forecast predicts future values using only information available at the forecast origin. **Trend** is long-term movement; **seasonality** is a repeating pattern; **residual** is what remains after modeled components.

Never randomly split a forecasting series when predicting the future. Use chronological or rolling-origin evaluation. Ensure features do not use future information. Compare seasonal-naive and recent-average baselines before complex models. MAE/RMSE summarize error but may hide systematic bias or peak misses. Report forecast horizon and data refresh schedule.

## 4. Graph learning

A **graph** has nodes and edges representing entities and relationships. Examples include people linked by interactions, molecules linked by bonds, or web pages linked by references. **Degree** counts a node's neighbors. **Message passing** updates a node representation using neighboring representations. A graph neural network can learn from node features and connections.

Graph splits are subtle: connected examples can leak information across train and test. Decide whether the task predicts unseen nodes, unseen edges, or future links. Inspect graph construction, missing edges, and privacy concerns. A graph is not necessarily complete or unbiased.

## 5. Robotics and embodied AI

A robot senses and acts in a physical environment. **Perception** estimates what is happening; **localization** estimates position; **mapping** represents surroundings; **planning** selects a path or action; **control** converts a desired action into motor commands. Sensors are noisy and actions have delay.

A robot must account for uncertainty, dynamics, collisions, battery, and safe fallback behavior. A **simulator** allows lower-risk experiments, but the **sim-to-real gap** means simulated dynamics differ from hardware. Test progressively in bounded environments and use emergency stops. A language model can help interpret instructions, but its output must be constrained by verified perception and safety controllers.

### Q&A and practice

**Can RL learn without a reward?** It needs feedback or another learning signal; the challenge is making that signal represent the real goal.
**Does a click mean a recommendation was good?** Not necessarily; the item must have been exposed, and clicks do not equal long-term satisfaction.
**Why is a random split dangerous for time series?** It can train on future patterns and test on the past.

Choose one specialty, define its prediction or action contract, build a naive baseline, identify leakage and safety risks, and design evaluation before choosing a complex model.