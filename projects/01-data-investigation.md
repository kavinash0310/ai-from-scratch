# Project 01 — Investigate a dataset and answer one question

## Goal

Practice programming, data types, cleaning, summary statistics, and clear communication before fitting a model. Choose a small public dataset with a clear license and record its source. Prefer a topic you understand well.

## Steps

1. Write one answerable question, such as “Which product category has the most missing records?” Avoid causal claims when the data is observational.
2. Load the file with Python or pandas. Record row/column counts, column meanings, units, source date, and license.
3. Profile types, unique values, missingness, duplicates, invalid ranges, and unexpected categories.
4. Define a cleaning rule for each issue. Keep the raw file unchanged and make cleaning reproducible in code.
5. Produce at least three summaries and two plots or text tables that directly help answer the question.
6. Write a one-page report with result, evidence, caveat, and next question.

## Deliverables

- README with question, data source/license, setup, and run steps.
- Reproducible analysis script or notebook.
- Data dictionary and cleaning decisions.
- Two or more figures/tables and a brief findings report.
- Limitations and privacy note.

## Acceptance checks

A new reader can obtain the data legally, rerun your analysis, see how missing data were handled, and distinguish a descriptive result from a causal conclusion. Do not include private or sensitive records.

## Stretch

Add a simple command-line option for input path, make a summary table for a second group, and explain whether the comparison is fair.