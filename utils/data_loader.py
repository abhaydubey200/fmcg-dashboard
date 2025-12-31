import streamlit as st
from utils.data_loader import load_dataset, save_dataset

st.title(" Upload FMCG Dataset")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel file",
    type=["csv", "xls", "xlsx"]
)

if uploaded_file:
    df = load_dataset(uploaded_file)
    if df is not None:
        save_dataset(df)
        st.success(" Dataset uploaded successfully")
        st.dataframe(df.head())
