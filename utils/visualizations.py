import plotly.express as px
import pandas as pd

def line_sales_trend(df, date_col, sales_col):
    trend = df.groupby(date_col)[sales_col].sum().reset_index()
    return px.line(trend, x=date_col, y=sales_col, title="Sales Trend")


def bar_top(df, group_col, value_col, title):
    agg = df.groupby(group_col)[value_col].sum().sort_values(ascending=False).head(10).reset_index()
    return px.bar(agg, x=group_col, y=value_col, title=title)
