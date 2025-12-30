import streamlit as st
import plotly.express as px
from utils.column_detector import auto_detect_columns
from utils.forecasting import sales_forecast
from utils.segmentation import outlet_segmentation
from utils.churn_analysis import churn_risk

st.header("🧠 Advanced Analytics & Predictions")

df = st.session_state.get("df")
if df is None:
    st.warning("Upload dataset first")
    st.stop()

cols = auto_detect_columns(df)

required = [
    cols["date"],
    cols["sales"],
    cols["outlet"]
]

if any(v is None for v in required):
    st.error("Required analytics columns not detected")
    st.stop()

# 📈 Sales Forecast
st.subheader("📈 Sales Forecast")

hist, future = sales_forecast(
    df,
    date_col=cols["date"],
    sales_col=cols["sales"]
)

fig1 = px.line(hist, x=cols["date"], y=cols["sales"], title="Historical Sales")
fig2 = px.line(future, x=cols["date"], y=cols["sales"], title="Forecasted Sales")

st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)

# 🧩 Outlet Segmentation
st.subheader("🧩 Outlet Segmentation")

seg_df = outlet_segmentation(
    df,
    outlet_col=cols["outlet"],
    sales_col=cols["sales"],
    orders_col=cols["outlet"]
)

fig3 = px.scatter(
    seg_df,
    x="Total_Sales",
    y="Order_Count",
    color="Segment",
    hover_name=cols["outlet"],
    title="Outlet Segmentation"
)
st.plotly_chart(fig3, use_container_width=True)

# ⚠️ Churn Risk
st.subheader("⚠️ Outlet Churn Risk")

churn_df = churn_risk(
    df,
    outlet_col=cols["outlet"],
    date_col=cols["date"]
)

fig4 = px.histogram(
    churn_df,
    x="Churn_Risk",
    title="Churn Risk Distribution"
)
st.plotly_chart(fig4, use_container_width=True)

st.dataframe(churn_df.sort_values("Days_Since_Last_Order", ascending=False))
