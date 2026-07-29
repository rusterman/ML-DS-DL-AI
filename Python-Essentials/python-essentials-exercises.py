"""

    1. Data Types Practice
    
    Exercise:
    Define and print the following variables:

    * An integer (`int`) with a value of 10.
    * A floating-point number (`float`) representing 9.81.
    * A string (`str`) that says "Python Essentials".
    * A list (`list`) containing numbers from 1 to 5.
    * A tuple (`tuple`) with two coordinates: (50, 100).
    * A dictionary (`dict`) with keys `name` (value: "John") and `age` (value: 28).
    * A set (`set`) containing numbers {1, 2, 2, 3}.
    * A boolean (`bool`) variable set to `False`.
"""
print("1. DATA TYPES PRACTICE: ")
# Your Solution...
my_int = 10
my_float = 9.81
my_str = "Python"
my_list = [1, 2, 3, 4, 5]
my_tuple = (10, 20)
my_dict = {'name': 'John', 'age': 28}
my_set = {1, 2, 2, 3}
my_bool = True

print("integer:", my_int)
print("float:", my_float)
print("string:", my_str)
print("list:", my_list)
print("tuple:", my_tuple)
print("dictionary:", my_dict)
print("set:", my_set)
print("boolean:", my_bool)


"""
    2. Iteration Practice
    
    Exercise:
    
    * Use a `for` loop to print numbers from 10 to 1 (descending).
    * Use a `while` loop to print even numbers between 2 and 10.
    * Use a list comprehension to create a list of cubes of numbers from 1 to 5 and print it.
"""
print()
print("2.ITERATION PRACTICE:")
# Your Solution...
for i in range(10, 1, -1):
    print(i, end = " ")
print()
i = 2
while (i < 10):
    print(i, end = " ")
    i += 1
print()
for i in my_list:
    print(i, end = " ")
print()


"""
    3. Functions Practice
    
    Exercise:
    Create the following functions:
    
    * A function named `area_of_circle` that takes radius as input and returns the area of a circle.
    * A function named `is_even` that returns `True` if a number is even, otherwise `False`.
    * A lambda function `multiply` that multiplies two numbers.
    
    Demonstrate each function with sample inputs.
"""
print()
print("3. FUNCTIONS PRACTICE:")
# Your Solution...
def are_of_circle(radius):
    return (3.14 * (radius ** 2))
def is_even(bool):
    return bool
multiply = lambda x, y: x * y

print("area:",are_of_circle(5))
print("even:", is_even(True))
print("multiply:", multiply(2, 3))

"""
    4. Importing and Using Libraries
    
    Exercise:
    
    * Import `math` and use it to calculate and print the square root of 64.
    * Import NumPy with alias `np` and create a NumPy array `[10, 20, 30, 40, 50]`, then print it.
    * Import `randint` from the `random` module and print a random integer between 5 and 15.
"""
print()
print("4. IPORTING AND USING LIBRARIES:")
# Your Solution...
import math
print(math.sqrt(64))
import numpy as np
print(np.array([10, 20, 30, 40, 50]))
from random import randint
print(randint(5, 15))


"""
    5. Symbolic Math with SymPy
    
    Exercise:
    Use SymPy to solve symbolically the quadratic equation: x^2 - 5x + 6 = 0. Print the solutions.
"""
print()
print("5.SYMBOLIC MATH WITH SYMPY:")
# Your Solution...
from sympy import symbols, Eq, solve

x = symbols('x')

equation = Eq(x**2 - 5*x + 6, 0)

solutions = solve(equation, x)

print("Solutions:", solutions)


"""
    6. Solving Equations with NumPy
    
    Exercise:
    Use NumPy to solve the following system of equations and print the solutions for x and y:
    4x + 3y = 20
    2x - y = 2
"""
print()
print("6.SOLVING EQUATIONS WITH NUMPY:")
# Your Solution...
import numpy as np

A = np.array([
    [4, 3],
    [2, -1]
])

B = np.array([20, 2])

solution = np.linalg.solve(A, B)

print("x =", solution[0])
print("y =", solution[1])