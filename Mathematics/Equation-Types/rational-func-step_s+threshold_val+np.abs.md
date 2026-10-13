```
2x - 1 = 0
2x = 1
x = 0.5   -   it's the vertical asymptote

Firstly, we should to find the step size in np.linspace:
Δx = stop - start / (num - 1) = (stop - start) / (num - 1)
Δx = (-5 - 5) / (1000 - 1) = -10 / 999 = 0.01001001001001001001001001001001 ≈ 0.010
step = Δx ≈ 0.010

That is why, we set the value 0.02 (manually) as the threshold?
This figure is a technical parameter selected based on the quality 
of the graph and the density of the points.
If we choose 0.02, we are actually removing a small zone from the graph:
0.02 from 0.010

−0.02 ≤ x − 0.5 ≤ 0.02
0.5 - 0.02 ≤ x ≤ 0.5 + 0.02
0.48 ≤ x ≤ 0.52

0.02 contains a fraction of 0.010. 
This is a filter that will ensure the deletion of only numbers close to 0.5 from the graph, 
while we obtain the result by means of a module:
|x - 0.5| > 0.02

We want to remove the points close to 0.5 on both the left and the right sides.
Therefore, x − 0.5 results in a negative value on the left and a positive value on the right.
`np.abs()` removes the negative sign: |x − 0.5|
This way, we obtain just the distance on both sides.
In other words, the reason we subtract 0.5 is to find the distance between x and 0.5.

Accordingly, for example, since the numbers -0.48548549 and +0.48548549 in the array 
give different results, one is deleted and the other one is not. 

Because of -0.48548549 far from 0.5, but +0.48548549 close to 0.5:
1) |−0.48548549 − 0.5| = |−0.98548549| = 0.98548549 > 0.02   V
2) |+0.48548549 − 0.5| = 0.01451451 < 0.02   X

In other words, this means that all x-values in the interval 
are within a distance of 0.02 or less from 0.5. 
(İntervaldakı bütün x-qiymətləri 0,5-e 0,02 və ya daha az məsafədə yerləşirler)
```