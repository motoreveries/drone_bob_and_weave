# The Bob & Weave
## An Automated Tactical Evasive Drone Flight Pattern Simulation
 <img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Nqbevh_5h0jJ0O2MHx5L9A.jpeg">
Using Python and Matplotlib, I designed and programmed an automated evasive maneuver flight path for a drone to avoid oncoming obstacles. This flight pattern focuses on variable altitude adjustments in combination with forward velocity to make an airborne drone a less vulnerable target to oncoming objects.
<br>
 <img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*lBiTXxZIm7UQrG0NnXEUEg.gif">

## Tools

[Python](https://www.python.org/downloads) <br>
[Matplotlib](https://matplotlib.org) <br>
Terminal or preferred command interface

## The Procedure

Step 1. Open terminal or preferred command interface. To make sure Python is installed, run:
```bash
python3 --version
```
You should get
```python
Python 3.13.1
```
Step 2. After you’ve installed Matplotlib, run: 
```bash
pip3 install numpy matplotlib
```
You should get confirmation of succesful installment.

Step 3. Create a file directory for Python to pull from.

Step 4. Create and save a new text file ending in the native Python file extension format “.py”.

    Example: DRONE_FLIGHT_SIMULATION.py

Step 5. In your newly created Python file, run the following code:
```python
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
total_duration = 20       # seconds
dt = 0.1                  # seconds per update
forward_velocity = 2      # m/s
amplitude = 2             # meters
period = 4                # seconds for one oscillation
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

```
Step 6. In your Terminal window, input your newly created directory file path proceeded by the command “cd” as shown in the example below.

```bash
cd /path/to/your/directory
```

Step 7. Run the following command to execute simulation.

```bash
python3 flight_simulation.py
```
A new window will open to display your flight path simulation.
<br>
 <img src="https://miro.medium.com/v2/resize:fit:1400/format:webp/1*g1mCsShuJHi1TOlxwvzMRA.gif">

## Modifications
This flight path can be customized as needed using the following parameters:
<ul>
  <li>forward_velocity: Controls how fast the drone moves horizontally (in meters per second).</li>
  <li>period: Controls how quickly the drone completes one full vertical oscillation (in seconds).</li>
  <li>total_duration: Sets the overall length of the flight simulation (in seconds).</li>
</ul>

Go back into your Python file and experiment with these parameters to adjust the flight path to your desired pattern.

```python
# Customization parameters for the flight pattern
total_duration = 20       # Overall simulation time (seconds)
forward_velocity = 2      # Horizontal speed (m/s)
period = 4                # Vertical oscillation period (seconds)

def simulate_flight_path(total_duration, dt, forward_velocity, amplitude, period, base_altitude):
    # Create time stamps for the simulation
    t = np.arange(0, total_duration, dt)
    
    # Determine horizontal position: increases linearly with time
    x = forward_velocity * t
    
    # Determine vertical position: oscillates with the given period
    z = base_altitude + amplitude * np.sin(2 * np.pi * t / period)
    
    return t, x, z
```
## Contribute
What kind of automated flight patterns can you come up with?

## License
<b>Public Domain</b>
<br>
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.


