""" Systems of Linear Equations Examples """

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

# 1. General n×n with NumPy
A = np.array([
    [1, 2, -1],
    [2, -1, 1],
    [3, 0, -2]
], dtype=float)
b = np.array([2, 1, -1], dtype=float)

v = np.linalg.solve(A, b)
print("1) NumPy solution of 3×3 system v =", v)
# Verify: A @ v ≈ b
print("   Check A·v =", A.dot(v))

# 2. Symbolic Solve with Sympy
x, y, a, b_sym, c, d, e, f = sp.symbols('x y a b c d e f')
eqs = [
    sp.Eq(a * x + b_sym * y, e),
    sp.Eq(c * x + d * y, f),
]
sol_sym = sp.solve(eqs, (x, y))
print("2) Symbolic solution:", sol_sym)

# Substitute numeric values
values = {a: 1, b_sym: 2, c: 3, d: 4, e: 5, f: 6}
numeric_sol = {var: expr.subs(values) for var, expr in sol_sym.items()}
print("   Example with numbers:", numeric_sol)


# 3. Graphing Two Equations with Matplotlib
def solve_2x2(a1, b1, a2, b2, c1, c2):
    """
    Solve
        a1*x + b1*y = c1
        a2*x + b2*y = c2
    """
    M = np.array([[a1, b1],
                  [a2, b2]], dtype=float)
    C = np.array([c1, c2], dtype=float)
    return np.linalg.solve(M, C)


# Lines:
#   L1: x + 2y = 4  →  y = (4 - x) / 2
#   L2: 3x − y = 1  →  y = 3x - 1
x_vals = np.linspace(-1, 5, 200)
y1 = (4 - x_vals) / 2
y2 = 3 * x_vals - 1

# Find intersection
xi, yi = solve_2x2(1, 2, 3, -1, 4, 1)

# Plot
plt.figure(figsize=(6, 6))
plt.plot(x_vals, y1, label='L1: x + 2y = 4')
plt.plot(x_vals, y2, label='L2: 3x − y = 1')
plt.scatter([xi], [yi],
            color='red', zorder=5,
            label=f'Intersection ({xi:.2f}, {yi:.2f})')

plt.title("Graphical Solution of Two Linear Equations")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.xlim(-1, 5)
plt.ylim(-2, 7)
plt.show()
