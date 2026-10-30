# Shared project rubric: 100 points

Use this rubric for every project. The score rewards a sound process and clear evidence, not just the final model metric.

| Area | Points | Full-credit evidence |
| --- | ---: | --- |
| Problem definition and scope | 10 | Names user, input, prediction/action moment, output, and non-goals |
| Data quality and rights | 10 | Documents source, license/permission, rows, labels, missingness, and known bias |
| Baseline and method choice | 15 | Establishes a simple baseline and justifies a suitable method |
| Correct implementation | 15 | Code runs from documented setup; preprocessing and training match the stated task |
| Evaluation design | 15 | Uses a realistic split, suitable metrics, and avoids leakage or test-set tuning |
| Error analysis and limitations | 15 | Inspects cases/slices, explains important failure modes, and avoids overclaiming |
| Reproducibility and engineering | 10 | Records versions/seeds/configuration; provides run instructions and saved outputs |
| Communication and responsible use | 10 | Clear README, visual or tabular results, privacy/safety notes, and intended-use boundary |
| **Total** | **100** | |

## Score interpretation

- **90–100:** strong, reviewable project; assumptions and failures are explicit.
- **75–89:** useful project with a few gaps that are fixable.
- **60–74:** demonstrates the main idea but evaluation or reproducibility is weak.
- **Below 60:** revisit scope, baseline, labels, or measurement before adding a larger model.

A very high score does not mean the model is ready for a high-impact use. It means the project artifact meets this educational rubric.