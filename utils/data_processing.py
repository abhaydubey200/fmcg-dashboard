import pandas as pd

def clean_fmcg_data(df: pd.DataFrame) -> pd.DataFrame:
    # Convert all column names to uppercase
    df.columns = df.columns.str.upper().str.strip()
    
    # Fill missing numeric columns with 0
    numeric_cols = df.select_dtypes(include="number").columns
    df[numeric_cols] = df[numeric_cols].fillna(0)
    
    # Fill missing string columns with 'Unknown'
    object_cols = df.select_dtypes(include="object").columns
    df[object_cols] = df[object_cols].fillna("Unknown")
    
    return df
