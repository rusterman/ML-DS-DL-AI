"""
Polynomial Equations: Exercises

This file contains practice exercises for evaluating, solving, and analyzing polynomial equations.
"""

import cmath
import numpy as np

"""
    1. Evaluate Polynomial
    Exercise:
    Use the evaluate_polynomial function to compute the value of 3x^3 - 2x^2 + x - 5 at x = 2.
    Print the result.
"""
# Your Solution...
def evaluate_polynomial(coeffs, x):
    result = 0
    degree = len(coeffs)

    for coef in coeffs:
        result += coef * (x ** (degree := degree - 1))

    return result


'''
    1.2 Evaluate Polynomial in the additional variation
'''
# Additional Solution...
def addition_polynomial(coeffs, x):
    result = 0
    degree = len(coeffs)

    for coef in range(degree):
        result += coeffs[coef] * (x ** (degree - coef - 1))

    return result


""" 
    1.3. Evaluate Polynomial via Horner's method (additional solution) 
    coeffs: list of coefficients [a_0, ..., a_n]
    Horner's recurrence: r_n+1 = r_n * x + a_n   ->   r_n+1 = r_n * x + coeffs[n]
    Polynomial: 3x^3 - 2x^2 + x - 5
                P(x) = 3x^3 - 2x^2 + x - 5
                a = [3, -2, 1, -5]
                
                r0 = 0
                r1 = r0 * x + 3
                r2 = r1 * x - 2
                ...
                r_n+1 = r_n * x + a_n       
"""
# Additional Solution...
def polynomial_horner(coeffs, x):
    result = 0

    for coef in coeffs:
        result = result * x + coef

    return result


"""
    2. Linear Equation
    Exercise:
    Solve the linear equation 5x + 7 = 0 using the solve_linear function.
    Print the solution.
"""
# Your Solution...
def solve_linear(a, b):
    if a == 0:
        raise ValueError("Coefficient a cannot be zero.")

    x = - b / a
    return [x]



"""
    3. Quadratic Formula
    Exercise:
    Solve the equation x^2 - 5x + 6 = 0. Compute the discriminant and both roots using the solve_quadratic function.
    Print the discriminant and roots.
"""
# Your Solution...
def solve_quadratic(a, b, c):
    """Solve ax^2 + bx + c = 0"""
    if a == 0:
        return solve_linear(b, c)

    D = b ** 2 - 4 * a * c
    sqrt_D = cmath.sqrt(D)

    root1 = (-b + sqrt_D) / (2 * a)
    root2 = (-b - sqrt_D) / (2 * a)

    return [root1, root2]


"""
    4. Nature of Roots
    Exercise:
    Determine the nature of roots for x^2 + 4x + 5 = 0 using solve_quadratic and discriminant logic.
    Print a message indicating whether the roots are real and distinct, real and equal, or complex.
"""
# Your Solution...
def nature_quadratic(a, b, c):
    """Solve ax^2 + bx + c = 0"""
    if a == 0:
        return solve_linear(b, c)

    D = b ** 2 - 4 * a * c

    if D > 0:
        nature = "Real and distinct"
    elif D == 0:
        nature = "Real and equal"
    else:
        nature = "Complex"

    return nature


"""
    5. Cubic Roots
    Exercise:
    Solve the cubic equation x^3 - 6x^2 + 11x - 6 = 0 using the solve_polynomial function.
    Print the roots.
"""
# Your Solution...
'''
    1.3. Solve Polynomial
    
    x^3 - 6x^2 + 11x - 6 = 0
    x^3 - 6x^2 + 9x + 2x - 6 = 0
    x(x - 3)^2 + 2(x - 3) = 0
    (x - 3)(x(x - 3) + 2) = 0
   
    1) x - 3 = 0
       x = 3
      
    2) x(x - 3) + 2 = 0
       x^2 - 3x + 2 = 0
     (ax^2 + bx + c = 0)
    
     D = b^2 - 4ac = 9 - 4 * 1 *2 = 1 > 0
     D > 0
    
     x1,2 = (-b ± √D) / 2a
     x1 = (-b + √D) / 2a = (3 + 1) / 2 = 2
     x2 = (-b - √D) / 2a = (3 - 1) / 2 = 1
    
     Roots: 3, 2, 1
'''
def solve_polynomial(cuffs):
    """Solve general polynomial for roots using numpy if available."""
    if np is None:
        raise ImportError("NumPy is required for solving general polynomials")
    return np.roots(cuffs)


"""
    6. Derivative Polynomial
    Exercise:
    Compute the derivative coefficients of the polynomial 2x^3 - 3x + 5 using the derivative_polynomial function.
    Print the list of derivative coefficients.
"""
# Your Solution...
def derivative_polynomial(cuffs):
    # 1st ver. - inspired by @rusterman
    degree = len(cuffs)

    derivatives = [cuff * (degree - i) for i, cuff in enumerate(cuffs[:-1], start=1)]

    # 2nd ver. - traditional way
    '''
    degree = len(cuffs)
    derivatives = []

    for i, cuff in enumerate(cuffs[:-1], start=1):
        derivatives.append(cuff * (degree - i))
    '''

    return derivatives




def main():
    # Example 1: Evaluate polynomial 3x^3 - 2x^2 + x - 5 at x = 2
    poly_equation = evaluate_polynomial([3, -2, 1, -5], 2)
    print("Evaluate Polynomial: value of 3x^3 - 2x^2 + x - 5: ", poly_equation)

    # Example 1.2: Evaluate Polynomial 3x^3 - 2x^2 + x - 5 at x = 2 in the additional variation
    poly_additio = evaluate_polynomial([3, -2, 1, -5], 2)
    print("Additional variation: value of 3x^3 - 2x^2 + x - 5: ", poly_additio)

    # Example 1.3: Evaluate Polynomial via Horner's method 3x^3 - 2x^2 + x - 5 at x = 2
    poly_horner = polynomial_horner([3, -2, 1, -5], 2)
    print("Evaluate via Horner's method: value of 3x^3 - 2x^2 + x - 5: ", poly_horner)

    # Example 2: Linear equation 5x + 7 = 0
    lin_equation = solve_linear(5, 7)
    print("Linear equation 5x + 7 = 0; roots: ", lin_equation)

    # Example 3: Quadratic equation x^2 - 5x + 6 = 0
    quad_equation = solve_quadratic(1, -5, 6)
    print("Quadratic equation x^2 - 5x + 6 = 0; roots: ", quad_equation)

    # Example 4: Nature of roots for x^2 + 4x + 5 = 0
    nature = nature_quadratic(2, 4, 5)
    print("Nature of Roots of quadratic equation x^2 + 4x + 5 = 0; nature:", nature)

    # Example 5: Cubic equation x^3 - 6x^2 + 11x - 6 = 0
    if np:
        cubic_roots = solve_polynomial([1, -6, 11, -6])
        print("Cubic equation x^3 - 6x^2 + 11x - 6 = 0; roots:", cubic_roots)
    else:
        print("NumPy not available; skipping cubic example.")

    # Example 6: Derivative of 2x^3 - 3x + 5
    deriv = derivative_polynomial([2, 0, -3, 5])
    print("Derivative coefficients of 2x^3 - 3x + 5:", deriv)


if __name__ == "__main__":
    main()