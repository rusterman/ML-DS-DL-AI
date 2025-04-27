""" Inequality Examples """

"""
    1. Simple Filtering with a Loop
       Find all x in [a, b] such that x² – 4x + 3 > 0
       (i.e. values outside the roots at x=1 and x=3)
"""


def filter_quadratic(a, b):
    result = []
    for x in range(a, b + 1):
        if x ** 2 - 4 * x + 3 > 0:
            result.append(x)
    return result


# Example: from -5 to 5
print("1) x² - 4x + 3 > 0 for x in [-5,5]:", filter_quadratic(-5, 5))


"""
    2. Using a List Comprehension
       Filter values in [-5,5] satisfying |x| < 3
"""
filtered = [x for x in range(-5, 6) if abs(x) < 3]
print("2) Values with |x| < 3:", filtered)


"""
    3. Symbolic Solving with Sympy
       Solve two inequalities:
         a)  2x + 3 > 5
         b)  x² – x ≤ 2
"""
import sympy as sp

x = sp.symbols('x', real=True)
sol1 = sp.solve_univariate_inequality(2 * x + 3 > 5, x)
sol2 = sp.solve_univariate_inequality(x ** 2 - x <= 2, x)

print("3a) 2x + 3 > 5  ⇒", sol1)  # x > 1
print("3b) x² – x ≤ 2  ⇒", sol2)  # -1 ≤ x ≤ 2


"""
    4. Graphing Inequality Regions with Matplotlib
       a) Region: y ≥ x−1
       b) Region: y ≤ −2x+4
"""
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

