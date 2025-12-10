# Last updated: 12/10/2025, 8:22:40 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        temp = headA
        te = headB
        while temp!= te:
            if temp:
                temp = temp.next
            else:
                temp = headB
            if te:
                te = te.next
            else:
                te= headA
        return te
        
            
            