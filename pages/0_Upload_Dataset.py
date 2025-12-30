import streamlit as st
import pandas as pd
from utils.data_loader import load_dataset

st.title("Upload FMCG Dataset")

uploaded_file = st.file_uploader("Upload your Excel/CSV file", type=["csv", "xlsx"])

if uploaded_file:
    try:
        df = load_dataset(uploaded_file)
        st.session_state['df'] = df
        st.success("Dataset loaded successfully!")
        st.dataframe(df.head())
    except Exception as e:
        st.error(f"Error loading dataset: {e}")
