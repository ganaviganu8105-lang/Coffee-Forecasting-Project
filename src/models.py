import pandas as pd
import os

df = pd.read_csv("C:/Users/DELL/Desktop/coffee forcasting project/data/processed/features.csv")

# Drop rows where forecasting cannot happen
df = df.dropna()

# ---------------- Naive Forecast ----------------
df['naive_forecast'] = df.groupby('store_id')['transaction_qty'].shift(1)

# ---------------- Moving Average Forecast ----------------
df['moving_avg_forecast'] = (
    df.groupby('store_id')['transaction_qty']
    .rolling(3)
    .mean()
    .reset_index(0, drop=True)
)

# Fill NaNs
df = df.fillna(0)

# Save hourly forecast output
os.makedirs("C:/Users/DELL/Desktop/coffee forcasting project/data/forecast", exist_ok=True)
df.to_csv("C:/Users/DELL/Desktop/coffee forcasting project/data/forecast/forecast_output.csv", index=False)

# ---------------- Daily Revenue Forecast ----------------
daily = pd.read_csv("C:/Users/DELL/Desktop/coffee forcasting project/data/processed/daily.csv")
daily['datetime'] = pd.to_datetime(daily['datetime'])

daily = daily.sort_values(['store_id', 'datetime'])
daily['revenue_forecast'] = daily.groupby('store_id')['revenue'].shift(1)
daily = daily.fillna(0)

daily.to_csv("C:/Users/DELL/Desktop/coffee forcasting project/data/forecast/revenue_forecast.csv", index=False)

print("✅ Forecast Generated Successfully")