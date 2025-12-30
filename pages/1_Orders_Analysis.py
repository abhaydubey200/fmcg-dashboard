import streamlit as st
import pandas as pd
from utils.visualizations import plot_orders_over_time

st.title("Orders Analysis")

if "df" in st.session_state:
    df = st.session_state.df
    st.dataframe(df.head(10))
    
    if "ORDER_DATE" in df.columns:
        st.plotly_chart(plot_orders_over_time(df, "ORDER_DATE"), use_container_width=True)
    else:
        st.warning("ORDER_DATE column not found in the dataset.")
else:
    st.warning("Please upload the dataset first in the Upload Dataset page.")
