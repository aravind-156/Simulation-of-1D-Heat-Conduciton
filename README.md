# Simulation of 1D Heat Conduction

This project simulates one-dimensional transient heat conduction in a rod using Explicit and Implicit Finite Difference Methods (FDM). It demonstrates how temperature evolves over time under given initial and Dirichlet boundary conditions.

---

## Methods Implemented

- **Explicit Finite Difference Method (Forward Time Centered Space - FTCS):**  
  Straightforward to implement but conditionally stable depending on the time step and grid spacing.

- **Implicit Finite Difference Method (Backward Time Centered Space - BTCS):**  
  Unconditionally stable and solved using the tridiagonal matrix algorithm.

Both methods were validated against analytical solutions to ensure accuracy.

---

## Files in This Repository

| File | Description |
|------|--------------|
| `explicit_solver.py` | Implements the explicit FDM for 1D transient heat conduction |
| `explicit_verification.py` | Compares explicit numerical results with analytical solution |
| `implicit_solver.py` | Implements the implicit FDM (Backward Euler) for the same problem |
| `implicit_verification.py` | Compares implicit results with analytical solution |
| `animation.py` | Generates an animation showing temperature variation along the rod over time |

---

## Author

**Aravind Krishnan**  
B.Tech in Mechanical Engineering  
National Institute of Technology, Tiruchirappalli  
Email: [aravindworkacc@gmail.com](mailto:aravindworkacc@gmail.com)
