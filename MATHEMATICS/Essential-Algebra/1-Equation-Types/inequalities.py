# inequalities_examples.py

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
       a) Region: y ≤ 2x + 1
       b) Region: y > x² – 1
"""
import numpy as np
import matplotlib.pyplot as plt

# Create grid
x_vals = np.linspace(-5, 5, 400)
y_vals = np.linspace(-5, 5, 400)
X, Y = np.meshgrid(x_vals, y_vals)

# a) y ≤ 2x + 1
region1 = (Y <= 2 * X + 1)
plt.figure(figsize=(5, 5))
plt.contourf(X, Y, region1, levels=[-0.5, 0.5, 1.5], alpha=0.4)
plt.plot(x_vals, 2 * x_vals + 1, 'k-', linewidth=1)
plt.title("Region: y ≤ 2x + 1")
plt.xlabel("x");
plt.ylabel("y")
plt.xlim(-5, 5);
plt.ylim(-5, 5)

# b) y > x² – 1
region2 = (Y > X ** 2 - 1)
plt.figure(figsize=(5, 5))
plt.contourf(X, Y, region2, levels=[-0.5, 0.5, 1.5], alpha=0.4)
plt.plot(x_vals, x_vals ** 2 - 1, 'k-', linewidth=1)
plt.title("Region: y > x² - 1")
plt.xlabel("x");
plt.ylabel("y")
plt.xlim(-5, 5);
plt.ylim(-5, 5)

plt.show()
