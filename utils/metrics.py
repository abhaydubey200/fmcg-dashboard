import pandas as pd


def calculate_kpis(df, cols):
    """
    Generic KPI engine for FMCG datasets
    Works even if some columns are missing
    """

    kpis = {}

    # Total Sales
    if cols.get("sales"):
        kpis["Total Sales"] = round(df[cols["sales"]].sum(), 2)
    else:
        kpis["Total Sales"] = 0

    # Orders Count
    if cols.get("order_id"):
        kpis["Total Orders"] = df[cols["order_id"]].nunique()
    else:
        kpis["Total Orders"] = len(df)

    # Active Outlets
    if cols.get("outlet"):
        kpis["Active Outlets"] = df[cols["outlet"]].nunique()
    else:
        kpis["Active Outlets"] = 0

    # Average Order Value
    if cols.get("sales") and cols.get("order_id"):
        orders = df.groupby(cols["order_id"])[cols["sales"]].sum()
        kpis["Avg Order Value"] = round(orders.mean(), 2)
    else:
        kpis["Avg Order Value"] = 0

    # Total Quantity
    if cols.get("quantity"):
        kpis["Total Quantity"] = round(df[cols["quantity"]].sum(), 2)
    else:
        kpis["Total Quantity"] = 0

    return kpis
