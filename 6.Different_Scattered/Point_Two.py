import numpy as np
from sklearn import cluster, datasets, mixture

# ============
# Generate datasets. We choose the size big enough to see the scalability
# of the algorithms, but not too big to avoid too long running times
# ============
n_samples = 500
noisy_circles = datasets.make_circles(n_samples=n_samples, factor=0.5, noise=0.05)
noisy_moons = datasets.make_moons(n_samples=n_samples, noise=0.05)
blobs = datasets.make_blobs(n_samples=n_samples, random_state=8)
no_structure = np.random.rand(n_samples, 2), None

# Anisotropically distributed data
random_state = 170
X, y = datasets.make_blobs(n_samples=n_samples, random_state=random_state)
transformation = [[0.6, -0.6], [-0.4, 0.8]]
X_aniso = np.dot(X, transformation)
aniso = (X_aniso, y)
# blobs with varied variances
varied = datasets.make_blobs(
n_samples=n_samples, cluster_std=[1.0, 2.5, 0.5], random_state=random_state
)

from sklearn.cluster import KMeans, SpectralClustering, DBSCAN, KMedoids
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# create a list of datasets
datasets = [noisy_circles, noisy_moons, blobs, no_structure, aniso, varied]

# create a list of clustering algorithms
algorithms = [KMeans(n_clusters=2), KMedoids(n_clusters=2), DBSCAN(eps=0.3, min_samples=10), SpectralClustering(n_clusters=2, affinity='nearest_neighbors')]

# loop over each dataset
for data in datasets:
    # create a standard scaler object
    scaler = StandardScaler()
    # scale the data
    X = scaler.fit_transform(data[0])
    # loop over each algorithm
    for algo in algorithms:
        # fit the algorithm on the data
        algo.fit(X)
        # plot the results
        plt.figure(figsize=(4, 4))
        plt.scatter(X[:,0], X[:,1], c=algo.labels_)
        plt.title(type(algo).__name__)
