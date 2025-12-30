# utils/visualizations.py
import plotly.express as px

def plot_orders_over_time(df, date_col):
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    orders_time = df.groupby(date_col).size().reset_index(name='Order Count')
    fig = px.line(orders_time, x=date_col, y='Order Count', title='Orders Over Time')
    return fig

def plot_top_categories(df, col, value_col='AMOUNT', top_n=10):
    if col not in df.columns:
        return None
    top_items = df.groupby(col)[value_col].sum().sort_values(ascending=False).head(top_n).reset_index()
    fig = px.bar(top_items, x=col, y=value_col, title=f'Top {top_n} {col} by {value_col}', text=value_col)
    return fig
