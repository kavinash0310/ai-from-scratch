"""Lab 04: compare a baseline and models with a leakage-aware workflow.

Uses a bundled teaching dataset from scikit-learn. This is an educational
benchmark only, not a medical tool. Compare a majority baseline, logistic
regression, and a random forest on the same held-out examples. The pipeline
fits feature scaling using training data only.
"""

from sklearn.datasets import load_breast_cancer
from sklearn.dummy import DummyClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

data = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.25, random_state=42, stratify=data.target
)
models = {
    "majority baseline": DummyClassifier(strategy="most_frequent"),
    "scaled logistic regression": make_pipeline(
        StandardScaler(), LogisticRegression(max_iter=2000, random_state=42)
    ),
    "random forest": RandomForestClassifier(
        n_estimators=200, random_state=42, min_samples_leaf=2
    ),
}

for name, model in models.items():
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    print(
        f"{name:28s} "
        f"accuracy={accuracy_score(y_test, predictions):.3f} "
        f"precision={precision_score(y_test, predictions):.3f} "
        f"recall={recall_score(y_test, predictions):.3f} "
        f"f1={f1_score(y_test, predictions):.3f}"
    )

print("\nTarget names:", list(data.target_names))
print("Do not select a model from accuracy alone: inspect errors and costs.")

# Learner tasks:
# 1. Compare stability by cross-validating on training data.
# 2. Inspect false positives and false negatives separately.
# 3. Change the decision threshold using predict_proba and explain the tradeoff.
# 4. Explain why the test set should not guide repeated tuning.
