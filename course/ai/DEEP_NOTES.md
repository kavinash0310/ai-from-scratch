# Classical AI — full beginner notes

Classical AI studies how a system can search possibilities, represent facts, reason with rules, and choose actions. It remains useful even when a learned model is part of the final product.

## 1. Search and planning

A **state** describes a situation. An **action** changes one state into another. A **goal test** checks whether a state satisfies a task. A **search problem** has an initial state, actions, transition rules, and a goal. A path is a sequence of actions; **path cost** measures expense such as distance, time, or energy.

Route finding is an example. State might be the current city, actions are roads, and cost is travel time. **Breadth-first search (BFS)** explores all states at one depth before going deeper; it finds a shortest path when every action has equal cost. **Depth-first search (DFS)** explores a branch deeply and may use less memory, but can miss a short solution or get trapped. **Uniform-cost search** expands the cheapest path so far and handles unequal nonnegative costs.

A **heuristic** estimates remaining cost. A* search ranks a path with g(n)+h(n): cost already paid plus estimated cost to the goal. If the heuristic never overestimates true remaining cost, A* can find an optimal path under standard assumptions. A weak heuristic gives little speed benefit; an overestimating heuristic may lose optimality.

A **planning problem** asks for actions whose preconditions are satisfied and effects reach a goal. Search can explode because possibilities grow quickly. Use compact state representation, avoid revisiting states, design a helpful heuristic, and measure solution quality and time.

Worked example: on a 3×3 grid, state is the agent's cell, actions move up/down/left/right if not blocked, and goal is target cell. Manhattan distance (horizontal plus vertical steps) is a heuristic when movement is four-directional and every step costs 1.

## 2. Logic and constraint solving

**Propositional logic** represents statements that are true or false. AND, OR, NOT, and implication combine statements. **Predicate logic** adds objects, properties, and relations, such as Likes(Ava, tea). A **knowledge base** stores facts and rules; an **inference rule** derives new facts from existing ones.

A rule “if raining, then ground is wet” can be written Rain implies Wet. From Rain and the rule, infer Wet. But implication is not a causal law: knowing Wet does not prove Rain, because a sprinkler could also wet the ground.

A **constraint satisfaction problem (CSP)** has variables, domains of allowed values, and constraints restricting combinations. In a timetable, variables are classes, domains are time slots, and constraints prohibit a teacher or room from being double-booked. **Backtracking search** assigns values and reverses a choice when it conflicts. **Constraint propagation** removes values that cannot work given current assignments.

Useful CSP strategies include choosing the variable with the fewest remaining values, trying the most constraining choices last, and propagating constraints after each assignment. These improve search order without changing valid solutions.

## 3. Uncertainty and game decisions

A **probability** assigns a degree of uncertainty to events. A Bayesian network represents conditional dependencies in a graph. **Bayes' rule** updates prior belief using evidence: posterior is proportional to likelihood times prior. A **prior** is belief before evidence; a **likelihood** says how compatible evidence is with a hypothesis; a **posterior** is belief after observing it.

Base rates matter. If an illness is rare, a positive test can still have a meaningful false-positive chance even when the test is accurate. Distinguish **sensitivity** (positive among truly positive cases) from **precision** (truly positive among predicted positives).

A game can be a tree of alternating decisions. **Minimax** chooses a move that maximizes a player's outcome, assuming an opponent responds optimally to minimize it. **Utility** is a numerical preference over outcomes. **Alpha-beta pruning** skips branches that cannot affect the final choice. In uncertain environments, **expectimax** averages outcomes by probability instead of assuming an adversary.

### Q&A and practice

**Is A* always best?** No. It needs a useful heuristic and memory; other methods fit different constraints.
**Does a logical rule learn from examples?** Not automatically; it reasons from explicit facts and rules unless paired with learning.
**Does 90% accuracy mean a rare disease detector is safe?** Not necessarily. Class imbalance, false negatives, and false positives need appropriate metrics.

Practice: implement BFS on a grid, solve a small scheduling CSP, calculate a Bayes update for a diagnostic test, and draw a two-ply minimax tree. For each, describe assumptions and failure modes. Continue to [machine learning](../ml/README.md).