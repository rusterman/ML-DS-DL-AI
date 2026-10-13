```
1 is written instead of i:
[1 for i in range(1, 5, 1) for j in range(1, 6, 1)]

First imagine it like this:
for i in range(1, 5):
    for j in range(1, 6):
        1

1st iteration of i -> [1 for j in range(1, 6, 1)]
i = 1

j = 1 → [1]
j = 2 → [1, 1]
j = 3 → [1, 1, 1]
j = 4 → [1, 1, 1, 1]
j = 5 → [1, 1, 1, 1, 1]
...
4th iteration of i -> [1 for j in range(1, 6, 1)]
i = 4

j = 1 → [1]
j = 2 → [1, 1]
j = 3 → [1, 1, 1]
j = 4 → [1, 1, 1, 1]
j = 5 → [1, 1, 1, 1, 1]

The general result would be:
[1, 1, 1, 1, 1,
 1, 1, 1, 1, 1,
 1, 1, 1, 1, 1,
 1, 1, 1, 1, 1]


According to the fact that 1 is written instead of i, 
if this were i**2:
[i**2 for i in range(1, 5, 1) for j in range(1, 6, 1)]

First, visualize it like this:
for i in range(1, 5):
    for j in range(1, 6):
        i**2

1st iteration of i -> [i**2 for j in range(1, 6, 1)]
i = 1

j = 1 → [1]
j = 2 → [1, 1]
j = 3 → [1, 1, 1]
j = 4 → [1, 1, 1, 1]
j = 5 → [1, 1, 1, 1, 1]
...
4th iteration of i -> [i**2 for j in range(1, 6, 1)]
i = 4

j = 1 → [16]
j = 2 → [16, 16]
j = 3 → [16, 16, 16]
j = 4 → [16, 16, 16, 16]
j = 5 → [16, 16, 16, 16, 16]

The overall result would be:
[1, 1, 1, 1, 1,
 4, 4, 4, 4, 4,
 9, 9, 9, 9, 9,
 16, 16, 16, 16, 16]

So, for example:
i = 1
j = 1 → add 1 → [1]
j = 2 → add 1 → [1, 1]
...
j = 5 → add 1 → [1, 1, 1, 1, 1]

i = 2
j = 1 → add 4 → [1, 1, 1, 1, 1, 4]
j = 2 → add 4 → [1, 1, 1, 1, 1, 4, 4]
...
j = 5 → add 4 → [1, 1, 1, 1, 1, 4, 4, 4, 4, 4]

The 5 iterations of j executed during each iteration of i In the loop,
the result would be:
i = 2
j = 1 → i**2 = 4
j = 2 → i**2 = 4
j = 3 → i**2 = 4
j = 4 → i**2 = 4
j = 5 → i**2 = 4
After the iterations, the result would be: 4, 4, 4, 4, 4
```