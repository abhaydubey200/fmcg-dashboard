import streamlit as st
from utils.visualizations import plot_top_skus

st.title("SKU Analysis")

if 'df' in st.session_state:
    df = st.session_state['df']
    st.plotly_chart(plot_top_skus(df, top_n=15), use_container_width=True)
else:
    st.warning("Please upload a dataset first on the Upload page.")
