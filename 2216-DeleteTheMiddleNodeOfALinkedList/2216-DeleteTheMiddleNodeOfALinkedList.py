# Last updated: 12/10/2025, 8:21:15 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return None
        s = head
        f = head
        while f.next and f.next.next:
            if f.next.next.next:
                s = s.next
                f = f.next.next
            else:
                break
        s.next = s.next.next
        return head
        
        
        