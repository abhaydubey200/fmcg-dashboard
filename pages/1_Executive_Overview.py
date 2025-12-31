from utils.kpi_drilldown import drilldown_data

st.subheader(" KPI Drill-Down")

kpi_selected = st.selectbox(
    "Select KPI to Drill Down",
    [
        "Total Sales",
        "Active Outlets",
        "Total Quantity",
        "Avg Order Value",
        "Discount %"
    ]
)

drill_df = drilldown_data(df, cols, kpi_selected)

if drill_df is not None:
    st.dataframe(drill_df, use_container_width=True)
else:
    st.info("No drill-down available for this KPI.")
