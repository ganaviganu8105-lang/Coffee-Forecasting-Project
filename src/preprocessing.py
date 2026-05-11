import pandas as pd
import os

# Load dataset
df = pd.read_csv(
    "C:/Users/DELL/Desktop/coffee forcasting project/data/raw/coffee_sales.csv",
    sep="\t",
    engine="python"
)

# Clean columns
df.columns = df.columns.str.strip()

print("Columns:", df.columns)

# Remove missing rows
df = df.dropna().reset_index(drop=True)

# ---------------- CREATE ARTIFICIAL DATE SERIES ----------------
base_date = pd.Timestamp("2025-01-01")

# Assign one progressive date for every 500 rows (simulating multiple days)
df['artificial_date'] = [base_date + pd.Timedelta(days=i//500) for i in range(len(df))]

# Combine artificial date + transaction time
df['datetime'] = pd.to_datetime(df['artificial_date'].astype(str) + ' ' + df['transaction_time'])

# Sort
df = df.sort_values('datetime')

# Extra columns
df['date'] = df['datetime'].dt.date
df['hour'] = df['datetime'].dt.hour
df['day_of_week'] = df['datetime'].dt.dayofweek

# Revenue
df['revenue'] = df['transaction_qty'] * df['unit_price']

# Ensure folder
os.makedirs("C:/Users/DELL/Desktop/coffee forcasting project/data/processed", exist_ok=True)

# Save cleaned
df.to_csv("C:/Users/DELL/Desktop/coffee forcasting project/data/processed/cleaned_data.csv", index=False)

print("✅ Preprocessing Done Successfully")