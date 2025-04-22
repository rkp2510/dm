# What is Random Forest Classification? 🌳🌳🌳
# Random Forest is a machine learning algorithm that helps us classify things into different groups. It is made up of many decision trees, and it works by combining the results of these trees to make better predictions. 🎯

# How Does It Work? 🤔
# Creates multiple decision trees 🌲🌲
# Each tree is trained on different parts of the data.
# Makes predictions using all trees 🔍
# Each tree gives its own answer.
# Takes a vote 🗳️
# The answer that most trees agree on is chosen.
# Example: Using Random Forest to Classify Emails 📧


import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.datasets import load_iris

#Load the Iris dataset
data = load_iris()
X = data.data # Features
y = data.target # Target labels

#Split the dataset into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Random Forest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the classifier
clf.fit(X_train, y_train)

#Make predictions on the test set
y_pred = clf.predict(X_test)

# Calculate accuracу
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

#Generate a classification report
print("\nclassification Report:")
print(classification_report(y_test, y_pred))
