# Last updated: 12/10/2025, 8:21:05 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head
        
        temp = head.next
        h = head
        new = 0
        while temp!= None:
            i = min(head.val,temp.val)
            
            while i>=2:
                if head.val%i==0 and temp.val%i==0:
                    new = i
                    break
                i-=1
            if i == 1:
                new = 1
            node = ListNode(new)
            head.next = node
            node.next = temp
            head = temp
            temp= temp.next

        return h


        