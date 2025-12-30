import streamlit as st
from utils.data_loader import load_dataset
from utils.visualizations import plot_orders_over_time

st.title("Orders Analysis")

df = load_dataset()
if df is not None:
    date_cols = [col for col in df.columns if "DATE" in col.upper()]
    if date_cols:
        st.plotly_chart(plot_orders_over_time(df, date_cols[0]), use_container_width=True)
    else:
        st.warning("No date column found in the dataset.")
else:
    st.info("Please upload a dataset to see the analysis.")
