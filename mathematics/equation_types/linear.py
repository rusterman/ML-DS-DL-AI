""" Linear Equations """

"""  
    1. Simple Equation: ax + b = 0  
"""
# Solve 3x + 6 = 18
a, b, c = 3, 6, 18

# ax + b = c  ⇒  x = (c - b) / a
x = (c - b) / a
print(f"x = {x}")  # x = 4.0


""" 
    2. Symbolic Solution with Sympy(sympy stands for symbolic mathematics)
    Use sympy to solve equations symbolically—handy when you don’t want to rearrange by hand. 
"""
from sympy import symbols, Eq, solve

# Define symbol
x = symbols('x')

# Define equation: 5x - 7 = 2x + 8
equation = Eq(5 * x - 7, 2 * x + 8)

# Solve
solutions = solve(equation, x)
print(solutions)  # [5]


""" 
    3. Solving a System of Linear Equations with NumPy
    For multiple variables, write in matrix form Ax=b and use numpy.linalg.solve.
"""
import numpy as np

# System:
# 2x + 3y =  8
# x -  y =  2

A = np.array([
    [2, 3],
    [1, -1]
])
b = np.array([8, 2])

x, y = np.linalg.solve(A, b)
print(f"x = {x}, y = {y}")  # x = 3.0, y = 0.666...
