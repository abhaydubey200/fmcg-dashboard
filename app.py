import streamlit as st
from config import APP_TITLE

st.set_page_config(
    page_title=APP_TITLE,
    layout="wide"
)

st.title(APP_TITLE)
st.markdown("📊 **Production-Grade FMCG Business Intelligence System**")

if "df" not in st.session_state:
    st.warning("⬅️ Please upload a dataset from the Upload page")
