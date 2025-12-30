import streamlit as st
import pandas as pd
from utils.ai_insights import get_ai_insights

st.title("📊 AI Insights for FMCG Data")

uploaded_file = st.file_uploader("Upload your FMCG dataset (CSV/Excel)", type=["csv", "xlsx"])

if uploaded_file:
    # Read uploaded file
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
    except Exception as e:
        st.error(f"Error reading file: {e}")
        st.stop()

    st.success(f"Data loaded successfully! {df.shape[0]} rows, {df.shape[1]} columns.")

    st.subheader("Sample Data")
    st.dataframe(df.head(10))

    # AI Insights
    question = st.text_area("Ask AI about your FMCG data", "Provide detailed analysis and trends.")

    if st.button("Generate AI Insights"):
        with st.spinner("Generating insights..."):
            insights = get_ai_insights(df, question)
            st.subheader("🤖 AI Insights")
            st.write(insights)
