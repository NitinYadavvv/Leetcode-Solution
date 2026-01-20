# Last updated: 1/20/2026, 8:03:31 AM
# Previous , Next and current with Left and right position
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
8
9        if not head or not head.next :
10            return head
11
12        prev = None
13        curr = head
14        next = None
15        p = None
16        L = 1 
17        while L!=left:
18            p = curr
19            curr = curr.next
20            L+=1
21        point = curr
22        R = L
23        while R!=right:
24            next = curr.next
25            curr.next = prev
26            prev = curr
27            curr = next 
28            R+=1
29        
30        next = curr.next
31        curr.next = prev
32        prev = curr
33        point.next = next
34        if left == 1:
35            return prev
36        p.next = prev
37        return head
38           
39
40
41        
42        
43
44        