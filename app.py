import streamlit as st
import joblib
import pandas as pd

# ==========================
# Load Trained Model
# ==========================

model = joblib.load("house_price_prediction_model.pkl")

# ==========================
# App Title
# ==========================

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

st.title("🏠 House Price Prediction")
st.write("Enter the house details below to predict the estimated sale price.")

st.divider()

# ==========================
# User Inputs
# ==========================

overall_quality = st.slider(
    "Overall Quality",
    min_value=1,
    max_value=10,
    value=5
)

gr_liv_area = st.number_input(
    "Ground Living Area (sq ft)",
    min_value=100,
    value=1500
)

garage_cars = st.slider(
    "Garage Capacity (Cars)",
    min_value=0,
    max_value=5,
    value=2
)

total_bsmt_sf = st.number_input(
    "Total Basement Area (sq ft)",
    min_value=0,
    value=900
)

year_built = st.number_input(
    "Year Built",
    min_value=1900,
    max_value=2025,
    value=2005
)

full_bath = st.slider(
    "Full Bathrooms",
    min_value=0,
    max_value=5,
    value=2
)

bedrooms = st.slider(
    "Bedrooms Above Ground",
    min_value=1,
    max_value=10,
    value=3
)

lot_area = st.number_input(
    "Lot Area (sq ft)",
    min_value=1000,
    value=8000
)

# ==========================
# Prediction
# ==========================

if st.button("Predict House Price"):

    input_data = pd.DataFrame([{
        "OverallQual": overall_quality,
        "GrLivArea": gr_liv_area,
        "GarageCars": garage_cars,
        "TotalBsmtSF": total_bsmt_sf,
        "YearBuilt": year_built,
        "FullBath": full_bath,
        "BedroomAbvGr": bedrooms,
        "LotArea": lot_area
    }])

    prediction = model.predict(input_data)

    st.success(f"🏡 Estimated House Price: ${prediction[0]:,.2f}")

st.divider()

st.caption("Developed by Misbah Bibi ❤️")