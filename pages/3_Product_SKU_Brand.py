import streamlit as st
from utils.data_loader import get_dataset
from utils.column_detector import auto_detect_columns
from utils.visualizations import bar_top

st.title(" Product / SKU / Brand")

df = get_dataset()
if df is None:
    st.stop()

cols = auto_detect_columns(df)

if cols.get("sku"):
    st.plotly_chart(
        bar_top(df, cols["sku"], cols["sales"], "Top SKUs"),
        use_container_width=True
    )

if cols.get("brand"):
    st.plotly_chart(
        bar_top(df, cols["brand"], cols["sales"], "Brand Contribution"),
        use_container_width=True
    )

if cols.get("quantity"):
    st.plotly_chart(
        bar_top(df, cols["sku"], cols["quantity"], "Top SKUs by Quantity"),
        use_container_width=True
    )
