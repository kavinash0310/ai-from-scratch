"""Lab 22: inspect synthetic classifier errors across two groups.

Aggregate metrics can hide differences in error rates. This demonstration
calculates true-positive and false-positive rates by group. It illustrates a
measurement step only: group metrics require context, valid labels, and care
about privacy, sample size, and the relevant fairness definition.
"""

examples = [
    # group, actual label, predicted label
    ("A", 1, 1), ("A", 1, 1), ("A", 1, 0), ("A", 1, 1),
    ("A", 0, 1), ("A", 0, 0), ("A", 0, 0), ("A", 0, 0),
    ("B", 1, 1), ("B", 1, 0), ("B", 1, 0), ("B", 1, 1),
    ("B", 0, 1), ("B", 0, 1), ("B", 0, 0), ("B", 0, 0),
]


def rates(rows):
    positives = [row for row in rows if row[1] == 1]
    negatives = [row for row in rows if row[1] == 0]
    true_positive_rate = sum(row[2] == 1 for row in positives) / len(positives)
    false_positive_rate = sum(row[2] == 1 for row in negatives) / len(negatives)
    return true_positive_rate, false_positive_rate


for group in sorted({row[0] for row in examples}):
    group_rows = [row for row in examples if row[0] == group]
    tpr, fpr = rates(group_rows)
    print(
        f"Group {group}: n={len(group_rows)}, "
        f"TPR={tpr:.2f}, FPR={fpr:.2f}"
    )

print("These rates do not, by themselves, decide whether a system is fair.")
# Discuss: Which error matters most in this context? Are labels reliable?
# Are group sizes large enough? What stakeholder input and legal context matter?
