# pages/7_Sales_Forecasting.py

import streamlit as st
import plotly.express as px

from utils.forecasting import prepare_time_series, forecast_sales
from utils.column_detector import auto_detect_columns

st.set_page_config(page_title="Sales Forecasting", layout="wide")

st.title("📈 Sales Forecasting Dashboard")

df = st.session_state.get("df")
if df is None:
    st.warning("⚠️ Please upload dataset first")
    st.stop()

cols = auto_detect_columns(df)

date_col = cols.get("date")
sales_col = cols.get("sales")

if not date_col or not sales_col:
    st.error("❌ Date or Sales column not detected")
    st.stop()

# Prepare Time Series
ts_df = prepare_time_series(df, date_col, sales_col)

# Historical Sales
st.subheader("📊 Historical Sales Trend")
fig1 = px.line(
    ts_df,
    x=date_col,
    y=sales_col,
    markers=True
)
st.plotly_chart(fig1, use_container_width=True)

# Forecast
st.subheader("🔮 Sales Forecast")
months = st.slider("Forecast Months", 3, 12, 6)

forecast_df = forecast_sales(ts_df, periods=months)

fig2 = px.line(
    forecast_df,
    x=date_col,
    y=sales_col,
    markers=True
)
st.plotly_chart(fig2, use_container_width=True)

# Combined View
st.subheader("📈 Actual vs Forecast")

combined = ts_df[[date_col, sales_col]].copy()
combined["Type"] = "Actual"

forecast_df["Type"] = "Forecast"

final_df = combined._append(forecast_df, ignore_index=True)

fig3 = px.line(
    final_df,
    x=date_col,
    y=sales_col,
    color="Type",
    markers=True
)
st.plotly_chart(fig3, use_container_width=True)
