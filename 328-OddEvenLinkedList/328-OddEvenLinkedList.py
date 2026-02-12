# Last updated: 2/12/2026, 10:52:18 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        

        if not head or not head.next:
            return head
        
        even = head.next
        curr = head
        nex = head.next
        c = 0
        while nex.next:
            curr.next = nex.next
            curr = nex
            nex = nex.next
            c+=1
        if c%2 == 1:
            curr.next = nex.next
            nex.next = even
        else:
            curr.next = even

        return head      
