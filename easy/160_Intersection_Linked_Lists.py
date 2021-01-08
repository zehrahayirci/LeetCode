# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        cur_A = headA
        cur_B = headB
        while cur_B != cur_A:
            cur_A = cur_A.next if cur_A else headB
            cur_B = cur_B.next if cur_B else headA

        return cur_A    
        #They will not hit the first round but the second one! 
        #because we skip the first unmatched parts 
   