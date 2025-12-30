import streamlit as st
from utils.column_detector import auto_detect_columns
from utils.visualizations import bar_top

st.header("📦 Product / SKU / Brand Dashboard")

df = st.session_state.get("df")
if df is None:
    st.warning("Upload dataset first")
    st.stop()

cols = auto_detect_columns(df)

if cols["sku"]:
    st.plotly_chart(
        bar_top(df, cols["sku"], cols["sales"], "Top SKUs"),
        use_container_width=True
    )

if cols["brand"]:
    st.plotly_chart(
        bar_top(df, cols["brand"], cols["sales"], "Brand Contribution"),
        use_container_width=True
    )

if cols["quantity"]:
    st.plotly_chart(
        bar_top(df, cols["sku"], cols["quantity"], "Top SKUs by Quantity"),
        use_container_width=True
    )
