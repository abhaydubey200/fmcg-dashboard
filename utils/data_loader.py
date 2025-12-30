import pandas as pd

def load_dataset(uploaded_file):
    """
    Load CSV or Excel file uploaded in Streamlit.
    Returns a Pandas DataFrame.
    """
    try:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith((".xls", ".xlsx")):
            df = pd.read_excel(uploaded_file, engine='openpyxl')
        else:
            raise ValueError("Unsupported file type. Please upload a CSV or Excel file.")
        return df
    except Exception as e:
        raise ValueError(f"Error loading dataset: {e}")
