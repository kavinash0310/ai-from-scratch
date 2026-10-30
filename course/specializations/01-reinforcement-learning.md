# Chapter 1 — Reinforcement learning

> **Book-length subject volume:** For expanded explanations, worked examples, review questions, and practice, read the [specializations textbook](TEXTBOOK.md).

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

## Agent, environment, and reward

An agent observes a state, takes an action, receives a reward, and moves to a new state. The agent seeks a policy that maximizes cumulative reward. A Markov decision process describes states, actions, transitions, rewards, and discount factor γ.

The Bellman idea expresses value as expected immediate reward plus discounted future value. Q-learning estimates action values from experience; policy-gradient methods directly adjust policy parameters.

Exploration gathers information about unknown actions; exploitation uses known high-value actions. In real environments exploration can cause harm, so training in simulation and evaluating logged data are important.

## Reward is a proxy

If the reward is incomplete, the agent may exploit it in an unintended way. For example, rewarding “time on site” might encourage addictive behavior rather than user benefit. Include constraints and evaluation beyond reward.

## Deeper walkthrough: a grid-world value update

Let an agent move through a small grid to a goal. Each state is a cell; actions are up, down, left, and right. A wall blocks movement. Reaching the goal gives +10, each step costs −1, and falling into a pit costs −10.

Q-learning updates an action-value estimate toward reward plus discounted future value:

Q(s,a) ← Q(s,a) + α[r + γ maxₐ′ Q(s′,a′) − Q(s,a)]

α is learning rate, γ discounts future rewards, and s′ is the next state. Exploration may use an ε-greedy policy: usually choose the best-known action, but sometimes sample another.

If the agent learns to loop near a reward because the episode never ends, the environment or reward is poorly designed. Add a step limit and inspect trajectories. Reward numbers are design choices, not moral values.

## Questions and answers

**What does a policy do?**  
It maps an observed state to an action or action distribution.

**Why is RL different from supervised learning?**  
The agent's actions influence what it observes next, and feedback may be delayed rather than attached as a fixed label for every example.

**Why can a reward be gamed?**  
The optimizer seeks exactly what the reward specifies, not the designer's unexpressed intention.

## Practice and mastery

Build a small grid-world agent. Change one reward and observe how the policy shifts. Compare its behavior with a hand-written policy and document unsafe states.