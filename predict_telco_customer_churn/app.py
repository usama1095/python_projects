# app.py
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
import json

app = Flask(__name__)

# Load model, scaler, and feature columns
model = pickle.load(open('churn_model.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))
with open('feature_columns.json', 'r') as f:
    feature_columns = json.load(f)

# Dropdown options
gender_options = ['Male', 'Female']
internet_options = ['DSL', 'Fiber optic', 'No']
contract_options = ['Month-to-month', 'One year', 'Two year']

@app.route('/')
def home():
    return render_template('index.html', 
                           gender_options=gender_options,
                           internet_options=internet_options,
                           contract_options=contract_options,
                           prediction_text='')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values
        gender = request.form['gender']
        tenure = int(request.form['tenure'])
        monthly_charges = float(request.form['monthly_charges'])
        total_charges = float(request.form['total_charges'])
        internet = request.form['internet']
        contract = request.form['contract']

        # Basic validation
        if tenure < 0 or monthly_charges < 0 or total_charges < 0:
            return render_template('index.html', prediction_text="Please enter valid positive numbers",
                                   gender_options=gender_options,
                                   internet_options=internet_options,
                                   contract_options=contract_options)

        # Create input dataframe aligned with model features
        input_df = pd.DataFrame(np.zeros((1, len(feature_columns))), columns=feature_columns)

        # Set numeric columns
        input_df['tenure'] = tenure
        input_df['MonthlyCharges'] = monthly_charges
        input_df['TotalCharges'] = total_charges

        # Set categorical columns
        if 'gender_Male' in feature_columns and gender == 'Male':
            input_df['gender_Male'] = 1

        if f'InternetService_{internet}' in feature_columns:
            input_df[f'InternetService_{internet}'] = 1

        if f'Contract_{contract}' in feature_columns:
            input_df[f'Contract_{contract}'] = 1

        # Scale input
        scaled_input = scaler.transform(input_df)

        # Prediction
        prediction = model.predict(scaled_input)[0]
        output = "Customer will churn" if prediction == 1 else "Customer will stay"

        return render_template('index.html', prediction_text=output,
                               gender_options=gender_options,
                               internet_options=internet_options,
                               contract_options=contract_options)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    app.run(debug=True)
