def kpi_total_sales(df, sales_col):
    return df[sales_col].sum()


def kpi_aov(df, sales_col):
    return df[sales_col].mean()


def kpi_orders(df):
    return len(df)
