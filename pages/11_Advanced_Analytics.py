# pages/11_Advanced_Analytics.py

import streamlit as st
import pandas as pd
import plotly.express as px
from utils.forecasting import prepare_time_series, sales_forecast
from utils.churn_analysis import detect_churn_outlets

st.set_page_config(
    page_title="Advanced Analytics",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 Advanced Analytics Dashboard")

# Sidebar: Upload Dataset
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

        st.header("1️⃣ Sales Forecasting")

        # Detect possible date & value columns
        date_cols = [col for col in df.columns if "date" in col.lower()]
        value_cols = [col for col in df.columns if col.lower() in ["amount", "total_quantity", "sales"]]

        if date_cols and value_cols:
            date_col = st.selectbox("Select Date Column", date_cols)
            value_col = st.selectbox("Select Value Column", value_cols)

            ts_df = prepare_time_series(df, date_col, value_col)
            forecast_df = sales_forecast(ts_df, periods=6)

            if forecast_df is not None:
                fig = px.line(
                    pd.concat([ts_df.rename(columns={"y": "Actual"}), forecast_df.rename(columns={"yhat": "Forecast"})], axis=0),
                    x="ds",
                    y=["y", "yhat"],
                    labels={"ds": "Date", "value": "Sales"},
                    title="Sales Forecast"
                )
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("Not enough data for forecasting.")
        else:
            st.warning("Dataset must have at least one date column and one numeric value column for forecasting.")

        st.header("2️⃣ Outlet Churn Analysis")
        if "OUTLET_ID" in df.columns and "ORDER_DATE" in df.columns:
            churn_results = detect_churn_outlets(df)
            st.dataframe(churn_results)
            fig_churn = px.pie(
                churn_results, names="Churn_Status", values="Count",
                title="Outlet Churn Distribution"
            )
            st.plotly_chart(fig_churn, use_container_width=True)
        else:
            st.info("Churn analysis requires 'OUTLET_ID' and 'ORDER_DATE' columns.")

    except Exception as e:
        st.error(f"Error loading dataset: {e}")
else:
    st.info("Please upload a dataset to start advanced analytics.")
