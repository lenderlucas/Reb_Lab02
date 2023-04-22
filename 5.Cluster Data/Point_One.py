from sklearn.datasets import make_blobs
from sklearn.cluster import  DBSCAN
from unsupervised.kmeans import KMeans
import matplotlib.pyplot as plt
import numpy as np

# Generate toy data
X, y = make_blobs(n_samples=500, n_features=2, centers=4, cluster_std=1, center_box=(-10.0, 10.0), shuffle=True, random_state=1)

# Perform k-means clustering with 4 clusters
kmeans = KMeans._initialize_centroids(n_clusters=4)
kmeans.fit(X)
kmeans_labels = KMeans._predict(X)

# Perform DBSCAN clustering with eps=1 and min_samples=5
dbscan = DBSCAN(eps=1, min_samples=5)
dbscan_labels = dbscan.fit_predict(X)

# Plot the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c=kmeans_labels)
plt.title('K-Means Clustering')

plt.subplot(1, 2, 2)
plt.scatter(X[:, 0], X[:, 1], c=dbscan_labels)
plt.title('DBSCAN Clustering')

plt.show()
