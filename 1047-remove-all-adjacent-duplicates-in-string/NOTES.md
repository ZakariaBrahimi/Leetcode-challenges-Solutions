### The optimal approach:
```
- stack = []
- Looping through the given string
- if stack is not empty and s[i] == stack[-1]
- pop the last item of the stack
- else:
- push s[i] to the stack
- Returning the stack joined togather
```

* **Time Complexity:**  the length of the given string, so it's **O(n)**
* **Space Complexity:**  the length of the stack used which takes in the **worst case** the same length of the given string , so it's **O(n)**
****
#### Recources:
- [LeetCode Remove All Adjacent Duplicates In String Solution Explained - Java](https://www.youtube.com/watch?v=hXEEr5WekSQ)
