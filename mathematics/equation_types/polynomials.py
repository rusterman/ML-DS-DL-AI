"""
    Polynomial Equations: Implementation in Python

    This file demonstrates solving and analyzing polynomial equations of various degrees.
"""

import cmath
import numpy as np


def evaluate_polynomial(coeffs, x):
    """Evaluate a polynomial at x.
    coeffs: list of coefficients [a_n, ..., a_0] representing a_n x^n + ... + a_0
    """
    result = 0
    degree = len(coeffs) - 1
    for i, coef in enumerate(coeffs):
        result += coef * (x ** (degree - i))
    return result


def solve_linear(a, b):
    """Solve ax + b = 0"""
    if a == 0:
        raise ValueError("Coefficient a cannot be zero for a linear equation.")
    return [-b / a]


def solve_quadratic(a, b, c):
    """Solve ax^2 + bx + c = 0"""
    if a == 0:
        return solve_linear(b, c)
    D = b**2 - 4*a*c
    sqrt_D = cmath.sqrt(D)
    root1 = (-b + sqrt_D) / (2*a)
    root2 = (-b - sqrt_D) / (2*a)

    return [root1, root2]


def solve_polynomial(cuffs):
    """Solve general polynomial for roots using numpy if available."""
    if np is None:
        raise ImportError("NumPy is required for solving general polynomials")
    return np.roots(cuffs)


def derivative_polynomial(cuffs):
    """Compute derivative coefficients of a polynomial."""
    degree = len(cuffs) - 1
    derivatives = [cuffs[i] * (degree - i) for i in range(degree)]
    return derivatives


def main():
    # Example 1: Linear equation 3x + 2 = 0
    lin_roots = solve_linear(3, 2)
    print("Linear equation 3x + 2 = 0; roots:", lin_roots)

    # Example 2: Quadratic equation 2x^2 - 4x - 6 = 0
    quad_roots = solve_quadratic(2, -4, -6)
    print("Quadratic equation 2x^2 - 4x - 6 = 0; roots:", quad_roots)

    # Example 3: Nature of roots for x^2 + 2x + 1 = 0
    roots = solve_quadratic(1, 2, 1)
    print("Quadratic equation x^2 + 2x + 1 = 0; roots:", roots)

    # Example 4: Cubic equation x^3 - 6x^2 + 11x - 6 = 0
    if np:
        cubic_roots = solve_polynomial([1, -6, 11, -6])
        print("Cubic equation x^3 - 6x^2 + 11x - 6 = 0; roots:", cubic_roots)
    else:
        print("NumPy not available; skipping cubic example.")

    # Example 5: Evaluate polynomial 2x^3 - 3x + 5 at x = 2
    value = evaluate_polynomial([2, 0, -3, 5], 2)
    print("Value of 2x^3 - 3x + 5 at x=2:", value)

    # Example 6: Derivative of 2x^3 - 3x + 5
    deriv = derivative_polynomial([2, 0, -3, 5])
    print("Derivative coefficients of 2x^3 - 3x + 5:", deriv)


if __name__ == "__main__":
    main()
