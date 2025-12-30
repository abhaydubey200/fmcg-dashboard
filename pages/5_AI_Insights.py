import streamlit as st
from utils.data_loader import load_data
from utils.ai_insights import get_ai_insights

st.title("🤖 AI Insights")

uploaded_file = st.file_uploader("Upload FMCG file", type=["csv","xlsx"], key="ai")

if uploaded_file:
    df = load_data(uploaded_file)
    if df is not None:
        st.subheader("Ask AI about this data")
        question = st.text_area("Type your question here")
        if st.button("Get AI Insights"):
            with st.spinner("Generating insights..."):
                insights = get_ai_insights(df, question)
                st.success(insights)
