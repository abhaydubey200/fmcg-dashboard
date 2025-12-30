import streamlit as st
import plotly.express as px

st.title("Outlet Analysis")

if 'df' in st.session_state:
    df = st.session_state['df']
    df_outlet = df.groupby('OUTLET_NAME')['AMOUNT'].sum().reset_index()
    fig = px.bar(df_outlet, x='OUTLET_NAME', y='AMOUNT', title='Sales by Outlet')
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("Please upload a dataset first on the Upload page.")
