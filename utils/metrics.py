def calculate_kpis(df, cols):
    """
    Production-grade KPI calculator
    Safe for any FMCG dataset
    """

    kpis = {
        "total_sales": 0,
        "total_orders": 0,
        "active_outlets": 0,
        "avg_order_value": 0,
        "total_quantity": 0,
    }

    # Total Sales
    if cols.get("sales"):
        kpis["total_sales"] = round(df[cols["sales"]].sum(), 2)

    # Total Orders
    if cols.get("order_id"):
        kpis["total_orders"] = df[cols["order_id"]].nunique()
    else:
        kpis["total_orders"] = len(df)

    # Active Outlets
    if cols.get("outlet"):
        kpis["active_outlets"] = df[cols["outlet"]].nunique()

    # Avg Order Value
    if cols.get("sales") and cols.get("order_id"):
        order_values = df.groupby(cols["order_id"])[cols["sales"]].sum()
        kpis["avg_order_value"] = round(order_values.mean(), 2)

    # Total Quantity
    if cols.get("quantity"):
        kpis["total_quantity"] = round(df[cols["quantity"]].sum(), 2)

    return kpis
