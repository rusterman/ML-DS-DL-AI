"""
    1. Simple Equation: ax + b = 0

    Exercise:
    Solve the equation 4x - 8 = 12. Write code to compute x and print the result.
"""
# Your Solution...
# 4*x - 8 = 12
a, b, c = 4, -8, 12

# ax + b = c  =>  x = (c - b) / a
x = (c - b) / a
print("x = ", x)  # x = 5.0


"""
    2. Symbolic Solution with Sympy
       Use sympy to solve equations symbolically—handy when you don’t want to rearrange by hand.
    
    Exercise:
    Symbolically solve the equation 7x + 5 = 3x + 13. Use sympy and print the solution.
"""
# Your Solution...
from sympy import Eq, solve, symbols

# 7*x + 5 = 3*x + 13
x = symbols('x')
equotion = Eq(7*x + 5, 3*x + 13)
print(solution := solve(equotion, x))  # [2]


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
import numpy as np

# 3x + 2y = 11
# 2x -  y =  1

A_matris = np.array([[3, 2],
             		 [2, -1]])
      
b_vector = np.array([11, 1])

x, y = np.linalg.solve(A_matris, b_vector)
x, y = round(x, 2), round(y, 2)
print(f"x = {x}, y = {y}")   # x = 1.86, y = 2.71
