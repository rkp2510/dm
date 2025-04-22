### **📌 Graph Visualization of a Network with Statistical Degree Measures**
# In network analysis, **degree statistics** such as **maximum, minimum, median, first quartile (Q1), and third quartile (Q3)** help us understand the connectivity of nodes in a graph.

# ### **🔹 Steps to Visualize the Network with Degree Statistics**
# 1. **Create a Graph** → Generate a random or real-world network.
# 2. **Compute Degree Statistics** → Find the min, max, median, Q1, and Q3 of node degrees.
# 3. **Color the Nodes Based on Degree Statistics** → Differentiate nodes using color coding.
# 4. **Visualize the Graph** → Display the network structure.


### **📌 Python Code for Visualization**
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Create a random graph (Erdős–Rényi model)
G = nx.erdos_renyi_graph(50, 0.1)  # 50 nodes, 10% connection probability

# Step 2: Compute the degree of each node
degrees = np.array([d for _, d in G.degree()])

# Step 3: Calculate statistical measures
min_deg = np.min(degrees)
max_deg = np.max(degrees)
median_deg = np.median(degrees)
q1 = np.percentile(degrees, 25)  # First quartile (Q1)
q3 = np.percentile(degrees, 75)  # Third quartile (Q3)

# Step 4: Assign colors based on degree statistics
node_colors = []
for deg in degrees:
    if deg == min_deg:
        node_colors.append("blue")  # Minimum degree nodes
    elif deg == max_deg:
        node_colors.append("red")  # Maximum degree nodes
    elif deg <= q1:
        node_colors.append("green")  # First quartile nodes
    elif deg >= q3:
        node_colors.append("orange")  # Third quartile nodes
    else:
        node_colors.append("purple")  # Median & other nodes

# Step 5: Draw the network graph
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)  # Position nodes using the force-directed layout
nx.draw(G, pos, node_color=node_colors, with_labels=True, edge_color="gray", node_size=500, font_size=8)

# Step 6: Add a legend
plt.title("Graph Visualization with Degree Statistics")
plt.show()

### **🔹 Explanation**
# - **Generated a random network** with 50 nodes and a 10% probability of edge creation.
# - **Computed the degree distribution** of nodes.
# - **Calculated statistical measures**:
#   - **Min Degree** (Least connected node)
#   - **Max Degree** (Most connected node)
#   - **Q1 (First Quartile)** (Nodes with lower degree distribution)
#   - **Q3 (Third Quartile)** (Nodes with higher degree distribution)
#   - **Median Degree**
# - **Colored nodes based on these statistics**:
#   - 🔵 **Blue** → Minimum degree nodes  
#   - 🔴 **Red** → Maximum degree nodes  
#   - 🟢 **Green** → First quartile (low-degree nodes)  
#   - 🟠 **Orange** → Third quartile (high-degree nodes)  
#   - 🟣 **Purple** → Median and other nodes  
# - **Used `nx.spring_layout()`** to position nodes for a clear visualization.

# ---

# ### **📌 Expected Output**
# - The graph will display nodes **colored based on their degree statistics**.
# - It helps in **identifying important (high-degree) nodes and low-degree nodes**.
# - Useful in **network resilience analysis, centrality analysis, and node importance detection**.

# Would you like a visualization with a different type of network (e.g., Scale-Free, Small-World)? 🚀
