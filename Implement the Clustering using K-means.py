import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Step 1: Generate sample data with 3 clusters
X, _ = make_blobs(n_samples=300, centers=3, random_state=42, cluster_std=1.0)

# Apply K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10) # Create KMeans model with 3 clusters
kmeans.fit(X)  # Fit the model to the data

# Step 3: Retrieve cluster labels and cluster centers
labels = kmeans.labels_ # Cluster assignments for each data point
centers = kmeans.cluster_centers_ # Coordinates of cluster centroids

# Plot the clusters
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap="viridis", marker="o", edgecolors="k")
plt.scatter(centers[:, 0], centers[:, 1], c="red", marker="X", s=200, label="Centroids")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.title("K-Means Clustering")
plt.legend()
plt.show()

# What is K-Means Clustering?
# K-Means is an unsupervised machine learning algorithm used for clustering data into K groups (clusters) based on their similarities.

# Another Program
# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

# Step 2: Sample Data (replace this with your own dataset)
data = {
    'Data Mining': [7, 8, 6, 9, 7, 5, 8, 7],
    'Web Designing': [5, 6, 7, 8, 6, 4, 5, 6],
    'Data Analytics': [8, 9, 7, 8, 9, 6, 7, 8],
    'Interest': [8, 7, 6, 9, 8, 5, 7, 6],
    'Difficulty': [6, 7, 5, 8, 7, 6, 6, 7],
}

# Step 3: Create DataFrame
df = pd.DataFrame(data)

# Step 4: Preprocess Data (Standardization)
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)

# Step 5: Apply K-Means Clustering
k = 3  # Number of clusters
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
kmeans.fit(scaled_data)

# Step 6: Add Cluster Labels to DataFrame
df['Cluster'] = kmeans.labels_

# Step 7: Reduce Data to 2D Using PCA for Visualization
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(scaled_data)

# Step 8: Plot Clusters
plt.figure(figsize=(8, 6))
plt.scatter(reduced_data[:, 0], reduced_data[:, 1], c=kmeans.labels_, cmap='viridis', edgecolors='k')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title('K-Means Clustering')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.colorbar(label='Cluster')
plt.legend()
plt.show()

# Step 9: Evaluate Clustering Using Silhouette Score
silhouette_avg = silhouette_score(scaled_data, kmeans.labels_)
print(f'Silhouette Score: {silhouette_avg:.3f}')

# Step 10: Print the DataFrame with Clusters
print("\nClustered Data:")
print(df)
