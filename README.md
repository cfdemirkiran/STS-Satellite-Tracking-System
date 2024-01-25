# STS-Satellite-Tracking-System
This Python script is part of the Satellite Tracking System (STS) project, tracking a satellite's movement and capturing UTC time at key points: 10 degrees before entry, 10 degrees before exit, and at the zenith. Input TLE data, observer's location, start date, and optional 10-degree angle adjustment for desired results.

The Satellite Tracking System (STS) project aims to provide a versatile tool for tracking the movement of satellites and capturing relevant data during specific phases of their trajectory. Satellite tracking is crucial for various applications, including telecommunications, Earth observation, and scientific research.

In satellite tracking systems, Two-Line Element (TLE) data is utilized to determine the orbital parameters of a satellite. TLE data includes information about the satellite's position, velocity, and orbital elements. This data, often provided by organizations like NORAD, allows accurate predictions of a satellite's location at any given time.

This Python script focuses on obtaining UTC time data during significant points in a satellite's pass. Specifically, it captures the time 10 degrees before the satellite enters the observer's field of view, 10 degrees before it exits, and at the zenith. The observer's geographical coordinates, TLE data of the target satellite, the start date, and an optional 10-degree angle adjustment are used as input parameters.

The implementation relies on the skyfield.api library, a powerful tool for high-precision astronomy calculations. It dynamically loads TLE data, calculates the satellite's position, and identifies the specified events during its pass.

Understanding the fundamentals of satellite tracking systems is essential for optimizing the script's usage. Satellites move along Keplerian orbits, and their positions can be accurately predicted based on the laws of celestial mechanics. The script's flexibility allows users to adapt it to different scenarios and satellite missions.

This project encourages exploration and experimentation in satellite tracking, fostering a deeper understanding of orbital dynamics and enabling users to interact with real-world data from Earth's orbiting satellites.
