import pandas as pd
import numpy as np

def prepare_time_series(df, date_col, value_col, freq="M"):
    """
    Prepares time series data for forecasting
    """
    ts = (
        df[[date_col, value_col]]
        .dropna()
        .assign(**{date_col: pd.to_datetime(df[date_col], errors="coerce")})
        .dropna()
        .groupby(pd.Grouper(key=date_col, freq=freq))
        .sum()
        .reset_index()
    )

    ts.rename(columns={value_col: "y", date_col: "ds"}, inplace=True)
    return ts


def sales_forecast(ts_df, periods=6):
    """
    Simple moving average based forecast
    (Production safe, no ML dependency)
    """

    if ts_df.shape[0] < 3:
        return None

    history = ts_df.copy()
    window = min(3, len(history))

    last_date = history["ds"].max()
    freq = pd.infer_freq(history["ds"]) or "M"

    future_dates = pd.date_range(
        start=last_date,
        periods=periods + 1,
        freq=freq
    )[1:]

    avg_value = history["y"].rolling(window).mean().iloc[-1]

    forecast_df = pd.DataFrame({
        "ds": future_dates,
        "yhat": [avg_value] * periods
    })

    return forecast_df
