# Last updated: 12/10/2025, 8:22:23 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        new = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new       
    

        


        