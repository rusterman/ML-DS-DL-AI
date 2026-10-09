"""
rational_function_exercises.py

Exercises for working with rational functions in Python.
"""

# 1. Simple Filtering with a Loop
"""
Exercise 1: Simple Filtering with a Loop
Write a function `filter_rational(a, b)` that:
- Iterates over integer x in the interval [a, b].
- Computes f(x) = (x**2 - 3*x) / (2*x - 1).
- Skips x where 2*x - 1 == 0.
- Returns a list of tuples (x, f(x)) for which f(x) > 0.

Test your function with a range from -5 to 5 and print the result.
"""
def filter_rational(a, b):
    result = []
    for x in range(a, b + 1):
        if 2 * x - 1 == 0:
            continue
        value = (x**2 - 3*x) / (2*x - 1)
        if value > 0:
            result.append((x, value))
    return result

# Example: from -5 to 5
print("1) (x^2 - 3x)/(2x - 1) > 0 for x in [-5,5]:", filter_rational(-5, 5))


# 2. Using a List Comprehension
"""
Exercise 2: Using a List Comprehension
Using a single list comprehension, build a list of tuples (x, f(x)) where:
- x takes half-integer values in [0, 3] (i.e., 0, 0.5, 1.0, ..., 3.0).
- f(x) = (x**2 - 3*x) / (2*x - 1).
- Excludes the point x = 0.5 (where denominator is zero).

Print your resulting list.
"""
'''
In Python, x is a name (or reference).
In the first iteration, x → 0.0; then x → 0.5; then x → 1.0.
x is not a variable created anew in each loop; rather, 
the name x is reused, but in each iteration, 
it is rebound to a new value via x := i / 2
'''
values = [
    (x, (x**2 - 3*x) / (2*x - 1) + 0)
    for i in range(0, 3)
    if (x := i / 2) is not None \
    and 2 * x - 1 != 0
]
print("2) Values of f(x) on [0,3] \\{0.5\\}:", values)


# 3. Symbolic Analysis with Sympy
"""
Exercise 3: Symbolic Analysis with Sympy
Using Sympy, perform the following tasks for f(x) = (x**2 - 3*x) / (2*x - 1):
- Find the roots of the numerator (zeros of f).
- Find the values of x where vertical asymptotes occur (denominator zeros).
- Perform polynomial division to determine the oblique/horizontal asymptote (quotient).
Print each result clearly.
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
'''
N - Numerator
D - Denominator
Q - Quotient
R - Remainder

N(x) / D(x) = Q(x) + R(x) / D(x)   →   polynomial division
(x^2 - 3x) / (2x - 1) = (x/2 - 5/4) + (-5/4 / (2x - 1)) =
                      = x/2 - 5/4 - 5 / (4 * (2x - 1))

N(x) = Q(x) * D(x) + R   →   for checking: sp.div(N, D) = N / D = (Q, R) method also works in this way
(x^2 - 3x) = (x/2 - 5/4) * (2x - 1) + (-5/4)
'''
print("3a) zeros of f(x):", zeros)               # x=0 or x=3
print("3b) vertical asymptotes at x =", asymptotes_vert)  # x=1/2
print("3c) asymptote y =", asymptote_line)       # y = x/2 - 5/4

# 4. Graphing with Matplotlib
"""
Exercise 4: Graphing with Matplotlib
Write code that:
- The equation is f(x) = (x**2 - 3*x) / (2*x - 1)
- Samples x values in the range [-5, 5], avoiding a neighborhood around the vertical asymptote x = 0.5.
- Computes f(x) for each sampled x.
- Plots f(x) as a continuous curve.
- Draws a dashed line for the oblique asymptote y = x/2 - 5/4.
- Draws a vertical dotted line at x = 0.5.
- Adds title, labels, legend, and grid.
Ensure your plot displays the function and its asymptotes clearly.
"""
import numpy as np
import matplotlib.pyplot as plt

# 1) Sample x-values, avoiding the asymptote
x_vals = np.linspace(-5, 5, 1000)
x_vals = x_vals[np.abs(x_vals - 0.5) > 0.02]  # drop points near x=0.5

# 2) Compute f(x)
y_vals = (x_vals**2 - 3*x_vals) / (2*x_vals - 1)

# 3) Define asymptote lines
asymp_vert_x = np.full_like(x_vals, 0.5)
asymp_obl_y = (x_vals / 2) - 5/4  # from polynomial division

# 4) Plot
plt.figure(figsize=(6,6))
plt.plot(x_vals, y_vals, label='f(x) = (x² - 3x)/(2x - 1)')
plt.plot(x_vals, asymp_obl_y, '--', label='Asymptote: y = x/2 - 5/4')
plt.axvline(0.5, color='red', linestyle=':', label='Vertical Asymptote x = 0.5')

plt.title("Graph of (x² - 3x)/(2x - 1) with Asymptotes")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.ylim(-10, 10)
plt.xlim(-5, 5)
plt.legend()
plt.grid(alpha=0.3)
plt.show()
