# Last updated: 12/10/2025, 8:25:15 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dum= ListNode(0)
        carry = 0
        tail = dum
        while l1 or l2 or carry:
            if l1:
                v1 = l1.val
                l1 = l1.next
            else:
                v1 = 0
            if l2:
                v2 = l2.val
                l2 = l2.next
            else:
                v2 = 0
            ans = v1+v2+carry
            carry = ans//10
            new = ListNode(ans%10)
            tail.next = new
            tail = new
            
        return dum.next
            
                
        