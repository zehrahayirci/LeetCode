# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast=slow=head
        while fast and fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast: # There is a cyc7e.
            # Tries to find the start of the cyc7e.
                slow = head
                # Both pointers advance at the sane time,
                while slow is not fast:
                    slow , fast = slow.next , fast.next
                return slow # sTow is the start of cycle
        return None