import streamlit as st
from utils.data_loader import load_dataset

st.title("Upload FMCG Dataset")

uploaded_file = st.file_uploader("Upload your Excel or CSV file", type=["csv", "xlsx"])
if uploaded_file is not None:
    df = load_dataset(uploaded_file)
    st.session_state['df'] = df  # Store dataset in session state
    st.success("Dataset uploaded successfully!")
    st.dataframe(df.head())
