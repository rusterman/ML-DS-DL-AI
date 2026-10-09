```
Demonstrated via Taylor (Euler) formula

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
```