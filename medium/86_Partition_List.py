# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        smaller = ks = ListNode(0)
        bigger = kg = ListNode(0)
        
        while head:
            if head.val < x:
                smaller.next = ListNode(head.val)
                smaller = smaller.next
            else:
                bigger.next = ListNode(head.val)
                bigger = bigger.next
            head = head.next
            
        smaller.next = kg.next 
        return ks.next