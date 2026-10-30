"""Lab 17: smooth noisy one-dimensional robot position measurements.

A Kalman filter alternates a prediction step and a measurement-update step.
Here the hidden position is approximately constant. The filter combines a
previous estimate with noisy sensor readings according to their uncertainty.
This is an educational scalar example, not a full robot localization system.
"""

import random
import math

rng = random.Random(17)
true_position = 10.0
measurements = [true_position + rng.gauss(0.0, 2.0) for _ in range(20)]

estimate = 0.0
estimate_variance = 10.0
process_variance = 0.05
measurement_variance = 4.0
filtered = []

for measurement in measurements:
    # Predict: assume position changes little, but allow uncertainty to grow.
    predicted_estimate = estimate
    predicted_variance = estimate_variance + process_variance

    # Update: weight the sensor by its reliability relative to prior uncertainty.
    kalman_gain = predicted_variance / (predicted_variance + measurement_variance)
    estimate = predicted_estimate + kalman_gain * (measurement - predicted_estimate)
    estimate_variance = (1.0 - kalman_gain) * predicted_variance
    filtered.append(estimate)

sensor_rmse = math.sqrt(sum((x - true_position) ** 2 for x in measurements) / len(measurements))
filter_rmse = math.sqrt(sum((x - true_position) ** 2 for x in filtered) / len(filtered))
print("First five raw measurements:", [round(x, 2) for x in measurements[:5]])
print("First five filtered estimates:", [round(x, 2) for x in filtered[:5]])
print("Sensor RMSE:", round(sensor_rmse, 3))
print("Filter RMSE:", round(filter_rmse, 3))

# Change measurement_variance to represent a better or worse sensor. In real
# robotics, state may include velocity/orientation and the motion model matters.
