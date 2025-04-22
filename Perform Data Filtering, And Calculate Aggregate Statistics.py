import pandas as pd
data = {
"Name": ["Ganesh", "Yogesh", "Mahesh", "Dinesh", "Harshal",
"Sachin"],
"Age": [20, 23, 19, 20, 30, 22],
"Salary": [30000, 40000, 35000, 40000, 50000, 33000],
"Department": ['HR', 'DEV', 'HR', 'CEO', 'DEV', 'CEO'],
"MOB": [4545453445, 6464646464, 7575757575, 5454545454,
8686868686, 5544554455]
}


# Create DataFrame
df = pd.DataFrame(data)


# Print the DataFrame
print(df)
print()


# Filter Employees by Department
hr_em = df[df['Department'] == 'HR']
dev_em = df[df['Department'] == 'DEV']
ceo_em = df[df['Department'] == 'CEO']


# Filter Employees by Salary
high_sal = df[df['Salary'] > 35000]
low_sal = df[df['Salary'] <= 35000]


# Print Filtered Data
print("HR Employees:\n", hr_em, "\n")
print("DEV Employees:\n", dev_em, "\n")
print("CEO Employees:\n", ceo_em, "\n")
print("High Salary Employees:\n", high_sal, "\n")
print("Low Salary Employees:\n", low_sal, "\n")


# Aggregate Statistics
agg_stats = {
'Age Mean': df['Age'].mean(),
'Age Sum': df['Age'].sum(),
'Age Count': df['Age'].count(),
'Age Median': df['Age'].median(),
'Age Min': df['Age'].min(),
'Age Max': df['Age'].max(),
'Salary Mean': df['Salary'].mean(),
'Salary Sum': df['Salary'].sum(),
'Salary Median': df['Salary'].median(),
'Salary Count': df['Salary'].count(),
'Salary Min': df['Salary'].min(),
'Salary Max': df['Salary'].max()
}


# Print Aggregate Statistics
print("\nAggregate Statistics:\n")
for key, value in agg_stats.items():
    print(f"{key}: {value}")
