import streamlit as st
from utils.data_loader import load_data, detect_columns
from utils.metrics import calculate_kpis

st.title("📊 Overview Dashboard")

uploaded_file = st.file_uploader("Upload your FMCG file", type=["csv","xlsx"], key="overview")

if uploaded_file:
    df = load_data(uploaded_file)
    if df is not None:
        st.success("Data loaded successfully!")
        st.subheader("Raw Data Preview")
        st.dataframe(df.head(50))
        
        # KPIs
        kpis = calculate_kpis(df)
        cols = st.columns(4)
        for i, (k, v) in enumerate(kpis.items()):
            cols[i].metric(k, v)
