import streamlit as st
from utils.data_loader import get_dataset
from utils.column_detector import auto_detect_columns
from utils.visualizations import bar_top

st.header(" Product / SKU / Brand Dashboard")

# ---- Load dataset safely from session ----
df = get_dataset()
if df is None:
    st.stop()

# ---- Auto detect columns ----
cols = auto_detect_columns(df)

# ---- SKU Sales ----
if cols.get("sku") and cols.get("sales"):
    st.plotly_chart(
        bar_top(df, cols["sku"], cols["sales"], "Top SKUs"),
        use_container_width=True
    )

# ---- Brand Contribution ----
if cols.get("brand") and cols.get("sales"):
    st.plotly_chart(
        bar_top(df, cols["brand"], cols["sales"], "Brand Contribution"),
        use_container_width=True
    )

# ---- SKU Quantity ----
if cols.get("sku") and cols.get("quantity"):
    st.plotly_chart(
        bar_top(df, cols["sku"], cols["quantity"], "Top SKUs by Quantity"),
        use_container_width=True
    )
