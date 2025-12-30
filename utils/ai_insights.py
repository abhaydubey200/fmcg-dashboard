# utils/ai_insights.py
from openai import OpenAI
from config import GEMINI_API_KEY

client = OpenAI(api_key=GEMINI_API_KEY)

def get_ai_insights(df, question):
    """Generate AI insights from dataframe using Gemini API"""
    if df.empty:
        return "Data is empty!"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert FMCG data analyst. Provide detailed insights and suggestions."},
            {"role": "user", "content": f"Columns: {list(df.columns)}\nSample Data: {df.head(10).to_dict()}\nQuestion: {question}"}
        ]
    )
    return response.choices[0].message.content
