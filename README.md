⚖️ Dataset Bias Audit System

A Machine Learning fairness auditing tool that detects bias in datasets and model predictions.
The system trains a classification model and evaluates whether predictions are fair across sensitive attributes such as gender, race, or demographic variables.

The project includes an interactive Streamlit dashboard where users can upload datasets and analyze bias automatically.

🚀 Project Overview

Machine learning models can unintentionally learn biased patterns from data.
This system helps detect such issues by providing a bias auditing pipeline.

The system performs:

Dataset preprocessing

Machine learning model training

Prediction generation

Bias detection using fairness metrics

✨ Features

✔ Upload any CSV dataset
✔ Automatic data preprocessing
✔ Random Forest classification model
✔ Bias detection using fairness metrics
✔ Interactive Streamlit dashboard
✔ Fast bias analysis

🧠 System Architecture
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
🛠 Technologies Used
Programming Language

Python

Machine Learning Libraries

scikit-learn

pandas

numpy

Fairness Analysis

Fairlearn

Interface

Streamlit

📁 Project Structure
AML/
│
├── data/
│   └── uploaded_dataset.csv
│
├── src/
│   ├── preprocessing.py
│   ├── model.py
│   ├── bias_detection.py
│   └── pipeline.py
│
├── app/
│   └── dashboard.py
│
├── requirements.txt
└── README.md
⚙️ Installation

Clone the repository:

git clone <repository-url>
cd AML

Install required dependencies:

pip install -r requirements.txt
▶ Running the Application

Start the Streamlit dashboard:

streamlit run app/dashboard.py

Open the application in your browser:

http://localhost:8501
📊 How to Use

1️⃣ Upload a CSV dataset
2️⃣ Select the target column
3️⃣ Select the sensitive attribute
4️⃣ Click Run Bias Analysis
5️⃣ View model accuracy and bias results

📈 Example Output
Model Accuracy: 0.85

Bias Score: 0.12

Bias Status: Bias Detected
Bias Interpretation
Bias Score	Meaning
< 0.05	Fair
0.05 – 0.10	Mild Bias
> 0.10	Bias Detected
💡 Example Use Cases

Detect bias in hiring datasets

Evaluate fairness in loan approval models

Analyze bias in income prediction systems

Study fairness in classification algorithms

🔮 Future Improvements

Possible enhancements include:

Automatic bias detection across all dataset columns

Bias visualization dashboards

Multiple fairness metrics (Equalized Odds, Disparate Impact)

Model comparison (Random Forest, XGBoost, Neural Networks)

Advanced bias mitigation techniques

🎓 Educational Purpose

This project demonstrates key concepts in:

Responsible AI

Fair Machine Learning

Model evaluation and auditing

It is suitable for:

Advanced Machine Learning coursework

AI fairness research demonstrations

Bias detection experiments

📜 License

This project is intended for educational and research purposes.
