# utils/visualizations.py
import pandas as pd
import plotly.express as px

def plot_orders_over_time(df, date_col='ORDER_DATE'):
    """
    Plot number of orders over time.
    """
    if date_col not in df.columns:
        return None
    
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df_time = df.groupby(df[date_col].dt.date).size().reset_index(name='Order_Count')
    
    fig = px.line(df_time, x=date_col, y='Order_Count', title='Orders Over Time')
    fig.update_layout(xaxis_title='Date', yaxis_title='Number of Orders')
    return fig

def plot_order_state_distribution(df, state_col='ORDERSTATE'):
    """
    Plot distribution of orders by state/status.
    """
    if state_col not in df.columns:
        return None
    
    df_state = df[state_col].value_counts().reset_index()
    df_state.columns = [state_col, 'Count']
    
    fig = px.pie(df_state, names=state_col, values='Count', title='Order State Distribution')
    return fig

def plot_sales_by_city(df, city_col='CITY', amount_col='AMOUNT', top_n=15):
    """
    Plot total sales by city as a bar chart.
    """
    if city_col not in df.columns or amount_col not in df.columns:
        return None
    
    df_city = df.groupby(city_col)[amount_col].sum().nlargest(top_n).reset_index()
    
    fig = px.bar(df_city, x=city_col, y=amount_col,
                 title=f'Top {top_n} Cities by Sales',
                 text=amount_col)
    fig.update_traces(textposition='outside')
    fig.update_layout(xaxis_title=city_col, yaxis_title='Total Sales')
    return fig

def plot_top_outlets(df, outlet_col='OUTLET_NAME', amount_col='AMOUNT', top_n=15):
    """
    Plot top outlets by sales/amount.
    """
    if outlet_col not in df.columns or amount_col not in df.columns:
        return None
    
    df_outlet = df.groupby(outlet_col)[amount_col].sum().nlargest(top_n).reset_index()
    
    fig = px.bar(df_outlet, x=outlet_col, y=amount_col,
                 title=f'Top {top_n} Outlets by Sales',
                 text=amount_col)
    fig.update_traces(textposition='outside')
    fig.update_layout(xaxis_title='Outlet', yaxis_title='Total Sales')
    return fig

def plot_top_skus(df, sku_col='SKU', amount_col='TOTAL_QUANTITY', top_n=15):
    """
    Plot top SKUs by quantity sold.
    """
    if sku_col not in df.columns or amount_col not in df.columns:
        return None
    
    df_sku = df.groupby(sku_col)[amount_col].sum().nlargest(top_n).reset_index()
    
    fig = px.bar(df_sku, x=sku_col, y=amount_col,
                 title=f'Top {top_n} SKUs by Quantity',
                 text=amount_col)
    fig.update_traces(textposition='outside')
    fig.update_layout(xaxis_title='SKU', yaxis_title='Quantity Sold')
    return fig

def plot_category_sales(df, category_col='CATEGORY', amount_col='AMOUNT', top_n=10):
    """
    Plot sales by category.
    """
    if category_col not in df.columns or amount_col not in df.columns:
        return None
    
    df_cat = df.groupby(category_col)[amount_col].sum().nlargest(top_n).reset_index()
    
    fig = px.bar(df_cat, x=category_col, y=amount_col,
                 title=f'Top {top_n} Categories by Sales',
                 text=amount_col)
    fig.update_traces(textposition='outside')
    fig.update_layout(xaxis_title='Category', yaxis_title='Total Sales')
    return fig

def plot_warehouse_performance(df, warehouse_col='WAREHOUSE', amount_col='AMOUNT', top_n=10):
    """
    Plot warehouse performance based on sales.
    """
    if warehouse_col not in df.columns or amount_col not in df.columns:
        return None
    
    df_wh = df.groupby(warehouse_col)[amount_col].sum().nlargest(top_n).reset_index()
    
    fig = px.bar(df_wh, x=warehouse_col, y=amount_col,
                 title=f'Top {top_n} Warehouses by Sales',
                 text=amount_col)
    fig.update_traces(textposition='outside')
    fig.update_layout(xaxis_title='Warehouse', yaxis_title='Total Sales')
    return fig
