import pandas as pd

def load_dataset(file):
    if str(file).endswith(".csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)
    return df

def detect_columns(df):
    return df.columns.tolist()
