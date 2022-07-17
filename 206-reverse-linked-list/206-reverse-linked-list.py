# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """if head == None:return
        
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
        return dummy.next"""
        
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
        
        