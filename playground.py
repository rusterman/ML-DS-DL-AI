""" Summation Exercises """

"""
    1. Simple Summation: ∑₍ᵢ₌₁₎ⁿ i

    Exercise:
    Compute the sum of integers from 1 to 50. Write code to compute and print the result.
"""


# Your Solution...
def simple_summation(n):
    total = 0
    for i in range(1, 50):
        total += i
    return total


"""
    2. Summation with Generator Expression
       Use Python’s built-in sum() with a generator for custom f(i).

    Exercise:
    Compute the sum of even numbers from 2 to 20 using sum() and a generator expression. Print the result.
"""


# Your Solution...
def summation_range(a, b, func=lambda x: x):
    return sum(func(i) for i in range(a, b + 1))


s
print(summation_range(1, 5, lambda x: x ** 2))


def summation_range(a, b, func=lambda x: x):
    return sum(func(i) for i in range(a, b + 1))


"""
    3. Symbolic Summation with Sympy
       Compute symbolic sums like ∑₍ᵢ₌₁₎ⁿ i².

    Exercise:
    Symbolically compute ∑₍ᵢ₌₁₎ⁿ i² using sympy, simplify the expression, and print both the symbolic formula and its value for n=10.
"""
# Your Solution...
from sympy import symbols, summation

i, n = symbols('i n')
expr = summation(i, (i, 1, n))
print(f"Symbolic sum ∑₍ᵢ₌₁₎ⁿ i = {expr}")
print(f"For n = 5: {expr.subs(n, 5)}")

"""
    4. Double Summation for Multiplication
       Express a * b as ∑₍ᵢ₌₁₎ᵃ ∑₍ⱼ₌₁₎ᵇ 1.

    Exercise:
    Write code that implements multiplication of a and b solely using a double summation.  
    For example, for a=4 and b=5, your code should compute 20 by summing 1 over the appropriate ranges. Print the result.
"""


# Your Solution...

def double_summation(a, b, func1=lambda x: x, func2=lambda x: x):
    return sum(
        func1(i) * func2(j)
        for i in range(1, a + 1)
        for j in range(1, b + 1)
    )
