import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.set_page_config(page_title="🏠 House Price Predictor - Pakistan", layout="centered")

st.title("🏠 House Price Prediction (Pakistan)")
st.markdown("Enter the details below to estimate house price:")

# User Inputs
city = st.selectbox("City", ['Lahore', 'Karachi', 'Islamabad', 'Rawalpindi', 'Multan'])
location = st.selectbox("Location", [
    'DHA Phase 6', 'Gulshan-e-Iqbal', 'G-11', 'Bahria Town', 'Model Town',
    'Johar Town', 'North Nazimabad', 'F-10', 'Saddar', 'Wapda Town'
])
bedrooms = st.slider("Bedrooms", 1, 10, 3)
bathrooms = st.slider("Bathrooms", 1, 10, 2)
area_sqft = st.number_input("Area (sqft)", min_value=500, max_value=10000, value=2000)
year_built = st.number_input("Year Built", min_value=1980, max_value=2025, value=2015)

# Predict button
if st.button("Predict Price"):
    # Prepare input DataFrame
    input_data = pd.DataFrame({
        'City': [city],
        'Location': [location],
        'Bedrooms': [bedrooms],
        'Bathrooms': [bathrooms],
        'Area_sqft': [area_sqft],
        'Year_Built': [year_built]
    })

    # Predict
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated House Price: Rs. {int(prediction):,}")