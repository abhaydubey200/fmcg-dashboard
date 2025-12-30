import pandas as pd

def preprocess(df, date_col):
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col], errors="coerce")
    df["Year"] = df[date_col].dt.year
    df["Month"] = df[date_col].dt.month
    df["MonthName"] = df[date_col].dt.strftime("%b")
    return df
