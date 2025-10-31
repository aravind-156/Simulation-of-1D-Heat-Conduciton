import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

# Physical properties of rod (aluminium)
L = 1             # Length in meters
alpha = 1e-4     # Thermal diffusivity in m^2/s

t_final = 1000      # Total simulation time

T_initial = 20    # Initial temperature of rod at all points at t=0 (Celcius)

# Boundary conditions
T_left = 0      # Celcius
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

# Initial conditions (sin wave)
T_prev = np.sin(np.pi * x/L)       # Temperature array with initial conditions
T_original = T_prev.copy()

# Boundary conditions
T_prev[0] = T_left
T_prev[-1] = T_right

#T_prev = T.copy()                # Copy of temperature array from previous iteration

num_steps = int(t_final/dt)      # Number of time steps in the simulation


# IMPLICIT METHOD

# Matrix A (Coeff of unknown future temperatures in the system of linear equations)
A = np.zeros((Nx-2,Nx-2))
np.fill_diagonal(A, 1 + 2*Fo)
np.fill_diagonal(A[:,1:], -Fo)      
np.fill_diagonal(A[1:,:], -Fo)         # A is tridiagonal

for i in range(num_steps):
    b = T_prev[1:-1].copy()            # b contains info about known temperatures at current time
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

# Exact analytical solution at the final time
T_analytical = np.exp(-alpha * (np.pi/L)**2 * t_final) * np.sin(np.pi *x/L)


# MATPLOTLIB 

plt.figure(figsize=(10, 6))            
plt.plot(x, T_analytical, "k-", linewidth = 2, label = "Analytical Solution")
plt.plot(x,T_final, "go", markersize = 4, label = "Implicit Numerical Solution")
plt.plot(x, T_original, "r--", linewidth = 1.5, label = "Initial temperature (t=0)")


#Labels
plt.xlabel("Position along rod (m)")
plt.ylabel("Temperature (unitless)")
plt.title(f"Verification of IMPLICIT solver at final time ({t_final}s)")
plt.grid(True)
plt.legend()

plt.show()