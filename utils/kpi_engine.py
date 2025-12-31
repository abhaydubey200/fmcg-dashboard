import pandas as pd
def safe_sum(df, col):
    return df[col].sum() if col and col in df else 0


def safe_mean(df, col):
    return round(df[col].mean(), 2) if col and col in df else 0


def calculate_kpis(df, cols):
    kpis = {}

    # SALES
    kpis["total_sales"] = safe_sum(df, cols.get("sales"))

    # QUANTITY
    kpis["total_qty"] = safe_sum(df, cols.get("quantity"))

    # OUTLETS
    outlet_col = cols.get("outlet")
    kpis["active_outlets"] = df[outlet_col].nunique() if outlet_col else 0

    # AOV
    order_col = cols.get("order_id")
    if order_col and cols.get("sales"):
        orders = df.groupby(order_col)[cols["sales"]].sum()
        kpis["aov"] = round(orders.mean(), 2)
    else:
        kpis["aov"] = 0

    # DISCOUNT %
    discount_col = cols.get("discount")
    if discount_col and cols.get("sales"):
        kpis["discount_pct"] = round(
            (df[discount_col].sum() / df[cols["sales"]].sum()) * 100, 2
        )
    else:
        kpis["discount_pct"] = 0

    return kpis
