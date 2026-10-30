# Chapter 3 — Time-series forecasting

Time-series observations are ordered in time and may contain trend, seasonality, cycles, and sudden shifts. Define the forecast horizon and the information cutoff: what will be known when the prediction is made?

Start with baselines such as last value, moving average, or seasonal repeat. Evaluate with chronological splits or rolling-origin evaluation. Random splitting can place future observations in training and produce an unrealistic score.

Report error by forecast horizon and time period. A single average can hide seasonal failure. Prediction intervals communicate uncertainty but rely on assumptions about past errors continuing.

## Questions and answers

**What is seasonality?**  
A pattern that repeats at a known calendar interval, such as daily or yearly.

**Why use a naive baseline?**  
It reveals whether complex models improve on simple persistence or seasonal structure.

**Why can historical accuracy fail after deployment?**  
Data distribution or relationships can change due to policy, market, weather, or behavior shifts.

## Practice and mastery

Forecast a public series with a seasonal-naive baseline and one model. Evaluate on several rolling windows, report error by horizon, and describe one structural change that could invalidate the forecast.