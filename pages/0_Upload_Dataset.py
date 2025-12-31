import streamlit as st
from utils.data_loader import load_dataset

st.header(" Upload FMCG Dataset")

uploaded_file = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])

if uploaded_file:
    df = load_dataset(uploaded_file)
    if df is not None:
        st.success(" Dataset loaded successfully")
        st.dataframe(df.head())
