import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Ethiopia Financial Inclusion Forecast", layout="wide")
@st.cache_data
def load_data():
    return pd.read_csv(
        "data/processed/ethiopia_fi_enriched.csv",
        parse_dates=["observation_date"]
    )

df = load_data()
obs = df[df.record_type == "observation"]
page = st.sidebar.selectbox(
    "Select Page",
    ["Overview", "Trends", "Forecasts", "Inclusion Projections"]
)
if page == "Overview":
    st.title("Ethiopia Financial Inclusion Overview")

    acc = obs[obs.indicator_code == "ACC_OWNERSHIP"].iloc[-1]
    print(obs["indicator_code"].unique())

    dp_data = obs[obs.indicator_code == "USG_P2P_VALUE"]

    if dp_data.empty:
        dp = None
    else:
        dp = dp_data.iloc[-1]

    

    col1, col2 = st.columns(2)

    col1.metric("Account Ownership (%)", f"{acc.value_numeric:.1f}")
    col2.metric("Digital Payment Usage (%)", f"{dp.value_numeric:.1f}")

    st.markdown("""
    **Key Insight:**  
    Digital payments are growing faster than account ownership, indicating increased usage intensity rather than new access.
    """)
elif page == "Trends":
    st.title("Trends Over Time")

    indicator = st.selectbox(
        "Select Indicator",
        obs.indicator.unique()
    )

    data = obs[obs.indicator == indicator]

    fig = px.line(
        data,
        x="observation_date",
        y="value_numeric",
        markers=True,
        title=indicator
    )

    st.plotly_chart(fig, use_container_width=True)
elif page == "Forecasts":
    st.title("Forecasts (2025–2027)")

    forecast_data = {
        "Year": [2025, 2026, 2027],
        "Access (Base)": [51, 53, 55],
        "Usage (Base)": [40, 45, 50]
    }

    forecast_df = pd.DataFrame(forecast_data)

    fig = px.line(
        forecast_df,
        x="Year",
        y=forecast_df.columns[1:],
        markers=True
    )

    st.plotly_chart(fig, use_container_width=True)
elif page == "Inclusion Projections":
    st.title("Progress Toward 60% Inclusion Target")

    years = [2024, 2025, 2026, 2027]
    values = [49, 51, 53, 55]

    fig = px.bar(
        x=years,
        y=values,
        labels={"x": "Year", "y": "Account Ownership (%)"}
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("At current trajectory, Ethiopia may reach 60% inclusion around 2029–2030.")
