# task 1 
"""
a = int(input("Reqem daxil edin: "))
b = int(input("Reqem daxil edin: "))
c = int(input("Reqem daxil edin: "))
x = (c - b) / a
print(f"x in qiymeti: {x}")
"""

"""
from sympy import symbols, Eq, solve

x = symbols('x')

equation = Eq(7*x + 5 , 3*x + 13)
solution = solve(equation , x) 
print(f"x = {solution}")
"""
"""
import numpy as np 
A = np.array([
    [3,2],
    [2,-1]
])

B = np.array([11,1])

solution = np.linalg.solve(A,B)
print("x =", solution[0])
print("y =", solution[1])
"""

"""
import math 

a = 1
b = -5
c = 6

diskrimnat = b**2 - 4 * a * c

if diskrimnat > 0:
    sqrt_d = math.sqrt(diskrimnat)
    x1 = (-b - sqrt_d) / (2*a)
    x2 = (-b + sqrt_d) / (2*a)
    print(f"x1 = {x1}, x2 = {x2}")

else:
    # kompleks köklər üçün cmath istifadə olunur
    import cmath
    sqrt_D = cmath.sqrt(diskrimnat)
    x1 = (-b + sqrt_D) / (2*a)
    x2 = (-b - sqrt_D) / (2*a)
    print(f"x1 = {x1}, x2 = {x2}")
"""
"""
a = 1
b = 4
c = 5

diskrimnat = b**2 - 4 * a * c

if diskrimnat > 0:
    print("Köklər real və müxtəlifdir.")
elif diskrimnat == 0:
    print("Köklər real və bərabərdir.")
else :
    print("Köklər kompleksdir.")
"""


