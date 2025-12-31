import streamlit as st
from utils.data_loader import get_dataset
from utils.column_detector import detect_columns
from utils.metrics import calculate_kpis

st.title(" Executive Overview")

df = get_dataset()

if df is None:
    st.warning("Please upload a dataset first.")
    st.stop()

cols = detect_columns(df)
kpis = calculate_kpis(df, cols)

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Sales", f"{kpis['total_sales']:,.0f}")
c2.metric("Total Orders", f"{kpis['total_orders']:,}")
c3.metric("Active Outlets", f"{kpis['active_outlets']:,}")
c4.metric("Avg Order Value", f"{kpis['avg_order_value']:,.0f}")
