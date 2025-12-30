# pages/8_Outlet_Segmentation.py

import streamlit as st
import plotly.express as px

from utils.segmentation import prepare_outlet_features, segment_outlets

st.set_page_config(page_title="Outlet Segmentation", layout="wide")
st.title("🏪 Outlet Segmentation")

df = st.session_state.get("df")

if df is None:
    st.warning("⚠️ Upload dataset first")
    st.stop()

# Prepare Features
try:
    outlet_df = prepare_outlet_features(df)
except Exception as e:
    st.error(str(e))
    st.stop()

# Select clusters
k = st.slider("Number of Segments", 2, 6, 3)

segmented_df = segment_outlets(outlet_df, k)

st.subheader("📋 Segmented Outlets")
st.dataframe(segmented_df, use_container_width=True)

# Visualization
num_cols = segmented_df.select_dtypes(include="number").columns.tolist()

if len(num_cols) >= 2:
    fig = px.scatter(
        segmented_df,
        x=num_cols[0],
        y=num_cols[1],
        color="Segment",
        hover_data=[segmented_df.columns[0]],
        title="Outlet Segments"
    )
    st.plotly_chart(fig, use_container_width=True)

# Segment Summary
st.subheader("📊 Segment Summary")
summary = segmented_df.groupby("Segment")[num_cols].mean().round(2)
st.dataframe(summary, use_container_width=True)
