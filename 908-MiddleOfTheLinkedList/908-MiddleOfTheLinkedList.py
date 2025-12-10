# Last updated: 12/10/2025, 8:21:38 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        p1 = head
        p2 = head
        while p2.next is not None and p2.next.next != None:
            p1 = p1.next
            p2 = p2.next.next
        if p2.next is None:
            return p1
        if p2.next.next is None:
            return p1.next
        
