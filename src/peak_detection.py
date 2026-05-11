import pandas as pd

df = pd.read_csv("C:/Users/DELL/Desktop/coffee forcasting project/data/processed/hourly.csv")

df['datetime'] = pd.to_datetime(df['datetime'])

# Extract hour
df['hour'] = df['datetime'].dt.hour

# ---------------- Overall Peak Demand Hours ----------------
overall_peak = df.groupby('hour')['transaction_qty'].sum().sort_values(ascending=False)

print("🔥 Overall Peak Demand Hours:")
print(overall_peak.head(5))

# ---------------- Store-wise Peak Demand Hours ----------------
print("\n🏪 Store-wise Peak Demand Hours:")

for store in df['store_id'].unique():
    store_data = df[df['store_id'] == store]
    store_peak = store_data.groupby('hour')['transaction_qty'].sum().sort_values(ascending=False)
    print(f"\nStore {store}:")
    print(store_peak.head(3))