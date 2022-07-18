# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        result = float('-inf')
        fast = slow = head
        
        # Reach the middle of list
        while(fast.next.next != None):
            fast = fast.next.next
            slow = slow.next
        
        # Reverse the right side of given list
        current = slow.next
        temp1 = None
        temp2 = slow.next
        
        while(current != None):
            temp2 = current.next
            current.next = temp1
            temp1 = current
            current = temp2
            
        current = head
        
        # Comparing the two halves of list
        while (temp1 != None):
            twin_sum = current.val + temp1.val
            result = max(result, twin_sum)
            current = current.next
            temp1 = temp1.next
        
        return result
    
# Time Complexity: O(n) ===> Iterate over the given list ===>>  O(n/2) + O(n/2) + O(n/2) = O(n)
# Space Cmplexity: O(1), No need for extra memory space
