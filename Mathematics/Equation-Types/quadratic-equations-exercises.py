"""
    Quadratic Equations: Exercises
"""

"""
    1. Quadratic Formula
    Exercise:
    Solve the equation x² - 5x + 6 = 0. Compute the discriminant and both roots, then print the results.
"""
# Your Solution...


"""
    2. Nature of Roots
    Exercise:
    Determine the nature of roots for x² + 4x + 5 = 0. 
    Print a message indicating whether the roots are real and distinct, real and equal, or complex.
"""
a = float(input())
b = float(input())
c = float(input())
D = b*b - 4*a*c
if(D > 0):
    print("The equation has two distinct real roots.")
    x1 = (-b + D**(0.5))/(2*a)
    x2 = (-b - D**(0.5))/(2*a)
    print(f"First root: {x1}")
    print(f"Second root: {x2}")
 
elif(D == 0):
    print("The equation has two equal real root.")
    x1 = (-b + D**(0.5))/(2*a)
    x2 = (-b - D**(0.5))/(2*a)
    print(f"First root: {x1}")
    print(f"Second root: {x2}") 
else:
    print("The roots of the equation are imaginary.")


