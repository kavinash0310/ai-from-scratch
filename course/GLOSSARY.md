# AI course glossary

This glossary defines the recurring vocabulary used across the course in beginner-friendly language. A word can have a more specialized meaning in a particular paper or library; the chapter linked beside it gives the context used here.

For a model-by-model guide to where common approaches are useful and how to compare their efficiency, see the [AI/ML Field Reference](AI-ML-FIELD-REFERENCE.md).

## Learning and software foundations

- **Algorithm:** a finite, ordered procedure for solving a problem.
- **API:** a defined interface that lets one program request information or actions from another.
- **Argument:** the actual value supplied when calling a function; a parameter is the named input in its definition.
- **Baseline:** a simple comparison method that establishes whether a more complex approach adds value.
- **Branch (Git):** a movable line of project history used to develop changes separately.
- **Bug:** a defect that makes software behave incorrectly or unsafely.
- **Commit:** a recorded snapshot of tracked file changes in Git.
- **Complexity:** how computation or memory use grows as input size increases.
- **Dependency:** an external package, service, or tool that a project needs.
- **Function:** a named calculation or action that can receive inputs and return a result.
- **Git:** a version-control system that records project history; GitHub hosts repositories and collaboration features.
- **Interpreter:** a program that reads source code and executes it.
- **Library:** reusable code that a program can call.
- **Parameter (function):** a named input in a function definition.
- **Repository:** project files and their version history.
- **Return value:** the result a function sends back to its caller.
- **Scope:** the part of a program where a name can be accessed.
- **SQL:** a language for querying and changing data in relational tables.
- **Test:** a check that compares actual behavior with expected behavior.
- **Type:** a category of value that determines which operations are valid, such as integer, text, or Boolean.
- **Variable:** a name that refers to a value in a program.
- **Virtual environment:** an isolated Python package setup for one project.

## Data and machine learning

- **Batch:** a group of examples processed together for one training update or prediction request.
- **Calibration:** agreement between predicted probabilities and observed frequencies; among cases assigned 0.8, about 80% should be positive for a calibrated classifier.
- **Classification:** predicting a category, often with probabilities for each category.
- **Confusion matrix:** a table counting correct and incorrect positive/negative predictions.
- **Data leakage:** information reaches model fitting or evaluation that would not be legitimately available at prediction time, or gives away the answer.
- **Dataset:** a collection of examples, often with features and sometimes labels.
- **Distribution shift:** a change between the data or conditions used for development and those encountered later.
- **Epoch:** one pass through all examples in a training dataset.
- **Feature:** an input signal used by a model to make a prediction.
- **Generalization:** how well a learned method works on new, relevant examples.
- **Hyperparameter:** a setting chosen by the developer, such as tree depth or learning rate, rather than learned directly as a model weight.
- **Label:** the target answer attached to an example, such as “spam” or a numeric house price.
- **Loss:** a number measuring how poorly a model's prediction matches a training target under a chosen objective.
- **Metric:** a defined measurement used to summarize model behavior; a metric can be correct but still fail to capture user impact.
- **Overfitting:** learning details of training examples that do not carry to new cases.
- **Precision:** among examples predicted positive, the fraction that truly are positive.
- **Recall:** among all truly positive examples, the fraction found by the model.
- **Regression (ML):** predicting a numeric quantity.
- **Regularization:** a training or modeling choice that discourages overly complex fits.
- **Sampling bias:** a mismatch between collected examples and the population or use case we care about.
- **Target:** the outcome the model is trained or evaluated to predict.
- **Test set:** held-out data reserved for a final performance estimate after choices are complete.
- **Training set:** data used to fit model parameters.
- **Underfitting:** using a model or training process too limited to capture the useful pattern.
- **Validation set:** data used during development to compare approaches and choose settings, without fitting final parameters on it.
- **Threshold:** a cutoff that turns a score or probability into a decision; it should reflect error costs and product needs.

## Mathematics and deep learning

- **Activation function:** a transformation applied in a neural-network layer, often adding non-linearity.
- **Backpropagation:** an efficient procedure that applies the chain rule to compute how parameters affect loss.
- **Bias (neural network):** a learned offset added to a weighted input; in fairness, bias also means systematic disadvantage, a different use of the word.
- **Chain rule:** a calculus rule for differentiating a function made by composing other functions.
- **Derivative:** the local rate of change of one quantity with respect to another.
- **Dot product:** multiply corresponding entries in two equal-length vectors and add the results.
- **Embedding:** a learned dense vector representing an item such as a word, image, or document.
- **Gradient:** a vector of partial derivatives showing how a scalar objective changes with each parameter.
- **Inference:** using a fitted model to produce outputs without changing its learned parameters.
- **Layer:** one stage in a neural network that transforms its input numbers.
- **Learning rate:** a training setting controlling the size of parameter updates.
- **Logit:** an unnormalized score produced before converting scores to probabilities.
- **Matrix:** a rectangular grid of numbers, commonly used for data or linear transformations.
- **Model:** a fitted or programmed mapping from inputs to outputs.
- **Neural network:** a composition of parameterized numeric operations trained to represent useful mappings.
- **Optimization:** searching for parameter values that minimize or maximize a defined objective.
- **Parameter (model):** an internal numeric value, such as a weight, that training can adjust.
- **Probability:** a number from 0 to 1 representing likelihood under a specified model or experiment.
- **Scalar:** one number.
- **Softmax:** a function that converts a list of scores into non-negative values that sum to 1.
- **Tensor:** a multidimensional array of numbers.
- **Vector:** an ordered list of numbers.
- **Weight:** a learned number that controls how strongly one input contributes to a calculation.

## NLP, Transformers, and LLMs

- **Attention:** a computation that forms weighted combinations of information from sequence positions.
- **Autoregressive model:** a model that predicts the next item using items already produced or observed.
- **Causal mask:** a rule that blocks a token position from using future tokens during next-token prediction.
- **Context window:** the maximum token sequence a model call can process under its implementation; it does not guarantee perfect recall.
- **Cross-entropy:** a loss commonly used to compare predicted probabilities with the correct class or next token.
- **Decoder:** a model component that produces an output sequence; decoder-only language models commonly predict next tokens.
- **Key (attention):** a learned vector compared with a query to calculate how relevant a position is.
- **Language model:** a model that assigns probabilities to sequences of language tokens or predicts missing/next tokens.
- **Multi-head attention:** several attention computations run in parallel with different learned projections.
- **NLP:** natural language processing, the field of methods for analyzing, transforming, or generating human language.
- **Pretraining:** broad initial training on large data before or alongside adapting a model to a specific use.
- **Query (attention):** a learned vector representing what one sequence position is seeking from other positions.
- **Tokenizer:** software that splits input into model units and maps those units to integer IDs.
- **Token:** a unit processed by a language model; it may be a word, word piece, punctuation, or byte-like unit.
- **Token ID:** an integer indexing a token in a tokenizer's vocabulary; the number itself is not a meaningful measurement.
- **Transformer:** a neural-network architecture whose core sequence operation uses attention.
- **Value (attention):** a learned vector containing information that is mixed according to attention weights.
- **Vocabulary (tokenizer):** the set of token units and IDs that a tokenizer can represent.

## Generative AI systems

- **Agent:** an application loop in which a model selects steps or tools, observes results, and continues under defined limits.
- **Chunk:** one piece made by splitting a longer document for storage or retrieval.
- **Decoding:** the method used to select the next token from model scores.
- **Embedding search:** retrieving items whose vectors are near the query vector under a similarity measure.
- **Grounding:** tying an answer to explicit evidence or trusted system state.
- **Hallucination:** a plausible-sounding generated claim that is unsupported or false.
- **Multimodal:** able to process or produce more than one kind of data, such as text, image, audio, or video.
- **Prompt:** the instructions and context supplied to a generative model.
- **Prompt injection:** untrusted content attempts to override instructions or make a model misuse tools or data.
- **RAG:** retrieval-augmented generation; retrieving external passages and giving them to a model as evidence while answering.
- **Reranker:** a model or scoring stage that reorders retrieved candidates for relevance.
- **Temperature:** a decoding setting that changes how concentrated or varied token sampling is; it does not make answers more factual.
- **Tool call:** a structured request for an application to run a function and return its result.
- **Top-p sampling:** a decoding method that samples from a set of likely tokens whose cumulative probability reaches a chosen value.
- **Vector database:** a system that stores and searches numeric vectors, often alongside source metadata.

## Specializations and engineering

- **Concept drift:** a change over time in the relationship between model inputs and the target.
- **Data drift:** a change in the distribution or structure of incoming model inputs.
- **Discount factor:** in reinforcement learning, a value controlling how much future rewards count relative to immediate rewards.
- **Graph:** a structure containing nodes (entities) and edges (relationships).
- **Policy (reinforcement learning):** a rule or model mapping states to actions.
- **Reward:** numeric feedback used to express the goal in reinforcement learning.
- **Seasonality:** a repeating time-based pattern, such as a weekly or yearly cycle.
- **Time series:** measurements ordered by time.
- **Transfer learning:** reusing a model or representation learned on one task to help with a related task.
- **Canary release:** deploying a new version to a small portion of traffic before a broader rollout.
- **Least privilege:** giving a service or user only the permissions needed for its task.
- **Monitoring:** ongoing checks of service health, data, model behavior, and real-world outcomes.
- **Privacy:** protecting information about people through limits on collection, access, use, and retention.
- **Rollback:** returning a service to a prior version when a release causes problems.

## Classical AI and search vocabulary

- **Action:** an available choice that changes the current state of a problem.
- **A* search:** a search algorithm that ranks paths using cost-so-far plus a heuristic estimate of remaining cost.
- **Backtracking:** a search process that undoes an assignment when it makes the remaining problem impossible.
- **Bayesian network:** a graph that represents random variables and conditional dependencies.
- **Breadth-first search:** a strategy that explores all states at one depth before states at the next depth.
- **Constraint:** a condition that limits which combinations of values are allowed.
- **Constraint satisfaction problem (CSP):** a problem defined by variables, possible values, and constraints.
- **Depth-first search:** a strategy that follows one branch deeply before returning to explore another.
- **Heuristic:** a rule or estimate that helps guide a search toward promising options.
- **Inference rule:** a formal pattern for deriving a conclusion from known facts.
- **Knowledge base:** stored facts and rules from which a reasoning system may derive conclusions.
- **Minimax:** a game-search method that selects a move assuming the opponent chooses the strongest response.
- **State:** a representation of the current situation in a search or decision problem.
- **Transition model:** a description of how an action changes one state into another.
- **Uniform-cost search:** a search strategy that expands the least-cost path found so far.

## Statistics, ML models, and metrics

- **Ablation:** an experiment that removes or changes one system component to estimate its contribution.
- **Area under the ROC curve (ROC-AUC):** a summary of how well a classifier ranks positive examples above negative ones across thresholds.
- **Area under the precision-recall curve (PR-AUC):** a summary of precision and recall across thresholds; often informative for rare positives.
- **Cross-validation:** repeated train/validation splits used to estimate model performance or compare settings.
- **F1 score:** the harmonic mean of precision and recall at a chosen threshold.
- **Feature scaling:** transforming numeric features to comparable ranges; it is important for many distance-based and gradient-based methods.
- **Imputation:** replacing or representing missing values using a defined procedure.
- **Mean absolute error (MAE):** average absolute difference between numeric predictions and targets.
- **Mean squared error (MSE):** average squared prediction error; large misses receive stronger penalty.
- **Root mean squared error (RMSE):** square root of mean squared error, expressed in the target's units.
- **Stratified split:** a data split designed to preserve chosen class proportions across partitions.
- **K-means:** a clustering algorithm that assigns examples to a chosen number of centroids to reduce within-cluster squared distance.
- **Principal component analysis (PCA):** a linear method that finds directions of high variance and can reduce dimensionality.
- **Random forest:** an ensemble that averages predictions from multiple randomized decision trees.
- **Gradient boosting:** an ensemble process that adds models in sequence to improve errors made so far.
- **Naive Bayes:** a probabilistic classifier that uses a simplifying conditional-independence assumption.
- **Decision tree:** a model that predicts by following feature-based splits through a tree structure.
- **Nearest-neighbor method:** a method that predicts from examples closest to a query under a chosen distance or similarity.
- **Confounder:** a variable related to multiple quantities that can create a misleading association.
- **Confidence interval:** a range produced by a statistical procedure to represent uncertainty in an estimate under stated assumptions.

## Neural networks and optimization

- **Adam:** an adaptive optimizer that uses running estimates of gradients and squared gradients.
- **Backpropagation:** an algorithm for computing gradients through a network by applying the chain rule.
- **Dropout:** a regularization method that randomly removes some activations during training.
- **Gradient descent:** an optimization method that changes parameters opposite the gradient to reduce an objective.
- **Momentum:** an optimizer technique that smooths updates using a running direction from earlier gradients.
- **ReLU:** the rectified linear activation, which returns zero for negative inputs and the input for positive values.
- **Sigmoid:** a function that maps a real-valued score to a value between zero and one.
- **Stochastic gradient descent (SGD):** gradient descent using a subset or mini-batch of training examples for each update.
- **Weight decay:** a regularization technique that discourages excessively large weights.
- **Fine-tuning:** continuing training of a pretrained model on a more specific dataset or task.
- **Feature extraction:** using a pretrained model to produce representations while keeping most of its learned weights fixed.

## NLP and Transformer vocabulary

- **Bag-of-words representation:** a document representation that records term counts or presence while ignoring word order.
- **Corpus:** a collection of text documents used for analysis or training.
- **Lemmatization:** mapping a word form to a dictionary base form using linguistic information.
- **Stemming:** reducing words with a heuristic process that strips endings; the result may not be a real word.
- **TF-IDF:** a text weighting scheme that gives more importance to terms frequent in one document but less common across a collection.
- **Recurrent neural network (RNN):** a neural model that processes a sequence while carrying a hidden state from one step to the next.
- **LSTM and GRU:** gated recurrent architectures designed to control what information is kept or updated across sequence steps.
- **Named-entity recognition (NER):** locating and classifying spans such as person, organization, location, or date names.
- **Perplexity:** a score derived from a language model's token prediction loss; useful for predictive comparison but not a complete measure of answer quality.
- **Positional encoding:** information added to a representation so a Transformer can use token order.
- **Query, key, and value:** learned attention vectors; query-key comparisons make weights and values supply the content being mixed.
- **Residual connection:** a path that adds a sublayer's input to its output, helping information and gradients travel through deep networks.
- **Layer normalization:** a transformation that normalizes activation values within a feature vector to stabilize computation.
- **Next-token prediction:** training a language model to assign probability to the next token given earlier tokens.
- **Beam search:** a decoding method that keeps several high-scoring partial sequences while generating.
- **LoRA:** a parameter-efficient adaptation method that represents weight updates with smaller low-rank matrices.
- **Quantization:** storing or computing model values at reduced numerical precision, potentially trading quality for memory or speed.

## Generative AI and retrieval vocabulary

- **Chunking:** dividing longer documents into smaller passages for indexing and retrieval.
- **Few-shot prompting:** including a small number of input/output examples in a prompt to demonstrate the desired pattern.
- **Grounded answer:** an answer whose claims are supported by supplied evidence or trusted system state.
- **Recall at k:** the fraction of test queries for which relevant evidence appears among the first k retrieved results.
- **Schema validation:** checking that generated structured data has required fields and correct types before use.
- **System prompt:** application-provided instructions that define a model's role or behavior for a conversation.
- **Diffusion model:** a generative model trained to reverse a gradual corruption process, often starting generation from noise.
- **Latent representation:** a compressed internal representation used for computation or generation.
- **Tool permission:** the explicitly granted ability for an application to invoke a defined function or access a resource.
- **Untrusted input:** user or retrieved content that must be treated as data rather than trusted instructions.

## Vision and specialized systems

- **Channel (image):** one plane of image values, such as red, green, or blue.
- **Convolution kernel:** a small learned array applied across local image neighborhoods.
- **Feature map:** the grid of responses produced by a convolution or other spatial operation.
- **Intersection over Union (IoU):** overlap area divided by combined area, commonly used to compare predicted and true boxes or masks.
- **Mean Average Precision (mAP):** an average of precision-recall performance across classes or thresholds; exact benchmark definitions vary.
- **Object detection:** predicting locations and categories of objects, commonly with bounding boxes.
- **Pooling:** reducing the spatial size of feature maps by summarizing local neighborhoods.
- **Semantic segmentation:** assigning a category to every image pixel.
- **Stride:** how far a convolution kernel moves between neighboring calculations.
- **Padding:** added border values used by a convolution to control output size and boundary behavior.
- **Cold start:** the difficulty of recommending for a new user or item with little interaction history.
- **Collaborative filtering:** recommendation from patterns in user-item interactions.
- **Exposure bias (recommendation):** observed interactions depend on which items were shown, so unobserved does not mean disliked.
- **Normalized Discounted Cumulative Gain (NDCG):** a ranking metric that rewards relevant items appearing near the top of a result list.
- **Forecast horizon:** how far into the future a time-series prediction is intended to reach.
- **Rolling-origin evaluation:** repeatedly training on past data and evaluating on the next future period.
- **Edge (graph):** a relationship connecting two nodes.
- **Node (graph):** an entity represented in a graph.
- **Message passing:** updating a graph node by combining information from neighboring nodes.
- **Policy (reinforcement learning):** a strategy that chooses actions from states.
- **Return (reinforcement learning):** accumulated reward over an episode or future time period.
- **Sim-to-real gap:** differences between a simulator and physical hardware that make simulated performance fail to transfer perfectly.
- **Control:** choosing actuator commands so a physical system follows a desired behavior.
- **Localization:** estimating a robot's position and orientation from sensor observations.

## How to use this glossary

When a term is unfamiliar, open the corresponding subject folder and read the matching chapter plus its [expanded notes](DEEP_GUIDES.md). Definitions are a starting point: make a tiny example, use the concept, and explain its limits in your own words.