# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        prehead = ListNode(-1)
        temp = prehead
        
        while l1 and l2:
        
            if l2.val > l1.val:
                temp.next = l1
                temp = l1
                l1 = l1.next
            
            else:
                temp.next = l2
                temp = l2
                l2 = l2.next
        
        if l1 == None:
            temp.next = l2
        
        if l2 == None:
            temp.next = l1
            
        return prehead.next
