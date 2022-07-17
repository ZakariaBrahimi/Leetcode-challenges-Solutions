* Acaully the fisrt approach coming up to my mind is the once bellow
* I have used **dummy technique** abd iterate through out the list one by one, then adding the iterated node to the beginning of dummy list.
```python
if head == None:return
dummy = current = ListNode()
dummy.next = head
head = head.next
current = tail = current.next
while head != None:
dummy.next = head
head = head.next
dummy.next.next = current
current = dummy.next
tail.next = None
return dummy.next
```
* And the other solution is traverse the linked list and change the order of them one **in-place** by one
​
* The time complexity of both solutions is **O(n)** the length of linked list because we have iterated on entire list.
* The space complexity of both solutions is **O(1)** because we we didn't use extra memory (only the memory space of the given list)