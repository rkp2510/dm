# What is Regression Analysis?
# Regression Analysis is a statistical method used to predict a dependent variable (output) based on one or more independent variables (inputs).

# 👉 Example: Predicting house prices based on factors like area, number of rooms, and location. 🏠

# 📌 What is Linear Regression?
# Linear Regression is the simplest form of regression analysis. It finds a straight-line relationship between the input (X) and the output (Y).

# 💡 Equation of Linear Regression:

# 𝑌=𝑚𝑋+𝑏

# Y = Predicted value (output)
# X = Input value (feature)
# m = Slope (rate of change)
# b = Intercept (value of Y when X = 0)

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Example dataset
data = {
    'X': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Independent variable
    'Y': [1.1, 2.2, 2.9, 4.0, 5.1, 5.8, 6.9, 8.0, 9.1, 10.0]  # Dependent variable
}

# Create DataFrame
df = pd.DataFrame(data)

# Split the data into features (X) and target (Y)
X = df[['X']]  # Features (independent variable) - double brackets for a DataFrame
Y = df['Y']  # Target (dependent variable)

# Split the data into training (80%) and testing (20%) sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Create and train the Linear Regression model
model = LinearRegression()
model.fit(X_train, Y_train)

# Make predictions on the test set
Y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)

# Print evaluation metrics
print(f'Mean Squared Error: {mse:.2f}')
print(f'R-squared: {r2:.2f}')

# Visualize the results
plt.scatter(X_train, Y_train, color='blue', label='Training Data')  # Training data points
plt.scatter(X_test, Y_test, color='green', label='Test Data')  # Testing data points
plt.plot(X_test, Y_pred, color='red', label='Regression Line')  # Regression line
plt.title('Linear Regression')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.show()
