import streamlit as st
import pandas as pd
from utils.visualizations import plot_sales_over_time, plot_sales_by_category

st.title("Sales Analysis")

if 'df' in st.session_state:
    df = st.session_state['df']

    st.subheader("Sales Over Time")
    st.plotly_chart(plot_sales_over_time(df, "ORDER_DATE", "AMOUNT"), use_container_width=True)

    st.subheader("Sales by Category")
    st.plotly_chart(plot_sales_by_category(df, "CATEGORY", "AMOUNT"), use_container_width=True)
else:
    st.warning("Please upload a dataset first on the Upload Dataset page.")
