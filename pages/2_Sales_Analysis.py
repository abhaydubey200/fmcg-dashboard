import streamlit as st
from utils.data_loader import load_data, detect_columns
from utils.visualizations import plot_orders_over_time, plot_top_categories

st.title("📈 Sales Analysis Dashboard")

uploaded_file = st.file_uploader("Upload FMCG file", type=["csv","xlsx"], key="sales")

if uploaded_file:
    df = load_data(uploaded_file)
    if df is not None:
        date_cols, num_cols, cat_cols = detect_columns(df)

        st.subheader("Orders Over Time")
        if date_cols:
            st.plotly_chart(plot_orders_over_time(df, date_cols[0]), use_container_width=True)

        st.subheader("Top Categories / SKUs")
        for col in ['CATEGORY','SKU_PLACED','BRAND']:
            fig = plot_top_categories(df, col)
            if fig:
                st.plotly_chart(fig, use_container_width=True)
