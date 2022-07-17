* Acaully the fisrt approach coming up to my mind is the once bellow
* I have used **dummy technique** abd iterate through out the list one by one, then adding the iterated node to the beginning of dummy list.
```py
if not head:
  return None
new_head = head
if head.next:
  new_head = self.reverseList(head.next)
  head.next.next = head
head.next = None
return new_head
```
* And the other solution is traverse the linked list and change the order of them one **in-place** by one
​
* The time complexity of both solutions is **O(n)** the length of linked list because we have iterated on entire list.
* The space complexity of both solutions is **O(1)** because we we didn't use extra memory (only the memory space of the given list)
