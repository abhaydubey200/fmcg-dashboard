import streamlit as st
from utils.visualizations import plot_sales_by_city

st.title("Sales Analysis")

if 'df' in st.session_state:
    df = st.session_state['df']
    st.plotly_chart(plot_sales_by_city(df), use_container_width=True)
else:
    st.warning("Please upload a dataset first on the Upload page.")
