""" Summation Exercises """

"""
    1. Simple Summation: ∑₍ᵢ₌₁₎ⁿ i

    Exercise:
    Compute the sum of integers from 1 to 50. Write code to compute and print the result.
"""
# Your Solution...
def simple_sum(num):
    total = 0

    for i in range(1, num + 1):
        total += i

    return total

n = 50
print(f"Sum of i from 1 to {n} is {simple_sum(n)}")



"""
    2. Summation with Generator Expression
       Use Python’s built-in sum() with a generator for custom f(i).

    Exercise:
    Compute the sum of even numbers from 2 to 20 using sum() and a generator expression. Print the result.
"""
# Your Solution...
def sum_even(a, b):
    return sum([i for i in range(a, b + 1, 2)])

print(f"Sum of even numbers from 2 to 20 is {sum_even(2, 20)}")


"""
    3. Symbolic Summation with Sympy
       Compute symbolic sums like ∑₍ᵢ₌₁₎ⁿ i².

    Exercise:
    Symbolically compute ∑₍ᵢ₌₁₎ⁿ i² using sympy, simplify the expression, and print both the symbolic formula and its value for n=10.
"""
# Your Solution...
from sympy import symbols, summation, factor

i, n = symbols('i n')
expr = factor(summation(i**2, (i, 1, n)))
print(f"Symbolic sum ∑₍ᵢ₌₁₎ⁿ i² = {expr}")  # n*(n + 1)*(2*n + 1)/6
print(f"For n = 10: {expr.subs(n, 10)}")  # 385


"""
    4. Double Summation for Multiplication
       Express a * b as ∑₍ᵢ₌₁₎ᵃ ∑₍ⱼ₌₁₎ᵇ 1.

    Exercise:
    Write code that implements multiplication of a and b solely using a double summation.  
    For example, for a=4 and b=5, your code should compute 20 by summing 1 over the appropriate ranges. Print the result.
"""
# Your Solution...
'''
Double Summation for Multiplication = Double Summation instead of single Multiplication
'''
# 1st version:
a = 4
b = 5
total_b = sum(1 for i in range(1, b + 1, 1))
total_a = sum(b for i in range(1, a + 1, 1))
print("Total a and b: ", total_a, total_b)

# 2nd version with simple for loops:
total_a = 0
total_b = 0
a = 4
b = 5
for i in range(1, b + 1):
    total_b += 1
for i in range(1, a + 1):
    total_a += total_b
print("Total a and b: ", total_a, total_b)

# 3rd version with Nested Loop, List Comprehension, Generator Expression:
a = 4
b = 5
total_ab = sum(1 for j in range(1, a + 1, 1) for i in range(1, b + 1, 1))
# total_ab = sum([1 for j in range(1, a + 1, 1) for i in range(1, b + 1, 1)])
print("Result of sum(): ", total_ab)

