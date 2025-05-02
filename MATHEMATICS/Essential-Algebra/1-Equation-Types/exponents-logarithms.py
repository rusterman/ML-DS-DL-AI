""" Exponent & Logarithm Examples """

"""
    1. Simple Loop
       Compute and print a^x for integer x in [start, end].
"""


def compute_powers(a, start, end):
    result = []
    for x in range(start, end + 1):
        result.append((x, a ** x))
    return result


# Example: 2^x for x from -3 to 5
print("1) 2^x for x in [-3,5]:", compute_powers(2, -3, 5))

"""
    2. Using a List Comprehension
       For base b and inputs in a list, compute log_b(x) where x > 0.
"""
import math

b = 3
inputs = [0.5, 1, 3, 9, 27]
logs = [(x, math.log(x, b)) for x in inputs if x > 0]
print(f"2) log base {b} of inputs:", logs)

"""
    3. Symbolic Verification with Sympy
       a) Verify exponent law: a^b * a^c == a^(b + c)
       b) Verify log law: log(x*y) == log(x) + log(y)
"""
import sympy as sp

a, b, c, x, y = sp.symbols('a b c x y', positive=True)

# a) exponent law
expr_exp = a ** b * a ** c - a ** (b + c)
print("3a) simplify(a^b * a^c - a^(b+c)) =", sp.simplify(expr_exp))

# b) logarithm law
expr_log = sp.log(x * y, a) - (sp.log(x, a) + sp.log(y, a))
print("3b) simplify(log_a(x*y) - (log_a(x)+log_a(y))) =", sp.simplify(expr_log))

"""
    4. Graphing with Matplotlib
       Plot y = a^x and y = log_a(x), show vertical asymptote x=0 for log.
"""
import numpy as np
import matplotlib.pyplot as plt

a = 2

# Exponential: x in [-5, 5]
x_exp = np.linspace(-5, 5, 500)
y_exp = a ** x_exp

# Logarithm: x in [0.1, 10]
x_log = np.linspace(0.1, 10, 500)
y_log = np.log(x_log) / np.log(a)

plt.figure(figsize=(6, 6))
plt.plot(x_exp, y_exp, label=f'y = {a}^x')
plt.plot(x_log, y_log, label=f'y = log_{a}(x)')
plt.axvline(0, linestyle=':', label='Vertical asymptote: x = 0 for log')

plt.title(f"Exponential and Logarithm Functions (base {a})")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(alpha=0.3)
plt.xlim(-5, 10)
plt.ylim(-5, max(y_exp.max(), y_log.max()) + 1)
plt.show()
