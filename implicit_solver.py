import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

# Physical properties of rod (aluminium)
L = 1             # Length in meters
alpha = 1e-4     # Thermal diffusivity in m^2/s

t_final = 150      # Total simulation time

T_initial = 20    # Initial temperature of rod at all points at t=0 (Celcius)

# Boundary conditions
T_left = 100      # Celcius
T_right = 0       # Celcius

# Grid settings 
Nx = 51          # Number of grid points 
dx = L/(Nx-1)     # Distance between grid points 

dt = 1          # Time step size (seconds)

# Fourier number
Fo = alpha * dt / dx**2
print(f"Fourier number is: {Fo}")

# Creation of 1D grid (array)
x = np.linspace(0,L,Nx)          # Holds the position value for each grid point

# Initial conditions (every grind point at 20C)
T_prev = np.full(Nx, T_initial, dtype = float)       # Temperature array with initial conditions
T_original = T_prev.copy()

# Boundary conditions
T_prev[0] = T_left
T_prev[-1] = T_right

num_steps = int(t_final/dt)      # Number of time steps in the simulation


# IMPLICIT METHOD

# Matrix A (Coeff of unknown future temperatures in the system of linear equations)
A = np.zeros((Nx-2,Nx-2))
np.fill_diagonal(A, 1 + 2*Fo)
np.fill_diagonal(A[:,1:], -Fo)      
np.fill_diagonal(A[1:,:], -Fo)         # A is tridiagonal

for i in range(num_steps):
    b = T_prev[1:-1].copy()            # b contains info about interior known temperatures at current time
    b[0] += Fo * T_left
    b[-1] += Fo * T_right

    T_int = la.solve(A,b)              # Solves for unknown temperatures at the next time step
    T_prev[1:-1] = T_int
    T_prev[0] = T_left
    T_prev[-1] = T_right
    
T_final = T_prev.copy()

print(f"Simulation is done after {num_steps} time steps")
print("\nFINAL TEMPERATURE DISTRIBUTION: (from left to right):")
print(np.round(T_final, 2))


# MATPLOTLIB 

plt.figure(figsize=(10, 6))            
plt.plot(x, T_final, marker="o", color = "green", linestyle="-", label="Final Temperature")
plt.plot(x, T_original, "r--", linewidth = 1.5, label = "Initial temperature (t=0)")


#Labels
plt.xlabel("Position along rod (m)")
plt.ylabel("Temperature (C)")
plt.title(f"Temperature distribution after {t_final} seconds (Implicit FDM)")
plt.grid(True)
plt.legend()

plt.show()