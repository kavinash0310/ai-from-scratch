# Hands-on AI/ML labs

These labs turn course notes into runnable experiments. Small examples make calculations visible; they are not production models or proof that a method is safe for real decisions.

## Setup

Install Python and the shared numerical and machine-learning libraries:

    python -m pip install numpy scikit-learn

Python, math, and search labs use only the standard library. Later labs use NumPy and scikit-learn. No GPU, paid API, or downloaded dataset is required. Run a script from the repository root, for example:

    python labs/math/02_gradient_descent.py

Read the script docstring first. If an import fails, install the named dependency into the same Python environment used to run the script. Use a virtual environment for course work.

## Lab map

| Lab | Subject | What you will learn |
| --- | --- | --- |
| [01 — Python fundamentals](python/01_values_functions.py) | Python | Values, loops, dictionaries, functions, input/output |
| [02 — Gradient descent](math/02_gradient_descent.py) | Math | Compute gradients and fit a line by repeated updates |
| [03 — Search and planning](ai/03_search.py) | Classical AI | Model a maze as states/actions; compare BFS and A* |
| [04 — ML workflow](ml/04_model_evaluation.py) | ML | Baseline, stratified split, pipeline, metrics, error tradeoffs |
| [05 — Logistic regression from scratch](ml/05_logistic_from_scratch.py) | ML/math | Sigmoid, cross-entropy, gradients, decision threshold |
| [06 — Clustering and PCA](ml/06_clustering_pca.py) | ML | Unsupervised grouping, scaling, dimensionality reduction |
| [07 — Backpropagation](deep-learning/07_backprop_xor.py) | Deep learning | Train a tiny network and inspect chain-rule updates |
| [08 — Convolution](computer-vision/08_convolution.py) | Vision | Apply a filter and interpret a feature map |
| [09 — Text baseline](nlp/09_tfidf_classifier.py) | NLP | Token counts, TF-IDF, sparse features, classification |
| [10 — Attention](llm/10_attention.py) | LLMs | Calculate scaled attention and a causal mask |
| [11 — Retrieval evaluation](generative-ai/11_retrieval_evaluation.py) | GenAI | Rank evidence and calculate Recall@k and reciprocal rank |
| [12 — Drift monitoring](engineering/12_drift_monitoring.py) | Engineering | Compare data summaries; interpret drift as a signal |
| [13 — Time-series baseline](specializations/13_time_series.py) | Forecasting | Chronological holdout and seasonal-naive evaluation |
| [14 — Matrix factorization](specializations/14_matrix_factorization.py) | Recommendation | Fit user/item factors on observed ratings |
| [15 — Graph message passing](specializations/15_graph_message_passing.py) | Graph learning | Aggregate neighboring node features |
| [16 — Q-learning](specializations/16_q_learning_grid.py) | Reinforcement learning | Learn a policy from state/action/reward interaction |
| [17 — Kalman filter](specializations/17_kalman_filter.py) | Robotics | Combine a prior estimate with noisy sensor readings |
| [18 — SQL basics](python/18_sql_basics.py) | Data | Tables, joins, aggregation, parameterized queries |
| [19 — Model-family comparison](ml/19_model_family_comparison.py) | ML | Compare linear, distance, tree, and ensemble models |
| [20 — Bigram language model](llm/20_bigram_language_model.py) | NLP/LLMs | Estimate and sample next-word probabilities |
| [21 — Reproducible experiment](research/21_reproducible_experiment.py) | Research | Save configuration, versions, split, and metrics |
| [22 — Subgroup metrics](engineering/22_subgroup_metrics.py) | Responsible AI | Inspect synthetic error rates across groups |

## How to study a lab

1. Read its matching chapter and expanded notes first.
2. Write what you expect the output or shapes to be before running it.
3. Run the script and trace one example through the code.
4. Change one value or assumption, rerun, and explain the difference.
5. Write a short report: purpose, method, output, limitation, next experiment.
6. Reimplement the central calculation without a library call where the lab asks for “from scratch.”

These are teaching demonstrations. Tiny data makes code understandable but performance estimates unreliable. Do not use demo metrics for consequential decisions. Continue with the [project ladder](../projects/README.md), [mastery checks](../assessments/MASTERY_CHECKS.md), and [100-point scorecard](../assessments/MASTERY_SCORECARD.md).