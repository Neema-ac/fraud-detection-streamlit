
import streamlit as st
import pandas as pd
import joblib

MODEL_PATH = 'fraud_detection_app/model/fraud_model.pkl'

def run():
    st.title("🕵️ Fraud Detection")
    uploaded = st.file_uploader("Upload CSV transaction data", type=['csv'])
    if uploaded:
        model = joblib.load(MODEL_PATH)
        df = pd.read_csv(uploaded)
        predictions = model.predict(df)
        df['Prediction'] = predictions
        st.write(df[df['Prediction'] == 1])
        st.success(f"Detected {sum(predictions)} potential frauds")
