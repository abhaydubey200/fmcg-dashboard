import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def prepare_time_series(df, date_col, sales_col):
    ts = df[[date_col, sales_col]].copy()
    ts[date_col] = pd.to_datetime(ts[date_col], errors="coerce")
    ts = ts.dropna()
    ts = ts.groupby(date_col)[sales_col].sum().reset_index()
    ts = ts.sort_values(date_col)
    return ts


def forecast_sales(ts, periods=30):
    ts = ts.copy()
    ts["t"] = np.arange(len(ts))

    X = ts[["t"]]
    y = ts.iloc[:, 1]

    model = LinearRegression()
    model.fit(X, y)

    future_t = np.arange(len(ts), len(ts) + periods)
    future_dates = pd.date_range(
        start=ts.iloc[-1, 0], periods=periods + 1, freq="D"
    )[1:]

    forecast = model.predict(future_t.reshape(-1, 1))

    forecast_df = pd.DataFrame({
        "Date": future_dates,
        "Forecast_Sales": forecast
    })

    return forecast_df
