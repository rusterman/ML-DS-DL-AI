"""
    1. Simple Equation: ax + b = 0

    Exercise:
    Solve the equation 4x - 8 = 12. Write code to compute x and print the result.
"""
# Your Solution...
print("1.Simple Equation: ax + b = 0")
a, b, c = 4, -8, 12
x = (c - b) / a
print(f"x = {x}")
print()

"""
    2. Symbolic Solution with Sympy
       Use sympy to solve equations symbolically—handy when you don’t want to rearrange by hand.
    
    Exercise:
    Symbolically solve the equation 7x + 5 = 3x + 13. Use sympy and print the solution.
"""
# Your Solution...
print("2. Symbolic Solution with Sympy: 7x + 5 = 3x + 13")
from sympy import Eq, solve, symbols

x = symbols("x")

equation = Eq(7 * x +  5, 3 * x + 13)

solutions = solve(equation, x)
print(solutions)
print()

"""
    3. Solving a System of Linear Equations with NumPy
       For multiple variables, write in matrix form Ax=b and use numpy.linalg.solve.
    
    Exercise:
       Solve the system:
           3x + 2y = 11
           2x -  y =  1
       Use numpy.linalg.solve and print x and y.
"""
# Your Solution... 
print("3. Solving a System of Linear Equations with NumPy: 3x + 2y = 11, 2x -  y =  1")
import numpy as np

A = np.array([
    [3, 2],
    [2, -1]
    ])
b = np.array([11, 1])

x, y = np.linalg.solve(A, b)
print(f"x = {x}, y = {y}")