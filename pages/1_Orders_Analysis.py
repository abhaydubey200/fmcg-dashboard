import streamlit as st
from utils.visualizations import plot_orders_over_time, plot_order_state_distribution

st.title("Orders Analysis")

if 'df' in st.session_state:
    df = st.session_state['df']

    st.plotly_chart(plot_orders_over_time(df, 'ORDER_DATE'), use_container_width=True)
    st.plotly_chart(plot_order_state_distribution(df), use_container_width=True)
else:
    st.warning("Please upload a dataset first on the Upload page.")
