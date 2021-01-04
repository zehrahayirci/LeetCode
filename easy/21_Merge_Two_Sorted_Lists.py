# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1:
        return l2
    if not l2:
        return l1
    
    start = None    
    if l1.val < l2.val:
        start = l1
        start.next = self.mergeTwoLists(l1.next, l2)
    else:
        start = l2
        start.next = self.mergeTwoLists(l1, l2.next)
    
    return start
    
            