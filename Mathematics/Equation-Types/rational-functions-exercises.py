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
    result=[]
    for x in range(a,b+1):
        if 2*x-1==0:
            continue
        if (x**2 - 3*x) / (2*x - 1)>0:
            result.append((x,(x**2 - 3*x) / (2*x - 1)))
    return result
print(filter_rational(-5,5))
# 2. Using a List Comprehension
"""
Exercise 2: Using a List Comprehension
Using a single list comprehension, build a list of tuples (x, f(x)) where:
- x takes half-integer values in [0, 3] (i.e., 0, 0.5, 1.0, ..., 3.0).
- f(x) = (x**2 - 3*x) / (2*x - 1).
- Excludes the point x = 0.5 (where denominator is zero).

Print your resulting list.
"""
result2=[(x/2, ((x/2)**2 - 3*(x/2)) / (2*(x/2) - 1)) for x in range(0,7) if x!=1]
print(result2)

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
x=sp.symbols('x')
f=(x**2 - 3*x) / (2*x - 1)
numerator=(x**2 - 3*x)
denominator= (2*x - 1)
roots_numerator=sp.solve(numerator,x)
roots_denominator=sp.solve(denominator,x)
quo,rem=sp.div(numerator,denominator)
asymptote=quo
print(f"roots of numerator: {roots_numerator}")
print(f"vertical asymptotes: {roots_denominator}")
print(f"oblique/horizontal asymptote: {asymptote}")

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
import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-5,0.49,100)
x2 = np.linspace(0.51,5,100)
y1=(x1**2-3*x1)/(2*x1-1)
y2=(x2**2-3*x2)/(2*x2-1)
plt.plot(x1,y1,'pink',label="f(x)")
plt.plot(x2,y2,'pink')
x=np.linspace(-5,5,400)
asym=x/2-5/4
plt.plot(x,asym,"b--",label='aysmptote')
plt.axvline(0.5, linestyle=':',color='magenta',label='Vertical asymptote')
plt.title("Graph of f(x)")
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()
