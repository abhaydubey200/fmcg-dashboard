import pandas as pd
import streamlit as st


def load_dataset(uploaded_file):
    """
    Load CSV or Excel and store in session_state
    """
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith((".xlsx", ".xls")):
            df = pd.read_excel(uploaded_file)
        else:
            st.error("Unsupported file format")
            return None

        st.session_state["fmcg_df"] = df
        return df

    except Exception as e:
        st.error(f"Error loading dataset: {e}")
        return None


def get_dataset():
    """
    Used by ALL pages except upload page
    """
    if "fmcg_df" not in st.session_state:
        st.warning(" Please upload a dataset from the Upload page.")
        return None

    return st.session_state["fmcg_df"]
