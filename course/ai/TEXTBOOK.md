# Classical artificial intelligence
## A beginner's textbook chapter

Classical AI includes search, planning, logic, constraints, and decision-making. These methods can solve important problems without learning a neural network. They are especially useful when actions and rules can be described explicitly.

## 1. Represent a problem as states and actions

A **state** describes the relevant situation. An **action** changes the state. A **transition model** says what state results from an action. A **goal test** checks whether the task is complete. A **path cost** measures the expense of a sequence of actions.

For route finding:
- State: current intersection.
- Action: take an outgoing road.
- Transition: arrive at the next intersection.
- Goal: reach the requested destination.
- Cost: travel time or distance.

This formulation turns a real problem into a graph. Graph nodes represent states; edges represent possible transitions. The graph can be implicit, meaning the program computes neighbors rather than storing every edge.

Choosing the state representation matters. If it leaves out information needed to determine legal future actions, search may return invalid plans. If it stores irrelevant detail, the state space becomes unnecessarily large.

## 2. Search strategies

**Breadth-first search (BFS)** explores states by number of actions from the start. It finds a path with the fewest actions when each action has equal cost. A queue stores the frontier; a visited set prevents repeated exploration.

**Depth-first search (DFS)** follows one branch deeply before returning. It can use little memory, but may wander into a long or infinite branch and does not generally find the shortest path.

**Uniform-cost search** expands the path with the smallest accumulated cost. It is appropriate when nonnegative actions have different costs.

Search can grow exponentially. If every state has b possible actions and a solution is depth d away, a naive search may examine roughly b raised to d states. Good state representation, repeated-state detection, and search guidance matter.

## 3. Heuristics and A*

A **heuristic** estimates cost remaining to a goal. A* ranks a state n by:

    f(n) = g(n) + h(n)

g(n) is the known cost from start to n; h(n) estimates the remaining cost. If h never overestimates the true remaining cost and costs are nonnegative under standard assumptions, A* can find an optimal path. A heuristic that is too weak still works but may guide search poorly. An overestimating heuristic may be faster but can lose the optimality guarantee.

For four-direction movement on a grid with unit costs, Manhattan distance is the sum of row and column differences. It is admissible when diagonal moves are forbidden and no shortcut reduces the number of required horizontal/vertical moves.

### Worked grid example

A robot starts at row 0, column 0 and seeks row 4, column 4. Manhattan distance is 8. A wall may force detours, so actual shortest route can be longer; it cannot be shorter if movement rules are as stated. A* uses 8 as a lower bound and updates the estimate as it reaches new cells.

## 4. Planning, logic, and constraints

A **planning problem** describes actions with preconditions and effects. To open a locked door, the precondition may be “has key”; the effect may be “door becomes open.” A planner searches for an action sequence that achieves the goal while respecting these conditions.

**Propositional logic** represents statements as true or false and combines them with AND, OR, NOT, and implication. **Predicate logic** adds objects, properties, and relations. A **knowledge base** stores facts and rules; an inference engine derives additional conclusions.

If a rule says Rain implies Wet, and Rain is known, infer Wet. But if Wet is known, Rain does not necessarily follow; a sprinkler could have caused it. This error is affirming the consequent. Logic is only as reliable as its premises and rules.

A **constraint satisfaction problem** has variables, domains, and constraints. In a schedule, each class is a variable, the available time slots are its domain, and constraints prevent a teacher or room from being double-booked. **Backtracking** tries an assignment and reverses it when a conflict appears. **Constraint propagation** removes impossible values before exploring more choices.

Useful heuristics include:
- choose the variable with the fewest legal values first;
- choose a value that restricts future variables least;
- propagate constraints after every assignment.

These affect search efficiency without changing which solutions are valid.

## 5. Reason under uncertainty

A deterministic rule may not be enough when observations are noisy. **Probability** represents uncertainty. **Bayes' rule** updates a prior belief using evidence:

    posterior is proportional to likelihood times prior

A **prior** is belief before observing the evidence. A **likelihood** is how compatible the evidence is with a hypothesis. A **posterior** is the updated belief.

Base rates matter. If an event is rare, many positive alerts may be false positives even when a detector performs well. Always track what the probability is conditioned on and what action follows.

A **Bayesian network** represents conditional dependencies in a graph. It can organize reasoning about causes and observations, but the graph structure and probability assumptions need evidence.

## 6. Games and adversarial decisions

A game tree alternates between the decisions of different players. **Minimax** assumes each player chooses the best move for their own objective. It searches possible moves and selects the one with the strongest worst-case response. **Utility** assigns numeric preference to outcomes. **Alpha-beta pruning** skips branches that cannot change the final choice.

When outcomes are random rather than chosen by an adversary, **expectimax** computes expected utility by weighting possible outcomes by probability. A game-playing search is only as good as its legal moves, evaluation function, and search depth.

## 7. When classical AI is useful

Use search for explicit action spaces such as routes and puzzles. Use constraints for scheduling and configuration. Use logic when rules must be explicit and auditable. Use probabilistic reasoning when uncertainty is central. Use game search where an opponent's choices matter.

A classical solution may fail when the state space is enormous, rules are hard to encode, or perception is noisy. A hybrid approach can use a learned model to interpret a scene and a planner to choose legal actions.

## 8. Questions and worked checks

**When is BFS optimal?** When each step has equal cost and the goal is to minimize number of steps.

**What does an admissible heuristic mean?** It never overestimates true remaining cost, preserving A*'s optimality under standard conditions.

**Why does wet ground not prove rain?** Several causes can produce the same observation; reversing an implication is invalid without more premises.

**What does constraint propagation do?** It removes values that cannot satisfy constraints before a full assignment is complete.

Exercise: define a search problem for crossing a river with a boat that holds two people, where some pairs cannot be left alone. State should include both river banks and boat location. Legal actions move one or two people with the boat. The goal has everyone on the destination bank. The constraints determine whether a state is legal.

Continue to [machine learning](../ml/README.md) and run the [search lab](../../labs/ai/03_search.py).