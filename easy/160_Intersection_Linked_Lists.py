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

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        countA = 0
        curA = headA
        while(curA):
            curA = curA.next
            countA+=1
        countB = 0
        curB = headB
        while(curB):
            curB = curB.next
            countB+=1
        print(countA,countB)
        fark = abs(countA-countB)
        if countA>countB:
            curA=headA
            curB=headB
        else:
            curA=headB
            curB=headA
        i = 0
        while i < fark:
            curA = curA.next
            i+=1
        print(i)
        while(curA != curB):
            curA=curA.next
            curB=curB.next
        
        return curB
            
   