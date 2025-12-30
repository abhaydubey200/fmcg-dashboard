import openai
import pandas as pd
import streamlit as st

def get_ai_insights(df: pd.DataFrame, question: str) -> str:
    """
    Generates AI insights using OpenAI Responses API (gpt-5-nano/gpt-4o-mini)
    Works for any FMCG dataset.
    """
    try:
        # Get API key from Streamlit secrets
        api_key = st.secrets["OPENAI_API_KEY"]
        client = openai.OpenAI(api_key=api_key)

        # Convert small dataframe to string to feed AI (limit large data!)
        df_preview = df.head(500).to_csv(index=False)

        prompt = f"""
        You are an expert FMCG data analyst. Analyze the following dataset and answer the user's question.
        Dataset Preview (first 500 rows):
        {df_preview}

        Question: {question}
        """

        response = client.responses.create(
            model="gpt-5-nano",
            input=prompt,
            store=True
        )

        return response.output_text

    except Exception as e:
        return f"AI Insights Error: {str(e)}"
