import streamlit as st
from utils.data_loader import get_dataset
from utils.visualizations import time_series

st.title(" Sales Performance")

df = get_dataset()
if df is None:
    st.stop()

st.plotly_chart(
    time_series(df, "date", "sales", "Sales Trend"),
    use_container_width=True
)
