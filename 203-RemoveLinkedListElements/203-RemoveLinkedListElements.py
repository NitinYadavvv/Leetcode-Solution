# Last updated: 12/10/2025, 8:22:24 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None
        temp = ListNode()
        temp.next = head
        t = temp
        while temp and temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return t.next