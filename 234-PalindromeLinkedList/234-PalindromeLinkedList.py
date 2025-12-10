# Last updated: 12/10/2025, 8:22:08 AM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rev(self,s):
        prev = None
        curr = s
        while curr:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        return prev

    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        new = self.rev(slow)
        
        while head != slow and new:
            if head.val != new.val:
                return False
            head = head.next
            new = new.next
        return True



    
                  


