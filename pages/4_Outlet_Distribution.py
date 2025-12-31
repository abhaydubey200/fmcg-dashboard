import streamlit as st
from utils.data_loader import get_dataset
from utils.visualizations import bar_top

st.title(" Outlet Distribution")

df = get_dataset()
if df is None:
    st.stop()

st.plotly_chart(
    bar_top(df, "outlet", "sales", "Sales by Outlet"),
    use_container_width=True
)
