import pandas as pd

def drilldown_data(df, cols, kpi):
    if kpi == "Total Sales":
        return df.groupby(cols.get("state") or cols.get("city") or cols.get("brand"))[
            cols["sales"]
        ].sum().sort_values(ascending=False).reset_index()

    if kpi == "Active Outlets":
        return df.groupby(cols.get("city") or cols.get("state"))[
            cols["outlet"]
        ].nunique().sort_values(ascending=False).reset_index(name="Outlet Count")

    if kpi == "Total Quantity":
        return df.groupby(cols.get("brand") or cols.get("sku"))[
            cols["quantity"]
        ].sum().sort_values(ascending=False).reset_index()

    if kpi == "Avg Order Value":
        orders = df.groupby(cols["order_id"])[cols["sales"]].sum()
        return orders.reset_index(name="Order Value")

    if kpi == "Discount %":
        return df[[cols["discount"], cols["sales"]]].describe()

    return None
