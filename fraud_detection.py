import pandas as pd
import joblib
import streamlit as st

# Load the trained model
model = joblib.load("fraud_detection_pipeline.pkl")

# Title
st.title("Fraud Detection Prediction App")

st.markdown(
    "Please enter the transaction details and click the Predict button."
)

st.divider()

# Transaction type
transaction_type = st.selectbox(
    "Transaction Type",
    ["CASH_OUT", "PAYMENT", "TRANSFER", "DEPOSIT"]
)

# Transaction details
amount = st.number_input(
    "Amount",
    min_value=0.0,
    value=1000.0
)

oldbalanceOrg = st.number_input(
    "Old Balance (Sender)",
    min_value=0.0,
    value=10000.0
)

newbalanceOrig = st.number_input(
    "New Balance (Sender)",
    min_value=0.0,
    value=9000.0
)

oldbalanceDest = st.number_input(
    "Old Balance (Receiver)",
    min_value=0.0,
    value=0.0
)

newbalanceDest = st.number_input(
    "New Balance (Receiver)",
    min_value=0.0,
    value=0.0
)

# Prediction
if st.button("Predict"):

    # Create input DataFrame
    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest
    }])

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Display prediction
    st.subheader(f"Prediction: {int(prediction)}")

    if prediction == 1:
        st.error("⚠️ The transaction is fraudulent.")
    else:
        st.success("✅ The transaction is not fraudulent.")