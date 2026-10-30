"""Lab 19: compare common model families on one fixed tabular split.

This demonstration compares regularized logistic regression, an RBF SVM,
nearest neighbors, a decision tree, a random forest, and gradient boosting.
Pipelines scale features only for methods that use distances or gradients.
The data is a teaching dataset, not a basis for medical decisions.
"""

from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import (
    GradientBoostingClassifier,
    RandomForestClassifier,
)
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

dataset = load_breast_cancer()
X_train, X_test, y_train, y_test = train_test_split(
    dataset.data,
    dataset.target,
    test_size=0.25,
    stratify=dataset.target,
    random_state=13,
)

models = {
    "logistic regression": make_pipeline(
        StandardScaler(), LogisticRegression(max_iter=2000, random_state=13)
    ),
    "RBF SVM": make_pipeline(StandardScaler(), SVC(random_state=13)),
    "5-nearest neighbors": make_pipeline(
        StandardScaler(), KNeighborsClassifier(n_neighbors=5)
    ),
    "decision tree": DecisionTreeClassifier(max_depth=4, random_state=13),
    "random forest": RandomForestClassifier(
        n_estimators=150, min_samples_leaf=2, random_state=13
    ),
    "gradient boosting": GradientBoostingClassifier(random_state=13),
}

print("Held-out comparison; positive class is the dataset's class 1.")
print(f"{'model':24s} {'precision':>10s} {'recall':>8s} {'F1':>8s}")
for name, model in models.items():
    model.fit(X_train, y_train)
    predicted = model.predict(X_test)
    print(
        f"{name:24s} "
        f"{precision_score(y_test, predicted):10.3f} "
        f"{recall_score(y_test, predicted):8.3f} "
        f"{f1_score(y_test, predicted):8.3f}"
    )

# This is one split, not a universal leaderboard. Compare cross-validation,
# latency, model size, threshold costs, and error slices before choosing a model.
