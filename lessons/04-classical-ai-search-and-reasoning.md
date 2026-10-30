# Lesson 04 — Classical AI: search, planning, and reasoning

## Learning goals

Understand how a computer can solve a problem by exploring possible states, how heuristic guidance helps, and when decisions involve uncertainty or an opponent.

## Represent the problem first

A **state** describes the situation now. An **action** changes one state to another. A **goal test** checks whether the desired situation has been reached. A **path cost** measures the cost of actions taken.

For a maze, a state is your current cell, actions move north/south/east/west, the goal is the exit, and cost may be the number of steps.

This representation is crucial: a search algorithm can only reason over what the program represents. If walls or movement constraints are missing, the answer can be invalid.

## Uninformed search

**Breadth-first search (BFS)** explores all states one step away, then two steps away, and so on. If every action costs the same, the first goal it finds uses the fewest actions. It stores a frontier of discovered states; a queue gives the first-discovered state first.

**Depth-first search (DFS)** follows one path deeply before backtracking. It can use less memory, but may spend a long time on a bad path and does not guarantee the shortest path.

When action costs vary, **Dijkstra’s algorithm** expands the currently cheapest known route. It is suitable when costs are non-negative.

## Heuristic search

A **heuristic** estimates how far a state is from the goal. A* combines the known cost so far, g(n), with the estimated remaining cost, h(n): f(n) = g(n) + h(n).

A useful heuristic points search toward the goal. For a grid with only horizontal and vertical moves, Manhattan distance is the number of horizontal plus vertical steps remaining.

If a heuristic never overestimates the true remaining cost, it is called admissible. Under the right conditions, A* can find an optimal path. A poor heuristic can make it little better than uninformed search; a misleading one can lose optimality.

## Games and competing goals

In a two-player zero-sum game, one player's gain is the other's loss. **Minimax** imagines that both players choose moves optimally: one player maximizes the score while the opponent minimizes it. The search alternates these roles down the game tree.

Searching every future move can be expensive. Depth limits stop the search early, and an evaluation function estimates who is ahead at the cutoff. This introduces approximation: an evaluation function is not the same as searching to the end.

## Logic and uncertainty

Rule-based systems represent explicit facts and rules. They work well when rules are known and stable, but maintenance becomes difficult when exceptions and interactions multiply.

Probabilistic reasoning represents uncertainty with probabilities. A Bayesian update combines prior belief and new evidence. In practice, the result is only as good as its assumptions and likelihood model.

Modern AI often combines explicit search with learned predictions. A learned heuristic might estimate which moves are promising, while a planner still checks legal actions.

## Compare algorithms fairly

When comparing search strategies, measure:
- whether a solution is found;
- whether it is optimal;
- number of states expanded;
- memory used;
- runtime under the same environment.

Search can be exponential: if each state branches into b possible actions and we look d steps ahead, exploring the whole tree can require roughly b raised to d states. Better representations, pruning, and heuristics reduce work but do not make every hard problem easy.

## Review questions with answers

**1. When does BFS find the shortest path?**  
When every action has equal cost and the search explores all states by increasing depth.

**2. Why can DFS fail to return the shortest route?**  
It follows a deep path before considering shorter alternatives. It may find a goal quickly, but not necessarily the shallowest one.

**3. What does A* combine?**  
The known cost already paid, g(n), and a heuristic estimate of remaining cost, h(n). The sum guides which state to examine next.

**4. What makes a heuristic admissible?**  
It never overestimates the true remaining cost. This property supports optimality for A* under standard conditions.

**5. What assumption does minimax make?**  
Both players choose moves to maximize their own outcome. If the opponent behaves differently or the game has randomness, the model should represent that.

## Practice

Implement BFS for a small grid. Keep a set of visited cells so loops do not revisit states forever. Then:
1. record the number of expanded states;
2. add a weighted cost and compare with Dijkstra;
3. add a Manhattan-distance heuristic and compare A*;
4. explain whether your heuristic can overestimate.

## Mastery check

Given a problem, identify state, actions, goal test, path cost, and whether BFS, Dijkstra, A*, or minimax fits.