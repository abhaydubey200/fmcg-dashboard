import streamlit as st
import pandas as pd
from utils.visualizations import plot_orders_over_time, plot_order_state_distribution

st.title("Orders Analysis")

if 'df' in st.session_state:
    df = st.session_state['df']

    st.subheader("Orders Over Time")
    date_col = "ORDER_DATE"  # Adjust based on dataset
    st.plotly_chart(plot_orders_over_time(df, date_col), use_container_width=True)

    st.subheader("Order State Distribution")
    st.plotly_chart(plot_order_state_distribution(df, "ORDERSTATE"), use_container_width=True)
else:
    st.warning("Please upload a dataset first on the Upload Dataset page.")
