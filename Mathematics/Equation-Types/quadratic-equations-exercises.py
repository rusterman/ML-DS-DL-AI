"""
    Quadratic Equations: Exercises
"""

"""
    1. Quadratic Formula
    Exercise:
    Solve the equation x² - 5x + 6 = 0. Compute the discriminant and both roots, then print the results.
"""
# Your Solution...
from math import sqrt
a,b,c=1,-5,6
D=b**2-4*a*c
if D<0:
    print("No real roots")
root1=(-b+sqrt(D))/(2*a)
root2=(-b-sqrt(D))/(2*a)
print(f"Discriminant: {D}")
print(f"root 1: {root1}\nroot 2: {root2}")



"""
    2. Nature of Roots
    Exercise:
    Determine the nature of roots for x² + 4x + 5 = 0. 
    Print a message indicating whether the roots are real and distinct, real and equal, or complex.
"""
# Your Solution...
a,b,c=1,-5,6
D=b**2-4*a*c
if D<0:
    print("No real roots")
elif D==0:
    print("Real and Unique root")
else:
    print("Real and distinct roots")

