import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os

# Load the trained model and scaler
with open(os.path.join(os.path.dirname(__file__),'trained_model.pkl'), 'rb') as file:
    model = pickle.load(file)

with open(os.path.join(os.path.dirname(__file__),'scaler.pkl'), 'rb') as file:
    scaler = pickle.load(file)

# Streamlit app

# Streamlit app layout
# can also make the layout --layout='wide'-- or --layout='centered'--
st.set_page_config(page_title="House Price Predection")

st.title("🏠 House Price Prediction")
st.write("Enter the details below to predict House Price.")

# User input
grliv_area = st.number_input(
    'GrLivArea', min_value=1, 
    max_value=10000, 
    value=1500, 
    step=1, 
    help="Enter the total living area of the house in square feet.",
)

overall_qual = st.number_input(
    'OverallQual', 
    min_value=1, 
    max_value=10, 
    value=5, 
    step=1, 
    help="Select the overall quality of the house (1-10 scale).",
)

garage_cars = st.number_input(
    'GarageCars', 
    min_value=0, 
    max_value=10, 
    value=2, 
    step=1, 
    help="Enter the number of cars",
)

year_built = st.date_input(
    'YearBuilt', 
    value=pd.to_datetime('2005-01-01'), 
    min_value=pd.to_datetime('1900-01-01'), 
    max_value=pd.to_datetime('2025-01-01'),
    help="Select the year when the house was built.",
)

# convert the year as integer
year_built = year_built.year

if st.button("Predict Price"):
    # Prepare the custom data with correct column names
    custom_data = pd.DataFrame([[grliv_area, overall_qual, garage_cars, year_built]], columns=['GrLivArea', 'OverallQual', 'GarageCars', 'YearBuilt'])

    # Scale the custom data using the loaded scaler
    custom_data_scaled = scaler.transform(custom_data)

    # Make the prediction
    y_pred_custom = model.predict(custom_data_scaled)

    # Display the result
    st.success(f"Predicted House Price is: ${y_pred_custom[0]:,.2f}")



