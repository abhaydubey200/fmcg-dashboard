import streamlit as st
import plotly.express as px
from utils.column_detector import auto_detect_columns
from utils.segmentation import prepare_outlet_features, segment_outlets

st.header("🧠 Outlet Segmentation & Churn Risk")

df = st.session_state.get("df")
if df is None:
    st.warning("Upload dataset first")
    st.stop()

cols = auto_detect_columns(df)

required = [cols["outlet"], cols["sales"], cols["order"]]
if any(v is None for v in required):
    st.error("Required columns not detected")
    st.stop()

clusters = st.slider("Number of Segments", 3, 6, 4)

agg = prepare_outlet_features(
    df,
    outlet_col=cols["outlet"],
    sales_col=cols["sales"],
    order_col=cols["order"]
)

segmented = segment_outlets(agg, clusters)

fig = px.scatter(
    segmented,
    x="Orders_Count",
    y="Total_Sales",
    color="Segment_Name",
    size="Avg_Order_Value",
    hover_name=cols["outlet"],
    title="Outlet Segmentation Map"
)

st.plotly_chart(fig, use_container_width=True)

st.subheader("📊 Outlet Segmentation Table")
st.dataframe(segmented.sort_values("Total_Sales", ascending=False))
