# Last updated: 12/10/2025, 8:22:45 AM
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
        if head is None or head.next is None:
            return False
        s = head
        f = head.next.next
        while f:
            if s == f:
                return True
            s = s.next
            if f.next is None:
                return False
            else:
                f = f.next.next
        return False
            