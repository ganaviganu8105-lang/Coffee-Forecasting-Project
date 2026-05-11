import streamlit as st
import pandas as pd

# ---------------- LOAD FILES ----------------
cleaned = pd.read_csv("C:/Users/DELL/Desktop/coffee forcasting project/data/processed/cleaned_data.csv")
forecast = pd.read_csv("C:/Users/DELL/Desktop/coffee forcasting project/data/forecast/forecast_output.csv")
revenue_forecast = pd.read_csv("C:/Users/DELL/Desktop/coffee forcasting project/data/forecast/revenue_forecast.csv")
category = pd.read_csv("C:/Users/DELL/Desktop/coffee forcasting project/data/processed/category_daily.csv")

# ---------------- DATETIME CONVERSION ----------------
cleaned['datetime'] = pd.to_datetime(cleaned['datetime'])
forecast['datetime'] = pd.to_datetime(forecast['datetime'])
revenue_forecast['datetime'] = pd.to_datetime(revenue_forecast['datetime'])
category['datetime'] = pd.to_datetime(category['datetime'])

# ---------------- TITLE ----------------
st.title("☕ Data-Driven Forecasting & Peak Demand Prediction Dashboard")

# ---------------- SELECTORS ----------------
store = st.selectbox("Select Store", sorted(cleaned['store_id'].unique()))
model = st.selectbox("Select Forecast Model", ["naive_forecast", "moving_avg_forecast"])
view = st.selectbox("Select Analysis View", ["Quantity Demand", "Revenue Trend", "Category Demand"])

# ---------------- FILTER DATA ----------------
filtered_cleaned = cleaned[cleaned['store_id'] == store].copy()
filtered_forecast = forecast[forecast['store_id'] == store].copy()
filtered_revenue = revenue_forecast[revenue_forecast['store_id'] == store].copy()

# ---------------- QUANTITY DEMAND VIEW ----------------
if view == "Quantity Demand":
    st.subheader("Hourly Coffee Demand Forecast")

    actual_demand = filtered_forecast.groupby('datetime')['transaction_qty'].sum()
    pred_demand = filtered_forecast.groupby('datetime')[model].sum()

    demand_chart = pd.DataFrame({
        "Actual Demand": actual_demand,
        "Forecasted Demand": pred_demand
    })

    st.line_chart(demand_chart)

    st.subheader("Peak Hours Analysis")
    peak = filtered_cleaned.groupby(filtered_cleaned['datetime'].dt.hour)['transaction_qty'].sum()
    st.bar_chart(peak)

# ---------------- REVENUE TREND VIEW ----------------
elif view == "Revenue Trend":
    st.subheader("Daily Revenue Forecast")

    filtered_revenue['date_only'] = filtered_revenue['datetime'].dt.date

    rev_actual = filtered_revenue.groupby('date_only')['revenue'].sum()
    rev_pred = filtered_revenue.groupby('date_only')['revenue_forecast'].sum()

    revenue_chart = pd.DataFrame({
        "Actual Revenue": rev_actual,
        "Forecasted Revenue": rev_pred
    })

    st.line_chart(revenue_chart)

# ---------------- CATEGORY DEMAND VIEW ----------------
elif view == "Category Demand":
    st.subheader("Category-Level Daily Demand")

    cat = category.groupby('product_category')['transaction_qty'].sum()
    st.bar_chart(cat)