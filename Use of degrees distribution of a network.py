### **📌 Degree Distribution of a Network in Graph Theory**
# In network analysis, the **degree distribution** represents how the degrees (number of connections) of nodes are distributed across the entire network. 
# It helps to analyze the structure and behavior of real-world networks, such as social networks, biological networks, and the internet.


import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Create a random graph
G = nx.erdos_renyi_graph(100, 0.05)  # 100 nodes, 5% connection probability

# Step 2: Compute degree of each node
degree_sequence = [d for n, d in G.degree()]

# Step 3: Plot the degree distribution
plt.hist(degree_sequence, bins=10, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.title("Degree Distribution of the Network")
plt.show()

### **🔹 Explanation**
# - **`nx.erdos_renyi_graph(100, 0.05)`** → Generates a random network with **100 nodes**, where each pair of nodes has a 5% chance of being connected.
# - **`G.degree()`** → Extracts the degree of each node.
# - **`plt.hist()`** → Plots the histogram of degree distribution.

# ---

# ### **🔹 Key Observations**
# - In a **random network**, the degree distribution follows a **bell-shaped curve**.
# - In a **scale-free network**, the distribution follows a **power law**, meaning few nodes have **very high degrees**, while most have **low degrees**.

# ---

# ### **📌 Real-World Example**
# 1. **Social Networks**: Some users (celebrities) have **millions** of connections, while most have **few**.
# 2. **Internet**: Some websites (like Google, Wikipedia) are highly connected, while most have fewer links.
# 3. **Biological Networks**: Some proteins interact with many others, making them essential for biological functions.
