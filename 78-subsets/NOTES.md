* is the time complexity O(2^n) since I am making 2 decisions and the height of the decision tree is n?
​
* You are making O(2^N) "decisions", but each of those requires an average N/2 work.Thus the runtime is O(N * 2N).
​
* **Specifically**, that work happens in this expression, which is somewhat hidden by python magic: `result.append(list(subset))`
* This expression makes a copy of subset, which requires time proportional to the length of subset, which is on average N/2.
* When you do a copy operation on mutable datatypes:
```
b = list(a)
a is b # False
```
* It copies the whole data to another memory location and the time complexity is defined by the total size of the list i.e. O(n)
* There are 3 ways to copy a list in python:
```
list.copy() # this doesn't work in python, avoid it
list[:]
list()
```
[check here](https://stackoverflow.com/questions/37059269/attributeerror-list-object-has-no-attribute-copy) to see the problem with using list.copy()
* It iterates thorugh all elements. So the time complexity defined by thr size of the list i.e. O(n)