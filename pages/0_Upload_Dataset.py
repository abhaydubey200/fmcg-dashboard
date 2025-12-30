import streamlit as st
import pandas as pd

st.title("Upload Your FMCG Dataset")

if "df" not in st.session_state:
    uploaded_file = st.file_uploader("Upload your dataset (CSV or Excel)", type=["csv", "xlsx"])
    if uploaded_file:
        try:
            if uploaded_file.name.endswith(".csv"):
                st.session_state.df = pd.read_csv(uploaded_file)
            else:
                st.session_state.df = pd.read_excel(uploaded_file)
            st.success("Dataset uploaded successfully! Navigate to other pages now.")
        except Exception as e:
            st.error(f"Error loading dataset: {e}")
else:
    st.success("Dataset already uploaded. You can navigate to other pages.")
    st.dataframe(st.session_state.df.head(10))
