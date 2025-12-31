import streamlit as st
from utils.column_detector import auto_detect_columns
from utils.visualizations import bar_top

st.header(" Outlet & Distribution Dashboard")

df = st.session_state.get("df")
if df is None:
    st.warning("Upload dataset first")
    st.stop()

cols = auto_detect_columns(df)

if cols["outlet"]:
    st.plotly_chart(
        bar_top(df, cols["outlet"], cols["sales"], "Top Outlets"),
        use_container_width=True
    )

if cols["city"]:
    st.plotly_chart(
        bar_top(df, cols["city"], cols["sales"], "Outlet Sales by City"),
        use_container_width=True
    )
