import streamlit as st
from utils.column_detector import auto_detect_columns
from utils.data_processing import preprocess
from utils.metrics import *
from utils.visualizations import *

st.header(" Executive Overview")

df = st.session_state.get("df")
if df is None:
    st.warning("Upload dataset first")
    st.stop()

cols = auto_detect_columns(df)

df = preprocess(df, cols["date"])

col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"{kpi_total_sales(df, cols['sales']):,.0f}")
col2.metric("Orders", kpi_orders(df))
col3.metric("Avg Order Value", f"{kpi_aov(df, cols['sales']):,.0f}")

st.plotly_chart(
    line_sales_trend(df, cols["date"], cols["sales"]),
    use_container_width=True
)

if cols["brand"]:
    st.plotly_chart(
        bar_top(df, cols["brand"], cols["sales"], "Top Brands"),
        use_container_width=True
    )
