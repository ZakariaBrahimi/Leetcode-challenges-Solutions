# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        # in-place solution 
        if head == None or head.next == None:
            return head
        
        current = head
        previous_node = None
        next_node = head
        
        while current != None:
            next_node = current.next
            current.next = previous_node
            previous_node = current
            current = next_node
            
        return previous_node