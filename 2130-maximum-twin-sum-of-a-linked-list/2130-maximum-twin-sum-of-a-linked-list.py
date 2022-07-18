# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        arr = list()
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
            
        return result