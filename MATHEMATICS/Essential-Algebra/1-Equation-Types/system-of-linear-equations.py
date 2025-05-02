""" Systems of Linear Equations Examples """

"""
    1. Simple 2×2 Solve via Cramer’s Rule
       Solve:
           a11*x + a12*y = b1
           a21*x + a22*y = b2
       using Cramer’s rule.
"""


def solve_2x2(a11, a12, a21, a22, b1, b2):
    det = a11 * a22 - a12 * a21
    if det == 0:
        raise ValueError("Singular system or infinite solutions")
    x = (b1 * a22 - a12 * b2) / det
    y = (a11 * b2 - b1 * a21) / det
    return x, y


# Example: 2x +  y = 5, 3x − 2y = 4
sol = solve_2x2(2, 1, 3, -2, 5, 4)
print("1) Solution of 2×2 system is x, y =", sol)

"""
    2. General n×n with NumPy
       Solve A·v = b for any square matrix A.
"""
import numpy as np

A = np.array([
    [1, 2, -1],
    [2, -1, 1],
    [3, 0, -2]], dtype=float)
b = np.array([2, 1, -1], dtype=float)

v = np.linalg.solve(A, b)
print("2) NumPy solution of 3×3 system v =", v)
# Verify: A @ v ≈ b
print("   Check A·v =", A.dot(v))

"""
    3. Symbolic Solve with Sympy
       Solve a parameterized 2×2 system symbolically.
"""
import sympy as sp

x, y, a, b, c, d, e, f = sp.symbols('x y a b c d e f')
# Equations: a x + b y = e,  c x + d y = f
eqs = [
    sp.Eq(a * x + b * y, e),
    sp.Eq(c * x + d * y, f),
]
sol_sym = sp.solve(eqs, (x, y))
print("3) Symbolic solution:", sol_sym)
# For example, plug in a=1, b=2, c=3, d=4, e=5, f=6:
print("   Example with numbers:", sol_sym.subs({a: 1, b: 2, c: 3, d: 4, e: 5, f: 6}))

"""
    4. Graphing Two Equations with Matplotlib
       Plot the lines and their intersection:
           L1: x + 2y = 4
           L2: 3x −  y = 1
"""
import matplotlib.pyplot as plt

# Define lines: solve each for y = m x + b
# L1: y = (4 − x) / 2
# L2: y = 3x − 1
x_vals = np.linspace(-1, 5, 200)
y1 = (4 - x_vals) / 2
y2 = 3 * x_vals - 1

# Compute intersection using our solve_2x2
xi, yi = solve_2x2(1, 2, 3, -1, 4, 1)

plt.figure(figsize=(6, 6))
plt.plot(x_vals, y1, label='L1: x + 2y = 4')
plt.plot(x_vals, y2, label='L2: 3x − y = 1')
plt.scatter([xi], [yi], color='red', zorder=5, label=f'Intersection ({xi:.2f}, {yi:.2f})')

plt.title("Graphical Solution of Two Linear Equations")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.xlim(-1, 5)
plt.ylim(-2, 7)
plt.show()
