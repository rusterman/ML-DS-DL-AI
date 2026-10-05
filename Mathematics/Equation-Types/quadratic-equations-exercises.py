"""
    Quadratic Equations: Exercises
"""

"""
    1. Quadratic Formula
    Exercise:
    Solve the equation x² - 5x + 6 = 0. Compute the discriminant and both roots, then print the results.
"""
# Your Solution...
print("Question 1")
a, b, c = 1, -5, 6
D = b ** 2 - 4 * a * c
root1 = (-b + D ** 1/2) / (2 * a)
root2 = (-b - D ** 1/2) / (2 * a)
print (f"roots:  {root1}, {root2}") 
print()

"""
    2. Nature of Roots
    Exercise:
    Determine the nature of roots for x² + 4x + 5 = 0. 
    Print a message indicating whether the roots are real and distinct, real and equal, or complex.
"""
# Your Solution...
print("Question 2")
a, b, c = 1, 4, 5
D = b ** 2 - 4 * c * a
if (D > 0):
    print("Real")
elif (D == 0):
    print ("Equal")
else:
    print ("Complex")
