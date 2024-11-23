# Load required libraries
library(tidyverse)
library(tseries)
library(forecast)
library(lubridate)

# Read the data
df <- read.csv("coca_cola.csv")

# Convert dates to proper date format
df$Date <- as.Date(df$Date)

# Create time series plot
ggplot(df, aes(x = Date, y = Price)) +
  geom_line() +
  theme_minimal() +
  labs(title = "Coca-Cola Stock Price Over Time",
       x = "Date",
       y = "Price") +
  theme(plot.title = element_text(hjust = 0.5))

# Convert to time series object
ts_data <- ts(df$Price, frequency = 252)  # 252 trading days per year

# Perform ADF test for stationarity
adf_test <- adf.test(ts_data)
print("ADF Test for Original Series:")
print(adf_test)

# If non-stationary, take first difference
diff1 <- diff(ts_data)
adf_diff1 <- adf.test(diff1)
print("\nADF Test for First Difference:")
print(adf_diff1)

# Plot differenced series
plot(diff1, main = "First Difference of Stock Prices",
     ylab = "Difference", xlab = "Time")

# If still non-stationary, take second difference
diff2 <- diff(diff1)
adf_diff2 <- adf.test(diff2)
print("\nADF Test for Second Difference:")
print(adf_diff2)

# Plot ACF and PACF of the stationary series
# (Using the appropriate differenced series based on ADF test results)
par(mfrow = c(2,1))
acf(diff1, main = "ACF of Differenced Series")
pacf(diff1, main = "PACF of Differenced Series")