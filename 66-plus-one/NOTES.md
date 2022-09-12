* the problem here is when I was thinkinh on a solution, the first approach come up to my mind is using **int()** and **str()** built-in functions and without caring on **edge cases**,  and this is so wrong on problem solving.
* I should first think smart, without the help of built-in functions, and make attention on details(edge cases) and figur out the I can add 1 to the last digit on the array
* Think smaaaaaaart
​
```
"""
[1,9,9]
[9,9,9]
[1,2,3]
-> '123' -> 123 -> 123 + 1 = 124 -> '124' -> [1,2,4]
1. Iterate and turn each num to string
2. concatinate all of numbers(strings)
3. turn it to integer and increment by one
4. turn to string
5. change the given array in place
"""
"""