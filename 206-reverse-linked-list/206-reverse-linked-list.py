# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
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
        