import streamlit as st
import pandas as pd

SESSION_KEY = "fmcg_df"


def load_dataset(uploaded_file):
    """Load CSV or Excel file"""
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith((".xls", ".xlsx")):
            df = pd.read_excel(uploaded_file)
        else:
            st.error("Unsupported file format")
            return None
        return df
    except Exception as e:
        st.error(f"File load failed: {e}")
        return None


def save_dataset(df):
    """Save dataset to session"""
    st.session_state[SESSION_KEY] = df


def get_dataset():
    """Safely get dataset from session"""
    df = st.session_state.get(SESSION_KEY)
    if df is None:
        st.warning("⚠️ Please upload dataset first")
        return None
    return df
