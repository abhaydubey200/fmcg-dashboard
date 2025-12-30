import pandas as pd
import streamlit as st
from openai import OpenAI

# Initialize Gemini/OpenAI client using Streamlit secrets
def init_client():
    api_key = st.secrets.get("OPENAI_API_KEY") or st.secrets.get("GEMINI_API_KEY")
    if not api_key:
        st.error("API key not found! Set it in Streamlit secrets.")
        st.stop()
    client = OpenAI(api_key=api_key)
    return client

# Function to get AI insights from a dataframe
def get_ai_insights(df: pd.DataFrame, question: str) -> str:
    client = init_client()

    # Convert top rows to string for AI context
    sample_data = df.head(20).to_csv(index=False)

    # Compose prompt
    prompt = f"""
    You are a professional FMCG data analyst.
    Data snippet:
    {sample_data}
    
    Question: {question}
    
    Provide a detailed analysis, insights, trends, and any recommendations.
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an expert FMCG data analyst."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"AI Insights Error: {e}")
        return ""
