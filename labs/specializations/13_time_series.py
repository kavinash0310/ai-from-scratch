"""Lab 13: compare a seasonal-naive forecast with a simple baseline.

We create a weekly pattern with a slow upward trend. Evaluation uses the last
12 observations, after training on earlier timestamps. This demonstrates a
rolling one-step forecast: the previous week's observed value is available
when forecasting each next day. It is not a random train/test split.
"""

import math

series = [
    20 + 0.08 * t + 4 * math.sin(2 * math.pi * t / 7)
    for t in range(60)
]
split = 48
train, test = series[:split], series[split:]
seasonal_predictions = [series[t - 7] for t in range(split, len(series))]
mean_prediction = sum(train) / len(train)
mean_predictions = [mean_prediction] * len(test)


def mae(actual, predicted):
    return sum(abs(a - p) for a, p in zip(actual, predicted)) / len(actual)


print("Training timestamps:", len(train))
print("Held-out future timestamps:", len(test))
print("Seasonal-naive MAE:", round(mae(test, seasonal_predictions), 3))
print("Training-mean MAE:  ", round(mae(test, mean_predictions), 3))
for day, actual, predicted in zip(range(split, len(series)), test, seasonal_predictions):
    print(f"t={day:02d} actual={actual:.2f} forecast={predicted:.2f}")

# Change the trend or seasonal period. Explain when the naive seasonal method
# fails. For a fixed-origin 12-step forecast, do not use test observations as
# inputs for later test predictions; make that forecasting contract explicit.
