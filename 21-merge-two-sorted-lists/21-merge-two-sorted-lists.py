# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        new_list_head = current = ListNode() # 0 -> None  // dummy head
        
        while (list1 != None and list2 != None):            
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # The 2 if statements bellow is the same as this statment ===>> current.next = list1 or list2
        
        if list1 == None:
            current.next = list2
            
        if list2 == None:
            current.next = list1
            
        return new_list_head.next # The actual first node value in the result list is 0 because of the first initialization ===>> 0->1->2->...->k