# Chapter 5 — Robotics and embodied AI

> **Book-length subject volume:** For expanded explanations, worked examples, review questions, and practice, read the [specializations textbook](TEXTBOOK.md).

> **Expanded lesson notes:** Open the [full subject notes](DEEP_NOTES.md) for step-by-step explanations, key vocabulary, worked examples, Q&A, and practice.

Robotics connects perception, state estimation, planning, and control to physical actions. Sensors are noisy and delayed. The world can move between observation and action. A safe robot must account for dynamics, actuator limits, collisions, and failures.

A loop is: observe → estimate state → plan → act → observe again. Simulators support safer experiments, but simulator-to-real differences can cause failure. Calibration, latency, hardware variation, and environmental changes all matter.

Use staged testing: offline simulation, controlled lab, limited environment, then broader deployment only with safety boundaries and a stop mechanism.

## Deeper walkthrough: noisy position sensing

Imagine a wheeled robot that estimates its position from wheel rotation. Small wheel slip accumulates, so its estimated position drifts. A camera landmark can correct the estimate but arrives intermittently and may be noisy.

The robot combines a motion model with sensor observations to estimate state, then plans a route and sends motor commands. A controller must account for how quickly the robot can turn and stop. A planner that assumes instant movement may select a path the hardware cannot follow.

Test first in simulation, then in a controlled physical space with a low speed limit, emergency stop, and obstacles. Compare predicted state with measured ground truth. Domain randomization can vary simulated friction and sensor noise, but it cannot guarantee reality is covered.

An AI controller should fail safe when localization confidence is too low. That means stopping, asking for assistance, or selecting a conservative action rather than continuing blindly.

## Questions and answers

**Why is robotics harder than image classification?**  
The system acts in a changing world and its actions affect future observations. Mistakes can have physical consequences.

**What is state estimation?**  
Combining noisy sensor observations to estimate the system's current state.

**Why can simulation results fail on hardware?**  
The simulator may not match friction, lighting, timing, sensor noise, or physical dynamics.

## Practice and mastery

Simulate a simple robot moving through a grid. Add noisy position observations and a collision constraint. Describe how state uncertainty affects safe planning.