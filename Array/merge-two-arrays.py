<<<<<<< HEAD
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
=======
  
def merge(a, b):
  start_index = len(b) - len(a)
  for i in a:
    b[start_index] = i
    start_index += 1
  return sorted(b)

def merge(a, b):
  a_index = len(a) - 1
  b_index = len(b) - len(a) - 1
  end = -1
  while a_index >= 0 and b_index >= 0:
    if a[a_index] > b[b_index]:
      b[end] = a[a_index]
      a_index -= 1
      end -= 1
    else:
      b[end] = b[b_index]
      b_index -= 1
      end -= 1
  if a_index < 0:
    for i in range(0, b_index):
      b[end] = b[b_index]
      b_index -= 1
      end -= 1
  else:
    for i in range(0, a_index):
      a[end] = a[a_index]
      a_index -= 1
      end -= 1
  return b
>>>>>>> parent of 7ddf2b3... Update merge-two-arrays.py
