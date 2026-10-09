```
Bisection + Horner's (including recursive method) + Cardano's (Tartaglia) + Linearization + Newton-Raphson's methods in a single solution.

In the "evaluate_polynomial" function within the "polynomials.py" file,
a solution is required for this example equation: 2x³ - 3x + 5 at x = 2.
That is what inspired me to make this investigation.
By focusing primarily on the "finding the real root of the polynomial",
distinctions regarding to the other sections listed below will
also automatically become clear:

2x³ - 3x + 5        → is a polynomial (of the 3rd degree)

2x³ - 3x + 5 = 0    → is a polynomial equation

P(x) = 0
2x³ - 3x + 5 = 0   → finding the real root of the polynomial by solving P(x) = 0

x = 2
2x³ - 3x + 5 = P(x) → evaluating the polynomial at any value of x (in this case at 2)
P(2) = 2 · 2³ - 3 · 2 + 5 = 15
or
x = 0
2x³ - 3x + 5 = P(x) → evaluating the polynomial at any value of x (in this case at 0)
P(0) = 2 · 0³ - 3 · 0 + 5 = 5


Starting from this section, the methods and functions used, the conclusions reached and
the final results obtained will be explained step by step.



Bisection method:
The bisection method finds the value of x that satisfies the condition P(x) ≈ 0.
Then, P(x) is calculated for the found value of x.

Bisection is a method of dividing a given interval in half:
2x³ - 3x + 5 = 0
[+2 +0 -3 +5]


We can test several methods to find the root x:
p = Leading coefficient = 2 → Divisors: ±1, ±2
q = Constant term = 5 → Divisors: ±1, ±5
x = ± (Constant term / Leading coefficient) = ± p/q

x = ±1/1 = ±1, 
    ±5/1 = ±5, 
    ±1/2 = ±0.5,
    ±5/2 = ±2.5

±1 , ±5 , ±0.5 , ±2.5

1 | 2  0  -3  5
  |    2   2 -1
----------------
  | 2  2  -1  4   →   4 ≠ 0


If none of the possible simple roots yield a result of 0, then this equation,
this polynomial has no rational roots.

If the function is negative at one point and positive at another, a zero must exist
there (within that interval).

The main approach involves searching between positive and negative values,
using the smallest values for x:

P(x) = 2x³ - 3x + 5
P(0) = 5 > 0 ✓
P(-1) = 6 > 0 ✓
P(-2) = -5 < 0 ✓

-2 < x < -1 
(-2 + (-1)) / 2 = -1.5   →    Intermediate Value Theorem


Let's check:
-1.5 | 2  0  -3   5
     |   -3  4.5 -2.25
-----------------------
     | 2 -3  1.5  2.75   →   2.75 ≠ 0

Therefore, the root is not in the range -2 < x < (-1); it's closer and lies between -2 and -1.5:
P(-1.5) = 2.75 > 0
P(-2) = -5 < 0

This expression (P(-1.5) = 2.75 > 0) is closer to the value of x than the previous one (P(-1) = 6 > 0).
In other words, x lies within a narrower interval:
-2 < x < -1.5
(-2 + (-1.5)) / 2 = -1.75   →    Intermediate Value Theorem


Let's check:
-1.75 | 2   0    -3      5
      |    -3.50  6.125 -5.46875
---------------------------------
      | 2  -3.50  3.125  -0.46875   →   -0.46875 ≠ 0


So: it is not (-2) < x < -1.5; the root is closer. Tt lies between -1.75 and -1.5.

It continues on like this:

[-1.75,      -1.625]
[-1.75,      -1.6875]
[-1.71875,   -1.6875]
[-1.71875,   -1.703125]
[-1.7109375, -1.703125]

P(-1.7109375) ≈ -0.02 < 0


Then, x ≈ -1.7108...
In short (ultimately), we proceed by reducing the interval (gradually narrowing it down).



Cardano's formula (finding the roots of a cubic equation)
Depressed Cubic Formula (form of the cubic equation):
Ax³ + Bx² + Cx + D = 0
2x³ + 0x² - 3x + 5 = 0

x³ + px + q = 0
x³ - (3/2)x + (5/2) = 0

p = -3/2
q = 5/2

Cardano's (Tartaglia's) formula:
x = ³√[-q/2 + √[(q/2)² + (p/3)³]] + ³√[-q/2 - √[(q/2)² + (p/3)³]] =
  = ³√[-5/4 + √[(5/4)² + (-5/2)³]] + ³√[-5/4 - √[(5/4)² + (-5/2)³]] =
  = ³√[(-5 + √23) / 4] + ³√[(-5 - √23) / 4]

We have reached this point, and the result we have arrived at reminds us of the
formula for the cube of a sum,- one of the algebraic identities for multiplication:
(a + b)³ = a³ + 3a²b + 3ab² + b³ = a³ + b³ + 3ab(a + b)

a = ³√[(-5 + √23) / 4]
a³ = (-5 + √23) / 4

b = ³√[(-5 - √23) / 4]
b³ = (-5 - √23) / 4

So, we shaped it like this:
a³ + b³ + 3ab(a + b) = (a + b)³
³√[(-5 + √23) / 4] + ³√[(-5 - √23) / 4] = x
(³√[(-5 + √23) / 4] + ³√[(-5 - √23) / 4])³ = x³
x³ = (³√[(-5 + √23) / 4] + ³√[(-5 - √23) / 4])³       →      (a + b)³
x³ = (³√(-5 + √23) + ³√(-5 - √23))³ / (³√4)³

4x³ = (³√(-5 + √23) + ³√(-5 - √23))³                  →       a = ³√(-5 + √23);  b = ³√(-5 - √23)
4x³ = (-5 + √23)^(1/3·3) + (-5 - √23)^(1/3·3) +
    + 3 · (-5 + √23)^(1/3·3) · (-5 - √23)^(1/3·3) ·   →       "Difference of Squares" formula
    * ((-5 + √23)^(1/3·3) + (-5 - √23)^(1/3·3))

Get attention:
a³ = -5 + √23
b³ = -5 - √23
3ab = 3 · ³√2 = 3 · 2^(1/3)
a + b = ³√(-5 + √23) · ³√(-5 - √23) =
      = (-5 + √23)^(1/3) + (-5 - √23)^(1/3)

Continue where we left off:
4x³ = -5 + √23 - 5 - √23 + 3 · ³√2 · ³√4 · x

As we mentioned above, ³√4 · x:
4x³ = (³√(-5 + √23) + ³√(-5 - √23))³
(4x³)^(1/3) = (((-5 + √23)^(1/3) + (-5 - √23)^(1/3))³)^(1/3)
4^(1/3)x = (-5 + √23)^(1/3) + (-5 - √23)^(1/3)
³√4 · x = (-5 + √23)^(1/3) + (-5 - √23)^(1/3)
³√4 · x = ³√(-5 + √23) + ³√(-5 - √23)

Again, continue from:
4x³ = -5 + √23 - 5 - √23 + 3 · ³√2 · ³√4 · x
4x³ = -10 + 3 · ³√2 · ³√4 · x                →         -10 = a³ + b³;  3 · ³√2 = 3ab
4x³ = -10 + 3 · ³√8 · x = -10 + 6x
4x³ = -10 + 6x
2x³ = -5 + 3x

Obtained result on the below side shows that we have performed all the operations correctly:
2x³ - 3x + 5 = 0

Where did we leave off?
Here: ³√[(-5 + √23) / 4] + ³√[(-5 - √23) / 4]



Linearization formula (tangent line approximation)
Linear approximation formula for a square root:
√23 = ?

L(x) = f(a) + f'(a)(x - a)
x - a = h
x = a + h

f(x) = √x = √(a + h)           →       f(x) = √x; f(x) = √(a + h)
f'(a) = 1 / (2√a)

f(a + h) ≈ f(a) + f'(a) · h
√(a + h) ≈ √a + (1 / 2√a) · h ≈ √a + h / (2√a)

1)
√23 = √(25 - 2)
a = 25; h = -2

√23 ≈ √25 + (-2) / (2 · √25) ≈ 5 + (-2) / 10
    ≈ 5 - 1/5 = 4,8
4,8² = 23,04 ≠ 23

2)
4,8 = √23,04
√23 ≈ 4,8 + (23 - 23,04) / (2 · 4,8)
    ≈ 4,8 + (-0,04) / 9,6
    ≈ 4,8 - 0,0041666667
    ≈ 4,7958333333

3)
4,7958333333² ≈ 23,000017360791388889
4,7958333333 ≈ √23,000017360791388889

√23 ≈ 4,7958333333 + (23 - 23,00001736068) / (2 · 4,7958333333)
    ≈ 4,7958333333 + (-0,00001736068) / 9,5916666666 ≈
    ≈ 4,7958333333 - 1,80998783667635e-6 ≈
    ≈ 4,7958333333 - 0,00000180998784 ≈
    ≈ 4,7958315233

We found √23 using the Linearization method.
We return to where we left off:
³√(-5 + √23) / 4] + ³√[(-5 - √23) / 4] =
= ³√[(-5 + 4,7958315233) / 4] + ³√[(-5 - 4,7958315233) / 4]

1) ³√[(-5 + 4,7958315233) / 4] = ³√[(-0,2041684767) / 4] → ³√(-0,051042119175)
2) ³√[(-5 - 4,7958315233) / 4] = ³√[(-9,7958315233) / 4] → ³√(-2,448957880825)

From this part, we will continue the solution using the Newton's method.



Newton-Raphson method:
xₙ₊₁ = (1/3) · (2 · xₙ + aₙ / xₙ²)

1)
aₙ = +0,0510542113175 ≈ +0,051    →    Question: Why didn't we take the number as it is, with a negative sign?
0,3³ = 0,027
0,4³ = 0,064
0,027 < 0,051 < 0,064

Which number should be selected: x₀ = ?
0,027 < x₀ < 0,064

Let this be: x₀ = 0,35
0,3³ < 0,35³ < 0,4³

So, this will be: x₀³ = 0,042875
0,027 < 0,042875 < 0,064
    
x₁ = (1/3) · (2 · 0,35 + 0,0510542113175 / 0,35²)
   = (1/3) · (0,70 + 0,0510542113175 / 0,1225) =
   = (1/3) · (0,70 + 0,41667036061) =
   = (1/3) · 1,116670360612245 ≈
   ≈ 0,37222345

x₂ = (1/3) · (2 · 0,37222345 + 0,0510542113175 / 0,37222345²) ≈
   ≈ 0,37094942

x₃ = (1/3) · (2 · 0,37094942 + 0,0510542113175 / 0,37094942²) ≈
   ≈ 0,37094503778              →            Question: On what basis do we decide to stop the iteration?

2)
a = +2,448957880825 ≈ +2,449      →      Question: Why didn't we take the number as it is, with a negative sign?
1,3³ = 2,197
1,4³ = 2,744
2,197 < 2,449 < 2,744

Which number should be selected: x₀ = ?
2,197 < x₀ < 2,744

Let this be: x₀ = 1,35
1,3³ < 1,35³ < 1,4³

So, this will be: x₀³ = 2,460375
2,197 < 2,460375 < 2,744

x₁ = (1/3) · (2 · 1,35 + 2,448957880825 / 1,35²) ≈
   ≈ 1,3479118209
x₂ = (1/3) · (2 · 1,3479118 + 2,448957880825 / 1,3479118²) ≈
   ≈ 1,3479085826
x₃ = (1/3) · (2 · 1,3579086 + 2,448957880825 / 1,3479085²) ≈
   ≈ 1,3479085826              →            Question: On what basis do we decide to stop the iteration?


Question: Why didn't we take the number as it is, with a negative sign?
Answer: An important point is that, despite dealing with ³√-0.051042119175
        and ³√-2.448957880825, we can treat these numbers in terms of their
        absolute values—since the cubic function y = x³ is an odd function
        and they are symmetric—meaning we can take the positive value and
        then simply place a negative sign in front of it.
        With a negative starting value, the iteration initially jumps far away
        from the root before gradually returning to the negative root—taking
        around 8–9 iterations—whereas starting with a positive value leads to
        a solution in 3 iterations, or even 2 in a very favorable case.

Odd functions: y = x³, y = x⁵, y = x⁷ or f(x) = sin x, f(x) = tg x
Most important rule: f(-x) = -f(x)
For an example: (-x)³ = -x³
                ³√-a = -³√a

Even functions: y = x², y = x⁴, y = x⁶ or f(x) = cos x
Most important rule: f(-x) = f(x)
For an example: (-x)² = x²
                √-a = √a   ∅

So, if f(x) = ctg(x), how do we check whether it is an odd or even function?
ctg(-x) = -(cos x / sin x) = -ctg x
Since the condition f(-x) = -f(x) is satisfied, it is an odd function.

Functions that are neither even nor odd: y = x + 1
This refers to functions whose domain is not symmetric about the point 0
or which do not satisfy the conditions - f(-x) = -f(x) or f(-x) = f(x)

Question: On what basis do we decide to stop the iteration?
Answer: When consecutive values repeat.
        Also, if a length limit has been set, we check it like this,
        for example: xₙ - xₙ₋₁ < 10⁻⁶


We take the numbers we obtained and place them back at the point where
we previously stopped (continuing from that point on the below):

³√[(-5 + √23) / 4] + ³√[(-5 - √23) / 4] = 
= ³√(-0,051042119175) + ³√(-2,448957880825) = 
= (-³√(0,051042119175)) + (-³√(2,448957880825)) = 
= (-0,37094503778) + (-1,34790858256) =
= -1,71885362034 ≈ -1,71885



Horner's recursive method to obtain the final result we need
First, Horner's recursive method finds the value of the polynomial
at a root x found via Cardano's method or bisection,- it evaluates P(x) at x:
if: 
P(x) = 2x³ + 0x² - 3x + 5 = 0

then:
1) rₙ = rₙ₋₁ · x + aₙ
2) bᵢ = aᵢ + x · bᵢ₋₁

[2   0   -3   5]
b₀ = 2
b₁ = 0 + x · b₀
b₂ = -3 + x · b₁
b₃ = 5 + x · b₂

So, we have found an approximate root value, however, it's important to note
that this is only one of the equation's three possible roots and it's an approximate real root.
In other words, at the root x = -1.71885, the value of the polynomial is very close to zero:
P(x) = P(-1.71885) ≈ 0.

2x³ - 3x + 5 = 0
2x³ + 0x² - 3x + 5 = 0

[2   0   -3   5]
b₀ = 2
b₁ = 0 + (-1,71885) · 2 = -3,4377
b₂ = -3 + (-1,71885) · (-3,4377) ≈ 2,908890645
b₃ = 5 + (-1,71885) · (2,908890645) = 0,00005331484175 ≈ 0

We will attempt to transition from a cubic equation to a quadratic equation
by using "Horner's method of division" to find the complex roots:
[2   0   -3   5]

x₁ = -1,7188536

-1,7188536 | 2    0            -3            5
           |      -3,4377072    5,908915     -4,9999997  
-------------------------------------------------------------
           | 2    -3,4377072    2,908915     0,000000298 ≈ 0

2x² - 3,4377072x + 2,908915 = 0
ax² + bx + c = 0

D = b² - 4ac
D ≈ (-3,4377072)² - 4 · 2 · 2,908915 ≈ -11,453489 < 0
x₂,₃ = (-b ± √D) / 2a
i = √(-1)
D < 0 → √D = √(-D) = √(-|D|) = √[D · (-1)] = i√D

x₂,₃ = (-3,4377072 ± i√(11,453489)) / 4
x₂ = (-3,4377072 + 3,3843004i) / 4
x₃ = (-3,4377072 - 3,3843004i) / 4

x₂,₃ = 4 · (-0,8594628 ± 0,84607509i) / 4
x₂ = -0,8594628 + 0,84607509i
x₃ = -0,8594628 - 0,84607509i

We found the complex roots of the quadratic equation.

Finally, let us verify the accuracy of our result by
substituting the "approximate real root" we obtained into the expression
as we noted at the beginning of this article:
P(x) = 0
2x³ - 3x + 5 = 0
P(-1,71885362) = 2 · (-1,71885362)³ - 3 · (-1,71885362) + 5 = 0,000000004154198217 ≈ 0

All founded 3 roots:
x₁ = -1,7188536
x₂ = -0,8594628 + 0,84607509i
x₃ = -0,8594628 - 0,84607509i
```