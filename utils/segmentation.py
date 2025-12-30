# utils/segmentation.py

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

from utils.column_detector import auto_detect_columns


def prepare_outlet_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create outlet-level aggregated features for clustering.
    Works with any FMCG dataset.
    """

    cols = auto_detect_columns(df)

    outlet_col = cols.get("outlet")
    sales_col = cols.get("sales")
    qty_col = cols.get("quantity")

    if outlet_col is None:
        raise ValueError("❌ Outlet column not detected in dataset")

    agg = {}

    if sales_col:
        agg[sales_col] = "sum"
    if qty_col:
        agg[qty_col] = "sum"

    outlet_df = (
        df
        .groupby(outlet_col)
        .agg(agg)
        .reset_index()
    )

    # Rename for consistency
    rename_map = {}
    if sales_col:
        rename_map[sales_col] = "Total_Sales"
    if qty_col:
        rename_map[qty_col] = "Total_Quantity"

    outlet_df.rename(columns=rename_map, inplace=True)

    # Fill missing numeric values
    for col in outlet_df.select_dtypes(include="number").columns:
        outlet_df[col] = outlet_df[col].fillna(0)

    return outlet_df


def segment_outlets(outlet_df: pd.DataFrame, n_clusters: int = 3) -> pd.DataFrame:
    """
    Perform KMeans clustering on outlet features.
    """

    feature_cols = outlet_df.select_dtypes(include="number").columns.tolist()

    if len(feature_cols) == 0:
        raise ValueError("❌ No numeric features available for clustering")

    scaler = StandardScaler()
    X = scaler.fit_transform(outlet_df[feature_cols])

    kmeans = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )

    outlet_df["Segment"] = kmeans.fit_predict(X)

    return outlet_df
