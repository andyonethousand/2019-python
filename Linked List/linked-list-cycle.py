  
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cycle_set = set()
        curr = head
        
        while curr:
            next = curr.next
            
            if curr.next in cycle_set:
                return True
            
            else:
                cycle_set.add(curr)
                curr = next
        
        return False