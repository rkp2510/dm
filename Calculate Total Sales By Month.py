import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    "Date": ["2024-01-05", "2024-01-15", "2024-02-10", "2024-02-20", 
             "2024-03-05", "2024-03-15", "2024-04-10", "2024-04-20"],
    "Sales": [100, 200, 150, 300, 250, 350, 400, 500]
}

# Convert to DataFrame
df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])  # Convert to datetime
df["Month"] = df["Date"].dt.strftime("%Y-%m")  # Extract 'YYYY-MM'

# Calculate total sales by month
monthly_sales = df.groupby("Month")["Sales"].sum()

# Print total sales by month
print("Total Sales by Month:\n", monthly_sales)

# Plot
plt.bar(monthly_sales.index, monthly_sales.values, color="skyblue")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.title("Total Sales by Month")
plt.xticks(rotation=45)
plt.show()
