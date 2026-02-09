from flask import Flask, render_template, request
import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# Load data
data = pd.read_csv("D:\Mohit\MINI PROJECT\Student Performance Prediction\students_data.csv")
X = data[['attendance', 'internal_marks', 'study_hours', 'prev_cgpa']]
y = data['result']

# Train-test split (VERY IMPORTANT)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Feature scaling (CRITICAL FIX)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Logistic Regression with balanced classes
model = LogisticRegression(class_weight='balanced')
model.fit(X_train, y_train)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    attendance = float(request.form['attendance'])
    internal_marks = float(request.form['internal_marks'])
    study_hours = float(request.form['study_hours'])
    prev_cgpa = float(request.form['prev_cgpa'])

    input_data = np.array([[attendance, internal_marks, study_hours, prev_cgpa]])
    input_scaled = scaler.transform(input_data)

    # Get probability instead of direct class
    prob = model.predict_proba(input_scaled)[0][1]

    # Custom threshold
    if prob >= 0.5:
        result = f"PASS 🎉 (Probability: {prob:.2f})"
    else:
        result = f"FAIL ❌ (Probability: {prob:.2f})"

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
