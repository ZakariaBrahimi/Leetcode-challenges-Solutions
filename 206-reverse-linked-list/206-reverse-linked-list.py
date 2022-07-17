# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        # Edge cases: empty list or list contains only one node
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
    
# There is another solution (acaully isn't effecient) which is recursive sollution,
# The resources of this approach are mentioned on the Notes.md file
