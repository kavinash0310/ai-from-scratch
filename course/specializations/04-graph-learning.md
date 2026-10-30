# Chapter 4 — Graph learning

A graph contains nodes and edges. Nodes might represent people, chemicals, or locations; edges represent relationships. Graphs may be directed, weighted, temporal, or have multiple node and edge types.

Graph neural networks update a node representation by aggregating information from its neighbors. Repeating this process lets a node incorporate multi-hop structure. Too many layers can oversmooth representations or spread irrelevant information.

Evaluation must prevent target or future edges from leaking into training. Removing node features may not remove sensitive relationship information.

## Deeper walkthrough: predict a missing link

Imagine four researchers represented as nodes and collaboration links as edges. The task is to estimate whether two people will collaborate next year. For a node u, a simple baseline might count shared neighbors with v. A graph model instead learns node vectors by combining information from neighbors.

To evaluate fairly, split by time: train on earlier edges and test on later edges. If future edges are used to construct neighborhoods, the test leaks its answer. Decide whether new people may appear at test time: a transductive setup knows the nodes, while an inductive setup must generalize to unseen nodes.

Graph structure itself can reveal private facts. Removing names does not remove relationship information. Choose access, retention, and aggregation rules before collecting a graph.

A useful first experiment compares shared-neighbor ranking, node-feature-only prediction, and a small graph model. If the graph model does not improve a realistic metric, extra complexity may not be justified.

## Questions and answers

**What is message passing?**  
A graph neural network operation where nodes gather and transform information from neighboring nodes.

**Why is an edge potentially sensitive?**  
Relationships can reveal identity, interests, health, or behavior even when node attributes are hidden.

**What is oversmoothing?**  
Repeated neighbor aggregation can make different node representations too similar.

## Practice and mastery

Represent a small citation or route graph. Identify nodes, edges, target, split, and possible leakage. Compare a graph method with a feature-only baseline.