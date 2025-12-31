import streamlit as st
from utils.data_loader import get_dataset
from utils.metrics import calculate_kpis

st.title(" Executive Overview")

df = get_dataset()
if df is None:
    st.warning("Upload dataset first")
    st.stop()

kpis = calculate_kpis(df)

c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Sales", f"{kpis.get('total_sales', 0):,.0f}")
c2.metric("Total Orders", kpis.get("total_orders", 0))
c3.metric("Total Quantity", kpis.get("total_quantity", 0))
c4.metric("Avg Order Value", f"{kpis.get('avg_order_value', 0):,.2f}")
