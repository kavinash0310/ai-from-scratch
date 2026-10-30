# Lab guide: expected behavior and how to interpret it

This page helps you check your understanding after running each script. It describes the behavior to look for, not a grade for model quality. Small and synthetic examples are deliberately simple; do not generalize their scores to real users or data.

## Python, math, and classical AI

### 01 — Python values and functions

You should see three item costs, an order total of **USD 13.25**, and an empty order total of zero. Trace how each dictionary goes into the function and how the returned tuple is later printed. If a task changes the data, the function should still calculate from the input rows instead of relying on hidden global variables.

### 02 — Gradient descent

The learned weight should move close to 2, the bias close to 1, and mean squared error close to zero. Each update uses the average gradient across all five examples. If increasing the learning rate makes loss jump or grow, the step may be too large. A low training error on these five points does not prove performance on future data.

### 03 — Search and planning

BFS and A* should both find a shortest route through the maze because every move costs one. They may expand different numbers of states; that depends on tie order and heuristic. BFS uses no estimate of the goal distance. A* prioritizes cost so far plus Manhattan distance. If you add different movement costs, plain BFS is no longer a least-cost algorithm.

## Supervised and unsupervised ML

### 04 — Model evaluation

The script prints accuracy, precision, recall, and F1 for a majority baseline, scaled logistic regression, and random forest using the same held-out rows. The baseline can look deceptively strong because one class is more common. Check the target names and remember the positive label in this dataset is class 1. The exercise is about a fair workflow, not diagnosing people.

### 05 — Logistic regression from scratch

Training cross-entropy should decrease and the two example points should receive different probabilities. The learned weights define a linear score; sigmoid maps it to a value from zero to one. A probability is not automatically calibrated, and a 0.5 cutoff is only a default decision rule.

### 06 — Clustering and PCA

K-means returns three centroids and one cluster ID per row. The silhouette score is one measure of distance-based separation; it does not tell you that the groups have real-world meaning. PCA should turn 180 rows of four features into 180 rows of two coordinates. The retained-variance fraction does not measure how much useful target information was retained.

### 19 — Model-family comparison

You should see one row of precision, recall, and F1 per model family. No row is a universal winner: the numbers depend on the chosen split, dataset, positive class, hyperparameters, and metric. The next step is cross-validation on training data, error inspection, and comparison of serving cost and threshold behavior.

## Deep learning, vision, and language

### 07 — Backpropagation on XOR

The four predicted probabilities should separate the two equal-input cases from the two different-input cases. Thresholding at 0.5 should usually produce XOR labels 0, 1, 1, 0 for this fixed initialization. If not, inspect the loss, gradient signs, shapes, and learning rate. The tiny training table only demonstrates that a hidden layer can make a nonlinear boundary.

### 08 — Convolution

The input is 5 by 5; the 3 by 3 kernel with no padding produces a 3 by 3 output. Strong values appear where the pixel intensity changes from dark to bright across rows. Flipping the kernel reverses the response sign. A feature-map response is not by itself an object detector.

### 09 — TF-IDF classifier

A classification report and several held-out text examples are printed. The vocabulary is sparse: each sentence uses only some of its possible terms. Because the dataset is tiny and deliberately repetitive, the report has high uncertainty; do not compare it to a production language model score.

### 10 — Attention

The attention matrix has three query rows and three key columns. Each row sums to one, while entries above the diagonal are zero because future positions are masked. The output has the same number of positions as the input. Change a query/key vector and observe that the mixing weights change.

### 20 — Bigram language model

The script lists likely next words after “models” and generates a short continuation from transition counts. It only conditions on the immediately previous word, so it may repeat phrases or stop early. The fixed random seed and sorted vocabulary make the sample reproducible within the same implementation. This frequency model is a teaching baseline, not a neural LLM.

## Retrieval, data, and engineering

### 11 — Retrieval evaluation

For each query, the script prints ranked document IDs and the rank of the expected evidence. Recall@3 and mean reciprocal rank fall between zero and one; higher is better for this toy query set. Lexical TF-IDF can miss a semantically related passage with different wording. These scores evaluate retrieval, not generated answer support.

### 12 — Drift monitoring

The stable incoming sample should have a mean and spread similar to the reference; the shifted sample should show a larger difference. The normalized mean-shift value is a simple alert signal. A shift alone does not prove the model became less accurate: check real outcomes and investigate collection changes.

### 18 — SQL basics

The join and aggregation should report Asha with two orders totaling 35, Noor with zero orders, and Ravi with one order totaling 40. Noor remains because the query uses a left join. The parameterized lookup returns Asha's two rows without joining user text into SQL syntax.

### 21 — Reproducible experiment

The script prints and saves a JSON record in the current directory. The fitted coefficients should be near 3 and -1.5 because those values generated the synthetic target; random noise and the particular split create small differences. The record includes software versions and the split. A seed helps reproduction but cannot guarantee bit-identical results in every environment.

### 22 — Subgroup metrics

For the fixed synthetic table, group A has TPR 0.75 and FPR 0.25; group B has TPR 0.50 and FPR 0.50. These are deliberately different. The calculation does not decide which fairness definition is appropriate or whether the group labels and outcomes are valid.

## Specialization labs

### 13 — Time-series baseline

The train portion contains 48 earlier timestamps and the test portion the following 12. The seasonal-naive forecast reuses the preceding week's value in a rolling one-step setup. Compare its MAE with the training-mean baseline. If changing the experiment to a fixed 12-step forecast, do not feed actual held-out values back into later predictions.

### 14 — Matrix factorization

The script reports train and held-out interaction counts, a held-out rating RMSE, and a ranking for one user. User and item vectors are learned only from training ratings. The small synthetic table is not a recommendation benchmark and cannot model exposure bias or new-user cold start.

### 15 — Graph message passing

Each node's new vector combines its own features with the mean of neighbor features. The output retains six nodes and two feature dimensions. Remove or corrupt an edge and inspect how messages change. This is one aggregation step, not a trained graph neural network.

### 16 — Q-learning

After repeated episodes, the greedy route should reach the goal while avoiding walls. If it loops, increase training episodes or inspect exploration and reward updates. The action-value table works because this world is tiny and discrete. Reward design can encourage unintended shortcuts in more complex tasks.

### 17 — Kalman filter

The filtered position estimates should be smoother than the raw sensor values, and in this fixed low-motion example the filter RMSE should usually be lower. If the robot actually moves quickly, an almost-constant-position model will lag. The process and sensor variances encode assumptions about how much the world and measurement can change.

## If the output differs

1. Confirm you are in the repository root and using the same Python environment where dependencies were installed.
2. Read the traceback from its last line upward; fix the first relevant cause.
3. Compare the script contents with the repository version before changing code.
4. Check array shapes, train/test membership, random seed, and data types.
5. Change one thing at a time and record the expected and observed results.

For the next step after a lab, complete a [graded project](../projects/README.md) and save your report in your learning log.