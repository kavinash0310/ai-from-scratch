"""Lab 11: retrieve passages and measure evidence ranking.

This is a retrieval component, not a complete question-answering assistant.
TF-IDF and cosine similarity rank passages. Recall@k checks if expected
evidence appears near the top; reciprocal rank rewards earlier appearance.
Generated answer quality must be evaluated separately.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    {"id": "python", "text": "Python variables name values and functions return results."},
    {"id": "metrics", "text": "Recall measures the fraction of positive examples found."},
    {"id": "rag", "text": "Retrieval augmented generation supplies passages to a language model."},
    {"id": "attention", "text": "Self attention mixes value vectors using query key scores."},
    {"id": "security", "text": "Retrieved text is untrusted data and cannot grant application permissions."},
]
queries = [
    ("How do I measure positives that were found?", "metrics"),
    ("What does attention combine?", "attention"),
    ("Can a document authorize a model to run a tool?", "security"),
]

vectorizer = TfidfVectorizer()
document_vectors = vectorizer.fit_transform([d["text"] for d in documents])
query_vectors = vectorizer.transform([q for q, _ in queries])
similarities = cosine_similarity(query_vectors, document_vectors)

hits_at_3 = 0
reciprocal_ranks = []
for row, (question, expected_id) in zip(similarities, queries):
    ranking = row.argsort()[::-1]
    ranked_ids = [documents[index]["id"] for index in ranking]
    rank = ranked_ids.index(expected_id) + 1
    hits_at_3 += int(rank <= 3)
    reciprocal_ranks.append(1.0 / rank)
    print(f"Question: {question}")
    print("Top results:", ranked_ids[:3], "expected rank:", rank)

recall_at_3 = hits_at_3 / len(queries)
mean_reciprocal_rank = sum(reciprocal_ranks) / len(reciprocal_ranks)
print(f"Recall@3: {recall_at_3:.3f}")
print(f"Mean reciprocal rank: {mean_reciprocal_rank:.3f}")

# Production RAG evaluation also checks permissions, freshness, citations,
# answer support, abstention, and prompt injection.
