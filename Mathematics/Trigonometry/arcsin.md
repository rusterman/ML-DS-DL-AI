```
While researching arcsin, I came across a definition that describes it very well: 
"The fact that arcsin function is the inverse function of sine means that the operations of 
sine and its inverse cancel each other out" (arcsin funksiyasının tərs olmasının 
mənası sinusla geri qayıtma əməliyyatlarının bir-birini ləğv etməsidir).

When asking "sin⁻¹(0.8) = ?", the question is: "Which angle has a sine of 0.8?"
sin⁻¹(0.8) = arcsin(0.8) = ?

In other words, you are given the sine and need to find the angle,- we are looking for the angle.

Note: 
When we say "sine," we are referring to the ratio - opposite / hypotenuse. 
Here, 0.8 is the value of the sine.

If the question were "sin(0.8) = ?", it would mean: "What is the sine of 0.8 radians?" - 
- we are looking for the sine of a given angle. 
Here, 0.8 represents radians.

We will try to find the angle corresponding to such a value of sin⁻¹ (which angle arcsin(−1) 
corresponds to):
sin⁻¹(0,8) = ?
sin⁻¹(0,8) = x   -->   x = sin⁻¹(0,8)
sin⁻¹(0,8) = arcsin(0.8) = x
sin(sin⁻¹(0,8)) = sin x

sin x = 0.8
sin(sin⁻¹(0,8)) = 0.8

x = θ (it does not matter x or θ)


Now, let's see how many degrees the angle with a sine of 0.8 is:
0.8 -> 0.707   -->   sin 45°
0.8 -> 0.866   -->   sin 60°

Therefore, the angle "x" we are looking for lies between 45° and 60°:
45° < x < 60°
+7   =52°  +7   =59

45° < x < 60°
+8   =53°  +8   =61

(52° + 53°) / 2 = 52.5°   -->   Arithmetic Mean

Convert to radians: 52.5 * (π / 180)
(525 * π) / 1800 ≈ 0.292 * π ≈ 0.916


We took x ≈ 0.916.
Now we calculate sin(0.916) using the Taylor (Maclaurin) series:

sin x = x - x³/6 + x⁵/120 - x⁷/5040 + ...
sin(0.916) ≈ 0.916 - (0.916)³/6 + (0.916)⁵/120 - (0.916)⁷/5040 ≈ 0.79317

However, we need to find the value corresponding to 0.8.
Therefore, we need to increase 0.916 slightly:
Δ(sin x) = 0.8 - 0.793 ≈ 0.007   -->   0.00683

Furthermore, we want to know how much sin x changes if we slightly alter x (0.916). 
We can determine this, using the derivative, since the derivative represents the rate of 
change of the function. Taking the derivative of sin x, we get:

d/dx sin x = cos x
Δ(sin x) ≈ cos x * Δx   -->   this is the fundamental formula
cos(0.916) ≈ 0.609   -->    0.608997708
sin(0.916) ≈ 0.79317
Δ(sin x) ≈ 0.007   -->   0.00683

Δ(sin x) ≈ cos x * Δx

0.007 x
0.00683 ≈ cos(0.916) * Δx
0.007 x
0.00683 ≈ 0.609 * Δx

Δx ≈ 0.00683 / 0.609 ≈ 0.011215

We need to increase x by approximately 0.011215 radians:
x ≈ 0.916 + ≈0.011215 ≈ 0.927215 (rad)
x ≈ 0.927215 * (180 / π≈3.14159) ≈ 53.125551074... ≈ 53.13

That is:
sin⁻¹(0.8) = arcsin(0.8) ≈ 0.927215 rad ≈ 53.13°


After all, Taylor (Maclaurin) series for arcsin:
arcsin x = x + x³/6 + 3x⁵/40 + 5x⁷/112 + ...

However, we use Newton's method for greater speed:
xₙ₊₁ = xₙ - (sin(xₙ) - 0.8) / cos(xₙ)

x₀ – initial guess?
sin(x) = ?   -->   working backwards [sin(0.8) = ?]

Note: A characteristic of the sine function is that, it takes an angle value and 
returns a corresponding number. 
This number represents a ratio (opposite/adjacent), but different angles can yield the same result:
sin(53.13°) ≈ 0.8
sin(126.87°) ≈ 0.8
sin(413.13°) ≈ 0.8
sin(486.87°) ≈ 0.8, etc.

In other words, if we say sin x = 0.8, we can find multiple values ​​for x due to the function's 
periodicity; normally, a mathematical function yields one result for one input. 
However, with sin⁻¹ x = ?, the process works in reverse, as previously mentioned:
sin x = 0.8   <--   working backwards

sin⁻¹(0.8) = 53.13°, 126.87°, 413.13°, ... - unlike a standard mathematical function, a single input 
can yield multiple outputs. Consequently, this no longer qualifies as a function. 
Therefore, one part of the graph is taken: −90° ≤ x ≤ 90°.

```