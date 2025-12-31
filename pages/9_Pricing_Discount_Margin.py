# pages/9_Pricing_Discount_Margin.py

import streamlit as st
import pandas as pd
import plotly.express as px
from utils.pricing_metrics import calculate_pricing_metrics

st.set_page_config(
    page_title="Pricing, Discount & Margin",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title(" Pricing, Discount & Margin Dashboard")

uploaded_file = st.sidebar.file_uploader(
    "Upload your dataset (Excel/CSV)", type=["csv", "xlsx"]
)

if uploaded_file is not None:
    try:
        # Load dataset safely
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file, engine='openpyxl')

        st.success(f"Dataset loaded successfully! Shape: {df.shape}")

        # Check required columns
        required_cols = ["SKU_ID", "UNITPRICE", "AMOUNT", "DISCOUNT_AMOUNT", "TOTAL_QUANTITY"]
        missing_cols = [col for col in required_cols if col not in df.columns]

        if missing_cols:
            st.warning(f"Missing columns for Pricing Analysis: {missing_cols}")
        else:
            pricing_df = calculate_pricing_metrics(df)

            # KPI Cards
            st.subheader("Key Metrics")
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Total Sales Amount", f"{pricing_df['Total_Sales'].sum():,.2f}")
            col2.metric("Total Discount", f"{pricing_df['Total_Discount'].sum():,.2f}")
            col3.metric("Avg Price per Unit", f"{pricing_df['Avg_UnitPrice'].mean():.2f}")
            col4.metric("Gross Margin %", f"{pricing_df['Margin_Percentage'].mean():.2f}%")

            # Top SKUs by Sales
            st.subheader("Top 10 SKUs by Sales")
            top_skus = pricing_df.nlargest(10, "Total_Sales")
            fig_sku = px.bar(top_skus, x="SKU_ID", y="Total_Sales", text="Total_Sales")
            st.plotly_chart(fig_sku, use_container_width=True)

            # Discount vs Sales Scatter
            st.subheader("Discount vs Sales Scatter")
            fig_disc = px.scatter(pricing_df, x="Total_Discount", y="Total_Sales", color="SKU_ID",
                                  size="Total_Quantity", hover_data=["SKU_ID"])
            st.plotly_chart(fig_disc, use_container_width=True)

    except Exception as e:
        st.error(f"Error loading dataset: {e}")

else:
    st.info("Please upload a dataset to start Pricing & Margin analysis.")
