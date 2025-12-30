import pandas as pd

def warehouse_kpis(df, warehouse_col, sales_col, qty_col):
    return (
        df.groupby(warehouse_col)
        .agg(
            Total_Sales=(sales_col, "sum"),
            Total_Quantity=(qty_col, "sum"),
            Order_Count=(warehouse_col, "count"),
        )
        .reset_index()
    )


def warehouse_asset_analysis(df, warehouse_col, asset_col, sales_col):
    return (
        df.groupby([warehouse_col, asset_col])
        .agg(
            Sales=(sales_col, "sum"),
            Orders=(sales_col, "count")
        )
        .reset_index()
    )
