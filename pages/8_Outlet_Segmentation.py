import streamlit as st
from utils.data_loader import get_dataset
from utils.segmentation import segment_outlets

st.title(" Outlet Segmentation")

df = get_dataset()
if df is None:
    st.stop()

segments = segment_outlets(df)
st.dataframe(segments)
