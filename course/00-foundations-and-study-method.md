# Part 0 — Foundations and how to study AI

## Chapter 1 — What AI includes

Artificial intelligence is a research and engineering field concerned with systems that perceive, reason, plan, learn, communicate, or act. It is not one model and does not require every system to imitate a person.

A maze-solving program can use search and never learn. A spam filter can learn from labeled examples. A modern language assistant can combine a pretrained language model, search, tools, safety rules, and a user interface. These are all AI-related systems, but they solve different problems.

- **Symbolic or rule-based AI** represents facts, rules, goals, and constraints explicitly.
- **Machine learning** fits patterns from examples.
- **Deep learning** uses layered neural networks to learn representations.
- **Natural language processing (NLP)** studies computational treatment of human language.
- **Large language models (LLMs)** are a subset of language models that use large-scale learned parameters and data.
- **Generative AI** creates new content by sampling or decoding from a learned model.

The useful question is not “Which AI is newest?” It is “What decision or output does the user need, what evidence is available, and what failure is acceptable?”

## Chapter 2 — How to learn without getting lost

AI contains many subfields. Beginners often jump between tools, prompts, libraries, and news. That creates familiarity without skill. Use this loop:

    concept → small example → code or calculation → test → explain → improve

For example, do not merely watch a neural-network video. Make a one-neuron calculation by hand, run a tiny training example, change its data, then explain why the output changed.

Keep three notebooks or files:
1. **Glossary:** term, plain-language meaning, and one example.
2. **Experiment log:** question, change, result, and interpretation.
3. **Mistake log:** error, how you found it, and how to avoid it.

A useful weekly session alternates learning and doing. Schedule small sessions you can repeat. When stuck, reduce the problem: use three examples instead of thousands, print intermediate values, or draw the data flow.

## The study ladder

1. **Recognize:** identify a concept in an example.
2. **Explain:** describe its purpose and assumptions.
3. **Use:** apply a library or method correctly.
4. **Implement:** recreate a small version.
5. **Evaluate:** design a fair test and inspect errors.
6. **Adapt:** choose among alternatives for a new task.
7. **Research:** formulate questions, reproduce results, and communicate uncertainty.

The course aims to take you through level 6 on core topics and introduce level 7. Advanced expertise comes from repeating this ladder in a specialty.

## A practical definition of progress

You are learning when you can answer:
- What problem is this method solving?
- What goes in and what comes out?
- What assumptions does it make?
- What is a simple baseline?
- How could the result be wrong?
- How will I check it?

If you can only repeat the name of a model, return to the example.

## Common beginner traps

- Starting with LLM APIs before learning data, Python, or evaluation.
- Collecting many courses and finishing none.
- Copying code that you cannot explain.
- Treating a benchmark score as proof of product usefulness.
- Believing advanced mathematics must be mastered before any coding.
- Believing advanced AI can be learned without mathematics or careful experiments.

## Q&A

**Is AI the same as ChatGPT?**  
No. ChatGPT is an AI product involving language models and software. AI also includes search, classical planning, computer vision, recommendations, robotics, and other fields.

**Do I need a degree or advanced math to begin?**  
No. Start with arithmetic, basic algebra, and Python. Add probability, vectors, matrices, derivatives, and optimization when the course uses them.

**Should I learn prompts first?**  
You can explore them, but prompting alone does not teach how models are trained, evaluated, grounded, or deployed. Treat it as one practical skill within the larger course.

**What does “from scratch” mean in this course?**  
You will understand and implement small algorithms and models. You will use libraries and pretrained models for realistic projects. Reproducing a tiny model is educational; training a large modern foundation model is not a prerequisite.

**How do I know when to move on?**  
When you can pass the mastery check and complete the exercise with only occasional reference help. You do not need perfect recall; you need the ability to reason and find trustworthy documentation.