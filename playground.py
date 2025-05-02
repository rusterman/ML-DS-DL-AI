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
        if (2 * x - 1) != 0:
            result.append((x ** 2 - 3 * x) / (2 * x - 1))

    return result


print(filter_rational(-5, 5))

# 2. Using a List Comprehension
"""
Exercise 2: Using a List Comprehension
Using a single list comprehension, build a list of tuples (x, f(x)) where:
- x takes half-integer values in [0, 3] (i.e., 0, 0.5, 1.0, ..., 3.0).
- f(x) = (x**2 - 3*x) / (2*x - 1).
- Excludes the point x = 0.5 (where denominator is zero).

Print your resulting list.
"""
xs = [i / 2 for i in range(0, 7)]
values = [
    (x, (x ** 2 - 3 * x) / (2 * x - 1))
    for x in xs
    if 2 * x - 1 != 0
]

print(xs)
print(values)

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
f = (x ** 2 - 3 * x) / (2 * x - 1)

zeros = sp.solve(sp.simplify(sp.factor(f.as_numer_denom()[0])), x)
asymptote_vert = sp.solve(sp.factor(f.as_numer_denom()[1]), x)
quo, rem = sp.div((x ** 2 - 3 * x), (2 * x - 1))
asymptote_line = quo

print("3a) zeros of f(x):", zeros)  # x=0 or x=3
print("3b) vertical asymptotes at x =", asymptote_vert)  # x=1/2
print("3c) asymptote y =", asymptote_line)  # y = x/2 - 5/4

# 4. Graphing with Matplotlib
"""
Exercise 4: Graphing with Matplotlib
Write code that:
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

# 1) Sample x values in the range [-5, 5]
x_vals = np.linspace(-5, 5, 1000)

# 2) Exclude a small neighborhood around the vertical asymptote at x = 0.5
mask = np.abs(x_vals - 0.5) > 0.02
x_plot = x_vals[mask]

# 3) Compute f(x) = (x^2 - 3x) / (2x - 1)
y_plot = (x_plot**2 - 3*x_plot) / (2*x_plot - 1)

# 4) Define the oblique asymptote y = x/2 - 5/4
asymp_obl = x_plot / 2 - 5/4

# 5) Plot the function and its asymptotes
plt.figure(figsize=(8, 8))
plt.plot(x_plot, y_plot, label='f(x) = (x² - 3x)/(2x - 1)')
plt.plot(x_plot, asymp_obl, linestyle='--', label='Oblique asymptote: y = x/2 - 5/4')
plt.axvline(0.5, linestyle=':', label='Vertical asymptote: x = 0.5')

# 6) Add title, labels, legend, and grid
plt.title("Graph of (x² - 3x)/(2x - 1) with Asymptotes")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)

# 7) Display the plot
plt.show()

