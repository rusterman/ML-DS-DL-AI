""" Summation Exercises """

"""
    1. Simple Summation: ∑₍ᵢ₌₁₎ⁿ i

    Exercise:
    Compute the sum of integers from 1 to 50. Write code to compute and print the result.
"""
# Your Solution...
def SimpleSummation(i,n):
    result=0
    for j in range(i,n+1):
        result+=j
    return result

"""
    2. Summation with Generator Expression
       Use Python’s built-in sum() with a generator for custom f(i).

    Exercise:
    Compute the sum of even numbers from 2 to 20 using sum() and a generator expression. Print the result.
"""
# Your Solution...

summ=sum(i for i in range(2,21,2))
print(summ)

"""
    3. Symbolic Summation with Sympy
       Compute symbolic sums like ∑₍ᵢ₌₁₎ⁿ i².

    Exercise:
    Symbolically compute ∑₍ᵢ₌₁₎ⁿ i² using sympy, simplify the expression, and print both the symbolic formula and its value for n=10.
"""
# Your Solution...
import sympy as sp
i,n=sp.symbols('i n')
expression=sp.summation(i**2,(i,1,n))
print(f"Symbolic sum ∑₍ᵢ₌₁₎ⁿ i² : {expression}")
print(f"n=10 : {expression.subs(n,10)}")

"""
    4. Double Summation for Multiplication
       Express a * b as ∑₍ᵢ₌₁₎ᵃ ∑₍ⱼ₌₁₎ᵇ 1.

    Exercise:
    Write code that implements multiplication of a and b solely using a double summation.  
    For example, for a=4 and b=5, your code should compute 20 by summing 1 over the appropriate ranges. Print the result.
"""
# Your Solution...
a,b,result=4,5,0
for i in range(a):
    for i in range(b):
        result+=1
print(result)
