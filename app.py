import streamlit as st

st.set_page_config(page_title="FMCG Dashboard", layout="wide")

st.title("FMCG Dashboard")
st.sidebar.title("Navigation")

st.sidebar.info(
    """
    Use the sidebar to navigate between pages:
    - Upload Dataset
    - Orders Analysis
    - Sales Analysis
    - Outlet Analysis
    - SKU Analysis
    - AI Insights
    """
)
