# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        # Edge case: list contains only one node
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

        
        
                
        
        
