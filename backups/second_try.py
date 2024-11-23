import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from datetime import datetime

# Set style for better visualizations
#plt.style.use('seaborn')

# Read the data
df = pd.read_csv('../data/future-gc00-daily-prices.csv', parse_dates=[0], index_col=0)

df['points'] = df["Open"].replace(",", "", regex=True).astype(float)
df = df.reindex(
    pd.bdate_range(start=df.index.min(), end=df.index.max()))
df['points'] = df['points'].interpolate()

# Create time series plot
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['points'])
plt.title('Coca-Cola Stock points Over Time')
plt.xlabel('Date')
plt.ylabel('points')
plt.grid(True)
plt.show()

# Function to perform and print ADF test results
def check_stationarity(series, title):
    print(f"\nAugmented Dickey-Fuller Test - {title}")
    result = adfuller(series.dropna())
    print('ADF Statistic:', result[0])
    print('p-value:', result[1])
    print('Critical values:')
    for key, value in result[4].items():
        print(f'\t{key}: {value}')

# Check stationarity of original series
check_stationarity(df['points'], "Original Series")

# First difference
diff1 = df['points'].diff().dropna()

# Plot first difference
plt.figure(figsize=(12, 6))
plt.plot(diff1.index, diff1)
plt.title('First Difference of Stock pointss')
plt.xlabel('Date')
plt.ylabel('points Difference')
plt.grid(True)
plt.show()

# Check stationarity of first difference
check_stationarity(diff1, "First Difference")

# Second difference if needed
diff2 = diff1.diff().dropna()
check_stationarity(diff2, "Second Difference")

# Plot ACF and PACF
# Using the appropriate differenced series (assuming first difference is sufficient)
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))

# ACF plot
plot_acf(diff1, ax=ax1, lags=40)
ax1.set_title('Autocorrelation Function')

# PACF plot
plot_pacf(diff1, ax=ax2, lags=40)
ax2.set_title('Partial Autocorrelation Function')

plt.tight_layout()
plt.show()

# Additional analysis: Calculate basic statistics
print("\nBasic Statistics of Returns (First Difference):")
print(diff1.describe())

# Calculate rolling statistics
rolling_mean = df['points'].rolling(window=20).mean()
rolling_std = df['points'].rolling(window=20).std()

# Plot original data with rolling statistics
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['points'], label='Original')
plt.plot(rolling_mean.index, rolling_mean, label='20-day Rolling Mean')
plt.plot(rolling_std.index, rolling_std, label='20-day Rolling Std')
plt.title('Stock points with Rolling Statistics')
plt.xlabel('Date')
plt.ylabel('points')
plt.legend()
plt.grid(True)
plt.show()