import streamlit as st
from utils.data_loader import load_dataset, save_dataset

st.set_page_config(page_title="Upload Dataset", layout="wide")

st.title(" Upload FMCG Dataset")

uploaded_file = st.file_uploader(
    "Upload CSV or Excel file",
    type=["csv", "xlsx", "xls"]
)

if uploaded_file:
    df = load_dataset(uploaded_file)

    if df is not None:
        save_dataset(df)
        st.success(" Dataset uploaded successfully!")
        st.write("Preview:")
        st.dataframe(df.head(), use_container_width=True)
