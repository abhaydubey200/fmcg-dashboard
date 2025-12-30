import streamlit as st
from utils.visualizations import plot_sku_by_brand, plot_sku_quantity_distribution

st.title("SKU Analysis")

if 'df' in st.session_state:
    df = st.session_state['df']

    st.subheader("SKU by Brand")
    st.plotly_chart(plot_sku_by_brand(df, "BRAND", "TOTAL_QUANTITY"), use_container_width=True)

    st.subheader("SKU Quantity Distribution")
    st.plotly_chart(plot_sku_quantity_distribution(df, "TOTAL_QUANTITY"), use_container_width=True)
else:
    st.warning("Please upload a dataset first on the Upload Dataset page.")
