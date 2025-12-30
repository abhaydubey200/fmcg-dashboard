import streamlit as st
from utils.column_detector import auto_detect_columns
from utils.visualizations import bar_top

st.header("👨‍💼 Field Force Productivity Dashboard")

df = st.session_state.get("df")
if df is None:
    st.warning("Upload dataset first")
    st.stop()

cols = auto_detect_columns(df)

if cols["rep"]:
    st.plotly_chart(
        bar_top(df, cols["rep"], cols["sales"], "Sales per Sales Rep"),
        use_container_width=True
    )

if cols["rep"] and cols["quantity"]:
    st.plotly_chart(
        bar_top(df, cols["rep"], cols["quantity"], "Quantity Sold per Rep"),
        use_container_width=True
    )
