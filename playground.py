"""
    Quadratic Equations: Exercises
"""

"""
    1. Quadratic Formula
    Exercise:
    Solve the equation x² - 5x + 6 = 0. Compute the discriminant and both roots, then print the results.
"""
# Your Solution...
a, b, c = 1, -5, 6
D = b**2 - 4*a*c
root1 = (-b + D**0.5)/(2*a)
root2 = (-b - D**0.5)/(2*a)
print(f"root1: {root1}, root2: {root2}")

"""
    2. Nature of Roots
    Exercise:
    Determine the nature of roots for x² + 4x + 5 = 0. 
    Print a message indicating whether the roots are real and distinct, real and equal, or complex.
"""
# Your Solution...
a, b, c = 1, 4, 5
D = b**2 - 4*a*c

if D > 0:
    print("Real and distinct")
elif D == 0:
    print("Real and equal")
else:
    print("Complex")

"""
    3. Vertex Form Conversion
    Exercise:
    Convert 2x² - 8x + 6 into vertex form a(x - h)² + k. Compute and print the vertex coordinates (h, k).
"""
# Your Solution...
