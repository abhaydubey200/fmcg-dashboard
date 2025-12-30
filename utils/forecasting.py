# utils/forecasting.py

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


def prepare_time_series(df, date_col, sales_col, freq="M"):
    """
    Convert raw FMCG sales data into time-series format
    """
    data = df[[date_col, sales_col]].copy()
    data[date_col] = pd.to_datetime(data[date_col], errors="coerce")

    data = (
        data
        .dropna()
        .groupby(pd.Grouper(key=date_col, freq=freq))[sales_col]
        .sum()
        .reset_index()
    )

    data["t"] = np.arange(len(data))
    return data


def forecast_sales(ts_df, periods=6):
    """
    Forecast future sales using Linear Regression
    """
    X = ts_df[["t"]]
    y = ts_df.iloc[:, 1]

    model = LinearRegression()
    model.fit(X, y)

    future_t = np.arange(len(ts_df), len(ts_df) + periods)
    future_sales = model.predict(future_t.reshape(-1, 1))

    future_dates = pd.date_range(
        start=ts_df.iloc[-1, 0],
        periods=periods + 1,
        freq="M"
    )[1:]

    forecast_df = pd.DataFrame({
        ts_df.columns[0]: future_dates,
        ts_df.columns[1]: future_sales
    })

    return forecast_df
