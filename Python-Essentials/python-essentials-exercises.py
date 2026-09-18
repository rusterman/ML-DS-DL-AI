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
import math

# Your Solution...
a=10
print(a)
b=9.81
print(b)
c="Python Essentials"
print(c)
ls=[1,2,3,4,5]
print(ls)
t=(50,100)
print(t)
d={'name':'John', 'age':28}
print(d)
set2={1,2,2,3}
print(set2)
bl=False
print(bl)

"""
    2. Iteration Practice
    
    Exercise:
    
    * Use a `for` loop to print numbers from 10 to 1 (descending).
    * Use a `while` loop to print even numbers between 2 and 10.
    * Use a list comprehension to create a list of cubes of numbers from 1 to 5 and print it.
"""

# Your Solution...
print('---------------------------')
for i in range(10,0,-1):
    print(i)
j=2
print()
while j<=10:
    if j%2==0:
        print(j)
    j+=1
print()
ls=[x**2 for x in range(1,6)]
print(ls)


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
print('---------------------------')
from math import pi
def area_of_circle(r):
    return pi*r**2
radius=int(input("Enter radius: "))
print(area_of_circle(radius))
print()
def is_even(num):
    return num%2==0
print(is_even(int(input("Enter a number: "))))
print()
x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
m=lambda x1,y1: x1*y1
print(m(x,y))
"""
    4. Importing and Using Libraries
    
    Exercise:
    
    * Import `math` and use it to calculate and print the square root of 64.
    * Import NumPy with alias `np` and create a NumPy array `[10, 20, 30, 40, 50]`, then print it.
    * Import `randint` from the `random` module and print a random integer between 5 and 15.
"""

# Your Solution...
print('---------------------------')
import math
print(math.sqrt(64))
print()
import numpy as np
arr=np.array([10,20,30,40,50])
print(arr)
print()
from random import randint
print(randint(5,15))

"""
    5. Symbolic Math with SymPy
    
    Exercise:
    Use SymPy to solve symbolically the quadratic equation: x^2 - 5x + 6 = 0. Print the solutions.
"""

# Your Solution...
print('---------------------------')
from sympy import symbols, Eq, solve
x=symbols('x')
equation=Eq(x**2-5*x+6,0)
solution= solve(equation,x)
print("Solution: ", solution)

"""
    6. Solving Equations with NumPy
    
    Exercise:
    Use NumPy to solve the following system of equations and print the solutions for x and y:
    4x + 3y = 20
    2x - y = 2
"""
# Your Solution...
print('---------------------------')
A=np.array([[4,3],
            [2,-1]])
B=np.array([20,2])
solution=np.linalg.solve(A,B)
x,y=solution
print("x: ",f'{x:.2f}')
print("y: ", f'{y:.2f}')

