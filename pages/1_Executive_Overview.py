import streamlit as st
import plotly.express as px

from utils.data_loader import get_dataset
from utils.column_detector import detect_columns
from utils.kpi_engine import calculate_kpis

st.set_page_config(page_title="Executive Overview", layout="wide")

st.title(" Executive Overview (CXO Dashboard)")

df = get_dataset()

if df is None:
    st.warning(" Please upload a dataset first.")
    st.stop()

cols = detect_columns(df)
kpis = calculate_kpis(df, cols)

# ---------- KPI ROW ----------
c1, c2, c3, c4, c5, c6 = st.columns(6)

c1.metric(" Total Sales", f"₹ {kpis['total_sales']:,.0f}")
c2.metric(" Active Outlets", kpis["active_outlets"])
c3.metric(" Total Quantity", f"{kpis['total_qty']:,.0f}")
c4.metric(" Avg Order Value", f"₹ {kpis['aov']:,.0f}")
c5.metric(" Discount %", f"{kpis['discount_pct']}%")
c6.metric(" Orders", df[cols["order_id"]].nunique() if cols.get("order_id") else 0)

st.divider()

# ---------- SALES TREND ----------
date_col = cols.get("date")
sales_col = cols.get("sales")

if date_col and sales_col:
    trend = (
        df.groupby(pd.to_datetime(df[date_col]).dt.to_period("M"))[sales_col]
        .sum()
        .reset_index()
    )
    trend[date_col] = trend[date_col].astype(str)

    fig = px.line(
        trend,
        x=date_col,
        y=sales_col,
        title=" Sales Trend (Monthly)"
    )

    st.plotly_chart(fig, use_container_width=True)
else:
    st.info(" Date column not detected for trend analysis.")
