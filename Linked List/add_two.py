# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre = temp = ListNode(0)
        takeover = 0
        
        while l1 or l2 or takeover:
            l1v = l2v = 0
            
            if l1:
                l1v = l1.val
                l1 = l1.next
            if l2:
                l2v = l2.val
                l2 = l2.next
            
            total = l1v + l2v + takeover
            takeover = total // 10
            val = total % 10
            temp.next = ListNode(val)
            temp = temp.next
            
        return pre.next     