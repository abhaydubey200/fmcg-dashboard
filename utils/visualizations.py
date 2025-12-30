# utils/visualizations.py

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def plot_orders_over_time(df, date_col='ORDER_DATE'):
    """
    Plot orders over time as a line chart.
    """
    if date_col not in df.columns:
        return None
    
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df_grouped = df.groupby(date_col)['ORDER_ID'].count().reset_index()
    
    fig = px.line(df_grouped, x=date_col, y='ORDER_ID',
                  title='Orders Over Time',
                  labels={'ORDER_ID': 'Number of Orders', date_col: 'Date'})
    return fig


def plot_order_state_distribution(df, state_col='ORDERSTATE'):
    """
    Plot distribution of order states as a pie chart.
    """
    if state_col not in df.columns:
        return None
    
    df_grouped = df[state_col].value_counts().reset_index()
    df_grouped.columns = [state_col, 'count']
    
    fig = px.pie(df_grouped, names=state_col, values='count',
                 title='Order State Distribution')
    return fig


def plot_top_skus(df, top_n=10, sku_col='SKU_CODE'):
    """
    Plot top N SKUs by total quantity.
    """
    if sku_col not in df.columns or 'TOTAL_QUANTITY' not in df.columns:
        return None
    
    df_sku = df.groupby(sku_col)['TOTAL_QUANTITY'].sum().nlargest(top_n).reset_index()
    
    fig = px.bar(df_sku, x=sku_col, y='TOTAL_QUANTITY',
                 title=f'Top {top_n} SKUs by Quantity',
                 text='TOTAL_QUANTITY')
    fig.update_traces(textposition='outside')
    fig.update_layout(xaxis_title=sku_col, yaxis_title='Total Quantity')
    return fig


def plot_sales_by_category(df, category_col='CATEGORY', amount_col='AMOUNT'):
    """
    Plot total sales by category as a bar chart.
    """
    if category_col not in df.columns or amount_col not in df.columns:
        return None
    
    df_cat = df.groupby(category_col)[amount_col].sum().reset_index()
    
    fig = px.bar(df_cat, x=category_col, y=amount_col,
                 title='Total Sales by Category',
                 text=amount_col)
    fig.update_traces(textposition='outside')
    fig.update_layout(xaxis_title=category_col, yaxis_title='Total Amount')
    return fig


def plot_outlet_distribution(df, outlet_col='OUTLET_NAME'):
    """
    Plot outlet distribution as a bar chart (number of orders per outlet).
    """
    if outlet_col not in df.columns or 'ORDER_ID' not in df.columns:
        return None
    
    df_outlet = df.groupby(outlet_col)['ORDER_ID'].count().nlargest(15).reset_index()
    
    fig = px.bar(df_outlet, x=outlet_col, y='ORDER_ID',
                 title='Top 15 Outlets by Orders',
                 text='ORDER_ID')
    fig.update_traces(textposition='outside')
    fig.update_layout(xaxis_title=outlet_col, yaxis_title='Number of Orders')
    return fig


def plot_sales_trend(df, date_col='ORDER_DATE', amount_col='AMOUNT'):
    """
    Plot sales trend over time.
    """
    if date_col not in df.columns or amount_col not in df.columns:
        return None
    
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df_grouped = df.groupby(date_col)[amount_col].sum().reset_index()
    
    fig = px.line(df_grouped, x=date_col, y=amount_col,
                  title='Sales Trend Over Time',
                  labels={amount_col: 'Total Sales', date_col: 'Date'})
    return fig
