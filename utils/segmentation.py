from sklearn.cluster import KMeans
import pandas as pd

def outlet_segmentation(df, outlet_col, sales_col, orders_col):
    data = (
        df.groupby(outlet_col)
        .agg(
            Total_Sales=(sales_col, "sum"),
            Order_Count=(orders_col, "count")
        )
        .reset_index()
    )

    kmeans = KMeans(n_clusters=3, random_state=42)
    data["Segment"] = kmeans.fit_predict(
        data[["Total_Sales", "Order_Count"]]
    )

    return data
