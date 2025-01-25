import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

# Load the trained model and scaler
with open('model_saved/trained_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('model_saved/scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

# Streamlit app layout
# can also make the layout --layout='wide'-- or --layout='centered'--
st.set_page_config(page_title="Medical Cost Predection",)

# Streamlit app
st.title("Insurance Charges Prediction")
st.write("Enter the details below to predict insurance charges.")

# User input
age = st.number_input('Age', min_value=1, max_value=100, value=25, step=1)
bmi = st.number_input('Bmi', min_value=10.0, max_value=50.0, value=22.0, step=0.1)
children = st.number_input('Number Of Children', min_value=0, max_value=10, value=0, step=1)

if st.button("Predict Charges"):
    # Prepare the custom data
    # custom_data = np.array([age, bmi, children]).reshape(1, -1)
    custom_data = pd.DataFrame([[age, bmi, children]], columns=['age', 'bmi', 'children'])

    # Scale the custom data using the loaded scaler
    custom_data_scaled = scaler.transform(custom_data)

    # Make the prediction
    y_pred_custom = model.predict(custom_data_scaled)

    # Display the result
    st.success(f"Predicted Insurance Charges: ${y_pred_custom[0]:.2f}")