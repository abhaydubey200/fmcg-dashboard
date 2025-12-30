import pandas as pd

def churn_risk(df, outlet_col, date_col):
    df[date_col] = pd.to_datetime(df[date_col])

    last_order = (
        df.groupby(outlet_col)[date_col]
        .max()
        .reset_index()
    )

    last_order["Days_Since_Last_Order"] = (
        pd.Timestamp.today() - last_order[date_col]
    ).dt.days

    last_order["Churn_Risk"] = last_order["Days_Since_Last_Order"].apply(
        lambda x: "High" if x > 60 else "Medium" if x > 30 else "Low"
    )

    return last_order
