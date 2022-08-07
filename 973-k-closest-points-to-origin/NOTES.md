* To heapify 2D array, **heapq** python module uses the first item in every 1D array to build the heap for example:
```python
min_heap = [[3,3],[5,-1],[-2,4], [1,3],[-2,2]]
heapq.heapify(min_heap) # return [[-2, 2], [1, 3], [-2, 4], [3, 3], [5, -1]]
print([-100,1000000] > [-20,4000000000]) # return False cuz we care only about the first # item which is -100 not 1000000 ==>> -100 < -20 this is why it's False
```