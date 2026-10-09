"""
linear_system_exercises.py

Exercises for solving systems of linear equations in Python.
"""

# 1. NumPy Solve for n×n
"""
Exercise 2: NumPy Solve for n×n
Using NumPy, solve `A · v = b` for a given square matrix `A` and vector `b`:
- Define `A` and `b` as NumPy arrays.
- Use `np.linalg.solve(A, b)` to compute `v`.
- Verify your solution by printing `A @ v`.

Example:
    A = [[1, 2, -1], [2, -1, 1], [3, 0, -2]]
    b = [2, 1, -1]
"""
import numpy as np
A = np.array([[1, 2, -1],
              [2, -1, 1],
              [3, 0, -2]])
b = np.array([2, 1, -1])
print(f"A = {str(A).replace("\n", "\n    ")}\nb = {b}")

v = np.linalg.solve(A, b)
print(f"v = {v}")

c = A @ v
# c = np.dot(A, v)

if np.allclose(c, b):
    print(f"A @ v = {c}")


# 2. Symbolic Solve with Sympy
"""
Exercise 3: Symbolic Solve with Sympy
Using Sympy, symbolically solve the system:
    a*x + b*y = e
    c*x + d*y = f
- Define symbols `x, y, a, b, c, d, e, f`.
- Construct the equations with `sp.Eq(...)`.
- Use `sp.solve` to find `(x, y)` in terms of the symbols.
- Then substitute `a=1, b=2, c=3, d=4, e=5, f=6` and print the numeric solution.
"""
from sympy import symbols, Eq, solve

x, y, a, b, c, d, e, f = symbols('x, y, a, b, c, d, e, f')
eq_1 = Eq(a*x + b*y, e)
eq_2 = Eq(c*x + d*y, f)

sol = solve([eq_1, eq_2], [x, y])
print(sol)

res_1 = sol[x].subs({a: 1, b: 2, c: 3, d: 4, e: 5, f: 6})
res_2 = sol[y].subs({a: 1, b: 2, c: 3, d: 4, e: 5, f: 6})
print(f"x = {res_1}, y = {res_2}", sep='\n')

# 3. Graphical Intersection with Matplotlib
"""
Exercise 4: Graphical Intersection with Matplotlib
Plot two lines and mark their intersection:
    L1: x + 2y = 4
    L2: 3x − y = 1
Write code that:
- Converts each equation into `y = m*x + c` form.
- Samples `x` over a suitable range.
- Plots both lines with labels.
- Computes their intersection using your `solve_2x2` function.
- Marks the intersection point on the plot.
- Adds title, axis labels, legend, and grid.
Ensure the intersection is clearly highlighted.
"""
import matplotlib.pyplot as plt
import numpy as np

def solve_2x2(L1, L2):
    (a1, b1, c1), (a2, b2, c2) = L1, L2

    A = np.array([
        [a1, b1],
        [a2, b2]
    ])
    b = np.array([c1, c2])

    return np.linalg.solve(A, b)


x_vals = np.linspace(-5, 5, 400)
# y_vals = np.linspace(-5, 5, 400)

#     ax+by=c
L1 = [1, 2, 4]      # L1: x + 2y = 4  =>  L1: a1=1, b1=2, c1=4
L2 = [3, -1, 1]     # L2: 3x − y = 1  =>  L2: a2=3, b2=-1, c2=1

x, y = solve_2x2(L1, L2)
# intersect = solve_2x2(L1, L2)

y1 = (4 - x_vals) / 2
y2 = 3 * x_vals - 1

plt.figure(figsize=(6,6))
plt.plot(x_vals, y1,  'b-', label='y = (4 - x) / 2')
plt.plot(x_vals, y2,  'r-', label='y = 3 * x - 1')
plt.plot(x, y, 'ko', markersize=5,  label='Intersection')
# plt.plot(intersect[0], intersect[1], 'ko', markersize=5, label='Intersection')

# plt.fill_between(x_vals, y1, y2, color='green', alpha=0.5)

plt.title("Intersection of: y = (4 - x) / 2  ∧  y = 3 * x - 1 ")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc='upper right')
plt.xlim(-1, 5)
plt.ylim(-2, 6)

plt.grid(True)
# plt.grid(True, linestyle='--', linewidth=0.5, alpha=0.5)
plt.show()
