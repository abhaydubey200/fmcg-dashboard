import pandas as pd
import streamlit as st

def load_dataset(file):
    try:
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file, engine="openpyxl")

        st.session_state["df"] = df
        return df

    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return None
