import numpy as np
import matplotlib.pyplot as plt

# 1) Create grid over x,y in [-1, 5]
x_vals = np.linspace(-1, 5, 400)
y_vals = np.linspace(-1, 5, 400)
X, Y = np.meshgrid(x_vals, y_vals)

# 2) Define each half‐plane
region1 = (Y >= X - 1)       # y ≥ x - 1
region2 = (Y <= -2*X + 4)    # y ≤ -2x + 4

# 3) Intersection: both must hold
feasible = region1 & region2

# 4) Plot the feasible region
plt.figure(figsize=(6,6))
plt.contourf(X, Y, feasible, levels=[-0.5, 0.5, 1.5], alpha=0.4)

# 5) Draw the boundary lines
plt.plot(x_vals,      x_vals - 1,  'b-', label='y = x - 1')
plt.plot(x_vals, -2*x_vals + 4,     'r-', label='y = -2x + 4')

# 6) Labels, legend, limits
plt.title("Feasible Region: { y ≥ x−1  ∧  y ≤ −2x+4 }")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc='upper right')
plt.xlim(-1, 5)
plt.ylim(-1, 5)

plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)
plt.show()
