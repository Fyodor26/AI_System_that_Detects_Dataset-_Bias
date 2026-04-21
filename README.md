# ⚖️ Dataset Bias Audit System

An advanced Machine Learning system that evaluates both **accuracy and fairness** of model predictions.  
It detects potential bias across different demographic groups and provides insights through an interactive dashboard.

---

## 🚀 Project Overview

Machine learning models can unintentionally learn biased patterns from data.  
This system identifies such biases by analyzing prediction differences across groups.

It helps answer:

- Is the model accurate?
- Is the model fair?

---

## ✨ Features

✔ Upload any CSV dataset  
✔ Automatic data preprocessing  
✔ Random Forest ML model  
✔ Bias detection using fairness metrics  
✔ Automatic bias scanning across all features  
✔ Bias ranking system  
✔ Visualization using charts  
✔ Interactive Streamlit dashboard  

---

## 🧠 System Architecture


Dataset Upload
↓
Data Preprocessing
↓
Feature Encoding
↓
Train Random Forest Model
↓
Generate Predictions
↓
Evaluate Accuracy
↓
Compute Fairness Metric
↓
Bias Detection
↓
Full Bias Scan (All Features)
↓
Bias Ranking
↓
Visualization (Charts)
↓
Dashboard Output


---

## 🛠 Technologies Used

- Python
- pandas
- numpy
- scikit-learn
- matplotlib
- streamlit
- fairlearn (optional)

---

## 📁 Project Structure


AML/
│
├── data/
│ └── uploaded_dataset.csv
│
├── src/
│ ├── preprocessing.py
│ ├── model.py
│ ├── bias_detection.py
│ └── pipeline.py
│
├── app/
│ └── dashboard.py
│
├── requirements.txt
└── README.md


---

## ▶️ Running the Project

### Install dependencies


pip install -r requirements.txt


### Run the dashboard


streamlit run app/dashboard.py


---

## 📊 How It Works

1. Upload dataset
2. Select target column
3. Select sensitive attribute (optional)
4. Run bias analysis OR full bias scan
5. View accuracy + bias results + charts

---

## 📈 Example Output


Model Accuracy: 0.86

Bias Score: 0.12

Bias Status: Bias Detected


Full Scan:


Bias Ranking

gender → 0.21
race → 0.18
education → 0.05

---

## 🎯 Key Concepts

- Machine Learning
- Fairness in AI
- Bias Detection
- Responsible AI
- Data Ethics

---

## 🌍 Applications

- Loan approval systems
- Hiring systems
- Healthcare AI
- Government decision systems

---

## ⚠️ Limitations

- Uses single fairness metric (basic version)
- Cannot determine root cause of bias
- Works best with binary classification

---

## 🔮 Future Improvements

- Multiple fairness metrics
- Model comparison (RF, XGBoost)
- Bias heatmaps
- Explainable AI (feature importance)
- Bias mitigation techniques

---

## 🎓 Purpose

This project demonstrates **Responsible AI and Fair Machine Learning**, making it suitable for:

- Advanced ML coursework
- Research projects
- AI ethics studies

---

## 📜 License

For educational and research purposes only.