# -*- coding: utf-8 -*-
"""Hypothyroidism in Benign Tumor

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OZST97ETSKABZLzI45OaMohdXMLKCmfn
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Load your dataset
data = pd.read_csv('/content/Hypothyroidism.csv')

# Preprocessing
# Assuming your dataset includes features like 'age', 'gender', and 'hypothyroidism_column'

# Encode categorical variables if any
label_encoder = LabelEncoder()
data['GENDER'] = label_encoder.fit_transform(data['GENDER'])  # Assuming 'gender' is a categorical feature

# Select features (X) and target (y)
X = data[['AGE', 'GENDER']]  # Assuming 'age' and 'gender' are features for prediction
y = data['HYP']  # Assuming 'hypothyroidism_column' is the target label

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Model training
model = LogisticRegression()
model.fit(X_train, y_train)

# Model evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)

# Filter the dataset to include only middle-aged individuals affected by hypothyroidism
middle_age_hypothyroidism = data[(data['AGE'] >= 35) & (data['AGE'] <= 55) & (data['HYP'] == 1)]

# Plotting the graph
# Assuming 'age' is the age of middle-aged individuals affected by hypothyroidism
plt.hist(middle_age_hypothyroidism[middle_age_hypothyroidism['GENDER'] == 1]['AGE'], bins=20, alpha=0.5, color='blue', label='Male')
plt.hist(middle_age_hypothyroidism[middle_age_hypothyroidism['GENDER'] == 0]['AGE'], bins=20, alpha=0.5, color='pink', label='Female')
plt.xlabel('AGE')
plt.ylabel('Frequency')
plt.title('Distribution of Middle-aged Individuals Affected by Hypothyroidism')
plt.legend()
plt.show()

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix

# Load your dataset
data = pd.read_csv('/content/Hypothyroidism.csv')

# Preprocessing
# Replace empty strings with NaN
data.replace(' ', np.nan, inplace=True)

# Drop rows with missing values
data.dropna(inplace=True)

# Encode categorical variables if any
label_encoder = LabelEncoder()
data['GENDER'] = label_encoder.fit_transform(data['GENDER'])  # Assuming 'gender' is a categorical feature

# Select features (X) and target (y)
X = data[['AGE', 'GENDER', 'T3', 'T4', 'TSH']]  # Assuming 'age', 'gender', 't3', 't4', 'tsh' are features for prediction
y = data['HYP']  # Assuming 'hypothyroidism_column' is the target label

# Split data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Dictionary to store models and their names
models = {
    'Logistic Regression': LogisticRegression(),
    'Decision Tree': DecisionTreeClassifier(),
    'Random Forest': RandomForestClassifier(),
    'Support Vector Machine': SVC(),
    'Gradient Boosting': GradientBoostingClassifier()
}

# Train and evaluate models
best_model = None
best_accuracy = 0

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"{name} Accuracy: {accuracy}")
    print(f"{name} Confusion Matrix:\n{confusion_matrix(y_test, y_pred)}\n")

    if accuracy > best_accuracy:
        best_accuracy = accuracy
        best_model = model

print(f"Best Model: {best_model.__class__.__name__} with Accuracy: {best_accuracy}")

# Filter the dataset to include only middle-aged individuals affected by hypothyroidism
middle_age_hypothyroidism = data[(data['AGE'] >= 35) & (data['AGE'] <= 55) & (data['HYP'] == 1)]

# Plotting the histograms for 't3', 't4', and 'tsh' levels separately for males and females
features = ['T3', 'T4', 'TSH']
colors = ['blue', 'green', 'red']

for feature in features:
    plt.figure(figsize=(10, 6))
    for gender_value, color in zip([1, 0], colors):
        filtered_data = middle_age_hypothyroidism[middle_age_hypothyroidism['GENDER'] == gender_value]
        plt.hist(filtered_data[feature], bins=20, alpha=0.5, color=color, label='Male' if gender_value == 1 else 'Female')
    plt.xlabel(feature.capitalize() + ' Level')
    plt.ylabel('Frequency')
    plt.title('Distribution of ' + feature.upper() + ' Levels for Middle-aged Individuals Affected by Hypothyroidism')
    plt.legend()
    plt.show()