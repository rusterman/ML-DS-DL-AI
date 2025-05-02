""" Rational Function Examples """

"""
    1. Simple Filtering with a Loop
       Find all integer x in [a, b] for which f(x) = (x^2 - 3x) / (2x - 1) is positive.
       (Skip x where the denominator is zero.)
"""

def filter_rational(a, b):
    result = []
    for x in range(a, b + 1):
        if 2 * x - 1 == 0:
            # skip the vertical asymptote at x = 1/2
            continue
        value = (x**2 - 3*x) / (2*x - 1)
        if value > 0:
            result.append((x, value))
    return result

# Example: from -5 to 5
print("1) (x^2 - 3x)/(2x - 1) > 0 for x in [-5,5]:", filter_rational(-5, 5))


"""
    2. Using a List Comprehension
       Compute f(x) at half‐integer steps in [0, 3], excluding the asymptote.
"""
xs = [i/2 for i in range(0, 7)]  # 0, 0.5, 1.0, ..., 3.0
values = [
    (x, (x**2 - 3*x)/(2*x - 1))
    for x in xs
    if 2*x - 1 != 0  # exclude x = 0.5
]
print("2) Values of f(x) on [0,3] \\{0.5\\}:", values)


"""
    3. Symbolic Analysis with Sympy
       a) Find the roots of the numerator (zeros of f).
       b) Find vertical asymptotes (denominator zeros).
       c) Compute the horizontal/oblique asymptote via polynomial division.
"""
import sympy as sp

x = sp.symbols('x')
f = (x**2 - 3*x) / (2*x - 1)

# a) zeros of f where numerator = 0 (but denom ≠ 0)
zeros = sp.solve(sp.simplify(sp.factor(f.as_numer_denom()[0])), x)
# b) vertical asymptotes where denominator = 0
asymptotes_vert = sp.solve(sp.factor(f.as_numer_denom()[1]), x)
# c) oblique/horizontal asymptote: do polynomial division
quo, rem = sp.div(x**2 - 3*x, 2*x - 1)
asymptote_line = quo  # y = quo + rem/(2x - 1) → asymptote y = quo

print("3a) zeros of f(x):", zeros)               # x=0 or x=3
print("3b) vertical asymptotes at x =", asymptotes_vert)  # x=1/2
print("3c) asymptote y =", asymptote_line)       # y = x/2 - 5/4


"""
    4. Graphing the Function and Its Asymptotes with Matplotlib
       Plot f(x) on [-5, 5], show vertical line at x=0.5 and the oblique asymptote.
"""
import numpy as np
import matplotlib.pyplot as plt

# 1) Sample x-values, avoiding the asymptote
x_vals = np.linspace(-5, 5, 1000)
x_vals = x_vals[np.abs(x_vals - 0.5) > 0.02]  # drop points near x=0.5

# 2) Compute f(x)
y_vals = (x_vals**2 - 3*x_vals) / (2*x_vals - 1)

# 3) Define asymptote lines
asymp_vert_x = 0.5 * np.ones_like(x_vals)
asymp_obl_y = (x_vals/2) - 5/4  # from polynomial division

# 4) Plot
plt.figure(figsize=(6,6))
plt.plot(x_vals, y_vals, label='f(x) = (x² - 3x)/(2x - 1)')
plt.plot(x_vals, asymp_obl_y, '--', label='Asymptote: y = x/2 - 5/4')
plt.axvline(0.5, color='grey', linestyle=':', label='Vertical Asymptote x = 0.5')

plt.title("Graph of (x² - 3x)/(2x - 1) with Asymptotes")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.ylim(-10, 10)
plt.xlim(-5, 5)
plt.legend()
plt.grid(alpha=0.3)
plt.show()
