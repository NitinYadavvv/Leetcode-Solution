# Last updated: 1/20/2026, 10:04:55 PM
# just maintain prev curr and next for reverese and for k element reverese maintain last and first pointer also for first pass add dummy
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8        if not head or not head.next:
9            return head
10        
11        tmp = head
12        l = 0
13        while tmp:
14            l+=1
15            tmp = tmp.next
16        dummy = ListNode(0)
17        dummy.next = head
18        last = dummy
19        first = head
20        for i in range(l//k):
21            
22            prev = None
23            curr = first
24            nex = None
25            t = k
26            while t:
27                nex = curr.next
28                curr.next = prev
29                prev = curr
30                curr = nex
31                t-=1
32            
33            last.next = prev
34            first.next = nex
35            last = first
36            first = nex
37            
38        return dummy.next