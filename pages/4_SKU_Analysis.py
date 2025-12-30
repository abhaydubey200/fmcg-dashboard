import streamlit as st
from utils.data_loader import load_data
from utils.visualizations import plot_top_categories

st.title("📦 SKU Analysis Dashboard")

uploaded_file = st.file_uploader("Upload FMCG file", type=["csv","xlsx"], key="sku")

if uploaded_file:
    df = load_data(uploaded_file)
    if df is not None:
        st.subheader("Top Selling SKUs")
        fig = plot_top_categories(df, 'SKU_PLACED', value_col='TOTAL_QUANTITY', top_n=20)
        if fig:
            st.plotly_chart(fig, use_container_width=True)

        st.subheader("Top Brands by Amount")
        fig = plot_top_categories(df, 'BRAND', value_col='AMOUNT', top_n=10)
        if fig:
            st.plotly_chart(fig, use_container_width=True)
