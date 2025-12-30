import pandas as pd
import plotly.express as px

def plot_orders_over_time(df, date_col):
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df_time = df.groupby(date_col).size().reset_index(name='Orders')
    fig = px.line(df_time, x=date_col, y='Orders', title='Orders Over Time')
    return fig

def plot_order_state_distribution(df):
    fig = px.pie(df, names='ORDERSTATE', title='Order State Distribution')
    return fig

def plot_sales_by_city(df):
    df_sales = df.groupby('CITY')['AMOUNT'].sum().reset_index()
    fig = px.bar(df_sales, x='CITY', y='AMOUNT', title='Sales by City')
    return fig

def plot_top_skus(df, top_n=10):
    df_sku = df.groupby('SKU_NAME')['TOTAL_QUANTITY'].sum().nlargest(top_n).reset_index()
    fig = px.bar(df_sku, x='SKU_NAME', y='TOTAL_QUANTITY', title=f'Top {top_n} SKUs')
    return fig
