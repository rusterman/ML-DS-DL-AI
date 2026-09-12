# inequalities_exercises.py

""" Inequality Exercises """
from seaborn.colors import xkcd_rgb

"""
    1. Simple Inequality with a Loop
       Find all integer x in [a, b] such that 2x – 5 > 3.

    Exercise:
    Write a function `filter_simple(a, b)` that returns a list of all x in the inclusive range [a, b]
    satisfying 2*x - 5 > 3, then print the result for a = -5, b = 10.
"""
# Your Solution...
def filter_simple(a, b):
    result = []

    for x in range(a, b + 1):
        if 2 * x - 5 > 3:
            result.append(x)

    return result


# Example: from -5 to 10
print("1) 2 * x - 5 > 3 for x in [-5, 10]:", filter_simple(-5, 10))


"""
    2. Symbolic Solution with Sympy
       Solve the quadratic inequality x² – 4x + 3 ≤ 0 symbolically.

    Exercise:
    Use sympy’s `solve_univariate_inequality` to find the solution set of
        x**2 - 4*x + 3 <= 0
    and print it.
"""
# Your Solution...


"""
    3. System of Linear Inequalities with Sympy
       Find the overlap region for:
           x + 2y ≤ 6
           2x -  y ≥ 1

    Exercise:
    Use sympy’s `reduce_inequalities` (or equivalent) to solve the system
        [x + 2*y <= 6,  2*x - y >= 1]
    and display the solution conditions.
"""
# Your Solution...
import sympy as sp

x = sp.symbols('x', real=True)
y = sp.symbols('y', real=True)

sol1 = sp.reduce_inequalities(x + 2 * y <= 6, x)
sol2 = sp.reduce_inequalities(2 * x - y >= 1, y)

print("3a) x + 2 * y <= 6  ⇒", sol1)  # x > 1
print("3b) 2 * x - y >= 1  ⇒", sol2)  # -1 ≤ x ≤ 2


"""
    4. Graphing a Feasible Region with Matplotlib
       Plot the region defined by:
           y ≥ x - 1
           y ≤ -2*x + 4

    Exercise:
    Create a grid over x,y in [-1, 5] and use numpy + matplotlib to shade the intersection
    of the two half-planes. Draw the boundary lines and show the feasible region.
"""
# Your Solution...
import numpy as np
import matplotlib.pyplot as plt

x, y = np.mgrid[-1:5:400j, -1:5:400j]
feasible = (y >= x - 1) & (y <= -2 * x + 4)

plt.figure(figsize=(6,6))
plt.contourf(x, y, feasible, levels=[-1, 0.5, 1.5], alpha=0.4)

# 1
x_val = np.linspace(-1, 5, 400)
plt.plot(x_val, x_val - 1, 'b-', label='y = x - 1')
plt.plot(x_val, -2 * x_val + 4, 'r-', label='y = -2x + 4')

# 2
'''
plt.plot(x_val := np.linspace(-1, 5, 500), x_val - 1, 'b-', label='y = x - 1')
plt.plot(x_val, -2 * x_val + 4, 'r-', label='y = -2x + 4')
'''

plt.title("Feasible Region: { y ≥ x−1  ∧  y ≤ −2x+4 }")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc='upper right')
plt.xlim(-1, 5)
plt.ylim(-1, 5)

plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)
plt.show()


"""
    5. Using a List Comprehension
       Filter values in [-5,5] satisfying |x| < 3

    Exercise:
    Write a single list comprehension that produces all integers x between -5 and 5
    for which abs(x) < 3, then print the resulting list.
"""
# Your Solution...
filter_val = [x for x in range(-5, 6) if abs(x) < 3]
print("5) Values with |x| < 3:", filter_val)

