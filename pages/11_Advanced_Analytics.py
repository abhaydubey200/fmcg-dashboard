import streamlit as st
import plotly.express as px

from utils.column_detector import auto_detect_columns
from utils.forecasting import prepare_time_series, sales_forecast

st.set_page_config(page_title="Advanced Analytics", layout="wide")
st.title("🧠 Advanced Analytics Dashboard")

df = st.session_state.get("df")

if df is None:
    st.warning("⚠️ Upload dataset first")
    st.stop()

cols = auto_detect_columns(df)

date_col = cols.get("date")
sales_col = cols.get("sales")

if date_col is None or sales_col is None:
    st.error("❌ Date or Sales column not detected")
    st.info("ℹ️ Required for forecasting: order_date + sales/amount")
    st.stop()

# ---------- PREPARE TIME SERIES ----------
ts_df = prepare_time_series(df, date_col, sales_col)

if ts_df is None or ts_df.empty:
    st.warning("Not enough data for forecasting")
    st.stop()

# ---------- FORECAST ----------
forecast_df = sales_forecast(ts_df, periods=6)

# ---------- VISUAL ----------
st.subheader("📈 Sales Forecast (Next 6 Periods)")

fig = px.line(
    ts_df,
    x="ds",
    y="y",
    markers=True,
    title="Historical Sales"
)

if forecast_df is not None:
    fig.add_scatter(
        x=forecast_df["ds"],
        y=forecast_df["yhat"],
        mode="lines+markers",
        name="Forecast",
        line=dict(dash="dash")
    )

st.plotly_chart(fig, use_container_width=True)

# ---------- INSIGHTS ----------
st.subheader("📌 Forecast Insights")

avg_growth = ts_df["y"].pct_change().mean() * 100

st.metric(
    "Avg Historical Growth %",
    f"{avg_growth:.2f}%"
)

st.info(
    "Forecast is based on recent moving average trend. "
    "Advanced ML models can be plugged later."
)
