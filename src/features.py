import pandas as pd
import os

df = pd.read_csv("C:/Users/DELL/Desktop/coffee forcasting project/data/processed/hourly.csv")

df['datetime'] = pd.to_datetime(df['datetime'])

# Sort by store and datetime
df = df.sort_values(['store_id', 'datetime'])

# Time features
df['hour'] = df['datetime'].dt.hour
df['day_of_week'] = df['datetime'].dt.dayofweek

# Store-wise Lag features
df['lag_1'] = df.groupby('store_id')['transaction_qty'].shift(1)
df['lag_24'] = df.groupby('store_id')['transaction_qty'].shift(24)
df['lag_168'] = df.groupby('store_id')['transaction_qty'].shift(168)

# Store-wise Rolling averages
df['rolling_3'] = df.groupby('store_id')['transaction_qty'].rolling(3).mean().reset_index(0, drop=True)
df['rolling_7'] = df.groupby('store_id')['transaction_qty'].rolling(7).mean().reset_index(0, drop=True)

# Fill missing lag values with 0
df = df.fillna(0)

# Ensure folder
os.makedirs("C:/Users/DELL/Desktop/coffee forcasting project/data/processed", exist_ok=True)

# Save features
df.to_csv("C:/Users/DELL/Desktop/coffee forcasting project/data/processed/features.csv", index=False)

print("✅ Features Created Successfully")