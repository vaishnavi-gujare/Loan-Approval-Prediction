# 🏦 Loan Approval Prediction System

## 📌 Project Overview

The Loan Approval Prediction System is a machine learning project that predicts whether a loan application will be approved or rejected based on the applicant's details. The project applies data preprocessing, exploratory data analysis (EDA), machine learning algorithms, hyperparameter tuning, and a Streamlit web application for real-time prediction.

---

## 📂 Dataset

- **Dataset Name:** Loan Approval Prediction Dataset
- **Source:** Kaggle
- **Target Variable:** `loan_status`

### Features

- Number of Dependents
- Education
- Self Employed
- Annual Income
- Loan Amount
- Loan Term
- CIBIL Score
- Residential Assets Value
- Commercial Assets Value
- Luxury Assets Value
- Bank Asset Value

---

## 🛠️ Technologies Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Joblib
- Streamlit
- Matplotlib
- Seaborn

---

## 📊 Data Preprocessing

The following preprocessing steps were performed:

- Loaded the dataset
- Removed unnecessary columns
- Checked missing values
- Removed duplicate records
- Encoded categorical variables using LabelEncoder
- Split data into training and testing sets
- Applied StandardScaler for feature scaling

---

## 📈 Exploratory Data Analysis (EDA)

EDA included:

- Dataset overview
- Summary statistics
- Missing value analysis
- Duplicate record analysis
- Class distribution
- Histograms
- Boxplots
- Countplots
- Correlation Heatmap

---

## 🤖 Machine Learning Models

The following classification algorithms were trained and evaluated:

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Support Vector Machine (SVM)
- Decision Tree
- Random Forest
- AdaBoost
- Gradient Boosting
- XGBoost (Model Comparison)

---

## ⚙️ Hyperparameter Tuning

The project includes:

- Manual Search
- GridSearchCV
- RandomizedSearchCV

---

## 📊 Model Evaluation

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

---

## 🏆 Best Model

After comparing all models, the **Random Forest Classifier** was selected for deployment because it provided excellent performance and reliable deployment compatibility.

---

## 💾 Saved Files

- loan_approval_model.pkl
- scaler.pkl
- education_encoder.pkl
- self_employed_encoder.pkl
- loan_status_encoder.pkl

---

## 🌐 Streamlit Application

The Streamlit application allows users to:

- Enter applicant details
- Predict whether the loan will be Approved or Rejected
- Display the prediction instantly

---

## 📁 Project Structure

```
Loan-Approval-Prediction/
│
├── app.py
├── loan_approval_dataset.csv
├── loan_approval_model.pkl
├── scaler.pkl
├── education_encoder.pkl
├── self_employed_encoder.pkl
├── loan_status_encoder.pkl
├── requirements.txt
└── README.md
```

---

## ▶️ Installation

Clone the repository:

```bash
git clone <repository-link>
```

Move to the project folder:

```bash
cd Loan-Approval-Prediction
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📷 Application Preview

The application accepts user input and predicts whether the loan application is approved or rejected.

---

## 🎯 Conclusion

This project demonstrates a complete machine learning workflow, including data preprocessing, exploratory data analysis, model training, hyperparameter tuning, model comparison, model saving, and deployment using Streamlit.

The system can assist in predicting loan approval decisions based on applicant information.

---

## 👩‍💻 Author

**Vaishnavi Gujare**
