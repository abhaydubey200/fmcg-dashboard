import openai
import pandas as pd

# Set your OpenAI API key here
openai.api_key = st.secrets.get("OPENAI_API_KEY", None)

def get_ai_insights(df: pd.DataFrame, question: str) -> str:
    if not openai.api_key:
        raise ValueError("OpenAI API key not found. Please set it in Streamlit secrets.")
    
    prompt = f"Analyze the following FMCG dataset:\n{df.head(50).to_dict()}\nAnswer this question: {question}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices[0].message.content
