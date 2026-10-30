"""Lab 09: a classical NLP text-classification baseline.

TF-IDF maps text to sparse weighted token features. Logistic regression learns
a decision boundary over those features. This tiny toy dataset demonstrates
a pipeline only; it cannot estimate real-world quality.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline

texts = [
    "excellent story and warm characters",
    "wonderful acting and a moving ending",
    "I enjoyed this clever and funny film",
    "beautiful music and a strong performance",
    "a delightful film with excellent pacing",
    "the story was touching and well written",
    "boring plot and very weak acting",
    "the film was dull and much too long",
    "poor writing made this story confusing",
    "a disappointing and forgettable movie",
    "the ending was tedious and predictable",
    "weak characters and unpleasant dialogue",
    "good acting but the plot was boring",
    "beautiful scenes but a dull story",
    "funny moments in an otherwise weak film",
    "moving story with some predictable scenes",
]
labels = [1] * 6 + [0] * 6 + [1, 0, 0, 1]

X_train, X_test, y_train, y_test = train_test_split(
    texts, labels, test_size=0.25, random_state=4, stratify=labels
)
model = make_pipeline(
    TfidfVectorizer(ngram_range=(1, 2), min_df=1),
    LogisticRegression(max_iter=1000, random_state=4),
)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(classification_report(y_test, predictions, target_names=["negative", "positive"]))

vectorizer = model.named_steps["tfidfvectorizer"]
print("Vocabulary size:", len(vectorizer.vocabulary_))
for text, truth, prediction in zip(X_test, y_test, predictions):
    print(f"true={truth} predicted={prediction} text={text}")

# Real NLP evaluation should prevent near-duplicate, author, time, or source
# leakage and should include the relevant language varieties and domains.
