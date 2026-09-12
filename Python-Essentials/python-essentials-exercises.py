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

# Your Solution...
print(int_val := 10)
print(float_var := 9.81)
print(char_arr := "Python Essentials")
print(num_list := [1, 2, 3, 4, 5])
print(xy_coor := (50, 100))
print(user_db := {"name": "John" , "age" : 28 })
print(num_set := {1, 2, 2, 3})
print(is_bool := False, end="\n\n")


"""
    2. Iteration Practice
    
    Exercise:
    
    * Use a `for` loop to print numbers from 10 to 1 (descending).
    * Use a `while` loop to print even numbers between 2 and 10.
    * Use a list comprehension to create a list of cubes of numbers from 1 to 5 and print it.
"""

# Your Solution...
for i in range(10, 1, -1):
    print(i)

print("\n\n")



val = 2
while val < 10:
    print(val)
    val += 2

print("\n\n")



print(cube_list := [x**3 for x in range(1, 5)], end="\n\n")

"""
    3. Functions Practice
    
    Exercise:
    Create the following functions:
    
    * A function named `area_of_circle` that takes radius as input and returns the area of a circle.
    * A function named `is_even` that returns `True` if a number is even, otherwise `False`.
    * A lambda function `multiply` that multiplies two numbers.
    
    Demonstrate each function with sample inputs.
"""

# Your Solution...
def area_of_circle(radius):
    return 3.14 * radius ** 2

print("Area of circle: {} when radius is {}: ".format(area_of_circle(8), 8), end="\n\n")



def is_even(num):
    return num & 1 == 0

print("12 is (Odd ? Even): ", is_even(12), end="\n\n")



multiply = lambda num1, num2: num1 * num2
print("5 * 10 = ", multiply(5, 10), end="\n\n")

"""
    4. Importing and Using Libraries
    
    Exercise:
    
    * Import `math` and use it to calculate and print the square root of 64.
    * Import NumPy with alias `np` and create a NumPy array `[10, 20, 30, 40, 50]`, then print it.
    * Import `randint` from the `random` module and print a random integer between 5 and 15.
"""

# Your Solution...
import math
print("The square root of 64 is:", math.sqrt(64), end="\n\n")



import numpy as np
print("Numpy array: ", np.array([10, 20, 30, 40, 50]), end="\n\n")



from random import randint
print("Random integer number: ", randint(5, 15), end="\n\n")

"""
    5. Symbolic Math with SymPy
    
    Exercise:
    Use SymPy to solve symbolically the quadratic equation: x^2 - 5x + 6 = 0. Print the solutions.
"""

# Your Solution...
from sympy import symbols, solve
x = symbols('x')
expr = x**2 - 5*x + 6
print(solve(expr, x), end="\n\n")

"""
    6. Solving Equations with NumPy
    
    Exercise:
    Use NumPy to solve the following system of equations and print the solutions for x and y:
    4x + 3y = 20
    2x - y = 2
"""

# Your Solution...
import numpy as np
A_matris = np.array([[4, 3], [2, -1]])
b_vector = np.array([20, 2])
print(np.linalg.solve(A_matris, b_vector))