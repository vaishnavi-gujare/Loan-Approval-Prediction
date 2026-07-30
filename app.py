import streamlit as st
import numpy as np
import joblib

# Load Model and Objects
model = joblib.load("loan_approval_model (1).pkl")
scaler = joblib.load("scaler.pkl")

education_encoder = joblib.load("education_encoder.pkl")
self_employed_encoder = joblib.load("self_employed_encoder.pkl")

st.set_page_config(page_title="Loan Approval Prediction", page_icon="🏦")

st.title("Loan Approval Prediction System")
st.write("Enter the applicant details to predict the loan status.")

# User Inputs
no_of_dependents = st.number_input("Number of Dependents", min_value=0, step=1)

education = st.selectbox(
    "Education",
    education_encoder.classes_
)

self_employed = st.selectbox(
    "Self Employed",
    self_employed_encoder.classes_
)

income_annum = st.number_input("Annual Income")

loan_amount = st.number_input("Loan Amount")

loan_term = st.number_input("Loan Term (Years)", min_value=1)

cibil_score = st.number_input(
    "CIBIL Score",
    min_value=300,
    max_value=900
)

residential_assets_value = st.number_input(
    "Residential Assets Value"
)

commercial_assets_value = st.number_input(
    "Commercial Assets Value"
)

luxury_assets_value = st.number_input(
    "Luxury Assets Value"
)

bank_asset_value = st.number_input(
    "Bank Asset Value"
)

# Prediction
if st.button("Predict"):

    education = education_encoder.transform([education])[0]
    self_employed = self_employed_encoder.transform([self_employed])[0]

    data = np.array([[
        no_of_dependents,
        education,
        self_employed,
        income_annum,
        loan_amount,
        loan_term,
        cibil_score,
        residential_assets_value,
        commercial_assets_value,
        luxury_assets_value,
        bank_asset_value
    ]])

    data = scaler.transform(data)

    prediction = model.predict(data)

    if prediction[0] == 1:
        st.success("Loan Approved")
    else:
        st.error(" Loan Rejected")