# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur=l=m= head
        count=0
        while cur != None:
            if count == k-1:
                val_a = cur.val
            count+=1
            cur=cur.next

        c = 1
        if count ==1:
            return head
        while l != None:
            if c == (count-k)+1:
                val_b=l.val
                l.val=val_a
            c+=1
            l=l.next
        d=1
        while m != None:
            if d == k:
                m.val=val_b
            d+=1
            m=m.next
        return head
        
        
            
        