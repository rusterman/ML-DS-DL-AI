""" Sigma Notation (Summation) Examples """

"""
    1. Simple Summation with a Loop
       Compute \sum_{i=1}^{n} i
"""


def simple_summation(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total


# Example
n = 10
print(f"Sum of i from 1 to {n} is {simple_summation(n)}")  # 55


"""
    2. Using built-in sum() with a Generator Expression
       Compute \sum_{i=a}^{b} f(i)
"""


def summation_range(a, b, func=lambda x: x):
    return sum(func(i) for i in range(a, b + 1))


# Example: sum of squares from 1 to 5
print(f"Sum of squares from 1 to 5 is {summation_range(1, 5, lambda x: x ** 2)}")  # 55

"""
    3. Symbolic Summation with Sympy
       Compute symbolic sums: \sum_{i=1}^{n} i
"""
from sympy import symbols, summation

i, n = symbols('i n')
expr = summation(i, (i, 1, n))
print(f"Symbolic sum of i from 1 to n: {expr}")  # n*(n + 1)/2
print(f"For n=10: {expr.subs(n, 10)}")  # 55

"""
    4. Summation using NumPy
       Compute large summations efficiently, e.g., geometric series:
       \sum_{i=0}^{n} r^i
"""
import numpy as np


def geometric_series(n, r):
    exponents = np.arange(0, n + 1)
    return np.sum(r ** exponents)


r = 0.5
n_val = 20
print(f"Sum of geometric series r={r} up to n={n_val} is {geometric_series(n_val, r)}")
