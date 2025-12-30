import streamlit as st
from utils.data_loader import load_data
from utils.visualizations import plot_top_categories

st.title("🏪 Outlet Analysis Dashboard")

uploaded_file = st.file_uploader("Upload FMCG file", type=["csv","xlsx"], key="outlet")

if uploaded_file:
    df = load_data(uploaded_file)
    if df is not None:
        st.subheader("Top Outlets by Sales Amount")
        fig = plot_top_categories(df, 'OUTLET_NAME', value_col='AMOUNT', top_n=20)
        if fig:
            st.plotly_chart(fig, use_container_width=True)

        st.subheader("Outlets by City")
        fig = plot_top_categories(df, 'CITY', value_col='AMOUNT')
        if fig:
            st.plotly_chart(fig, use_container_width=True)
