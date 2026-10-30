# AI/ML Field Reference: Core Terms, Model Families, and Efficiency

This is a broad field map for learners who want to recognize the main language and model families used in AI and machine learning. It is designed as a reference, not a claim that one page can contain every term in a changing research field. Use it to understand the landscape, choose what to study next, and ask better questions.

For the longer chapter lessons, see the [course path](README.md) and [expanded deep-study notes](DEEP_GUIDES.md). For more definitions, also use the [course glossary](GLOSSARY.md).

## 1. How to understand “efficient”

There is no universally most efficient AI model. “Efficiency” must name the resource or outcome being compared.

- **Data efficiency:** how much labeled or interaction data is needed to reach useful quality.
- **Training efficiency:** time, accelerator-hours, energy, or money required to fit or adapt the model.
- **Inference efficiency:** latency, throughput, energy, and cost when serving predictions.
- **Memory efficiency:** memory needed for parameters, optimizer state, activations, and input context.
- **Statistical efficiency:** quality and reliability of the result for the available data and assumptions.
- **Engineering efficiency:** how easily the model can be trained, debugged, deployed, monitored, and maintained.

A small linear model may be the most efficient for a transparent numeric decision. A tree ensemble may be more accurate with less data preparation on medium-sized tables. A pretrained Transformer may be efficient when language understanding is needed and a suitable model can be reused, yet expensive to train from scratch. A retrieval system may be cheaper and easier to update than fine-tuning when facts change often. Always compare complete systems on the same task, data split, hardware, quality target, and latency budget.

**Training cost and serving cost are different.** A model can be expensive to train once but cheap to serve many times, or cheap to train but slow for each request. **Quality per dollar** and **quality per second** are more useful than parameter count alone.

## 2. The field map

Artificial intelligence (AI) is the broad field of systems that perceive, reason, learn, plan, communicate, or act. Machine learning (ML) is a set of AI methods that learn patterns from data. Deep learning (DL) is ML using neural networks with multiple learned layers. Natural language processing (NLP), computer vision (CV), speech, robotics, and recommendation are application areas. Generative AI describes systems that create content; large language model (LLM) describes a family of language models, not all AI.

A system can combine several approaches:

- **Symbolic or rule-based AI:** people specify facts, rules, search, or constraints.
- **Supervised learning:** learn from examples paired with target answers.
- **Unsupervised learning:** find structure without target labels.
- **Self-supervised learning:** create training targets from the data itself, such as predicting a missing or next token.
- **Semi-supervised learning:** use a smaller labeled set together with a larger unlabeled set.
- **Reinforcement learning (RL):** learn actions from rewards and interaction with an environment.
- **Hybrid systems:** combine models with search, databases, code, rules, sensors, and human review.

These categories describe learning setups or system styles. They are not a ranking of intelligence.

## 3. Core terms used across AI and ML

### Data and problem definition

- **Example or sample:** one observation used to learn or evaluate, such as one patient, transaction, sentence, or image.
- **Dataset:** a collection of examples, usually organized into records or tensors.
- **Feature:** an input signal available to the model at the real prediction moment.
- **Target:** the outcome a model is intended to predict.
- **Label:** the known target attached to a training example.
- **Feature engineering:** choosing, cleaning, transforming, or combining inputs using domain knowledge.
- **Preprocessing:** operations such as parsing, resizing, scaling, tokenizing, or handling missing values.
- **Missing value:** an absent or unknown entry; “missing” can itself reflect a process and should not be filled blindly.
- **Data leakage:** information unavailable at real prediction time, or information that reveals the answer, reaches training or evaluation.
- **Sampling bias:** collected examples differ systematically from the people, events, or conditions where the system will be used.
- **Distribution shift:** development data and future inputs or outcomes come from different distributions.
- **Data provenance:** where data came from, how it was collected, and what permissions or transformations apply.
- **Data split:** the partition into training, validation, and test data. Use time- or group-aware splits when examples are related.
- **Training set:** data used to fit model parameters.
- **Validation set:** data used to compare models and choose settings during development.
- **Test set:** held-out data used for a final estimate after decisions are complete.
- **Baseline:** a simple method that shows how much a more complex method improves over a reasonable starting point.

### Models and learning

- **Model:** a learned or programmed mapping from inputs to outputs.
- **Algorithm:** the procedure used to fit, search, or calculate a model.
- **Parameter:** a value learned by fitting, such as a neural-network weight.
- **Hyperparameter:** a setting chosen by the practitioner, such as tree depth, number of clusters, or learning rate.
- **Training:** fitting parameters to data under a learning objective.
- **Inference:** using fitted parameters to produce a prediction without updating them.
- **Objective:** the quantity a training or decision procedure tries to minimize or maximize.
- **Loss function:** a numerical penalty used during fitting. Lower training loss does not alone prove better real-world performance.
- **Optimizer:** the procedure that updates model parameters using information such as gradients.
- **Gradient:** a vector of partial derivatives showing how the objective changes as each parameter changes.
- **Epoch:** one pass through the training examples.
- **Batch or mini-batch:** examples processed together for an update.
- **Learning rate:** a setting controlling update size during gradient-based training.
- **Generalization:** performance on new examples from the intended use environment.
- **Overfitting:** learning accidental detail in training data that does not transfer to new examples.
- **Underfitting:** failing to represent a pattern needed for the task.
- **Regularization:** a method that discourages brittle or overly complex fits.
- **Inductive bias:** assumptions a model family makes about which patterns are likely. These assumptions can help when they match the task and hurt when they do not.
- **Calibration:** whether predicted probabilities correspond to observed frequencies.
- **Threshold:** a cutoff that converts a score or probability to a decision; choose it using error costs and product requirements.
- **Cross-validation:** repeated train/validation splits used to estimate variation or compare settings. It must respect time and group structure.

### Evaluation and deployment

- **Confusion matrix:** counts of true positives, false positives, true negatives, and false negatives.
- **Accuracy:** fraction of predictions that are correct; it can hide poor performance on rare classes.
- **Precision:** among predicted positives, the fraction that are actually positive.
- **Recall or sensitivity:** among actual positives, the fraction found.
- **Specificity:** among actual negatives, the fraction correctly identified as negative.
- **F1 score:** harmonic mean of precision and recall at a selected threshold.
- **ROC-AUC:** ranking quality across classification thresholds; it does not guarantee calibrated probabilities.
- **PR-AUC:** summary of precision-recall tradeoffs; often useful when positives are rare.
- **MAE:** mean absolute prediction error, in target units.
- **MSE/RMSE:** mean squared error and its square root; large errors receive greater penalty.
- **R-squared:** a relative measure of variance explained under a chosen evaluation set; it can be negative on held-out data.
- **NDCG:** ranking metric that rewards relevant results near the top.
- **Ablation:** remove or change one system component to test its contribution.
- **Robustness:** how performance behaves under reasonable changes, noise, adversarial input, or distribution shift.
- **Fairness:** an analysis of who receives benefits and errors; no single metric settles every fairness question.
- **Explainability:** methods for understanding a model's behavior globally or for a specific prediction. An explanation can be approximate.
- **Drift monitoring:** checks for changes in input data or model outcomes after deployment.
- **MLOps:** engineering practices for data, training, versions, deployment, monitoring, and maintenance of ML systems.

## 4. Model families and where they are most useful

The table describes typical strengths, not guarantees. The most efficient choice depends on data size and quality, hardware, latency, error costs, and maintenance requirements.

| Model family | Often a strong fit for | Practical efficiency and main tradeoff |
| --- | --- | --- |
| Constant or majority baseline | First benchmark for almost any supervised task | Extremely cheap and essential for context; deliberately ignores useful features. |
| Linear regression, ridge, lasso | Numeric prediction with approximately additive effects; interpretable baselines | Fast to train and serve, compact, and often data-efficient; cannot model complex interactions unless features encode them. |
| Logistic regression and generalized linear models | Classification, risk scores, count/rate outcomes | Fast, compact, and comparatively easy to calibrate or inspect; linear decision structure may be too simple. |
| Generalized additive models (GAMs) | Interpretable nonlinear effects on tabular data | Often a useful compromise between a straight line and a black box; interactions need explicit handling. |
| Naive Bayes | Fast text classification and small-data baselines | Very cheap and often strong with sparse word counts; independence assumptions are simplified and probabilities may be poorly calibrated. |
| Decision tree | Small interpretable decision rules | Cheap inference and visual explanation; a single tree can be unstable and overfit. |
| Random forest / Extra Trees | General tabular classification and regression | Handles nonlinear feature interactions with little scaling; parallel tree training is practical, but forests can consume memory and be larger than linear models. |
| Gradient-boosted trees: XGBoost, LightGBM, CatBoost | High-quality tabular prediction, including mixed nonlinear patterns | Frequently excellent on medium-sized tables and can handle feature interactions; tuning and serving are more involved, and extreme sparse/high-dimensional data may need other methods. |
| Support-vector machine (SVM) | Smaller or medium datasets with a clear margin or useful kernel | Strong in some high-dimensional settings; kernel SVM training can scale poorly with example count and probability calibration is separate. |
| k-nearest neighbors (k-NN) | Similarity lookup, small datasets, simple local baselines | Almost no fitting cost; prediction can be slow and storage-heavy because examples are retained. Feature scaling and distance choice matter. |
| K-means | Fast grouping when clusters are roughly compact and number of groups is known | Scales well and is simple; assumes distance-based, roughly spherical groups and requires a chosen cluster count. |
| DBSCAN / HDBSCAN | Density-based clusters, irregular shapes, and outlier discovery | Can discover noise and non-spherical structure without fixing k in the same way; sensitive to density settings and distance computation. |
| Hierarchical clustering | Small/medium datasets where nested grouping is valuable | Produces a useful tree of groupings; pairwise distances can become costly as the dataset grows. |
| Gaussian mixture model (GMM) | Soft clustering or density modeling with ellipsoidal components | Gives probabilistic membership; assumptions about component shape and number affect results. |
| Principal component analysis (PCA) | Compressing correlated numeric features and visualizing dominant variation | Fast linear reduction; preserves variance, not necessarily task-relevant information. |
| Isolation Forest | Anomaly detection in mixed numeric tabular data | Practical for large data and does not need labels; “unusual” is not necessarily fraudulent or harmful. |
| Multilayer perceptron (MLP) | Flexible function approximation on vectors and tabular data | Highly parallelizable on accelerators; often needs more tuning/data than tree boosting on ordinary medium-sized tables. |
| Convolutional neural network (CNN), including ResNet | Images, local spatial patterns, and some audio/time-frequency inputs | Convolutions reuse local filters and exploit spatial structure; image pipelines and sufficient training data or pretraining matter. |
| Vision Transformer (ViT) | Image understanding when large-scale pretraining or data is available | Attention offers flexible global interactions and hardware parallelism; patch attention and data/compute demands can be high. |
| RNN, LSTM, GRU | Sequential streams and compact stateful sequence processing | Can process streaming data with small recurrent state; token-by-token computation limits parallel training and long-range dependencies can be difficult. |
| Transformer encoder, such as BERT-style models | Text classification, extraction, ranking, and contextual representations | Bidirectional context is effective for understanding tasks; full attention has sequence-length memory/compute cost and the encoder does not generate freely by default. |
| Decoder-only Transformer / LLM | Next-token generation, instruction following, code and dialogue | One pretrained model can serve many language tasks; training from scratch is extremely costly, inference memory/latency grows with model and context, and factual reliability must be evaluated. |
| Encoder-decoder Transformer, such as T5-style models | Input-to-output tasks such as translation, rewriting, and summarization | Explicitly separates input encoding and output generation; requires appropriate task data and still has neural serving costs. |
| Bi-encoder embeddings | Fast semantic search and candidate retrieval | Encode documents once, then search vectors cheaply; nearest semantic text may not be actually relevant, so measure retrieval recall. |
| Cross-encoder reranker | Reordering a small set of retrieved passages or search results | Jointly reads query and candidate for more precise relevance; slower because each pair is scored separately, so use after a fast candidate stage. |
| Autoencoder / variational autoencoder (VAE) | Compression, representation learning, reconstruction, and some generation | Encoder-decoder structure is useful for compact latent codes; reconstruction quality is not the same as task utility or faithful generation. |
| Generative adversarial network (GAN) | Fast image generation after training and certain translation tasks | Generator inference can be one forward pass; training can be unstable and coverage/mode collapse must be checked. |
| Diffusion model | High-quality image/audio generation and iterative editing | Strong sample quality and flexible conditioning in many settings; iterative denoising can make generation slower without acceleration methods. |
| Graph neural network (GCN, GraphSAGE, GAT) | Node/edge prediction and data where relationships carry signal | Uses graph neighborhoods and features; neighborhood sampling and graph changes affect memory, scalability, and generalization. |
| Matrix factorization | Recommendation from user-item interaction matrices | Compact factors can rank many user-item pairs efficiently; cold-start entities and exposure bias require side information or other methods. |
| Two-tower retrieval model | Large-scale candidate generation in recommendation/search | User and item vectors can be computed separately and indexed; a separate ranker is usually needed for fine-grained interactions. |
| ARIMA / exponential smoothing | Classical time-series forecasting with trend/seasonality assumptions | Fast, inspectable, and strong baselines for many series; complex nonlinear patterns and many related series may require richer models. |
| Temporal CNN / sequence Transformer | Many related series, complex covariates, long contexts | Can share representations across series; needs careful chronological evaluation and enough representative data. |
| Tabular Q-learning / SARSA | Small discrete reinforcement-learning problems | Can be simple and interpretable for compact state/action spaces; table size grows quickly and interaction data may be expensive. |
| Deep Q-network (DQN) | Discrete-action control from high-dimensional observations | Neural function approximation handles large observations; typically sample-hungry and not a general solution for continuous actions. |
| PPO | General-purpose on-policy control and simulator benchmarks | Conceptually straightforward and often practical to implement; on-policy samples are discarded, so interaction can be costly. |
| SAC / TD3 | Continuous-control problems in simulation | Off-policy replay can reuse experience and support continuous actions; tuning, reward design, and safe transfer remain difficult. |
| Search, planning, and constraint solvers | Route finding, scheduling, puzzles, and rules with known structure | Can give exact or explainable solutions when states/rules are explicit; search may grow combinatorially and needs a valid formulation. |

### Important comparisons

**Trees versus neural networks on tables:** tree ensembles are an important first comparison for medium-sized tabular data; neural networks are not automatically superior because they are deeper. The result depends on dataset, preprocessing, tuning budget, and evaluation. See the [tabular benchmark study](https://arxiv.org/abs/2207.08815).

**Retrieval versus fine-tuning:** retrieval supplies changing external evidence at answer time; fine-tuning changes model behavior using examples. Use retrieval when answers must cite or reflect changing documents. Use fine-tuning when a stable behavior or format must be learned and evaluation shows prompting is insufficient. They can be combined.

**Model versus system:** a retrieval-augmented generation (RAG) pipeline, an agent, or a recommender is not necessarily one model. It is a system made from models plus data, indexes, code, policies, user interfaces, and monitoring.

## 5. Model efficiency by workload

| Workload | Useful first candidates | What often saves resources | What to measure |
| --- | --- | --- | --- |
| Small labeled table | Majority/mean baseline, logistic/linear model, shallow tree | Keep feature processing simple; compare compact interpretable models before ensembles. | Validation metric, calibration, training time, and decision threshold. |
| Medium-sized tabular data | Gradient-boosted trees, random forest, linear baseline | Use a strong baseline and modest tuning; avoid neural architectures without evidence. | Split quality, feature leakage, CPU time, model size, subgroup errors. |
| Very large sparse text | TF-IDF with linear classifier; pretrained language model if task needs context | Sparse linear models can be cheap and effective; use a pretrained encoder rather than train one from scratch. | F1/PR-AUC, memory, throughput, quality by language/domain. |
| Images with limited labels | Pretrained CNN or ViT with transfer learning | Reuse pretrained features; freeze layers first, then fine-tune only if validation gains justify it. | Per-class recall, latency, memory, data leakage by subject/site. |
| Search over many documents | Bi-encoder retrieval followed by optional reranking | Precompute document vectors; rerank only a small candidate set. | Recall@k, NDCG, answer support, index size, latency. |
| Knowledge assistant over changing files | Hybrid keyword/vector retrieval plus a generator | Update the index without retraining the language model; include metadata and access filters. | Evidence recall, groundedness, citation support, abstention, end-to-end cost. |
| Recommendation | Popularity baseline, matrix factorization, two-tower retrieval plus ranker | Separate cheap candidate generation from expensive ranking; cache stable item vectors. | NDCG/Recall@k, diversity, coverage, exposure bias, online outcomes. |
| Forecasting | Seasonal-naive, moving average, ETS/ARIMA | Backtest by time; use a simple per-series model when relationships are simple. | Error by horizon, bias, peak performance, compute per series. |
| Robotics/control | Classical controller/planner before learned policy; simulator policy after | Keep safety constraints outside unconstrained model outputs; reuse simulation carefully. | Safety violations, sample cost, sim-to-real gap, recovery performance. |

## 6. Core keywords experts should use precisely

These distinctions prevent common communication mistakes:

- **AI vs ML vs deep learning:** umbrella field vs learning from data vs neural networks with multiple layers.
- **Model vs algorithm vs system:** fitted mapping vs fitting procedure vs complete application and operations.
- **Parameter vs hyperparameter:** learned internal value vs developer-selected setting.
- **Training vs inference:** adjust parameters from examples vs use fixed parameters to calculate outputs.
- **Loss vs metric:** optimization signal vs report card. They can differ; a lower loss is not always a better product.
- **Probability vs score:** calibrated chance under a model vs a ranking number that may not represent probability.
- **Correlation vs causation:** variables moving together vs evidence that changing one produces a change in the other.
- **Feature importance vs causal effect:** predictive usefulness under a method vs impact of intervening on a variable.
- **Accuracy vs quality:** one metric vs whether the complete behavior is useful, safe, and appropriate.
- **Embedding vs token ID:** learned vector representation vs integer lookup index.
- **Attention vs explanation:** learned weighted information mixing vs a complete reason for an output. Attention weights alone do not establish causality.
- **Hallucination vs uncertainty:** unsupported generated claim vs a model's uncertainty; fluent confidence can be misleading.
- **RAG vs fine-tuning:** add evidence at inference vs change learned parameters through further training.
- **Prompting vs tool use:** instruct a model vs let an application execute a validated function.
- **Open weights vs open source:** weights available under a license vs all data, code, and training process available; licenses vary.
- **Benchmark vs deployment:** standardized test conditions vs real users, inputs, costs, and consequences.
- **Drift vs failure:** data distribution changed vs a demonstrated unacceptable outcome; drift is a signal to investigate.
- **Explainability vs interpretability:** explanation produced by a method vs a model whose mechanism is directly understandable; definitions vary across literature.
- **Robustness vs security:** resilience to variation or perturbation vs resistance to malicious access or manipulation; systems may need both.
- **Sample efficiency vs compute efficiency:** how much experience/data is needed vs how much runtime or hardware is consumed.
- **Throughput vs latency:** requests handled per time interval vs delay for one request.
- **Precision vs recall:** how many predicted positives are correct vs how many real positives are found.
- **Bias-variance tradeoff:** overly simple models miss pattern; overly flexible models may react to sample noise. This is one lens, not a complete diagnosis.
- **Causal inference:** estimating effects of interventions under assumptions; prediction alone does not identify causal impact.
- **Representation learning:** learning useful transformed features rather than hand-coding every feature.
- **Self-supervised learning:** deriving training targets from unlabelled data structure, such as the next token.
- **Transfer learning:** reusing representations or weights learned on a source task for a related target task.
- **Fine-tuning:** continue model training on a narrower dataset or objective.
- **Quantization:** reducing numeric precision to lower model memory or speed computation, with possible quality changes.
- **Distillation:** train a smaller model to imitate outputs or internal behavior of a larger teacher model.
- **Pruning:** remove or zero components to reduce computation or model size, with possible quality tradeoffs.
- **Mixture of Experts (MoE):** architecture with multiple expert subnetworks and a routing mechanism; only some experts may activate per input, while total stored parameters can remain large.
- **Foundation model:** broadly pretrained model intended for adaptation to many tasks; the term does not guarantee quality, safety, openness, or suitability.
- **Multimodal model:** model that accepts or produces multiple data types, such as text and images.
- **Agent:** model-driven application loop that observes, chooses actions or tools, and continues under defined limits; the agent is the application behavior, not merely a model name.
- **Human-in-the-loop:** people review or make decisions at selected points; it works only when reviewers have context, authority, and time.
- **Reproducibility:** ability to rerun the documented process with comparable artifacts and results.
- **Reproducibility seed:** controls some random-number choices but does not guarantee identical results across hardware/software.
- **Confidence interval:** a range from a statistical procedure representing uncertainty under assumptions; it is not a guarantee about one future case.
- **Ablation study:** controlled removal or modification of components to test which parts matter.
- **Data card/model card:** documentation of data or model intended uses, construction, evaluation, and limitations.
- **Human evaluation rubric:** explicit criteria used by reviewers to judge qualities automatic scores miss.
- **Red teaming:** structured attempts to find failures, misuse, vulnerabilities, or unsafe behavior before and during deployment.
- **Least privilege:** give each user, tool, or service only the access required for its task.
- **Privacy-preserving learning:** methods that reduce exposure of sensitive data; protections have assumptions and can involve utility or computation tradeoffs.
- **Differential privacy:** a formal privacy framework that bounds how much one record can influence released results, under stated parameters and implementation assumptions.
- **Federated learning:** training across data held at multiple clients without centralizing raw examples; update leakage, communication, and client bias remain concerns.
- **Online learning:** update a model incrementally as new examples arrive; requires safeguards against feedback loops and corrupted data.
- **Continual learning:** learn across a stream of tasks while trying to retain useful prior capabilities; catastrophic forgetting is a central challenge.
- **Out-of-distribution (OOD):** input unlike the data or conditions a model was developed on; a model may be unreliable even when input syntax is valid.
- **Abstention:** intentionally defer or say insufficient evidence when the system cannot meet a confidence or evidence requirement.
- **Selective prediction:** make predictions only on cases meeting a chosen confidence/risk policy and defer the rest.
- **Model registry:** versioned record of model artifacts, configurations, evaluations, and deployment status.
- **Canary deployment:** send a limited share of production traffic to a new model version before broader release.
- **Rollback:** return to a prior known version after a deployment problem.

## 7. A practical way to choose a model

1. **Write the task in one sentence.** Name the input, prediction moment, output, and person who uses it.
2. **Choose the right learning setup.** Do you have labels, only raw data, interaction/reward, known rules, or external documents?
3. **Check data validity.** Inspect permissions, representativeness, missingness, label quality, duplicates, and leakage.
4. **Build a baseline.** Start with a rule, constant, linear model, simple seasonal forecast, or popularity ranking.
5. **Choose 2–3 suitable families.** Pick models whose inductive biases fit the data; do not compare every algorithm blindly.
6. **Create a realistic split before tuning.** Group related people/items together or train on earlier time and test on later time.
7. **Choose metrics from error costs.** Decide what false positives, false negatives, misses, latency, and abstention cost.
8. **Measure efficiency in the intended setting.** Include data preparation, tuning, training, serving, memory, and maintenance.
9. **Inspect examples and subgroups.** Aggregate scores can conceal systematic failure.
10. **Deploy only with monitoring and rollback.** Track the version, data, service health, outcomes, and incident owner.

### Fast model-selection questions

- Tabular records and not much data? Compare regularized linear models with boosted trees.
- Images? Start with a pretrained CNN or vision Transformer and test transfer learning.
- Text categories? Compare a TF-IDF linear baseline with a pretrained encoder.
- Search across documents? Use keyword and embedding retrieval, then optionally rerank.
- Need current source-grounded answers? Consider a retrieval system; test whether evidence is retrieved and cited.
- Need to generate media? Select the generation family for that modality and plan evaluation for quality, provenance, and safety.
- Need actions in a changing environment? First check whether rules, optimization, or a classical controller solve it; use RL only when interaction and reward assumptions are justified.
- Need an expert answer about “best model”? Ask: best on which dataset, metric, error cost, hardware, time budget, and deployment constraints?

## 8. Frequently asked questions

**Which AI model is best overall?** None. A good model is the one that meets the task's quality, cost, latency, privacy, and maintenance constraints on representative data.

**Should I always start with the newest LLM?** No. If a small classifier, search index, deterministic program, or simple baseline solves the task, it may be cheaper, faster, easier to audit, and more reliable.

**Why can boosting beat a deep network on a table?** Tree splits can naturally handle nonlinear thresholds and mixed feature scales with modest data. Deep networks have different assumptions and may need more data, tuning, or architecture design. Benchmark rather than relying on reputation.

**Is the most accurate model the most efficient?** Not necessarily. Compare quality at the required operating point, including latency, memory, energy, false-error costs, and ongoing maintenance.

**How do I become expert in these terms?** Do not memorize definitions alone. Implement a small method, compare a baseline, read the primary paper, reproduce a result, inspect errors, and explain assumptions.

## 9. Further reading: official documentation and primary research

- [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html) — supervised learning, clustering, preprocessing, model selection, and metrics.
- [scikit-learn model evaluation guide](https://scikit-learn.org/stable/modules/model_evaluation.html) — scoring, classification/regression metrics, and baseline checks.
- [scikit-learn clustering guide](https://scikit-learn.org/stable/modules/clustering.html) — algorithm assumptions and relative use cases.
- [Random Forests, Breiman (2001)](https://doi.org/10.1023/A:1010933404324) — tree ensembles and the role of tree strength and correlation.
- [XGBoost: A Scalable Tree Boosting System](https://arxiv.org/abs/1603.02754) — scalable, regularized gradient-boosted trees.
- [Why do tree-based models still outperform deep learning on tabular data?](https://arxiv.org/abs/2207.08815) — benchmark study emphasizing inductive bias and medium-sized tables.
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) — original Transformer architecture.
- [BERT](https://arxiv.org/abs/1810.04805) — bidirectional Transformer encoder pretraining.
- [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385) — residual connections in deep vision networks.
- [Denoising Diffusion Probabilistic Models](https://arxiv.org/abs/2006.11239) — foundational diffusion model formulation.
- [LoRA](https://arxiv.org/abs/2106.09685) — low-rank adaptation for reducing trainable parameters.
- [GraphSAGE](https://arxiv.org/abs/1706.02216) — inductive representation learning over graph neighborhoods.
- [Deep Q-Network](https://www.nature.com/articles/nature14236) and [PPO](https://arxiv.org/abs/1707.06347) — representative deep RL methods.
- [Matrix Factorization Techniques for Recommender Systems](https://doi.org/10.1109/MC.2009.263) — latent-factor recommendation methods.

Results in these papers are tied to their tasks, datasets, and setups. Read limitations and later comparisons before treating a historical result as a present-day ranking.