# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        result_list = current = ListNode() # 0 -> None
        i = list1
        j = list2
        
        while (i != None and j != None):            
            if i.val < j.val:
                current.next = i
                i = i.next
            else:
                current.next = j
                j = j.next
            current = current.next
        
        # The 2 while loops bellow is the same as this statment == current.next = i or j
        while i == None and j != None:
            current.next = j
            current = current.next
            j = j.next
                
        while j == None and i != None:
            current.next = i
            current = current.next
            i = i.next
            
        return result_list.next # The actual first node value in the result list is 0 because of the first initialization ===>> 0->1->2->...->k