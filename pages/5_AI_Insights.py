import streamlit as st
import pandas as pd
from utils.ai_insights import get_ai_insights

st.set_page_config(page_title="AI Insights", layout="wide")

st.title("🤖 AI Insights for FMCG Data")

# Upload CSV or Excel
uploaded_file = st.file_uploader("Upload your FMCG dataset", type=["csv", "xlsx"])

if uploaded_file:
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.success("Dataset loaded successfully!")
        st.dataframe(df.head(10))

        # Ask AI question
        question = st.text_area("Enter your question about the dataset:")

        if st.button("Get AI Insights") and question.strip() != "":
            with st.spinner("Generating AI insights..."):
                insights = get_ai_insights(df, question)
                st.markdown("### AI Insights:")
                st.info(insights)

    except Exception as e:
        st.error(f"Error loading dataset: {e}")
