import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Create a sample dataset
np.random.seed(42)
data = pd.DataFrame({
    "Feature1": np.random.rand(10),
    "Feature2": np.random.rand(10),
    "Feature3": np.random.rand(10),
    "Feature4": np.random.rand(10)
})

# Step 2: Compute the correlation matrix
correlation_matrix = data.corr()

# Step 3: Visualize the correlation matrix using a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Matrix Heatmap")
plt.show()


# ### **🔹 Explanation**
# 1. **Generate Random Data**: Creates a **10×4** dataset with random values.
# 2. **Compute Correlation Matrix**: Uses `data.corr()` to calculate correlations between features.
# 3. **Heatmap Visualization**:
#    - Uses `sns.heatmap()` to plot the matrix.
#    - The `cmap="coolwarm"` color scheme is applied.
#    - `annot=True` displays **correlation values** inside the cells.

# ### **🔹 Output**
# - A heatmap where:
#   - **Red shades** → Positive correlation.
#   - **Blue shades** → Negative correlation.
#   - **White areas** → Weak or no correlation.
