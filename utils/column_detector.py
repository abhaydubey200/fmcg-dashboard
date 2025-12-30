def detect_column(columns, keywords):
    for col in columns:
        for key in keywords:
            if key in col.lower():
                return col
    return None


def auto_detect_columns(df):
    cols = df.columns

    return {
        "date": detect_column(cols, ["date", "order_date"]),
        "sales": detect_column(cols, ["amount", "sales", "value"]),
        "quantity": detect_column(cols, ["qty", "quantity"]),
        "sku": detect_column(cols, ["sku", "product"]),
        "brand": detect_column(cols, ["brand"]),
        "city": detect_column(cols, ["city"]),
        "state": detect_column(cols, ["state"]),
        "outlet": detect_column(cols, ["outlet"]),
        "rep": detect_column(cols, ["user", "salesman", "rep"])
    }
