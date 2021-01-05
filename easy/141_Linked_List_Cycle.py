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
        while head:
            if head.next == None:
                return False
            else: 
                
                if head.val == "visited":
                    return True
                else: 
                    head.val = "visited"
                    return self.hasCycle(head.next)
            