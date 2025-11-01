# Simulation of 1D Heat Conduction

Designed two Python solvers based on Explicit and Implicit Finite Difference Method to simulate one dimensional transient heat conduction in a rod. Initial and Dirichlet boundary conditions were imposed. The numerical solutions were validated against known analytical results, demonstrating high accuracy of the solvers. The animation generated showed how the temperature profile would vary with time.

---

## Methods Implemented

- **Explicit Finite Difference Method**  
  Stability depends on Fourier Number.
- **Implicit Finite Difference Method**  
  Unconditionally stable.

Both methods were validated against analytical solutions to ensure accuracy.

---

## Files in This Repository

| File | Description |
|------|--------------|
| `explicit_solver.py` | Implements the explicit FDM for 1D transient heat conduction |
| `explicit_verification.py` | Compares explicit numerical results with analytical solution |
| `implicit_solver.py` | Implements the implicit FDM for the same problem |
| `implicit_verification.py` | Compares implicit results with analytical solution |
| `animation.py` | Generates an animation showing temperature variation along the rod over time |

---

