import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# Physical properties of rod (aluminium)
L = 1             # Length in meters
alpha = 1e-4      # Thermal diffusivity in m^2/s

t_final = 250      # Total simulation time

T_initial = 20    # Initial temperature of rod at all points at t=0 (Celcius)

# Boundary conditions
T_left = 100      # Celcius
T_right = 0       # Celcius

# Grid settings 
Nx = 51          # Number of grid points 
dx = L/(Nx-1)     # Distance between grid points 

dt = 0.1          # Time step size (seconds)

# Fourier number
Fo = alpha * dt / dx**2
print(f"Fourier number is: {Fo}")

# Stability condition
if Fo > 0.5:
    print("WARNING! Fo must be <=0.5. Simulation likely to become unstable")

# Creation of 1D grid (array)
x = np.linspace(0,L,Nx)          # Holds the position value for each grid point

# Initial conditions (every grind point at 20C)
T_prev = np.full(Nx, T_initial, dtype = float)       # Temperature array with initial conditions
T_original = T_prev.copy()

# Boundary conditions
T_prev[0] = T_left
T_prev[-1] = T_right

#T_prev = T.copy()                # Copy of temperature array from previous iteration

num_steps = int(t_final/dt)      # Number of time steps in the simulation

# Animation
ani_interval = 10                # Data to be stored after every animation interval (every 10 time steps)
T_data = [T_prev.copy()]              # List of temperature array which are stored, to be used for animation
time_points = [0]                # Times points when data is stored 


for n in range(num_steps):                                                    # Number of time steps
    T_new = T_prev.copy()
    for i in range(1,Nx-1):                                                   # Selecting all the interior points
        T_new[i] = T_prev[i] + Fo*(T_prev[i+1] - 2*T_prev[i] + T_prev[i-1])       # Explicit FDM formula

    T_new[0] = T_left
    T_new[-1] = T_right

    T_prev = T_new.copy()

    if (n+1) % ani_interval == 0:
        T_data.append(T_prev.copy())
        time_points.append((n+1)*dt)

T_final = T_prev.copy()

print(f"Simulation is done after {num_steps} time steps")
print("\nFINAL TEMPERATURE DISTRIBUTION: (from left to right):")
print(np.round(T_final, 2))



# ANIMATION

fig, ax = plt.subplots(figsize = (10,6))

# Plot limits
ax.set_xlim(0,L)
ax.set_ylim(-5,105)

# Initial state
line, = ax.plot(x, T_data[0], marker = "o", linestyle = "-", label = "Temperature")

ax.set_xlabel("Position along the rod (m)")
ax.set_ylabel("Temperature (C)")
ax.set_title("Temperature evolution")
ax.grid(True)
ax.legend()
time_text = ax.text(0.02, 0.95, "", transform = ax.transAxes)

# Update function
def update(frame):
    line.set_ydata(T_data[frame])
    time_text.set_text(f"Time = {time_points[frame]:.2f} s")
    return line, time_text

ani = FuncAnimation(fig, update, frames = len(T_data), interval = 50, blit = True)

plt.show()

ani.save("1D_Heat_Conduction.mp4", writer = "ffmpeg", fps = 20)