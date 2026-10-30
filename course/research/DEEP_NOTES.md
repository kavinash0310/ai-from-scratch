# Research and capstones — full beginner notes

Moving from model use to AI expertise means asking precise questions, reading evidence carefully, and producing results others can inspect.

## 1. Reading research papers

A research paper makes a claim under an experimental setup. Read it in passes:
1. Abstract: identify the task and claimed contribution.
2. Introduction: understand why the problem matters.
3. Figures and method: trace inputs, transformations, outputs, and assumptions.
4. Experiments: identify datasets, baselines, metrics, and comparisons.
5. Limitations and related work: find boundary conditions and earlier ideas.
6. Equations and appendix: work through details after the big picture is clear.

A **claim** is what authors say the method achieves. **Evidence** supports some claims, but not necessarily all deployments. A **baseline** anchors comparisons. An **ablation** removes or changes a component to estimate its contribution. **Statistical significance** and practical importance differ: a tiny effect can be statistically detectable but irrelevant in practice.

Ask: Was the test set representative? Were baselines tuned fairly? Could leakage or contamination explain the result? Are compute and data budgets comparable? Can the result be reproduced? Does the paper measure the thing it claims to improve? A benchmark score is not proof of general capability.

For a paper summary, write five sentences: problem, prior limitation, proposed method, strongest evidence, most important caveat. Then explain the central figure without reading the prose.

## 2. Reproducible experiments and capstones

A **research question** is answerable and scoped. A **hypothesis** predicts an outcome and reason. An **experimental variable** is what changes; controls stay fixed. A **reproduction** tries to repeat a published result; a **replication** tests whether a finding holds in a new setting. Define success before viewing final results.

Record code version, data source/license/version, preprocessing, split, environment, random seeds, hardware, model settings, metrics, and failed runs. Use a fixed test set only for final evaluation; keep a development set for choices. Save raw predictions and error examples, not only aggregate scores.

A strong capstone starts with a problem statement and baseline. It delivers a working artifact, dataset card, model or system card, evaluation, limitations, and setup instructions. Include an ablation or error analysis that answers a question. A negative result is valuable when the experiment is sound and conclusion clear.

### Q&A and capstone checklist

**Do I need every equation before reading a paper?** No. First map the problem and method; return to the math needed to verify the central claim.
**Is rerunning the authors' code enough?** It is one reproduction step; check data, versions, metrics, and whether results match.
**What makes a project expert-level?** Clear assumptions, strong baselines, reliable evaluation, insight into errors, reproducibility, and honest limitations—not just model size.

Capstone sequence: propose one question; search prior work; define data and ethical constraints; implement a baseline; choose a leakage-safe split; run controlled experiments; analyze errors; document and present results. Use the [source guide](../SOURCES.md) for official courses and primary papers.