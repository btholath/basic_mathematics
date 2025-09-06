import matplotlib.pyplot as plt
import numpy as np

# Speeds in km/h converted to km/min
sheriff_speed = 180 / 60  # 3 km/min
robber_speed = 150 / 60   # 2.5 km/min

# Robber's head start in minutes
head_start_min = 5
head_start_km = robber_speed * head_start_min

# Time range in minutes
time = np.arange(0, 40, 0.5)

# Distance calculations
robber_distance = robber_speed * (time + head_start_min)
sheriff_distance = sheriff_speed * time

# Catch-up point
catch_time = 25  # minutes after sheriff starts
catch_distance = sheriff_speed * catch_time

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(time, robber_distance, label='Bank Robber (Slope = 2.5)', color='blue')
plt.plot(time, sheriff_distance, label='Sheriff (Slope = 3)', color='green')

# Dotted lines at intersection
plt.axvline(x=catch_time, linestyle='--', color='gray')
plt.axhline(y=catch_distance, linestyle='--', color='gray')

# Mark intersection point
plt.scatter(catch_time, catch_distance, color='red', zorder=5)
plt.text(catch_time + 1, catch_distance + 2, f'Catch at {catch_time} min,\n{catch_distance} km', color='black')

# Labels and legend
plt.xlabel('Time (minutes)')
plt.ylabel('Distance (km)')
plt.title('Sheriff vs Bank Robber: Distance-Time Graph')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
plt.savefig("/workspaces/basic_mathematics/linear_algebra_for_representations/thief_robber_car_chase_01.png")
