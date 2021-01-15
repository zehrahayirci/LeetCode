# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        count_a = 0 
        cur = list1
        while cur.next:
            
            print(cur.val)
            if count_a+1 ==a:
                head_a=cur
            if count_a==b:
                head_b=cur.next
            cur = cur.next
            count_a+=1
            
        head_a.next=list2
        while head_a.next:
            head_a=head_a.next
        head_a.next=head_b
        return list1
    
'''
Input
[0,3,2,1,4,5]
3
4
[1000000,1000001,1000002]
'''