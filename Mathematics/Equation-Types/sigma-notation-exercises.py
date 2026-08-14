""" Summation Exercises """

"""
    1. Simple Summation: ∑₍ᵢ₌₁₎ⁿ i

    Exercise:
    Compute the sum of integers from 1 to 50. Write code to compute and print the result.
"""
# Your Solution...
print("1.Simple Summation: ∑₍ᵢ₌₁₎ⁿ i")
def simple_summation(n):
    result = 0
    for i in range (1, n + 1):
        result += i
    return result

n = 50 
print(f"Sum of i from 1 to {n} is {simple_summation(n)}")
print()


"""
    2. Summation with Generator Expression
       Use Python’s built-in sum() with a generator for custom f(i).

    Exercise:
    Compute the sum of even numbers from 2 to 20 using sum() and a generator expression. Print the result.
"""
# Your Solution...
print("2. Summation with Generator Expressio")
def summation_range(a, b, func= lambda x: x):
    return sum(func(i) for i in range (a, b + 1, 2))

print(f"Sum of squares from 2 to 20 is {summation_range(2, 20)}")
print()

"""
    3. Symbolic Summation with Sympy
       Compute symbolic sums like ∑₍ᵢ₌₁₎ⁿ i².

    Exercise:
    Symbolically compute ∑₍ᵢ₌₁₎ⁿ i² using sympy, simplify the expression, and print both the symbolic formula and its value for n=10.
"""
# Your Solution...
from sympy import symbols, summation
print("3. Symbolic Summation with Sympy")
i, n = symbols("i n")
expr = summation (i ** 2, (i , 1, n))
print(f"Dustur: {expr}")
print(f"1 to 10: {expr.subs(n, 10)}")
print()
"""
    4. Double Summation for Multiplication
       Express a * b as ∑₍ᵢ₌₁₎ᵃ ∑₍ⱼ₌₁₎ᵇ 1.

    Exercise:
    Write code that implements multiplication of a and b solely using a double summation.  
    For example, for a=4 and b=5, your code should compute 20 by summing 1 over the appropriate ranges. Print the result.
"""
# Your Solution...
print("4. Double Summation for Multiplication")
def Sum(a, b):
    result = 0
    for i in range (1, a + 1):
        for j in range (1, b + 1):
            result += 1
    return result
print(f"a=4 b=5 result: {Sum(4, 5)}")
    

