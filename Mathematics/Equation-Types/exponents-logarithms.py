""" Exponent & Logarithm Examples """

"""
    1. Simple Loop
       Compute and print a^x for integer x in [start, end].
"""
def compute_powers(a, start, end):
    result = []
    for x in range(start, end + 1):
        result.append((x, a ** x))
    return result


# Example: 2^x for x from -3 to 5
print("1) 2^x for x in [-3,5]:", compute_powers(2, -3, 5))

"""
    2. Using a List Comprehension
       For base b and inputs in a list, compute log_b(x) where x > 0.
"""
# Your Solution... Demonstrated via Taylor (Euler) formula
"""
Only the number 0.5 is more interesting than the others: 1, 3, 9, 27

log_3 0.5 = ln0.5 / ln3 = ?

ln ((1 + x) / (1 - x)) = 2 * (x + x^3 / 3 + x^5 / 5 + x^7 / 7 + ...)
-1 < x = 1
-1 < 0.5 < 1

1) ln0.5:
(1 + x) / (1 - x) = 0.5
1 + x = 0.5 - 0.5x
1.5x = -0.5
x = -0.5 / 1.5 = -1 / 0.3 = -10 / 3 ≈ -3.3333

or we can calculate just -ln2 instead of ln0.5, 
because of ln0.5 = ln1/2 = -ln2.
-ln2
(1 + x) / (1 - x) = 2
1 + x = 2 - 2x
3x = 1
x = 1/3 ≈ 0.3333 ==> ln0.5 = -ln2 ==> x = -0.3333

-ln2 ≈ 2 * (1/3 + (1/3)^3 / 3 + (1/3)^5 / 5 + (1/3)^7 / 7) = 
     = 2 * (0.3333 + 0.012346 + 0.000823 + 0.000065) = 
     = 2 * 0.346567 = 0.693134 ==> ln0.5 = -ln2 = -0.693134
     

2) ln3:
(1 + x) / (1 - x) = 3
1 + x = 3 * (1 - x)
1 + x = 3 - 3x
4x = 2
x = 0.5

ln3 ≈ 2 * (0.5 + 0.5^3 / 3 + 0.5^5 / 5 + 0.5^7 / 7) = 
    = 2 * (0.5 + ≈0.041667 + 0.00625 + ≈0.001116) = 
    = 2 * 0.549033 = 1.098066
    

Our final result: log_3 0.5 = ln0.5 / ln3 ≈ -0.693134 / 1.098066 ≈ -0.63123163817
Computer's final result: log_3 0.5 = ln0.5 / ln3 ≈ -0.63092975357


Let's add more terms to achieve the goal: (1/3)^9 / 9 + (1/3)^11 / 11

1) ln0.5 = -ln2:
-ln2 ≈ 2 * (1/3 + (1/3)^3 / 3 + (1/3)^5 / 5 + (1/3)^7 / 7 + (1/3)^9 / 9 + (1/3)^11 / 11) = 
     = 2 * (0.3333 + 0.012346 + 0.000823 + 0.000065 + 5.645029 + 5.131845) = 
     = 2 * 0.346573 = 0.693146 ==> ln0.5 = -ln2 = -0.693146
     
2) ln3:
ln3 ≈ 2 * (0.5 + 0.5^3 / 3 + 0.5^5 / 5 + 0.5^7 / 7 + 0.5^9 / 9 + 0.5^11 / 11) = 
    = 2 * (0.5 + ≈0.041667 + 0.00625 + ≈0.001116 + ≈2.170139 + 4.438920) = 
    = 2 * 0.549294 ≈ 1.098589

The final result after second effort: log_3 0.5 = ln0.5 / ln3 ≈ -0.693146 / 1.098589 ≈ -0.63094245319444266
Computer's final result: log_3 0.5 = ln0.5 / ln3 ≈ -0.6309297535714574

Yes, as you can see above, we were able to achieve the same successful result as with the computer.
We observe that, to arrive at the result calculated by the computer, 
we must also include the terms raised to the 9th power and if necessary, the 11th power.
"""
import math

b = 3
inputs = [0.5, 1, 3, 9, 27]
logs = [(x, math.log(x, b)) for x in inputs if x > 0]
print(f"2) log base {b} of inputs:", logs)

"""
    3. Symbolic Verification with Sympy
       a) Verify exponent law: a^b * a^c == a^(b + c)
       b) Verify log law: log(x*y) == log(x) + log(y)
"""
import sympy as sp

a, b, c, x, y = sp.symbols('a b c x y', positive=True)

# a) exponent law
expr_exp = a ** b * a ** c - a ** (b + c)
print("3a) simplify(a^b * a^c - a^(b+c)) =", sp.simplify(expr_exp))

# b) logarithm law
expr_log = sp.log(x * y, a) - (sp.log(x, a) + sp.log(y, a))
print("3b) simplify(log_a(x*y) - (log_a(x)+log_a(y))) =", sp.simplify(expr_log))

"""
    4. Graphing with Matplotlib
       Plot y = a^x and y = log_a(x), show vertical asymptote x=0 for log.
       
       Note: Generally it should to be x = log_a(y), but when plotting a graph, 
             we usually represent the function in the form of y.
             It is simply for representing the inverse function in the standard form of the y
             when plotting the graph.
             This also looks incorrect, as if it's a different equation, but the purpose 
             of the graph (when constructing the inverse function) is to show the inverse 
             of the exponential function.
"""
import numpy as np
import matplotlib.pyplot as plt

a = 2

# Exponential: x in [-5, 5]
x_exp = np.linspace(-5, 5, 500)
y_exp = a ** x_exp

# Logarithm: x in [0.1, 10]
x_log = np.linspace(0.1, 10, 500)
y_log = np.log(x_log) / np.log(a)

plt.figure(figsize=(6, 6))
plt.plot(x_exp, y_exp, label=f'y = {a}^x')
plt.plot(x_log, y_log, label=f'y = log_{a}(x)')
plt.axvline(0, linestyle=':', label='Vertical asymptote: x = 0 for log')

plt.title(f"Exponential and Logarithm Functions (base {a})")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(alpha=0.3)
plt.xlim(-5, 10)
plt.ylim(-5, max(y_exp.max(), y_log.max()) + 1)
plt.show()
