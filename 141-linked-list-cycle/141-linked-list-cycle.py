# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        # if not head or not head.next:
        #     return False
        current = head
        nodes_set = set()
        
        while current:
            if current in nodes_set:
                return True
            nodes_set.add(current)
            current = current.next
        
        return False
        
        