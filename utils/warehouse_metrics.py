import pandas as pd

def detect_warehouse_column(df: pd.DataFrame):
    candidates = [
        "warehouse", "warehouse_name",
        "depot", "depot_name",
        "distribution_center", "dc",
        "godown"
    ]

    for col in df.columns:
        if col.lower() in candidates:
            return col

    return None


def warehouse_sales_summary(df: pd.DataFrame, sales_col: str):
    warehouse_col = detect_warehouse_column(df)

    if warehouse_col is None:
        return None, None

    summary = (
        df.groupby(warehouse_col)[sales_col]
        .sum()
        .reset_index()
        .sort_values(sales_col, ascending=False)
    )

    return summary, warehouse_col
