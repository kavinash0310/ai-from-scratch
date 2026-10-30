# Chapter 3 — Time-series forecasting

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

Time-series observations are ordered in time and may contain trend, seasonality, cycles, and sudden shifts. Define the forecast horizon and the information cutoff: what will be known when the prediction is made?

Start with baselines such as last value, moving average, or seasonal repeat. Evaluate with chronological splits or rolling-origin evaluation. Random splitting can place future observations in training and produce an unrealistic score.

Report error by forecast horizon and time period. A single average can hide seasonal failure. Prediction intervals communicate uncertainty but rely on assumptions about past errors continuing.

## Deeper walkthrough: rolling-origin evaluation

Assume monthly sales from January 2021 through December 2025 and a three-month forecast horizon. Train through December 2023 and predict January–March 2024. Then move the cutoff forward one month, refit if appropriate, and predict the next three months. Repeat across several cutoffs.

This tests the real direction of use: the model only sees the past. Compare a seasonal-naive forecast (same month last year) with a learned model. Report error separately for each horizon month because month three may be much harder than month one.

For series with changing scale, MAPE can explode when actual values are near zero. Mean absolute error remains in the target units; scaled errors may aid comparison across series. Choose metrics before selecting the winning model.

Forecast intervals and scenarios matter when a decision depends on risk. A point prediction of 100 does not tell a planner whether plausible values range from 98 to 102 or from 40 to 160.

## Questions and answers

**What is seasonality?**  
A pattern that repeats at a known calendar interval, such as daily or yearly.

**Why use a naive baseline?**  
It reveals whether complex models improve on simple persistence or seasonal structure.

**Why can historical accuracy fail after deployment?**  
Data distribution or relationships can change due to policy, market, weather, or behavior shifts.

## Practice and mastery

Forecast a public series with a seasonal-naive baseline and one model. Evaluate on several rolling windows, report error by horizon, and describe one structural change that could invalidate the forecast.