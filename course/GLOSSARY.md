# AI course glossary

This glossary defines the recurring vocabulary used across the course in beginner-friendly language. A word can have a more specialized meaning in a particular paper or library; the chapter linked beside it gives the context used here.

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

## How to use this glossary

When a term is unfamiliar, open the corresponding subject folder and read the matching chapter plus its [expanded notes](DEEP_GUIDES.md). Definitions are a starting point: make a tiny example, use the concept, and explain its limits in your own words.