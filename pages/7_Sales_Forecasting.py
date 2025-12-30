import streamlit as st
import plotly.express as px
from utils.column_detector import auto_detect_columns
from utils.forecasting import prepare_time_series, forecast_sales

st.header("🔮 Sales Forecasting Dashboard")

df = st.session_state.get("df")
if df is None:
    st.warning("Upload dataset first")
    st.stop()

cols = auto_detect_columns(df)

if not cols["date"] or not cols["sales"]:
    st.error("Date or Sales column not detected")
    st.stop()

periods = st.slider("Forecast Days", 7, 180, 30)

ts = prepare_time_series(df, cols["date"], cols["sales"])
forecast_df = forecast_sales(ts, periods)

fig = px.line(ts, x=ts.columns[0], y=ts.columns[1], title="Historical Sales")
fig.add_scatter(
    x=forecast_df["Date"],
    y=forecast_df["Forecast_Sales"],
    mode="lines",
    name="Forecast"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("📊 Forecast Table")
st.dataframe(forecast_df)
