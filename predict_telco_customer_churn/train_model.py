# train_model.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import pickle

# Load dataset
data = pd.read_csv('data/Telco-Customer-Churn.csv')

# Drop irrelevant columns
data = data.drop(['customerID'], axis=1)

# Handle missing values
data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')
data = data.dropna()

# Convert categorical columns using one-hot encoding
categorical_cols = ['gender', 'Partner', 'Dependents', 'PhoneService',
                    'MultipleLines', 'InternetService', 'OnlineSecurity',
                    'OnlineBackup', 'DeviceProtection', 'TechSupport',
                    'StreamingTV', 'StreamingMovies', 'Contract',
                    'PaperlessBilling', 'PaymentMethod']

data = pd.get_dummies(data, columns=categorical_cols, drop_first=True)

# Encode target
data['Churn'] = data['Churn'].map({'Yes':1, 'No':0})

# Features and target
X = data.drop('Churn', axis=1)
y = data['Churn']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Save model and scaler
pickle.dump(model, open('churn_model.pkl', 'wb'))
pickle.dump(scaler, open('scaler.pkl', 'wb'))

# Save feature columns for Flask input alignment
import json
with open('feature_columns.json', 'w') as f:
    json.dump(list(X.columns), f)

print("Model trained and saved!")
