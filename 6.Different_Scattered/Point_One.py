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


import matplotlib.pyplot as plt

# noisy circles
plt.figure(figsize=(4, 4))
plt.scatter(noisy_circles[0][:,0], noisy_circles[0][:,1])
plt.title("Noisy Circles")

# noisy moons
plt.figure(figsize=(4, 4))
plt.scatter(noisy_moons[0][:,0], noisy_moons[0][:,1])
plt.title("Noisy Moons")

# blobs
plt.figure(figsize=(4, 4))
plt.scatter(blobs[0][:,0], blobs[0][:,1])
plt.title("Blobs")

# no structure
plt.figure(figsize=(4, 4))
plt.scatter(no_structure[0][:,0], no_structure[0][:,1])
plt.title("No Structure")

# anisotropic
plt.figure(figsize=(4, 4))
plt.scatter(X_aniso[:,0], X_aniso[:,1])
plt.title("Anisotropic")

# varied variances
plt.figure(figsize=(4, 4))
plt.scatter(varied[0][:,0], varied[0][:,1])
plt.title("Varied Variances")
