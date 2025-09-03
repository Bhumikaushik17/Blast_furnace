import streamlit as st
import numpy as np
import joblib
import pandas as pd

# ---------------------------
# Load Models & Scalers
# ---------------------------
rf_prod_model = joblib.load("rf_prod_model.joblib")
rf_fuel_model = joblib.load("rf_fuel_model.joblib")
scaler_prod = joblib.load("scaler_prod.joblib")
scaler_fuel = joblib.load("scaler_fuel.joblib")

# ---------------------------
# App Title
# ---------------------------
st.title("Blast Furnace BF1 Optimization")
st.write("Predict **Throughput** and **Fuel Rate** with Recommendations to improve performance.")

# ---------------------------
# Features used for both models
# ---------------------------
feature_names = [
    'Coke rate- BF1(kg/thm)',
    'Nut Coke - BF1(Kg/thm)',
    'Total Coke Rate (Coke Rate+Nut Coke) BF1',
    'PCI rate- BF1(kg/thm)',
    'Slag Rate - BF1(Kg/thm)',
    'O2 Enrichment - BF1(%)',
    'ETA CO Levels- BF1(%)',
    'Sinter Consumption- BF1(%)'
]

# ---------------------------
# User Input Section
# ---------------------------
st.header("Enter Current Parameter Values")
input_data = []
for feature in feature_names:
    value = st.number_input(f"{feature}", value=0.0)
    input_data.append(value)

input_data = np.array(input_data).reshape(1, -1)

# ---------------------------
# Predict Button
# ---------------------------
if st.button("Predict"):
    # Scale inputs
    input_scaled_prod = scaler_prod.transform(input_data)
    input_scaled_fuel = scaler_fuel.transform(input_data)

    # Predictions
    throughput_pred = rf_prod_model.predict(input_scaled_prod)[0]
    fuelrate_pred = rf_fuel_model.predict(input_scaled_fuel)[0]

    # Show predictions
    st.subheader("Predicted Results")
    st.write(f"**Throughput (MT):** {throughput_pred:.2f}")
    st.write(f"**Fuel Rate (kg/thm):** {fuelrate_pred:.2f}")

    # ---------------------------
    # Recommendation Logic
    # ---------------------------
    st.subheader("Recommendations for Improvement")

    recs = []
    if throughput_pred < 3000:
        recs.append("Increase **O2 Enrichment** by 5-10%")
        recs.append("Increase **PCI Rate** slightly")
    if fuelrate_pred > 500:
        recs.append("Reduce **Coke Rate** & **Nut Coke**")
        recs.append("Optimize **Slag Rate** and **Sinter Consumption**")

    if not recs:
        st.success("Current operating parameters are already optimized!")
    else:
        for r in recs:
            st.info(r)

  
