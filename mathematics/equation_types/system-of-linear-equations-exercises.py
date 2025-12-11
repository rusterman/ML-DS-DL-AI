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

Example:
    A = [[1, 2, -1], [2, -1, 1], [3, 0, -2]]
    b = [2, 1, -1]
"""

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
