* The solution below is accepted - the time complexity of this approach and the other is O(n), and n the length of the given list.
* The only different is on space complexity
* The space complexity of the other approach is O(1) because of we don't need any extra memory space - **in-place**
* But for the below approach is O(n) because of we need extra memory space to put all nodes value on an array.
```python
if not head.next:
  return True
arr = []
current = head
while current != None:
  arr.append(current.val)
  current = current.next
left = 0
right = len(arr) - 1
while left <= right:
  if arr[left] == arr[right]:
    left += 1
    right -= 1
  else:
  return False
return True
```

***
#### Resources:
- [Check for Palindromic Linked List | Snapdeal | Adobe | Amazon](https://www.youtube.com/watch?v=-DtNInqFUXs)
- [Palindrome Linked List | LeetCode 234 | C++, Java, Python](https://www.youtube.com/watch?v=H3J-HoGCVXs)
- [Palindrome Linked List - Leetcode 234 - Python - NeetCode](https://www.youtube.com/watch?v=yOzXms1J6Nk)
