# utils/data_loader.py
import pandas as pd
import streamlit as st

def load_data(file):
    """Load CSV or Excel file and return a DataFrame"""
    try:
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)
        return df
    except Exception as e:
        st.error(f"Error loading file: {e}")
        return None

def detect_columns(df):
    """Detect numeric, categorical, and date columns dynamically"""
    date_cols = [col for col in df.columns if "date" in col.lower()]
    num_cols = df.select_dtypes(include=['int', 'float']).columns.tolist()
    cat_cols = df.select_dtypes(include=['object']).columns.tolist()
    return date_cols, num_cols, cat_cols
