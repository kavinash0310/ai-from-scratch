# The AI From Scratch Roadmap

A guided sequence from zero coding experience to building, evaluating, and sharing practical AI projects.

For the expanded subject-by-subject curriculum, follow the [full course index](course/README.md) and study through its linked subject folders. The timeline below is the core beginner-to-builder route; advanced specialization and expertise take sustained practice beyond that schedule.

**Pace:** about 7–9 months at 6–8 focused hours per week. Weeks are estimates. Move on when you can do the checkpoint, not when a calendar says so. If you already know a stage, use its checkpoint to decide whether to review or continue.

## The complete route

| Stage | Suggested time | Main outcome |
| --- | --- | --- |
| 0. Get ready | 1 week | A working study setup and a clear goal |
| 1. Python foundations | 4–5 weeks | Write, debug, and explain small programs |
| 2. Math and data | 3–4 weeks | Explore data and understand the math used by models |
| 3. AI foundations | 2–3 weeks | Implement search and reason about decisions |
| 4. Machine learning | 5–6 weeks | Train and honestly evaluate traditional models |
| 5. Deep learning | 5–6 weeks | Train a small neural network with PyTorch |
| 6. Choose a specialty | 3–5 weeks | Build depth in one AI area |
| 7. Generative AI and LLMs | 4–5 weeks | Build and evaluate a grounded LLM application |
| 8. Ship a capstone | 3–4 weeks | Present a useful, tested, documented project |

---

## Stage 0 — Get ready

**Subject folder:** [Foundations](course/foundations/README.md).

### Learn
- What AI, machine learning, deep learning, and generative AI mean.
- How to use a code editor or browser notebook.
- How files, folders, and the terminal fit together.
- How to save versions of your work with Git and GitHub.

### Do
- Create a folder for this learning path.
- Write one sentence describing what you want to make with AI.
- Set a realistic weekly study time.
- Open a Python notebook and run a one-line program.
- Learn the basics of commits and repositories with [GitHub Learn](RESOURCES.md#tools-and-workflow).

### Checkpoint
You can run a small Python program, find its output, and save your work.

---

## Stage 1 — Python foundations

**Subject folder:** [Python and software foundations](course/python/README.md).

**Suggested time:** 4–5 weeks

### Learn
- Values, variables, strings, numbers, and Boolean logic.
- Conditions, loops, lists, dictionaries, and sets.
- Functions, parameters, return values, and scope.
- Reading and writing text and CSV files.
- Imports, packages, exceptions, debugging, and basic tests.
- How to break a problem into smaller steps.

### Practice projects
1. Number guessing game or quiz.
2. Expense tracker that reads and writes a CSV file.
3. Text analyzer that counts words and finds common terms.

### Checkpoint
Build one small program from a blank file, use functions to organize it, handle at least one error case, and explain how the program works.

**Main study resource:** [Harvard CS50’s Introduction to Programming with Python](RESOURCES.md#python).

---

## Stage 2 — Math and data

**Subject folder:** [Mathematics](course/mathematics/README.md).

**Suggested time:** 3–4 weeks. Keep practicing these ideas throughout the roadmap.

### Learn
- Algebra, functions, and reading graphs.
- Mean, median, spread, and outliers.
- Probability, samples, and why a result can be uncertain.
- Vectors and matrices as ways to represent many numbers.
- Derivatives as a measure of how a result changes.
- Python tools for arrays, tables, and plots.

### Practice project
Choose a small public dataset. Ask three questions, clean the data, make a few plots, and write what the data does and does not show.

### Checkpoint
You can describe a dataset, calculate a simple summary, read a chart, and explain why correlation alone does not prove cause.

**Study the concepts when you need them:** [Math and data resources](RESOURCES.md#math-and-data).

---

## Stage 3 — AI foundations

**Subject folder:** [Classical AI](course/ai/README.md).

**Suggested time:** 2–3 weeks

### Learn
- How to turn a real-world task into a search or decision problem.
- State spaces, actions, costs, and goals.
- Breadth-first search, depth-first search, and A* search.
- How uncertainty and an opponent change a decision.
- Why a good problem definition matters as much as the algorithm.

### Practice projects
1. Find a route through a grid with breadth-first search.
2. Add weighted steps and implement A*.
3. Optional: make a small game-playing agent using minimax.

### Checkpoint
You can explain how your program represents a problem, why it chooses a path or move, and where it may fail.

---

## Stage 4 — Machine learning

**Subject folder:** [Machine learning](course/ml/README.md).

**Suggested time:** 5–6 weeks

### Learn
- Features, labels, examples, and training data.
- Regression, classification, and clustering.
- Training, validation, and test sets.
- Baselines, metrics, overfitting, and regularization.
- Data cleaning, preprocessing, and feature engineering.
- Cross-validation, pipelines, and data leakage.
- Why the right metric depends on the problem and its costs.

### Practice project
Choose a tabular dataset. Define a prediction goal, make a simple baseline, train at least two models, compare suitable metrics, and inspect errors.

### Checkpoint
Your project keeps test data out of training and preprocessing, compares against a baseline, explains the selected metric, and records known limitations.

**Main study resources:** [Google’s Machine Learning Crash Course](RESOURCES.md#machine-learning) and the [scikit-learn getting started guide](RESOURCES.md#machine-learning).

---

## Stage 5 — Deep learning

**Subject folders:** [Deep learning](course/deep-learning/README.md) and [computer vision](course/computer-vision/README.md).

**Suggested time:** 5–6 weeks

### Learn
- Tensors, layers, weights, and activation functions.
- Loss functions, gradient descent, and backpropagation intuition.
- Training versus inference.
- Batches, learning rates, epochs, and validation.
- How to read learning curves and recognize overfitting.
- The basic PyTorch workflow: data, model, loss, optimizer, training loop.

### Practice projects
1. Train a small neural network on a simple tabular or digit dataset.
2. Make an image classifier using a small, clearly documented dataset.
3. Compare its results to a simple baseline.

### Checkpoint
You can describe what the model receives, what it predicts, how its loss changes during training, and how you measured its performance.

**Main study resource:** [PyTorch Tutorials](RESOURCES.md#deep-learning).

---

## Stage 6 — Choose a specialty

**Subject folder:** [Specializations](course/specializations/README.md).

**Suggested time:** 3–5 weeks

Choose one area for a first focused project. You can explore others later.

| Area | Learn | Starter project |
| --- | --- | --- |
| Computer vision | Image preprocessing, convolutional networks, transfer learning | Classify a small set of objects |
| Natural language processing | Tokenization, text representations, sequence tasks | Classify the topic or sentiment of short texts |
| Recommendation systems | User-item data, ranking, feedback, cold start | Recommend a small set of books or songs |
| Time series | Time order, forecasting baselines, changing patterns | Forecast a simple public time series |
| Reinforcement learning | Agent, environment, reward, policy, exploration | Teach an agent a tiny grid-world task |

### Checkpoint
You can explain why the chosen model fits the data, compare it with a simple baseline, and discuss who could be affected by its errors.

---

## Stage 7 — Generative AI and large language models

**Subject folders:** [NLP](course/nlp/README.md), [LLMs](course/llm/README.md), and [generative AI](course/generative-ai/README.md).

**Suggested time:** 4–5 weeks

### Learn
- Tokens, embeddings, attention, and the transformer idea.
- The difference between using a pretrained model and training one.
- Prompting, context limits, and structured outputs.
- Retrieval-augmented generation (RAG): chunking, embeddings, retrieval, and citations.
- How to build a small evaluation set and check answer quality.
- Privacy, source attribution, hallucinations, and prompt injection basics.

### Practice project
Build a question-answering tool over a small collection of documents. Show which sources support each answer. Test it with questions that are answerable, unanswerable, and ambiguous.

### Checkpoint
You can identify what came from the language model and what came from retrieved sources, measure answer quality on example questions, and describe when the app should say “I don’t know.”

**Main study resource:** [Hugging Face LLM Course](RESOURCES.md#generative-ai-and-llms).

---

## Stage 8 — Ship a capstone responsibly

**Subject folders:** [Engineering and responsible AI](course/engineering/README.md) and [research](course/research/README.md).

**Suggested time:** 3–4 weeks

### Build
Pick a real, small problem you care about and make a usable demo.

Your project should include:
- A clear user and problem statement.
- A lawful, documented data source and a simple baseline.
- An evaluation plan with examples the model has not seen during training.
- A useful interface or clear instructions to run it.
- A README with setup, results, limitations, and next steps.
- Privacy and safety notes appropriate to the project.

### Final checkpoint
A new person can understand the problem, run or view the demo, see how you evaluated it, and understand where it should not be trusted.

Use the [project template](templates/project-template.md) and update [your progress tracker](PROGRESS.md).

---

## After the roadmap

The next step depends on your goal:

- **AI application developer:** APIs, web development, databases, retrieval, evaluation, and deployment.
- **Machine learning engineer:** data pipelines, experiment tracking, deployment, monitoring, and systems.
- **ML researcher:** deeper linear algebra, probability, optimization, papers, and research reproduction.
- **AI for another field:** combine the foundations with domain knowledge and carefully chosen projects.

You do not need to master every branch before choosing. Build the foundation, finish a few projects, then go deeper where your interests point.