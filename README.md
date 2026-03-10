Dataset Bias Audit System

A Machine Learning fairness auditing tool that detects bias in datasets and model predictions.
The system trains a classification model and evaluates whether predictions are fair across sensitive attributes such as gender, race, or other demographic variables.

The project includes an interactive Streamlit dashboard where users can upload any dataset and analyze bias automatically.

Project Overview

Machine learning models can unintentionally learn biased patterns from data. This project provides a system that:

Trains a machine learning model on uploaded datasets

Detects potential bias in predictions

Evaluates fairness using statistical metrics

Provides a user-friendly interface for bias analysis

This project demonstrates concepts from:

Responsible AI

Fair Machine Learning

Model evaluation and auditing

Features

Upload any CSV dataset

Automatic data preprocessing

Random Forest classification model

Bias detection using fairness metrics

Interactive Streamlit dashboard

Fast analysis suitable for large datasets

System Architecture
Dataset Upload
       ↓
Data Preprocessing
       ↓
Model Training (Random Forest)
       ↓
Prediction Generation
       ↓
Fairness Evaluation
       ↓
Bias Detection
       ↓
Results Dashboard
Technologies Used

Programming Language:

Python

Machine Learning Libraries:

scikit-learn

pandas

numpy

Fairness Analysis:

Fairlearn

Visualization and Interface:

Streamlit

Project Structure
AML/
│
├── data/
│   └── uploaded_dataset.csv
│
├── src/
│   ├── preprocessing.py
│   ├── model.py
│   ├── bias_detection.py
│   ├── pipeline.py
│
├── app/
│   └── dashboard.py
│
├── requirements.txt
└── README.md
Installation

Clone the repository:

git clone <repository-url>
cd AML

Install dependencies:

pip install -r requirements.txt
Running the Application

Start the Streamlit dashboard:

streamlit run app/dashboard.py

Then open the browser at:

http://localhost:8501
How to Use

Upload a dataset in CSV format

Select the target column (prediction variable)

Select the sensitive attribute (e.g., gender, race)

Click Run Bias Analysis

View model accuracy and bias results

Example Output
Model Accuracy: 0.85

Bias Score: 0.12

Bias Status: Bias Detected

Interpretation:

Bias Score	Meaning
< 0.05	Fair
0.05 – 0.10	Mild Bias
> 0.10	Bias Detected
Example Use Cases

Detect bias in hiring datasets

Evaluate fairness in loan approval models

Analyze bias in income prediction datasets

Study fairness in classification systems

Future Improvements

Potential extensions include:

Automatic bias detection across all features

Visualization dashboards for fairness metrics

Support for multiple fairness metrics

Model comparison (Logistic Regression, Random Forest, XGBoost)

Bias mitigation algorithms

Educational Purpose

This project is designed for:

Advanced Machine Learning coursework

Responsible AI research demonstrations

Bias detection and fairness evaluation studies

License

This project is intended for educational and research purposes.
