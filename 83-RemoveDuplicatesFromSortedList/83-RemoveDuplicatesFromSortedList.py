# Last updated: 12/10/2025, 8:23:44 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        temp = head
        while temp and temp.next:
            while temp and temp.next and temp.val == temp.next.val:
                temp.next = temp.next.next
            if temp:
                temp = temp.next
        return head

        