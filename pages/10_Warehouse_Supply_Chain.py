import streamlit as st
import plotly.express as px
from utils.column_detector import auto_detect_columns
from utils.warehouse_metrics import (
    warehouse_kpis,
    warehouse_asset_analysis
)

st.header("🏭 Warehouse & Supply Chain Performance")

df = st.session_state.get("df")
if df is None:
    st.warning("Upload dataset first")
    st.stop()

cols = auto_detect_columns(df)

required = [
    cols["warehouse"],
    cols["sales"],
    cols["quantity"],
    cols["asset_type"]
]

if any(v is None for v in required):
    st.error("Warehouse related columns not detected")
    st.stop()

# KPIs
warehouse_df = warehouse_kpis(
    df,
    warehouse_col=cols["warehouse"],
    sales_col=cols["sales"],
    qty_col=cols["quantity"]
)

c1, c2, c3 = st.columns(3)
c1.metric("Total Warehouses", warehouse_df.shape[0])
c2.metric("Total Sales", f"₹{warehouse_df['Total_Sales'].sum():,.0f}")
c3.metric("Total Quantity", f"{warehouse_df['Total_Quantity'].sum():,.0f}")

# Warehouse Performance Bar
fig1 = px.bar(
    warehouse_df.sort_values("Total_Sales", ascending=False),
    x=cols["warehouse"],
    y="Total_Sales",
    title="Warehouse-wise Sales Performance"
)
st.plotly_chart(fig1, use_container_width=True)

# Asset Owned vs Non-Owned
asset_df = warehouse_asset_analysis(
    df,
    warehouse_col=cols["warehouse"],
    asset_col=cols["asset_type"],
    sales_col=cols["sales"]
)

fig2 = px.bar(
    asset_df,
    x=cols["warehouse"],
    y="Sales",
    color=cols["asset_type"],
    title="Owned vs Non-Owned Warehouse Performance"
)
st.plotly_chart(fig2, use_container_width=True)

# Warehouse Table
st.subheader("📋 Warehouse Performance Table")
st.dataframe(
    warehouse_df.sort_values("Total_Sales", ascending=False)
)
