import streamlit as st
from utils.data_loader import load_dataset
from utils.ai2_insights import get_ai_insights

st.title("AI Insights")

df = load_dataset()
if df is not None:
    question = st.text_input("Ask a question about your dataset")
    if question:
        insights = get_ai_insights(df, question)
        st.write(insights)
else:
    st.info("Please upload a dataset to get AI insights.")
