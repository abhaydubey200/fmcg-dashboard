import streamlit as st
from utils.ai_insights import get_ai_insights

st.title("AI Insights")

if 'df' in st.session_state:
    df = st.session_state['df']

    question = st.text_input("Ask a question about your dataset")
    if question:
        try:
            insights = get_ai_insights(df, question)
            st.write(insights)
        except Exception as e:
            st.error(f"AI Insights Error: {e}")
else:
    st.warning("Please upload a dataset first on the Upload page.")
