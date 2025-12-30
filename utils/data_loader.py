import pandas as pd
import streamlit as st

# Session state key to store dataset
DATA_KEY = "fmcg_data"

def load_dataset():
    """Load dataset once and store it in session state"""
    if DATA_KEY not in st.session_state:
        uploaded_file = st.file_uploader("Upload your FMCG dataset (Excel/CSV)", type=["xlsx", "csv"])
        if uploaded_file:
            try:
                if uploaded_file.name.endswith(".csv"):
                    df = pd.read_csv(uploaded_file)
                else:
                    df = pd.read_excel(uploaded_file)
                st.session_state[DATA_KEY] = df
                st.success("Dataset loaded successfully!")
            except Exception as e:
                st.error(f"Error loading file: {e}")
                return None
        else:
            return None
    return st.session_state.get(DATA_KEY, None)
