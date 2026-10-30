"""Lab 12: compare reference and incoming feature summaries.

Data drift means incoming inputs differ from a reference period. This example
compares means and standard deviations for one synthetic feature. A detected
shift is an investigation signal, not proof that model quality has degraded.
"""

import numpy as np

rng = np.random.default_rng(11)
reference = rng.normal(loc=0.0, scale=1.0, size=1000)
incoming_stable = rng.normal(loc=0.1, scale=1.0, size=1000)
incoming_shifted = rng.normal(loc=1.0, scale=1.2, size=1000)


def summarize(name, values):
    print(
        f"{name:18s} n={len(values):4d} "
        f"mean={values.mean(): .3f} std={values.std(ddof=1):.3f}"
    )


def mean_shift_in_reference_sd(reference_values, current_values):
    scale = reference_values.std(ddof=1)
    if scale == 0:
        raise ValueError("Reference standard deviation must be nonzero")
    return abs(current_values.mean() - reference_values.mean()) / scale


summarize("reference", reference)
summarize("incoming stable", incoming_stable)
summarize("incoming shifted", incoming_shifted)
print("Stable shift in reference SD:",
      round(mean_shift_in_reference_sd(reference, incoming_stable), 3))
print("Larger shift in reference SD:",
      round(mean_shift_in_reference_sd(reference, incoming_shifted), 3))

# Real monitoring also needs schema/missingness checks, labels, privacy limits,
# alert ownership, and a response plan.
