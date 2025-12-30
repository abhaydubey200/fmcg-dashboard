import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def sales_forecast(df, date_col, sales_col, periods=6):
    temp = df[[date_col, sales_col]].copy()
    temp[date_col] = pd.to_datetime(temp[date_col])
    temp = temp.groupby(date_col)[sales_col].sum().reset_index()

    temp["t"] = np.arange(len(temp))

    X = temp[["t"]]
    y = temp[sales_col]

    model = LinearRegression()
    model.fit(X, y)

    future_t = np.arange(len(temp), len(temp) + periods)
    future_sales = model.predict(future_t.reshape(-1, 1))

    future_df = pd.DataFrame({
        date_col: pd.date_range(
            start=temp[date_col].max(),
            periods=periods + 1,
            freq="M"
        )[1:],
        sales_col: future_sales
    })

    return temp, future_df
