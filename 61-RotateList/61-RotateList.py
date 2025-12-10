# Last updated: 12/10/2025, 8:24:18 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        s = head
        f = head
        t = head
        n = 0
        while t:
            t= t.next
            n+=1
        k = k%n
        for _ in range(k):
            f = s
            while f.next.next is not None:
                f = f.next
            f.next.next = s
            s = f.next
            f.next = None
        return s
        