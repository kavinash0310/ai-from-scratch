# Chapter 4 — Graph learning

A graph contains nodes and edges. Nodes might represent people, chemicals, or locations; edges represent relationships. Graphs may be directed, weighted, temporal, or have multiple node and edge types.

Graph neural networks update a node representation by aggregating information from its neighbors. Repeating this process lets a node incorporate multi-hop structure. Too many layers can oversmooth representations or spread irrelevant information.

Evaluation must prevent target or future edges from leaking into training. Removing node features may not remove sensitive relationship information.

## Questions and answers

**What is message passing?**  
A graph neural network operation where nodes gather and transform information from neighboring nodes.

**Why is an edge potentially sensitive?**  
Relationships can reveal identity, interests, health, or behavior even when node attributes are hidden.

**What is oversmoothing?**  
Repeated neighbor aggregation can make different node representations too similar.

## Practice and mastery

Represent a small citation or route graph. Identify nodes, edges, target, split, and possible leakage. Compare a graph method with a feature-only baseline.