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
    
    # Time & Space Complexity is O(n), where n is the length of the given list
        
        
        
        
        # to discuss 
        # Time Complexity: O(n) ===> Iterate over the given list
        # Space Cmplexity: O(n) ===>> n is length of new array(length of given list)
        """arr = list()
        current = head
        result = float('-inf')
        
        while current:
            val = current.val
            arr.append(val)
            current = current.next
        
        for i in range(len(arr)):
            target_index = len(arr) - 1 - i
            twin_sum = arr[i] + arr[target_index]
            result = max(result, twin_sum)
            
        return result"""