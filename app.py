# app.py
import streamlit as st
from utils.data_loader import load_data, detect_columns
from utils.metrics import calculate_kpis
from utils.visualizations import plot_orders_over_time, plot_top_categories
from utils.ai_insights import get_ai_insights

st.set_page_config(page_title="FMCG Dashboard", layout="wide")
st.title("📊 FMCG Advanced Analytics Dashboard")

uploaded_file = st.file_uploader("Upload your FMCG Excel or CSV file", type=["csv","xlsx"])

if uploaded_file:
    df = load_data(uploaded_file)
    if df is not None:
        st.success("✅ Data loaded successfully!")
        with st.expander("Show Raw Data"):
            st.dataframe(df.head(100))

        # Detect column types
        date_cols, num_cols, cat_cols = detect_columns(df)

        # Sidebar filters
        st.sidebar.header("Filters")
        filters = {}
        for col in cat_cols:
            vals = df[col].dropna().unique().tolist()
            if vals:
                filters[col] = st.sidebar.multiselect(f"Filter by {col}", options=vals, default=vals)

        filtered_df = df.copy()
        for col, vals in filters.items():
            filtered_df = filtered_df[filtered_df[col].isin(vals)]

        # Display KPIs
        st.markdown("## 📌 Key Metrics")
        kpis = calculate_kpis(filtered_df)
        cols = st.columns(4)
        for i, (k, v) in enumerate(kpis.items()):
            cols[i].metric(k, v)

        # Visualizations
        st.markdown("## 📈 Visual Analysis")
        if date_cols:
            st.plotly_chart(plot_orders_over_time(filtered_df, date_cols[0]), use_container_width=True)
        for col in ['OUTLET_NAME','SKU_PLACED','CITY']:
            fig = plot_top_categories(filtered_df, col)
            if fig:
                st.plotly_chart(fig, use_container_width=True)

        # AI Insights
        st.markdown("## 🤖 AI Insights")
        question = st.text_area("Ask AI about this data")
        if st.button("Get AI Insights") and question:
            with st.spinner("Generating insights..."):
                st.success(get_ai_insights(filtered_df, question))

        # Download filtered data
        st.markdown("## 💾 Download Filtered Data")
        csv = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button("Download CSV", data=csv, file_name="filtered_fmcg_data.csv", mime="text/csv")
