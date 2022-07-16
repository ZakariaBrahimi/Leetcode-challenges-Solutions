# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        result_list = current = ListNode()
        i = list1
        j = list2
        #current = result_list
        
        while (i != None and j != None):
            """if i.val == j.val:
                result_list = i
                result_list.next = j
                i = i.next
                j = j.next
                current = result_list.next"""
            if i.val < j.val:
                current.next = i
                current = current.next
                i = i.next
            else:
                current.next = j
                current = current.next
                j = j.next
            
            """while i == None and j != None:
                current.next = j
                current = current.next
                j = j.next
                
            while j == None and i != None:
                current.next = i
                current = current.next
                i = i.next"""
        current.next = i or j
                
        return result_list.next