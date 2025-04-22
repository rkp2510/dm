# What is Association Rule Mining?
# Association Rule Mining is a technique used in data mining to find relationships between different items in large datasets. 

# What is the Apriori Algorithm?
# The Apriori algorithm helps find these relationships in a dataset by:

# Finding frequent itemsets (which items are often bought together).
# Generating rules (If X is bought, Y is also likely to be bought)

import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Sample dataset (List of transactions)
transactions = [
    ['Milk', 'Bread', 'Butter'],
    ['Milk', 'Diaper', 'Beer', 'Eggs'],
    ['Milk', 'Bread', 'Diaper', 'Beer'],
    ['Bread', 'Butter'],
    ['Milk', 'Bread', 'Diaper', 'Butter'],
    ['Beer', 'Diaper']
]

# Convert transactions into a DataFrame
te = TransactionEncoder()
te_array = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_array, columns=te.columns_)

# Step 1: Find Frequent Itemsets using Apriori
frequent_itemsets = apriori(df, min_support=0.4, use_colnames=True)

# Step 2: Generate Association Rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)

# Print Frequent Itemsets and Association Rules
print("\nFrequent Itemsets:")
print(frequent_itemsets)

print("\nAssociation Rules:")
print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
