# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if not head.next:
            return True
        
        slow = fast = head
        
        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next
    
        prev = None
        while slow:
            next_node = slow.next

            slow.next = prev
            prev = slow
            slow = next_node
        
        dummy = head
        while prev:
            if dummy.val == prev.val:
                dummy = dummy.next
                prev = prev.next
            else:
                return False
        
        return True
        
        
        
        
        """"# Edge case: list contains only one node
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
        return True"""

        
        
                
        
        
