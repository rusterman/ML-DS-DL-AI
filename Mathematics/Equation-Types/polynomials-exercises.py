"""
Polynomial Equations: Exercises

This file contains practice exercises for evaluating, solving, and analyzing polynomial equations.
"""

"""
    1. Evaluate Polynomial
    Exercise:
    Use the evaluate_polynomial function to compute the value of 3x^3 - 2x^2 + x - 5 at x = 2.
    Print the result.
"""
# Your Solution...
# x=2
# def polynomial(x0):
#     return 3*x0**3-2*x0**2+x0-5
# print(polynomial(x))

# def evaluate_polynomial(coeff, x):
#     result=0
#     index=0
#     degree=len(coeff)-1
#     while(degree>=0):
#         result+=coeff[index]*x**degree
#         degree-=1
#         index+=1
#     return result
# coeff=[3,-2,1,-5]
# x=2
# print(evaluate_polynomial(coeff,x))  

# def evaluate_polynomial(coeff, x):
#     degree=len(coeff)-1
#     result=0
#     for i, coef in enumerate(coeff):
#         result+=coef*x**(degree-i)
#     return result
# print(evaluate_polynomial(coeff,x))

"""
    2. Linear Equation
    Exercise:
    Solve the linear equation 5x + 7 = 0 using the solve_linear function.
    Print the solution.
"""
# Your Solution...
# def solve_linear(a,b):
#     if a==0:
#         raise ValueError("The value of coeff cannot be zero for linear equation")
#     return (-b/a)
# print(solve_linear(5,7))

"""
    3. Quadratic Formula
    Exercise:
    Solve the equation x^2 - 5x + 6 = 0. Compute the discriminant and both roots using the solve_quadratic function.
    Print the discriminant and roots.
"""
# Your Solution...
# from math import sqrt
# def solve_quadratic(a,b,c):
#     if a==0:
#         return solve_linear(b,c)
#     D=b**2-4*a*c
#     if D<0:
#         print("No real roots")
#         return D, None, None
#     root1=(-b+sqrt(D))/(2*a)
#     root2=(-b-sqrt(D))/(2*a)
#     return D,root1,root2
# quad_solutions=solve_quadratic(1,-5,6)
# print(f"Discriminant: {quad_solutions[0]}")
# print(quad_solutions[1],quad_solutions[2])

"""
    4. Nature of Roots
    Exercise:
    Determine the nature of roots for x^2 + 4x + 5 = 0 using solve_quadratic and discriminant logic.
    Print a message indicating whether the roots are real and distinct, real and equal, or complex.
"""
# Your Solution...
# quad_solutions2=solve_quadratic(1,4,5)
# if quad_solutions2[0]<0:
#     print("Complex roots")
# elif quad_solutions2[0]==0:
#     print("Real and unique")
# else:
#     print("Real and distinct")

"""
    5. Cubic Roots
    Exercise:
    Solve the cubic equation x^3 - 6x^2 + 11x - 6 = 0 using the solve_polynomial function.
    Print the roots.
"""
# Your Solution...
# import numpy as np
# def solve_polynomial(coeff):
#     return np.roots(coeff)
# print(solve_polynomial([1,-6,11,-6]))

"""
    6. Derivative Polynomial
    Exercise:
    Compute the derivative coefficients of the polynomial 2x^3 - 3x + 5 using the derivative_polynomial function.
    Print the list of derivative coefficients.
"""
# Your Solution...

def derivative_polynomial(coeff):
    degree=len(coeff)-1
    derivative=[]
    for i,coef in enumerate(coeff):
        if degree-i>0:
            derivative.append(coef*(degree-i))
    return derivative
coeff=[2,0,-3,5]
print(derivative_polynomial(coeff))