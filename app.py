import streamlit as st
import pandas as pd
import joblib

# =====================================================
# Page Configuration
# =====================================================

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

# =====================================================
# Load Model
# =====================================================

model = joblib.load("house_price_prediction_model.pkl")

# =====================================================
# Custom CSS
# =====================================================

st.markdown("""
<style>
.main{
    background-color:#f5f7fa;
}

h1{
    color:#0E76A8;
    text-align:center;
}

.prediction-box{
    background-color:#d4edda;
    padding:20px;
    border-radius:10px;
    border:2px solid #28a745;
    text-align:center;
    font-size:28px;
    font-weight:bold;
}

.footer{
    text-align:center;
    color:gray;
    font-size:15px;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# Title
# =====================================================

st.markdown("<h1>🏠 House Price Prediction</h1>", unsafe_allow_html=True)

st.write(
    "Predict the estimated selling price of a house using a trained **Machine Learning Linear Regression Model**."
)

st.divider()

# =====================================================
# Sidebar
# =====================================================

st.sidebar.header("🏠 Enter House Details")

overall_quality = st.sidebar.slider(
    "Overall Quality",
    1,
    10,
    5
)

gr_liv_area = st.sidebar.number_input(
    "Ground Living Area (sq ft)",
    min_value=500,
    max_value=6000,
    value=1500
)

garage_cars = st.sidebar.slider(
    "Garage Cars",
    0,
    5,
    2
)

total_bsmt_sf = st.sidebar.number_input(
    "Basement Area (sq ft)",
    min_value=0,
    max_value=4000,
    value=900
)

year_built = st.sidebar.number_input(
    "Year Built",
    min_value=1900,
    max_value=2025,
    value=2005
)

full_bath = st.sidebar.slider(
    "Full Bathrooms",
    0,
    5,
    2
)

bedrooms = st.sidebar.slider(
    "Bedrooms Above Ground",
    1,
    10,
    3
)

lot_area = st.sidebar.number_input(
    "Lot Area (sq ft)",
    min_value=1000,
    max_value=30000,
    value=8000
)

# =====================================================
# Display Inputs
# =====================================================

st.subheader("📋 House Information")

col1, col2 = st.columns(2)

with col1:
    st.write(f"**Overall Quality:** {overall_quality}")
    st.write(f"**Ground Living Area:** {gr_liv_area} sq ft")
    st.write(f"**Garage Cars:** {garage_cars}")
    st.write(f"**Basement Area:** {total_bsmt_sf} sq ft")

with col2:
    st.write(f"**Year Built:** {year_built}")
    st.write(f"**Full Bathrooms:** {full_bath}")
    st.write(f"**Bedrooms:** {bedrooms}")
    st.write(f"**Lot Area:** {lot_area} sq ft")

st.divider()

# =====================================================
# Prediction
# =====================================================

if st.button("🏠 Predict House Price", use_container_width=True):

    input_data = pd.DataFrame({
        "OverallQual": [overall_quality],
        "GrLivArea": [gr_liv_area],
        "GarageCars": [garage_cars],
        "TotalBsmtSF": [total_bsmt_sf],
        "YearBuilt": [year_built],
        "FullBath": [full_bath],
        "BedroomAbvGr": [bedrooms],
        "LotArea": [lot_area]
    })

    prediction = model.predict(input_data)

    st.markdown(
        f"""
        <div class="prediction-box">
        💰 Estimated House Price <br><br>
        ${prediction[0]:,.2f}
        </div>
        """,
        unsafe_allow_html=True
    )

st.divider()

# =====================================================
# Footer
# =====================================================

st.markdown(
    """
    <div class="footer">
    Developed with ❤️ by <b>Misbah Bibi</b><br>
    Machine Learning Project using Python, Scikit-learn & Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
