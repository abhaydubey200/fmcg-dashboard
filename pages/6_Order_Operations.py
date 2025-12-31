import streamlit as st
from utils.data_loader import get_dataset

st.title(" Order Operations")

df = get_dataset()
if df is None:
    st.stop()

st.dataframe(df.head())
