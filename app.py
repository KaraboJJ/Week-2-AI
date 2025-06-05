import streamlit as st
import pandas as pd
import numpy as np
import joblib

from sklearn.ensemble import RandomForestRegressor


model = joblib.load("crop_yield_model.pkl")

st.title("Crop Yield Predictor")
st.subheader("Aligned with UN SDG 2: Zero Hunger")
st.markdown("Enter environmental and agricultural factors to predict expected crop yield.")

crop = st.selectbox("Crop Type", ["Wheat", "Rice", "Maize"])
region = st.selectbox("Region", ["Africa", "Asia", "Europe"])
soil_type = st.selectbox("Soil Type", ["Sandy", "Loamy", "Clay"])
rainfall = st.slider("Rainfall (mm)", 0, 1000, 500)
temperature = st.slider("Avg Temperature (°C)", 5, 45, 25)
fertilizer_used = st.slider("Fertilizer Used (kg/ha)", 0, 500, 100)

def encode_inputs(crop, region, soil_type, rainfall, temperature, fertilizer_used):
    input_dict = {
        'Rainfall': rainfall,
        'Temperature': temperature,
        'Fertilizer_Used': fertilizer_used,
        'Crop_Rice': 1 if crop == "Rice" else 0,
        'Crop_Wheat': 1 if crop == "Wheat" else 0,
        'Region_Europe': 1 if region == "Europe" else 0,
        'Region_Asia': 1 if region == "Asia" else 0,
        'Region_Africa': 1 if region == "Africa" else 0,
        'Soil_Type_Loamy': 1 if soil_type == "Loamy" else 0,
        'Soil_Type_Sandy': 1 if soil_type == "Sandy" else 0
    }
    return pd.DataFrame([input_dict])

input_data = encode_inputs(crop, region, soil_type, rainfall, temperature, fertilizer_used)

if st.button("Predict Yield"):
    yield_prediction = model.predict(input_data)[0]
    st.success(f"Estimated Crop Yield: **{yield_prediction:.2f} tons/hectare**")
