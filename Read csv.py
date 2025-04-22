import pandas as pd

# Read the CSV file
df = pd.read_csv("employees.csv")  # Replace with your file name

# Display the first 5 rows
print(df.head())


# 1. Filter rows where 'Salary' is greater than 50,000
high_salary = df[df["SALARY"] > 10000]
print("\nEmployees with Salary > 10000:\n", high_salary)


# 2. Select employees from the department ID 20
it_department = df[df["DEPARTMENT_ID"] == 20]
print("\nEmployees in Department ID 20:\n", it_department)




# 4. Filter only selected columns: 'Name', 'Salary', 'EMAIL'
selected_columns = df[["FIRST_NAME", "SALARY", "EMAIL"]]
print("\nSelected Columns:\n", selected_columns)


# 5. Remove duplicate rows
df_cleaned = df.drop_duplicates()
print("\nData after removing duplicates:\n", df_cleaned.head())


# 6. Handle missing values (fill with mean)
df_filled = df.fillna(df.mean(numeric_only=True))
print("\nData after filling missing values:\n", df_filled.head())




// Download Dataset From Here 
https://gist.github.com/kevin336/acbb2271e66c10a5b73aacf82ca82784 #file-employees-csv
