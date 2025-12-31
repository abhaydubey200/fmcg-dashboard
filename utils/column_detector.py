def detect_columns(df):
    """
    Automatically detect common FMCG columns
    Works with ANY dataset (no hard dependency)
    """

    columns = [c.lower() for c in df.columns]

    def find(keys):
        for col in df.columns:
            for k in keys:
                if k in col.lower():
                    return col
        return None

    return {
        "date": find(["date", "order_date", "created"]),
        "sales": find(["amount", "sales", "revenue", "value"]),
        "quantity": find(["qty", "quantity", "cases", "kg", "pieces"]),
        "order_id": find(["order_id", "order"]),
        "outlet": find(["outlet", "store", "retailer"]),
        "city": find(["city"]),
        "state": find(["state", "region"]),
        "sku": find(["sku", "product"]),
        "brand": find(["brand"]),
        "warehouse": find(["warehouse", "depot"]),
        "sales_rep": find(["user", "rep", "salesman", "employee"]),
        "order_status": find(["status", "state"])
    }
