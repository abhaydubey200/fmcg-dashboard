# utils/visualizations.py

import pandas as pd
import plotly.express as px

def plot_orders_over_time(df, date_col):
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df_grouped = df.groupby(date_col).sum().reset_index()
    fig = px.line(df_grouped, x=date_col, y='AMOUNT', title='Orders Over Time')
    return fig

def plot_top_categories(df, col, value_col='AMOUNT', top_n=10):
    top = df.groupby(col)[value_col].sum().sort_values(ascending=False).head(top_n).reset_index()
    fig = px.bar(top, x=col, y=value_col, title=f'Top {top_n} {col}')
    return fig
