import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_error

# Load forecast data
df = pd.read_csv("C:/Users/DELL/Desktop/coffee forcasting project/data/forecast/forecast_output.csv")

# Remove zero forecasts if needed
df = df[(df['naive_forecast'] != 0) & (df['moving_avg_forecast'] != 0)]

# ---------------- Naive Forecast Evaluation ----------------
naive_mae = mean_absolute_error(df['transaction_qty'], df['naive_forecast'])
naive_rmse = np.sqrt(((df['transaction_qty'] - df['naive_forecast']) ** 2).mean())
naive_mape = (np.abs((df['transaction_qty'] - df['naive_forecast']) / df['transaction_qty']).mean()) * 100

# ---------------- Moving Average Evaluation ----------------
mov_mae = mean_absolute_error(df['transaction_qty'], df['moving_avg_forecast'])
mov_rmse = np.sqrt(((df['transaction_qty'] - df['moving_avg_forecast']) ** 2).mean())
mov_mape = (np.abs((df['transaction_qty'] - df['moving_avg_forecast']) / df['transaction_qty']).mean()) * 100

print("📊 MODEL EVALUATION RESULTS")

print("\nNaive Forecast Model")
print("MAE:", naive_mae)
print("RMSE:", naive_rmse)
print("MAPE:", naive_mape)

print("\nMoving Average Forecast Model")
print("MAE:", mov_mae)
print("RMSE:", mov_rmse)
print("MAPE:", mov_mape)