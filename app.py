import streamlit as st
from loan_approval_model import load_model, predict  # Ensure these functions are correctly defined

# Load the model
model = load_model()

# Streamlit app
st.title("Loan Application")
st.write("Input your data to determine your eligibility for a loan.")

# Input variables
ip_no_of_dependents = st.slider("Select the number of dependents", 0, 10, 2)
ip_education = st.selectbox("Choose your education level", ["Not Graduate", "Graduate"])
ip_self_employed = st.selectbox("Are you self-employed?", ["No", "Yes"])
ip_income_annum = st.number_input("Enter your annual income:", min_value=10000, max_value=500000, value=36000)
ip_loan_amount = st.number_input("Enter the loan amount:", min_value=10000, value=10000)
ip_loan_term = st.slider("Select the loan term (months):", 1, 360, 12)
ip_cibil_score = st.slider("Select your CIBIL score:", 300, 850, 750)
ip_residential_assets_value = st.number_input("Enter the estimated residential asset value:", min_value=100000, max_value=5000000, value=500000)
ip_commercial_assets_value = st.number_input("Enter the estimated commercial asset value:", min_value=100000, max_value=5000000, value=500000)
ip_luxury_assets_value = st.number_input("Enter the estimated luxury asset value:", min_value=100000, max_value=5000000, value=500000)
ip_bank_asset_value = st.number_input("Enter the bank asset value:", min_value=50000, value=50000)

# Prepare input for the model
user_input = [
    ip_no_of_dependents,
    1 if ip_education == "Graduate" else 0,
    1 if ip_self_employed == "Yes" else 0,
    ip_income_annum,
    ip_loan_amount,
    ip_loan_term,
    ip_cibil_score,
    ip_residential_assets_value,
    ip_commercial_assets_value,
    ip_luxury_assets_value,
    ip_bank_asset_value
]

# Predict button
if st.button("Predict"):
    try:
        prediction = predict(model, user_input)
        result = "Approved" if prediction[0] == 1 else "Rejected"
        st.write(f"Prediction: {result}")
    except Exception as e:
        st.error(f"An error occurred: {e}")
