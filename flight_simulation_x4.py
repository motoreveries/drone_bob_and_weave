import numpy as np
import matplotlib
matplotlib.use('TkAgg')  # Force the TkAgg backend, which is usually reliable on macOS
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def simulate_flight_path(total_duration=20, dt=0.1, forward_velocity=2, amplitude=2, period=4, base_altitude=5):
    """
    Simulate the drone flight path.
    
    The drone flies forward (x-direction) at a constant speed,
    and its altitude (z) oscillates in a sine-wave pattern.
    """
    t = np.arange(0, total_duration, dt)
    x = forward_velocity * t
    z = base_altitude + amplitude * np.sin(2 * np.pi * t / period)
    return t, x, z

# Simulation parameters
total_duration = 8       # seconds
dt = 0.1                  # seconds per update
forward_velocity = 4      # m/s
amplitude = .5            # meters
period = 1.25                # seconds for one oscillation
base_altitude = 5         # meters

# Get simulated flight path data
t, x, z = simulate_flight_path(total_duration, dt, forward_velocity, amplitude, period, base_altitude)

# Set up the Matplotlib figure and axes
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_xlim(0, x[-1] + 1)
ax.set_ylim(0, base_altitude + amplitude + 2)
ax.set_xlabel('Forward Distance (m)')
ax.set_ylabel('Altitude (m)')
ax.set_title('Simulated Drone Flight Path')

# Create the plot elements: a line for the flight path and a point for the drone
path_line, = ax.plot([], [], 'b-', lw=2, label='Flight Path')
drone_point, = ax.plot([], [], 'ro', markersize=8, label='Drone')
ax.legend()

def init():
    """Initialize the animation."""
    path_line.set_data([], [])
    drone_point.set_data([], [])
    return path_line, drone_point

def update(frame):
    """Update the plot for each frame."""
    frame = int(frame)  # Ensure frame is an integer
    print("Updating frame:", frame)  # Debug print
    if frame == 0:
        path_line.set_data([], [])
        # Provide the data as sequences (lists) for a single point:
        drone_point.set_data([x[0]], [z[0]])
    else:
        path_line.set_data(x[:frame+1], z[:frame+1])
        drone_point.set_data([x[frame]], [z[frame]])
    return path_line, drone_point

# Create the animation object. Blitting is disabled to avoid backend issues.
ani = FuncAnimation(fig, update, frames=range(len(t)),
                    init_func=init, blit=False, interval=dt*1000)

plt.show()
