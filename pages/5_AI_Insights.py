import streamlit as st
from utils.ai_insights import get_ai_insights

st.title("AI Insights")

if "df" in st.session_state:
    df = st.session_state.df
    question = st.text_input("Ask a question about your data:")
    
    if st.button("Get Insights") and question:
        try:
            insights = get_ai_insights(df, question)
            st.markdown(f"**AI Insights:** {insights}")
        except Exception as e:
            st.error(f"AI Insights Error: {e}")
else:
    st.warning("Please upload the dataset first in the Upload Dataset page.")
