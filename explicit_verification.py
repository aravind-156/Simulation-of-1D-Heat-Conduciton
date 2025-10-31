import numpy as np
import matplotlib.pyplot as plt

# Physical properties of rod (aluminium)
L = 1               # Length in meters
alpha = 1e-4        # Thermal diffusivity in m^2/s

t_final = 500      # Total simulation time


# Boundary conditions
T_left = 0          # Uniteless
T_right = 0         # Unitless

# Grid settings 
Nx = 51            # Number of grid points 
dx = L/(Nx-1)       # Distance between grid points 

dt = 0.1            # Time step size (seconds)

# Fourier number
Fo = alpha * dt / dx**2
print("Fourier number is:", Fo)

# Stability condition
if Fo > 0.5:
    print("WARNING! Fo must be <=0.5. Simulation likely to become unstable")

# Creation of 1D grid (array)
x = np.linspace(0,L,Nx)          # Holds the position value for each grid point

# Initial conditions (every grind point at the sin curve)
T_prev = np.sin(np.pi * x/L)          # Temperature array with initial conditions
T_original = T_prev.copy()

# Boundary conditions
T_prev[0] = T_left
T_prev[-1] = T_right

#T_prev = T.copy()                # Copy of temperature array from previous iteration

num_steps = int(t_final/dt)      # Number of time steps in the simulation

for n in range(num_steps): 
    T_new = T_prev.copy()                                                   
    for i in range(1,Nx-1):                                                   
        T_new[i] = T_prev[i] + Fo*(T_prev[i+1] - 2*T_prev[i] + T_prev[i-1])       # Explicit FDM formula
    
    T_new[0] = T_left                                                       
    T_new[-1] = T_right

    T_prev = T_new.copy()

T_final = T_prev.copy()

print("Simulation is done after", num_steps, "time steps")
print("\nFINAL TEMPERATURE DISTRIBUTION: (from left to right):")
print(np.round(T_final, 2))

# Exact analytical solution at the final time
T_analytical = np.exp(-alpha * (np.pi/L)**2 * t_final) * np.sin(np.pi * x/L)



# MATPLOTLIB 

plt.figure(figsize = (10,6))
plt.plot(x, T_analytical, "k-", linewidth = 2, label = " Known Analytical Solution")
plt.plot(x, T_final, "go", markersize = 4, label = "Explicit Numerical Solution")
plt.plot(x, T_original, "r--", linewidth = 1.5, label = "Initial temperature (t=0)")

plt.xlabel("Position along rod (m)")
plt.ylabel("Temperature (unitless)")
plt.title(f"Verification of EXPLICIT solver at final time ({t_final}s)")
plt.grid(True)
plt.legend()

plt.show()

