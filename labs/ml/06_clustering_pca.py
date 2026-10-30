"""Lab 06: scaling, K-means clustering, and PCA.

The dataset is synthetic so its structure is known. K-means groups points by
distance to centroids; PCA rotates numeric features into directions of
descending variance. High variance is not automatically task-relevant.
"""

from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

X, true_groups = make_blobs(
    n_samples=180, centers=3, n_features=4, cluster_std=1.15, random_state=7
)
X_scaled = StandardScaler().fit_transform(X)
clusterer = KMeans(n_clusters=3, n_init=10, random_state=7)
predicted_groups = clusterer.fit_predict(X_scaled)
print("Cluster centers shape:", clusterer.cluster_centers_.shape)
print("Silhouette score:", round(silhouette_score(X_scaled, predicted_groups), 3))
print("This score measures one geometric notion, not universal truth.")

pca = PCA(n_components=2, random_state=7)
projected = pca.fit_transform(X_scaled)
print("Original shape:", X_scaled.shape)
print("2-D projected shape:", projected.shape)
print("Variance retained:", round(float(pca.explained_variance_ratio_.sum()), 3))

# Learner tasks:
# 1. Try k=2 and k=4. Explain what the score can and cannot decide.
# 2. Remove scaling and see how a large-scale feature could dominate distance.
# 3. Compare clusters to true_groups only because synthetic labels are known.
