"""Lab 21: record enough experiment metadata to reproduce a comparison.

A seed alone does not guarantee identical results on every system. Record
the data recipe, split, model, settings, metric, and package versions too.
This script uses synthetic data and writes a JSON result record locally.
"""

import json
import platform
from pathlib import Path

import numpy as np
import sklearn
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

seed = 21
rng = np.random.default_rng(seed)
X = rng.uniform(-2, 2, size=(300, 2))
noise = rng.normal(0, 0.5, size=300)
y = 3 * X[:, 0] - 1.5 * X[:, 1] + noise
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=seed
)

model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
record = {
    "question": "Can a linear model recover a synthetic linear relationship?",
    "data_recipe": "300 two-feature rows; y = 3*x0 - 1.5*x1 + Gaussian noise",
    "seed": seed,
    "split": "80/20 random split with random_state=21",
    "model": "scikit-learn LinearRegression",
    "metric": "mean absolute error",
    "test_mae": float(mean_absolute_error(y_test, predictions)),
    "coefficients": model.coef_.tolist(),
    "intercept": float(model.intercept_),
    "python": platform.python_version(),
    "numpy": np.__version__,
    "scikit_learn": sklearn.__version__,
    "limitation": "Synthetic data and one split do not establish real-world performance.",
}

output_path = Path("experiment-record.json")
output_path.write_text(json.dumps(record, indent=2), encoding="utf-8")
print(json.dumps(record, indent=2))
print("Saved record to:", output_path)

# Extension: repeat with multiple seeds, report the mean and spread, and keep
# a separate final test set if you make model-selection decisions.
