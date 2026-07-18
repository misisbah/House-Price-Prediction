import streamlit as st
import joblib
import pandas as pd

# ==========================
# Load Trained Model
# ==========================
model = joblib.load("house_price_prediction_model.pkl")

# ==========================
# Page Config
# ==========================
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# Custom CSS
# ==========================
st.markdown("""
    <style>
        .main {
            padding-top: 1rem;
        }
        .stButton>button {
            width: 100%;
            background-color: #2E7D32;
            color: white;
            font-weight: 600;
            font-size: 1.1rem;
            padding: 0.6rem 0;
            border-radius: 10px;
            border: none;
            transition: background-color 0.2s ease;
        }
        .stButton>button:hover {
            background-color: #1B5E20;
            color: white;
        }
        .result-card {
            background: linear-gradient(135deg, #2E7D32 0%, #43A047 100%);
            padding: 2rem;
            border-radius: 16px;
            text-align: center;
            color: white;
            margin-top: 1.5rem;
        }
        .result-card h2 {
            color: white;
            margin: 0;
            font-size: 2.2rem;
        }
        .result-card p {
            margin: 0.3rem 0 0 0;
            opacity: 0.9;
        }
        .section-title {
            font-size: 1.1rem;
            font-weight: 600;
            color: #2E7D32;
            margin-top: 0.5rem;
            margin-bottom: 0.5rem;
        }
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)

# ==========================
# Sidebar
# ==========================
with st.sidebar:
    st.markdown("## 🏠 About")
    st.write(
        "This app predicts a house's sale price based on key property "
        "features using a trained machine learning model."
    )
    st.markdown("---")
    st.markdown("**Model inputs used:**")
    st.markdown(
        "- Overall Quality\n"
        "- Living Area\n"
        "- Garage Capacity\n"
        "- Basement Area\n"
        "- Year Built\n"
        "- Bathrooms & Bedrooms\n"
        "- Lot Area"
    )
    st.markdown("---")
    st.caption("Developed by Misbah Bibi ❤️")

# ==========================
# Header
# ==========================
st.title("🏠 House Price Prediction")
st.write("Enter the house details below to get an estimated sale price.")
st.divider()

# ==========================
# User Inputs (organized in columns)
# ==========================
st.markdown('<p class="section-title">🏗️ Structure & Quality</p>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    overall_quality = st.slider("Overall Quality", 1, 10, 5)
with col2:
    year_built = st.number_input("Year Built", min_value=1900, max_value=2025, value=2005)
with col3:
    garage_cars = st.slider("Garage Capacity (Cars)", 0, 5, 2)

st.markdown('<p class="section-title">📐 Area Details</p>', unsafe_allow_html=True)
col4, col5, col6 = st.columns(3)
with col4:
    gr_liv_area = st.number_input("Ground Living Area (sq ft)", min_value=100, value=1500)
with col5:
    total_bsmt_sf = st.number_input("Total Basement Area (sq ft)", min_value=0, value=900)
with col6:
    lot_area = st.number_input("Lot Area (sq ft)", min_value=1000, value=8000)

st.markdown('<p class="section-title">🛏️ Rooms</p>', unsafe_allow_html=True)
col7, col8 = st.columns(2)
with col7:
    full_bath = st.slider("Full Bathrooms", 0, 5, 2)
with col8:
    bedrooms = st.slider("Bedrooms Above Ground", 1, 10, 3)

st.divider()

# ==========================
# Prediction
# ==========================
predict_col = st.columns([1, 2, 1])[1]
with predict_col:
    predict_clicked = st.button("🔮 Predict House Price")

if predict_clicked:
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

    with st.spinner("Calculating estimate..."):
        prediction = model.predict(input_data)

    st.markdown(f"""
        <div class="result-card">
            <p>Estimated Sale Price</p>
            <h2>${prediction[0]:,.2f}</h2>
        </div>
    """, unsafe_allow_html=True)

st.divider()
st.caption("Developed by Misbah Bibi ❤️")
