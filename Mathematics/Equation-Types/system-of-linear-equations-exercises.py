"""
linear_system_exercises.py

Exercises for solving systems of linear equations in Python.
"""

# 1. NumPy Solve for n×n
"""
Exercise 2: NumPy Solve for n×n
Using NumPy, solve `A · v = b` for a given square matrix `A` and vector `b`:
- Define `A` and `b` as NumPy arrays.
- Use `np.linalg.solve(A, b)` to compute `v`.
- Verify your solution by printing `A @ v`.

"""
import numpy as np
A =np.array( [[1, 2, -1], [2, -1, 1], [3, 0, -2]])
b = np.array([2, 1, -1])
v=np.linalg.solve(A,b)
print(v)
print(f"verifying {A.dot(v)}")


# 2. Symbolic Solve with Sympy
"""
Exercise 3: Symbolic Solve with Sympy
Using Sympy, symbolically solve the system:
    a*x + b*y = e
    c*x + d*y = f
- Define symbols `x, y, a, b, c, d, e, f`.
- Construct the equations with `sp.Eq(...)`.
- Use `sp.solve` to find `(x, y)` in terms of the symbols.
- Then substitute `a=1, b=2, c=3, d=4, e=5, f=6` and print the numeric solution.
"""
import sympy as sp
x,y,a,b,c,d,e,f=sp.symbols('x y a b c d e f')
eqs=[sp.Eq(a*x+b*y,e),
     sp.Eq(c*x+d*y,f)]
solution=sp.solve(eqs,(x,y))
print(solution)
print(f"substitution for x {solution[x].subs({a:1,b:2,c:3,d:4,e:5,f:6})}")
print(f"substitution for y {solution[y].subs({a:1,b:2,c:3,d:4,e:5,f:6})}")

# 3. Graphical Intersection with Matplotlib
"""
Exercise 4: Graphical Intersection with Matplotlib
Plot two lines and mark their intersection:
    L1: x + 2y = 4
    L2: 3x − y = 1
Write code that:
- Converts each equation into `y = m*x + c` form.
- Samples `x` over a suitable range.
- Plots both lines with labels.
- Computes their intersection using your `solve_2x2` function.
- Marks the intersection point on the plot.
- Adds title, axis labels, legend, and grid.
Ensure the intersection is clearly highlighted.
"""
import matplotlib.pyplot as plt
import sympy as sp
x,y=sp.symbols('x y')
x_vals=np.linspace(-5,5,200)
y1=sp.Eq(x+2*y,4)
y2=sp.Eq(3*x-y,1)
sol=sp.solve((y1,y2),(x,y))
print(sol)
plt.plot(x_vals,(4-x_vals)/2,"pink",label="L1: x+2y=4")
plt.plot(x_vals,3*x_vals-1,"blue",label="L2: 3x-y=1")
plt.title("Intersection of Two Lines")
plt.scatter(sol[x],sol[y],color="magenta",label="Intersection point")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()