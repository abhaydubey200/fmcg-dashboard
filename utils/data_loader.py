import streamlit as st
import pandas as pd

def load_dataset(uploaded_file):
    if uploaded_file is None:
        return None

    try:
        if uploaded_file.name.endswith(".csv"):
            return pd.read_csv(uploaded_file)

        if uploaded_file.name.endswith((".xlsx", ".xls")):
            return pd.read_excel(uploaded_file)

    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return None


def save_dataset(df):
    st.session_state["dataset"] = df


def get_dataset():
    return st.session_state.get("dataset", None)
