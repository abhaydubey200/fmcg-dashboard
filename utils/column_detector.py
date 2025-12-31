def auto_detect_columns(df):
    """
    Auto-detect FMCG dataset columns safely.
    Works with ANY company data.
    """

    columns = {c.lower(): c for c in df.columns}

    def find(keys):
        for k in keys:
            for col in columns:
                if k in col:
                    return columns[col]
        return None

    return {
        "date": find(["date", "order_date", "bill_date"]),
        "sales": find(["amount", "sales", "net_amount", "ex_fact_amount"]),
        "quantity": find(["quantity", "qty", "cases", "kg"]),
        "order_id": find(["order_id", "order"]),
        "outlet": find(["outlet", "store", "retailer"]),
        "city": find(["city"]),
        "state": find(["state"]),
        "brand": find(["brand"]),
        "sku": find(["sku", "product"]),
        "category": find(["category"]),
        "warehouse": find(["warehouse"]),
        "sales_rep": find(["user", "salesman", "rep"]),
        "order_state": find(["orderstate", "status"]),
        "discount": find(["discount"]),
    }


# BACKWARD COMPATIBILITY (VERY IMPORTANT)
detect_columns = auto_detect_columns
