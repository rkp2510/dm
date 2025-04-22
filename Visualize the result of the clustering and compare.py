import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Step 1: Generate synthetic data
X, y = make_blobs(n_samples=300, centers=4, random_state=42)

# Step 2: Apply K-Means clustering
kmeans = KMeans(n_clusters=4, random_state=42)
kmeans.fit(X)

# Step 3: Get the labels and centers
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# Step 4: Visualize the results
plt.figure(figsize=(8, 6))

# Plot data points with colors based on the labels
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis", label="Data points")

# Plot the cluster centers
plt.scatter(centers[:, 0], centers[:, 1], s=200, c="red", marker="X", label="Cluster Centers")

plt.title("K-Means Clustering")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()


#  Explanation
# Data Generation: make_blobs is used to create 300 data points grouped into 4 clusters.
# K-Means Clustering:
# Applies KMeans(n_clusters=4, random_state=42).
# Trains the model with kmeans.fit(X).
# Gets cluster labels and centroids.
# Visualization:
# Plots data points, colored by their assigned clusters.
# Highlights cluster centers with a red "X".
