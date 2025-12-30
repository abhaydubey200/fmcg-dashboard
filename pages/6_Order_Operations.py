import streamlit as st
from utils.column_detector import auto_detect_columns
from utils.visualizations import bar_top

st.header("🚚 Order & Operations Dashboard")

df = st.session_state.get("df")
if df is None:
    st.warning("Upload dataset first")
    st.stop()

cols = auto_detect_columns(df)

if "ORDERSTATE" in df.columns:
    st.plotly_chart(
        bar_top(df, "ORDERSTATE", cols["sales"], "Order State Performance"),
        use_container_width=True
    )

if "ORDERTYPE" in df.columns:
    st.plotly_chart(
        bar_top(df, "ORDERTYPE", cols["sales"], "Order Type Performance"),
        use_container_width=True
    )
