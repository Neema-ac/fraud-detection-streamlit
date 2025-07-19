
import streamlit as st
import pandas as pd
def run():
    st.title("📊 Dashboard")
    uploaded = st.file_uploader("Upload CSV", type=["csv"])
    if uploaded:
        df = pd.read_csv(uploaded)
        st.dataframe(df.head())
        st.metric("Total Transactions", len(df))
        if 'Time' in df.columns:
            st.metric("Unique Time Entries", df['Time'].nunique())
