import streamlit as st
import joblib
import pandas as pd

st.title("🏠 House Price Prediction App")

model = joblib.load("Models/best_model.pkl")

st.sidebar.header("Input Features")
area = st.sidebar.number_input("Area (sq ft)", min_value=500, max_value=10000, value=2000)
rooms = st.sidebar.slider("Number of Rooms", 1, 10, 3)
location = st.sidebar.selectbox("Location", ["Urban", "Suburban", "Rural"])

input_data = pd.DataFrame({
    "Area": [area],
    "Rooms": [rooms],
    "Location": [location]
})

if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated House Price: ${prediction:,.2f}")
