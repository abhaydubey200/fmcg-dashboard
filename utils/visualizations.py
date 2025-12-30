import plotly.express as px
import pandas as pd

def plot_orders_over_time(df, date_col):
    df = df.copy()
    if date_col not in df.columns:
        raise ValueError(f"{date_col} not found in dataframe")
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    daily_orders = df.groupby(df[date_col].dt.date).size().reset_index(name="Orders")
    fig = px.line(daily_orders, x=date_col, y="Orders", title="Orders Over Time")
    return fig
