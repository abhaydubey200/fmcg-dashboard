import streamlit as st
from utils.visualizations import plot_outlets_by_city, plot_outlets_by_type

st.title("Outlet Analysis")

if 'df' in st.session_state:
    df = st.session_state['df']

    st.subheader("Outlets by City")
    st.plotly_chart(plot_outlets_by_city(df, "CITY"), use_container_width=True)

    st.subheader("Outlets by Type")
    st.plotly_chart(plot_outlets_by_type(df, "TYPE"), use_container_width=True)
else:
    st.warning("Please upload a dataset first on the Upload Dataset page.")
