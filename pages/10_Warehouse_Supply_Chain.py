import streamlit as st
import plotly.express as px

from utils.data_loader import get_dataset
from utils.column_detector import detect_columns
from utils.warehouse_metrics import warehouse_sales_summary

st.set_page_config(page_title="Warehouse & Supply Chain", layout="wide")

st.title("🏭 Warehouse & Supply Chain Performance")

df = get_dataset()

if df is None:
    st.warning(" Please upload a dataset first.")
    st.stop()

# Detect required columns
cols = detect_columns(df)

sales_col = cols.get("sales")

if sales_col is None:
    st.error("Sales column not detected in dataset.")
    st.stop()

summary, warehouse_col = warehouse_sales_summary(df, sales_col)

if summary is None:
    st.info(
        " Warehouse / Depot column not found in this dataset.\n\n"
        "Supported names:\n"
        "`warehouse`, `depot`, `distribution_center`, `godown`"
    )
    st.stop()

# KPI
st.metric(
    label="Total Warehouses",
    value=summary[warehouse_col].nunique()
)

# Chart
fig = px.bar(
    summary.head(15),
    x=warehouse_col,
    y=sales_col,
    title="Top Warehouses by Sales",
    labels={sales_col: "Total Sales"},
)

st.plotly_chart(fig, use_container_width=True)

# Table
st.subheader(" Warehouse-wise Sales Details")
st.dataframe(summary, use_container_width=True)
