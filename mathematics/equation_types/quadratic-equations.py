"""
    Quadratic Equations: Key Examples
"""

"""
    1. Quadratic Formula: ax² + bx + c = 0
    Example:
    Solve 2x² - 4x - 6 = 0. Compute discriminant and roots using the quadratic formula.
"""
a, b, c = 2, -4, -6
D = b ** 2 - 4 * a * c
root1 = (-b + D ** 0.5) / (2 * a)
root2 = (-b - D ** 0.5) / (2 * a)
print(f"Example 1: Roots: {root1}, {root2}")  # Roots: 3.0, -1.0


"""
    2. Nature of Roots via Discriminant
    Example:
    For x² + 2x + 1 = 0, discriminant = 0 → real and equal roots.
"""
a, b, c = 1, 2, 1
D = b ** 2 - 4 * a * c
if D > 0:
    nature = "Real and distinct"
elif D == 0:
    nature = "Real and equal"
else:
    nature = "Complex"
print(f"Example 2: Nature of roots: {nature}")  # Real and equal
