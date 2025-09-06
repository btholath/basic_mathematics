"""
Problem Breakdown (in simple terms)
• 	The bank robber starts first and drives at 150 km/h.
• 	The sheriff starts 5 minutes later but drives faster at 180 km/h.
• 	We want to know when the sheriff catches up and how far both have traveled by then.

Math Behind It
Let:
- t = time in minutes since the sheriff started
- Robber's head start = 150 \times \frac{5}{60} = 12.5 km

Distance by sheriff = Distance by robber
180 × (t / 60) = 150 × (t / 60 + 5 / 60)

Solving gives:
t = 25 minutes
Distance = 75 km

"""
import matplotlib.pyplot as plt
import numpy as np

# Speeds in km/h
sheriff_speed = 180
robber_speed = 150

# Convert speeds to km/min
sheriff_speed_min = sheriff_speed / 60
robber_speed_min = robber_speed / 60

# Robber's head start in km
head_start = robber_speed_min * 5  # 5 minutes

# Time range in minutes
time = np.arange(0, 40, 0.5)  # 0 to 40 minutes

# Distance calculations
robber_distance = robber_speed_min * (time + 5)  # Robber starts 5 min earlier
sheriff_distance = sheriff_speed_min * time

# Find intersection point
catch_time = 25  # minutes
catch_distance = sheriff_speed_min * catch_time

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time, robber_distance, label='Bank Robber (150 km/h)', color='blue')
plt.plot(time, sheriff_distance, label='Sheriff (180 km/h)', color='green')
plt.axvline(x=catch_time, linestyle='--', color='gray', label='Catch Point')
plt.axhline(y=catch_distance, linestyle='--', color='gray')

# Annotate catch point
plt.scatter(catch_time, catch_distance, color='red')
plt.text(catch_time + 1, catch_distance + 2, f'Catch at {catch_time} min, {catch_distance} km', color='black')

# Labels and legend
plt.xlabel('Time (minutes)')
plt.ylabel('Distance (km)')
plt.title('Sheriff vs Bank Robber: Chase Graph')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
plt.savefig("/workspaces/basic_mathematics/linear_algebra_for_representations/thief_robber_car_chase.png")
