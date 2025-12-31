# pages/10_Warehouse_Supply_Chain.py

import streamlit as st
import plotly.express as px
import pandas as pd

from utils.column_detector import auto_detect_columns

st.set_page_config(page_title="Warehouse & Supply Chain", layout="wide")
st.title("🏭 Warehouse & Supply Chain Performance")

# Load dataset
df = st.session_state.get("df")

if df is None:
    st.warning(" Please upload dataset from Upload page")
    st.stop()

# Detect columns
cols = auto_detect_columns(df)

warehouse_col = cols.get("warehouse")
sales_col = cols.get("sales")
qty_col = cols.get("quantity")
asset_col = cols.get("asset_owned")

# -------- VALIDATION --------
if warehouse_col is None:
    st.error(" Warehouse column not detected in dataset")
    st.info(" Expected names: warehouse, warehouse_name, depot, dc")
    st.stop()

# -------- KPI SECTION --------
st.subheader(" Supply Chain KPIs")

kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:
    st.metric(
        "Total Warehouses",
        df[warehouse_col].nunique()
    )

with kpi2:
    if sales_col:
        st.metric(
            "Total Sales",
            f"{df[sales_col].sum():,.0f}"
        )
    else:
        st.metric("Total Sales", "N/A")

with kpi3:
    if qty_col:
        st.metric(
            "Total Quantity",
            f"{df[qty_col].sum():,.0f}"
        )
    else:
        st.metric("Total Quantity", "N/A")

# -------- WAREHOUSE PERFORMANCE --------
st.subheader(" Warehouse-wise Performance")

group_cols = [warehouse_col]
agg_map = {}

if sales_col:
    agg_map[sales_col] = "sum"
if qty_col:
    agg_map[qty_col] = "sum"

warehouse_perf = (
    df
    .groupby(group_cols)
    .agg(agg_map)
    .reset_index()
)

warehouse_perf.rename(columns={
    sales_col: "Total_Sales",
    qty_col: "Total_Quantity"
}, inplace=True)

st.dataframe(warehouse_perf, use_container_width=True)

# -------- VISUALIZATION --------
if sales_col:
    fig = px.bar(
        warehouse_perf.sort_values("Total_Sales", ascending=False),
        x=warehouse_col,
        y="Total_Sales",
        title="Warehouse-wise Sales",
        text_auto=True
    )
    st.plotly_chart(fig, use_container_width=True)

# -------- ASSET UTILIZATION --------
if asset_col:
    st.subheader(" Asset Utilization")

    asset_df = (
        df
        .groupby([warehouse_col, asset_col])
        .size()
        .reset_index(name="Orders")
    )

    fig2 = px.bar(
        asset_df,
        x=warehouse_col,
        y="Orders",
        color=asset_col,
        title="Asset Owned vs Non-Owned by Warehouse",
        barmode="group"
    )
    st.plotly_chart(fig2, use_container_width=True)
else:
    st.info(" Asset ownership data not available in this dataset")
