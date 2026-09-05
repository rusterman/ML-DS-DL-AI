# inequalities_exercises.py

""" Inequality Exercises """

"""
    1. Simple Inequality with a Loop
       Find all integer x in [a, b] such that 2x – 5 > 3.

    Exercise:
    Write a function `filter_simple(a, b)` that returns a list of all x in the inclusive range [a, b]
    satisfying 2*x - 5 > 3, then print the result for a = -5, b = 10.
"""
# Your Solution...
def filter_simple(a, b):
    result=[]
    for i in range(a,b+1):
        if 2*i-5>3:
            result.append(i)
    return result
print(filter_simple(-5,10))

"""
    2. Symbolic Solution with Sympy
       Solve the quadratic inequality x² – 4x + 3 ≤ 0 symbolically.

    Exercise:
    Use sympy’s `solve_univariate_inequality` to find the solution set of
        x**2 - 4*x + 3 <= 0
    and print it.
"""
# Your Solution...
import sympy as sp
x=sp.symbols('x')
solution=sp.solve_univariate_inequality(x**2-4*x+3<=0,x)
print(solution)

"""
    3. System of Linear Inequalities with Sympy
       Find the overlap region for:
           x + 2y ≤ 6
           2x -  y ≥ 1

    Exercise:
    Use sympy’s `reduce_inequalities` (or equivalent) to solve the system
        [x + 2*y <= 6,  2*x - y >= 1]
    and display the solution conditions.
"""
# Your Solution...
y=sp.symbols('y')
solution2=sp.reduce_inequalities([x<=6-2*y ,  x<=(1+y)/2],x)
print(solution2)

"""
    4. Graphing a Feasible Region with Matplotlib
       Plot the region defined by:
           y ≥ x - 1
           y ≤ -2*x + 4

    Exercise:
    Create a grid over x,y in [-1, 5] and use numpy + matplotlib to shade the intersection
    of the two half-planes. Draw the boundary lines and show the feasible region.
"""
# Your Solution...
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(-1,5,200)
y=np.linspace(-1,5,200)
X,Y=np.meshgrid(x,y)
region1=(Y>=x-1)
region2=(Y<=-2*x+4)
feasible=region1&region2
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(-1, 5)
plt.ylim(-1, 5)
plt.plot(x,x-1,'pink',label="y=x-1")
plt.plot(x,-2*x+4,'purple',label="y=-2*x+4")
plt.contourf(X,Y,feasible,alpha=0.5)
plt.grid()
plt.legend()
plt.title("Feasible region")
plt.show()
"""
    5. Using a List Comprehension
       Filter values in [-5,5] satisfying |x| < 3

    Exercise:
    Write a single list comprehension that produces all integers x between -5 and 5
    for which abs(x) < 3, then print the resulting list.
"""
# Your Solution...
result=[x for x in range(-5,6) if abs(x)<3]
print(result)