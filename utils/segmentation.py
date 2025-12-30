import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def prepare_outlet_features(df, outlet_col, sales_col, order_col):
    agg = df.groupby(outlet_col).agg(
        Total_Sales=(sales_col, "sum"),
        Orders_Count=(order_col, "count"),
        Avg_Order_Value=(sales_col, "mean")
    ).reset_index()

    return agg


def segment_outlets(agg_df, n_clusters=4):
    features = agg_df[["Total_Sales", "Orders_Count", "Avg_Order_Value"]]

    scaler = StandardScaler()
    scaled = scaler.fit_transform(features)

    model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    agg_df["Segment"] = model.fit_predict(scaled)

    segment_map = {
        0: "Low Value / Churn Risk",
        1: "Medium Value",
        2: "High Value",
        3: "Star Outlets"
    }

    agg_df["Segment_Name"] = agg_df["Segment"].map(segment_map)

    return agg_df
