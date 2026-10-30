# Part 3 — Data and classical AI

## Chapter 13 — Frame a task and define examples

A project should start with the decision or action a person needs. Define one example, input available at prediction time, target or goal, baseline, success metric, and consequence of errors.

For a delivery-lateness model, one example is one shipment; the prediction is made when it is accepted; the target is whether it will be late. The actual arrival timestamp is not available at prediction time and would leak the answer.

Build a data dictionary: each column's definition, type, units, source, time, and known issues. Check missing values, duplicate records, outliers, label consistency, permission, and representation. Data reflects how it was collected, including gaps and historical decisions.

## Chapter 14 — Search and planning

A search problem is represented by:
- initial state;
- legal actions;
- transition function;
- goal test;
- path cost.

Breadth-first search finds a shortest path when every action has equal cost. Depth-first search uses memory differently but does not guarantee the shortest path. Dijkstra handles non-negative varying costs. A* prioritizes g(n)+h(n): known cost plus a heuristic estimate of remaining cost. An admissible heuristic never overestimates the true remaining cost.

A planning problem can include many objects and constraints. Constraint satisfaction represents variables, possible values, and rules. Backtracking assigns values and reverses choices that lead to conflict. Heuristics such as choosing the most constrained variable first can reduce search.

In games, minimax explores alternating decisions under an assumed optimal opponent. Alpha-beta pruning avoids evaluating branches that cannot affect the final choice.

## Chapter 15 — Logic and knowledge representation

Propositional logic describes statements that are true or false and combines them with AND, OR, and NOT. First-order logic represents objects and relations. A rule-based system uses facts and rules to derive conclusions.

Explicit knowledge is interpretable and can be reliable when rules are stable. But the number of exceptions may grow. A learned model handles patterns that are hard to write as rules, but may be less transparent. Hybrid systems use rules for constraints and models for uncertain patterns.

## Chapter 16 — Uncertainty and probabilistic reasoning

Real systems often have incomplete evidence. Bayesian networks represent variables and conditional dependencies. A hidden Markov model represents a sequence with hidden states that generate observations. These models can answer questions about likely hidden causes, but their independence assumptions must be examined.

Do not confuse a graph of statistical dependencies with a causal graph. Predictive association alone does not tell us the effect of an intervention.

## Chapter 17 — When to use classical AI

Search is useful when actions and goals can be represented and the state space is manageable. ML is useful when examples reveal patterns that are hard to specify. Rules are useful for explicit policies and constraints. A practical system may use a model to estimate cost and a search algorithm to choose a plan.

## Q&A

**Does AI always learn from data?**  
No. Search, planning, logic, and rule-based systems can perform intelligent tasks without training examples.

**When is BFS better than A*?**  
For an unweighted graph where shortest path matters and the search size is reasonable, BFS is simple and guaranteed to find the shallowest goal. A* may explore fewer states when a good heuristic is available.

**Can a model replace explicit rules?**  
Sometimes, but rules may be required for legal, safety, or business constraints. A learned score should not override a hard constraint unless the system design explicitly allows it.

**What makes a heuristic useful?**  
It guides search toward promising states while remaining cheap to compute. For optimal A*, admissibility and algorithm conditions matter; a heuristic that overestimates can forfeit optimality.

**Why distinguish association from causation?**  
Two variables can move together because of a third factor or selection effect. Intervention questions need causal assumptions and designs beyond ordinary prediction.

## Practice

1. Write a data contract for predicting late deliveries: unit, prediction time, candidate features, target, source, baseline, and failure cost.
2. Draw a small grid and implement BFS. Record the states visited and path length.
3. Add different movement costs and compare Dijkstra with BFS.
4. Create a simple scheduling CSP with variables, allowed values, and constraints.
5. Identify one association that should not be interpreted causally.

## Mastery check

You can define a valid prediction example without leakage, select an appropriate search method, and describe where rules or probabilistic reasoning fit.