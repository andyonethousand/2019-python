# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Divide and conquer

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        N = len(lists)
        
        if N == 0:
            return None
        
        if N == 1:
            return lists[0]
        
        if N == 2:
            prehead = cur = ListNode(0)
            l1 = lists[0]
            l2 = lists[1]
            
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                
                cur = cur.next
            
            if l1:
                cur.next = l1
            if l2:
                cur.next = l2
            
            return prehead.next
        
        mid = N // 2
        l1 = self.mergeKLists(lists[0: mid + 1])
        l2 = self.mergeKLists(lists[mid + 1:])
        
        return self.mergeKLists([l1, l2])