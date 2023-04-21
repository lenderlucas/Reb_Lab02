from sklearn.cluster import KMeans
from sklearn_extra.cluster import KMedoids
from sklearn.metrics import silhouette_score
from sklearn.metrics import silhouette_samples
import matplotlib as plt
import matplotlib.cm as cm

# Iterate over values of K
for n_clusters in range(2, 6):
    # Run k-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=1)
    cluster_labels = kmeans.fit_predict(X)

    # Compute the silhouette score and plot silhouette plots
    silhouette_avg = silhouette_score(X, cluster_labels)
    print(f"For n_clusters = {n_clusters}, the average silhouette_score is: {silhouette_avg:.2f}")

    # Compute the silhouette scores for each sample
    sample_silhouette_values = silhouette_samples(X, cluster_labels)

    # Plot the silhouette plots
    fig, ax = plt.subplots(1, 1)
    fig.set_size_inches(7, 4)
    ax.set_xlim([-0.1, 1])
    ax.set_ylim([0, len(X) + (n_clusters + 1) * 10])
    y_lower = 10
    for i in range(n_clusters):
        # Aggregate the silhouette scores for samples belonging to cluster i, and sort them
        ith_cluster_silhouette_values = sample_silhouette_values[cluster_labels == i]
        ith_cluster_silhouette_values.sort()

        size_cluster_i = ith_cluster_silhouette_values.shape[0]
        y_upper = y_lower + size_cluster_i

        # Choose a color for the cluster
        color = cm.nipy_spectral(float(i) / n_clusters)

        # Fill in the silhouette plot
        ax.fill_betweenx(np.arange(y_lower, y_upper),
                          0, ith_cluster_silhouette_values,
                          facecolor=color, edgecolor=color, alpha=0.7)

        # Label the silhouette plots with their cluster number at the middle
        ax.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

        # Compute the new y_lower for next plot
        y_lower = y_upper + 10

    # Label the silhouette plot
    ax.set_title(f"Silhouette plot for {n_clusters} clusters")
    ax.set_xlabel("Silhouette coefficient values")
    ax.set_ylabel("Cluster labels")
    ax.axvline(x=silhouette_avg, color="red", linestyle="--")
    ax.set_yticks([])

    plt.show()

    # Run k-medoids clustering
    kmedoids = KMedoids(n_clusters=n_clusters, random_state=1)
    cluster_labels = kmedoids.fit_predict(X)

    # Compute the silhouette score and plot silhouette plots
    silhouette_avg = silhouette_score(X, cluster_labels)
    print(f"For n_clusters = {n_clusters}, the average silhouette_score is: {silhouette_avg:.2f}")

   