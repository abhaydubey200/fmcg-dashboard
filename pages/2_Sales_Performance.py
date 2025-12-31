import streamlit as st
from utils.column_detector import auto_detect_columns
from utils.data_processing import preprocess
from utils.visualizations import line_sales_trend, bar_top

st.header(" Sales Performance Dashboard")

df = st.session_state.get("df")
if df is None:
    st.warning("Upload dataset first")
    st.stop()

cols = auto_detect_columns(df)
df = preprocess(df, cols["date"])

if cols["state"]:
    st.plotly_chart(
        bar_top(df, cols["state"], cols["sales"], "Sales by State"),
        use_container_width=True
    )

if cols["city"]:
    st.plotly_chart(
        bar_top(df, cols["city"], cols["sales"], "Sales by City"),
        use_container_width=True
    )

st.plotly_chart(
    line_sales_trend(df, cols["date"], cols["sales"]),
    use_container_width=True
)
