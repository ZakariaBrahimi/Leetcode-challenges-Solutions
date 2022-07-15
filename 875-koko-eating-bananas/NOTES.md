* This is the trick, what I did is as bellow:
```python
math.ceil( banana / middle )
```
* But the correct (maybe it's the same) solution is using this bellow:
```python
(banana-1) // middle ) + 1
```
* It seems like they both are the same, but here is the different:
* by using first method: ===>> **3 / 6 = 0**
* But by using the second method: ===>> **(( 3 - 1 ) // 6 ) + 1 = 1**
​
​
* And the other trick is to treat the given problem like a stupid one, start from 0, like someone who never has studied Data structures and algorithms in his entire life
​