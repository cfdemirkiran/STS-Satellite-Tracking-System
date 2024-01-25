#
# STS - Satellite Tracking System Project
# Author         : Cem Furkan DEMİRKIRAN
# Date Time      : 14 Jan 2024
#
# Project Detail : In the satellite tracking project we have developed, we obtain UTC
# time data at 10 degrees before entering the satellite's field of view, 10 degrees
# before exiting, and at the exact zenith point. To acquire this data, it is necessary
# to input the TLE (Two-Line Element) data of the selected satellite, the start date
# information, and the duration for which measurements are desired as parameters.
# Optionally, the angle setting of 10 degrees can be adjusted according to preference.
#

from skyfield.api import load, Topos
from datetime import datetime, timedelta
import io
import os

def calculate_passes(tle_line1, tle_line2, observer_latitude, observer_longitude, start_date):
    # Combine TLE lines into a single string
    tle_data = f"{tle_line1}\n{tle_line2}"

    # Temporary file for TLE data
    with io.open("tle_file.txt", mode="w", encoding="utf-8") as tle_file:
        tle_file.write(tle_data)

    # Load Skyfield data from the temporary file
    satellites = load.tle_file("tle_file.txt")
    observer_location = Topos(latitude=observer_latitude, longitude=observer_longitude)

    # Set up time range for passes
    ts = load.timescale()
    start_time = ts.utc(*start_date)
    end_time = start_time + timedelta(days=2)

    # Calculate passes
    t, events = satellites[0].find_events(observer_location, start_time, end_time, altitude_degrees=10.0)

    # Print the passes
    for ti, event in zip(t, events):
        name = ("rise above 10°", "culminate     ", "set below 10° ")[event]
        print(f"{name} at {ti.utc_datetime()}")

    # Remove the temporary file
    os.remove("tle_file.txt")

# Example usage
tle_line1 = '1 58743U 24005R   24018.54375291 -.00188678  00000-0 -10906-2 0  9997'
tle_line2 = '2 58743  43.0052 157.6181 0003025 252.5106 107.5434 15.78148885  2835'

observer_latitude = 41.01  # Latitude of Istanbul
observer_longitude = 28.95  # Longitude of Istanbul
start_date = (2024, 1, 24)

calculate_passes(tle_line1, tle_line2, observer_latitude, observer_longitude, start_date)
