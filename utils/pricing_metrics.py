import pandas as pd

def calculate_pricing_metrics(df, price_col, qty_col, discount_col):
    df = df.copy()

    df["Gross_Sales"] = df[price_col] * df[qty_col]
    df["Net_Sales"] = df["Gross_Sales"] - df[discount_col]

    df["Discount_Percent"] = (
        (df[discount_col] / df["Gross_Sales"]) * 100
    ).fillna(0)

    return df


def sku_level_pricing(df, sku_col):
    return (
        df.groupby(sku_col)
        .agg(
            Gross_Sales=("Gross_Sales", "sum"),
            Net_Sales=("Net_Sales", "sum"),
            Discount_Amount=("SCHEME_DISCOUNT", "sum"),
            Avg_Discount_Percent=("Discount_Percent", "mean"),
        )
        .reset_index()
    )
