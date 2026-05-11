import pandas as pd
import os

df = pd.read_csv("C:/Users/DELL/Desktop/coffee forcasting project/data/processed/cleaned_data.csv")

df['datetime'] = pd.to_datetime(df['datetime'])

# ---------------- Hourly Demand per Store ----------------
hourly = df.groupby([
    'store_id',
    pd.Grouper(key='datetime', freq='h')
])['transaction_qty'].sum().reset_index()

# ---------------- Daily Revenue per Store ----------------
daily = df.groupby([
    'store_id',
    pd.Grouper(key='datetime', freq='D')
])['revenue'].sum().reset_index()

# ---------------- Category Daily Demand ----------------
category_daily = df.groupby([
    'product_category',
    pd.Grouper(key='datetime', freq='D')
])['transaction_qty'].sum().reset_index()

# Ensure folder exists
os.makedirs("C:/Users/DELL/Desktop/coffee forcasting project/data/processed", exist_ok=True)

# Save files
hourly.to_csv("C:/Users/DELL/Desktop/coffee forcasting project/data/processed/hourly.csv", index=False)
daily.to_csv("C:/Users/DELL/Desktop/coffee forcasting project/data/processed/daily.csv", index=False)
category_daily.to_csv("C:/Users/DELL/Desktop/coffee forcasting project/data/processed/category_daily.csv", index=False)

print("✅ Time Series Created Successfully")