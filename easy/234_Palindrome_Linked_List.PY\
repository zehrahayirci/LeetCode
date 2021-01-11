# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        if head.next is None:
            return True
        # At least two size
        left = head
        right = head.next
        cur = head.next
        left_prev = None
                
        i = 1 
        while cur.next:
            i+=1
            if i%2==1:
                a = left
                b = left.next
                left.next = left_prev
                left_prev = a
                left = b
            else:
                right = right.next 
            cur = cur.next 
        left.next = left_prev
        while right:
            if not left.val == right.val:
                return False
            left = left.next
            right = right.next
        return True
    ''''
        if head == None:
            return True 
        if head.next==None:
            return True
        first = head.val
        n_h = head.next
        while head.next.next:
            head = head.next
        last =head.next.val
        print(first,last)
        head.next=None 
        print(n_h)
        if first == last :
            return self.isPalindrome(n_h)
        else:
            return False 
    '''