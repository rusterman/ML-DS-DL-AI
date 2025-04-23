"""
    Polynomial Equations: Exercises

    This file contains practice exercises for evaluating, solving, and analyzing polynomial equations.
"""

import cmath

"""
    1. Evaluate Polynomial
    Exercise:
    Use the evaluate_polynomial function to compute the value of 3x^3 - 2x^2 + x - 5 at x = 2.
    Print the result.
"""


# Your Solution...
def evaluate_polynomial(coefficients, x):
    result = 0
    degree = len(coefficients) - 1

    for i, coefficient in enumerate(coefficients):
        result += coefficient * x ** (degree - i)

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
        raise ValueError("a cannot be zero")

    return -b / a


"""
    3. Quadratic Formula
    Exercise:
    Solve the equation x^2 - 5x + 6 = 0. Compute the discriminant and both roots using the solve_quadratic function.
    Print the discriminant and roots.
"""


# Your Solution...
def solve_quadratic(a, b, c):
    if a == 0:
        return solve_linear(b, c)

    d = a * b - 4 * a * c
    sqrt_d = cmath.sqrt(d)
    root1 = (-b + sqrt_d) / (2 * a)
    root2 = (-b - sqrt_d) / (2 * a)

    return [root1, root2]


"""
    4. Nature of Roots
    Exercise:
    Determine the nature of roots for x^2 + 4x + 5 = 0 using solve_quadratic and discriminant logic.
    Print a message indicating whether the roots are real and distinct, real and equal, or complex.
"""


# Your Solution...
def nature_of_roots(a, b, c):
    d = a * b - 4 * a * c

    if d > 0:
        print("The roots are real and distinct")
    elif d == 0:
        print("The roots are real")
    else:
        print("The roots are in complex plane")

    return solve_quadratic(a, b, c)


"""
    5. Cubic Roots
    Exercise:
    Solve the cubic equation x^3 - 6x^2 + 11x - 6 = 0 using the solve_polynomial function.
    Print the roots.
"""


# Your Solution...
def cubic_roots(a, b, c, x):
    return evaluate_polynomial([a, b, c, 0], x)




def main():
    # 3x^3 - 2x^2 + x - 5
    value = evaluate_polynomial([3, -2, 1, -5], 2)
    print(f"evaluate_polynomial: {value}")

    # 5x + 7 = 0
    value = solve_linear(5, 7)
    print(f"solve_linear: {value}")

    # x^2 - 5x + 6 = 0
    roots = solve_quadratic(2, -5, 6)
    print(f"solve_quadratic: {roots}")

    # x^2 + 4x + 5
    value = nature_of_roots(2, 4, 5)
    print(f"nature_of_roots: {value}")


if __name__ == "__main__":
    main()
