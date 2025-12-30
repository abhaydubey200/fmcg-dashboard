# utils/metrics.py
import pandas as pd

def calculate_kpis(df):
    """Calculate basic KPIs dynamically"""
    total_orders = len(df)
    total_quantity = df.select_dtypes(include=['int', 'float']).sum().sum() if not df.empty else 0
    total_amount = df['AMOUNT'].sum() if 'AMOUNT' in df.columns else 0
    total_rejected = df['REJECTED_ORDER_COMMENT'].notna().sum() if 'REJECTED_ORDER_COMMENT' in df.columns else 0
    
    kpis = {
        "Total Orders": total_orders,
        "Total Quantity": total_quantity,
        "Total Amount": total_amount,
        "Rejected Orders": total_rejected
    }
    return kpis
