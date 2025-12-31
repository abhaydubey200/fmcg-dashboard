import streamlit as st
import plotly.express as px

from utils.data_loader import get_dataset
from utils.column_detector import detect_columns
from utils.metrics import calculate_kpis

st.set_page_config(page_title="Executive Overview", layout="wide")

st.title(" Executive Overview (CXO Dashboard)")

df = get_dataset()

if df is None:
    st.warning(" Please upload a dataset from 'Upload Dataset' page.")
    st.stop()

cols = detect_columns(df)

kpis = calculate_kpis(df, cols)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Sales", f"{kpis['total_sales']:,.0f}")
c2.metric("Total Orders", kpis["total_orders"])
c3.metric("Active Outlets", kpis["active_outlets"])
c4.metric("Avg Order Value", f"{kpis['avg_order_value']:,.0f}")

# Sales Trend
if cols.get("date") and cols.get("sales"):
    trend = (
        df.groupby(cols["date"])[cols["sales"]]
        .sum()
        .reset_index()
    )

    fig = px.line(
        trend,
        x=cols["date"],
        y=cols["sales"],
        title="Sales Trend Over Time"
    )

    st.plotly_chart(fig, use_container_width=True)
