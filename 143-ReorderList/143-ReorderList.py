# Last updated: 1/12/2026, 11:26:46 PM
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """

        self.head = head
        fast = head
        s = [head]
        while fast.next:
            fast = fast.next
            s.append(fast)
        
        fast = s.pop()
        while fast != self.head and self.head.next != fast:
            fast.next = self.head.next
            self.head.next = fast
            self.head = fast.next
            fast = s.pop()
        
        if self.head.next != fast:
            self.head.next = None
        else:
            fast.next = None

        


        