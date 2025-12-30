# utils/segmentation.py

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from utils.column_detector import auto_detect_columns


def prepare_outlet_features(df):
    """
    Prepare outlet-level features for clustering
    """
    cols = auto_detect_columns(df)

    outlet_col = cols.get("outlet")
    sales_col = cols.get("sales")
    qty_col = cols.get("quantity")

    if not outlet_col:
        raise ValueError("Outlet column not found")

    agg_dict = {}
    if sales_col:
        agg_dict[sales_col] = "sum"
    if qty_col:
        agg_dict[qty_col] = "sum"

    outlet_df = (
        df
        .groupby(outlet_col)
        .agg(agg_dict)
        .reset_index()
    )

    # Fill missing numeric values
    for c in outlet_df.columns:
        if c != outlet_col:
            outlet_df[c] = outlet_df[c].fillna(0)

    return outlet_df


def segment_outlets(outlet_df, n_clusters=3):
    """
    Apply KMeans clustering on outlet features
    """
    feature_cols = outlet_df.select_dtypes(include="number").columns

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(outlet_df[feature_cols])

    model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    outlet_df["Segment"] = model.fit_predict(X_scaled)

    return outlet_df
