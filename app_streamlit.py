import streamlit as st
from predict import predict_single

st.title("Customer Churn Prediction")

input_data = {
    "gender": st.selectbox("Gender", ["Male", "Female"]),
    "SeniorCitizen": st.selectbox("Senior Citizen", [0, 1]),
    "Partner": st.selectbox("Partner", ["Yes", "No"]),
    "Dependents": st.selectbox("Dependents", ["Yes", "No"]),
    "tenure": st.slider("Tenure", 0, 72),
    "PhoneService": st.selectbox("Phone Service", ["Yes", "No"]),
    "MultipleLines": st.selectbox("Multiple Lines", ["No phone service", "Yes", "No"]),
    "InternetService": st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"]),
    "OnlineSecurity": st.selectbox("Online Security", ["Yes", "No", "No internet service"]),
    "Contract": st.selectbox("Contract", ["Month-to-month", "One year", "Two year"]),
    "MonthlyCharges": st.slider("Monthly Charges", 10, 150),
    "TotalCharges": st.slider("Total Charges", 10, 10000),
    "PaymentMethod": st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]),
}

if st.button("Predict"):
    prediction, prob = predict_single(input_data)
    st.write(f"### Prediction: {prediction}")
    st.write(f"### Probability: {prob}")
