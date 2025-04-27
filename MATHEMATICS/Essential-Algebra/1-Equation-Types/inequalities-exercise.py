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


"""
    2. Symbolic Solution with Sympy
       Solve the quadratic inequality x² – 4x + 3 ≤ 0 symbolically.

    Exercise:
    Use sympy’s `solve_univariate_inequality` to find the solution set of
        x**2 - 4*x + 3 <= 0
    and print it.
"""
# Your Solution...


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


"""
    5. Using a List Comprehension
       Filter values in [-5,5] satisfying |x| < 3

    Exercise:
    Write a single list comprehension that produces all integers x between -5 and 5
    for which abs(x) < 3, then print the resulting list.
"""
# Your Solution...
