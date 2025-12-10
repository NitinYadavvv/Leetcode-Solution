# Last updated: 12/10/2025, 8:24:52 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head.next is None:
            return None
        c = 0
        temp = head
        while temp:
            c+=1
            temp = temp.next
        till = c - n
        if till == 0:
            head = head.next
            return head
        temp = head
        i=1
        while i<=till:
            if i == till:
                temp.next = temp.next.next
            temp = temp.next
            i+=1
        return head
            
        
