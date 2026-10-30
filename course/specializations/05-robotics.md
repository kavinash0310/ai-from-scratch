# Chapter 5 — Robotics and embodied AI

Robotics connects perception, state estimation, planning, and control to physical actions. Sensors are noisy and delayed. The world can move between observation and action. A safe robot must account for dynamics, actuator limits, collisions, and failures.

A loop is: observe → estimate state → plan → act → observe again. Simulators support safer experiments, but simulator-to-real differences can cause failure. Calibration, latency, hardware variation, and environmental changes all matter.

Use staged testing: offline simulation, controlled lab, limited environment, then broader deployment only with safety boundaries and a stop mechanism.

## Questions and answers

**Why is robotics harder than image classification?**  
The system acts in a changing world and its actions affect future observations. Mistakes can have physical consequences.

**What is state estimation?**  
Combining noisy sensor observations to estimate the system's current state.

**Why can simulation results fail on hardware?**  
The simulator may not match friction, lighting, timing, sensor noise, or physical dynamics.

## Practice and mastery

Simulate a simple robot moving through a grid. Add noisy position observations and a collision constraint. Describe how state uncertainty affects safe planning.