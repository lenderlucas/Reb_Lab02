import numpy as np

def k_medoids(X, n_clusters, max_iter=100):
    # Initialize medoids randomly
    medoids_idx = np.random.choice(X.shape[0], n_clusters, replace=False)
    medoids = X[medoids_idx]
    
    for i in range(max_iter):
        # Calculate distance matrix
        D = np.sum((X[:, np.newaxis, :] - medoids)**2, axis=2)
        
        # Assign each point to the closest medoid
        labels = np.argmin(D, axis=1)
        
        # Update medoids
        for j in range(n_clusters):
            cluster_points = X[labels == j]
            if len(cluster_points) > 0:
                new_medoid = cluster_points[np.argmin(np.sum((cluster_points[:, np.newaxis, :] - cluster_points)**2, axis=2))]
                medoids[j] = new_medoid
                
    return labels, medoids