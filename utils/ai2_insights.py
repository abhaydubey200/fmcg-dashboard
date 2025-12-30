import openai
import pandas as pd
import os

# Make sure you set your API key in environment variable
openai.api_key = os.getenv("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")

def get_ai_insights(df: pd.DataFrame, question: str) -> str:
    try:
        prompt = f"Analyze the following FMCG dataset:\n{df.head(50).to_dict()}\nQuestion: {question}"
        response = openai.responses.create(
            model="gpt-5-nano",
            input=prompt
        )
        return response.output_text
    except Exception as e:
        return f"AI Insights Error: {e}"
