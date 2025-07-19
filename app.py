
import streamlit as st
from utils.auth import create_user_table, verify_user
import pages.dashboard as dashboard
import pages.fraud_detection as detection

create_user_table()

st.sidebar.title("🔐 Login")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")
role = st.sidebar.selectbox("Role", ["analyst", "admin", "auditor"])
login_btn = st.sidebar.button("Login")
if login_btn:
    user = verify_user(username, password)
    if user and user[2] == role:
        st.sidebar.success(f"Welcome, {username} ({role})")
        page = st.selectbox("Navigate to", ["Dashboard", "Fraud Detection"])
        if page == "Dashboard":
            dashboard.run()
        elif page == "Fraud Detection":
            detection.run()
    else:
        st.sidebar.error("Invalid credentials or role mismatch.")
