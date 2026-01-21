# Last updated: 1/21/2026, 7:30:41 PM
# use next and current pointer and a even pointer which always point to the starting of the even nodes and just the change the curr.next = nex.next
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
8        
9
10        if not head or not head.next:
11            return head
12        
13        even = head.next
14        curr = head
15        nex = head.next
16        c = 0
17        while nex.next:
18            curr.next = nex.next
19            curr = nex
20            nex = nex.next
21            c+=1
22        if c%2 == 1:
23            curr.next = nex.next
24            nex.next = even
25        else:
26            curr.next = even
27
28        return head      
29