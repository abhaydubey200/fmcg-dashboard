import streamlit as st
from utils.data_loader import get_dataset
from utils.pricing_metrics import pricing_summary

st.title(" Pricing & Margin")

df = get_dataset()
if df is None:
    st.stop()

st.dataframe(pricing_summary(df))
