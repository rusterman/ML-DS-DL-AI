"""
linear_system_exercises.py

Exercises for solving systems of linear equations in Python.
"""

# 1. Cramer's Rule for 2×2
"""
Exercise 1: Cramer's Rule for 2×2
Write a function `solve_2x2(a11, a12, a21, a22, b1, b2)` that:
- Computes determinant `det = a11*a22 - a12*a21`.
- Raises `ValueError` if `det == 0`.
- Calculates `x = (b1*a22 - a12*b2)/det` and `y = (a11*b2 - b1*a21)/det`.
- Returns the tuple `(x, y)`.

Test your function with the system:
    2x + y = 5
    3x − 2y = 4
and print the solution.
"""

# 2. NumPy Solve for n×n
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

# 3. Symbolic Solve with Sympy
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

# 4. Graphical Intersection with Matplotlib
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
